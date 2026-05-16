#!/usr/bin/env python3
"""Integrate daily-summary PRs into main without losing content."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


DAILY_PATH_RE = re.compile(r"^daily/\d{4}-\d{2}-\d{2}-[A-Za-z0-9._-]+\.md$")


def run(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("+ " + " ".join(args))
    result = subprocess.run(args, text=True, capture_output=True)
    if check and result.returncode != 0:
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        raise subprocess.CalledProcessError(result.returncode, args, result.stdout, result.stderr)
    return result


def output(args: list[str]) -> str:
    return run(args).stdout.strip()


def github_repo() -> str:
    if os.environ.get("GITHUB_REPOSITORY"):
        return os.environ["GITHUB_REPOSITORY"]

    remote = output(["git", "remote", "get-url", "origin"])
    if remote.startswith("git@github.com:"):
        repo = remote.removeprefix("git@github.com:").removesuffix(".git")
    else:
        repo = remote.rstrip("/").removesuffix(".git").split("github.com/")[-1]

    if "/" not in repo:
        raise RuntimeError(f"Cannot determine GitHub repository from origin: {remote}")
    return repo


def gh_json(args: list[str]) -> object:
    return json.loads(output(["gh", *args]))


def current_branch() -> str:
    return output(["git", "branch", "--show-current"])


def list_open_prs(repo: str, base: str) -> list[dict]:
    data = gh_json(
        [
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "open",
            "--base",
            base,
            "--limit",
            "100",
            "--json",
            "number,title,headRefName,headRepositoryOwner,isDraft,baseRefName",
        ]
    )
    if not isinstance(data, list):
        raise RuntimeError("Unexpected gh pr list response")
    return data


def pr_files(repo: str, number: int) -> list[dict]:
    data = gh_json(["api", f"repos/{repo}/pulls/{number}/files", "--paginate", "--slurp"])
    if data and isinstance(data, list) and isinstance(data[0], list):
        data = [item for page in data for item in page]
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected files response for PR #{number}")
    return data


def owner_login(value: object) -> str | None:
    if isinstance(value, dict):
        return value.get("login")
    if isinstance(value, str):
        return value
    return None


def is_daily_summary_pr(repo: str, pr: dict) -> tuple[bool, str, list[str]]:
    number = int(pr["number"])
    files = pr_files(repo, number)
    paths = [item["filename"] for item in files]
    daily_paths = [path for path in paths if DAILY_PATH_RE.match(path)]

    if not daily_paths:
        return False, "no daily/*.md summary file", []

    unexpected = [path for path in paths if path != "README.md" and not DAILY_PATH_RE.match(path)]
    if unexpected:
        return False, "unexpected files: " + ", ".join(unexpected), []

    non_additions = [
        item["filename"]
        for item in files
        if DAILY_PATH_RE.match(item["filename"]) and item.get("status") != "added"
    ]
    if non_additions:
        return False, "daily files are not pure additions: " + ", ".join(non_additions), []

    return True, "daily summary PR", daily_paths


def checkout_daily_file(repo: str, pr_number: int, path: str) -> bool:
    target = Path(path)
    if target.exists():
        existing = target.read_text(encoding="utf-8")
        incoming = output(["git", "show", f"pr-{pr_number}:{path}"])
        if existing == incoming:
            print(f"Already present with identical content: {path}")
            return False
        raise RuntimeError(f"Refusing to overwrite existing file with different content: {path}")

    target.parent.mkdir(parents=True, exist_ok=True)
    run(["git", "checkout", f"pr-{pr_number}", "--", path])
    return True


def read_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            frontmatter = text[4:end].splitlines()
            for line in frontmatter:
                if line.startswith("title:"):
                    return line.split(":", 1)[1].strip().strip('"')

    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped.lstrip("#").strip()

    return path.stem


def rebuild_readme() -> bool:
    readme = Path("README.md")
    daily_files = sorted(Path("daily").glob("*.md"), reverse=True)
    entries = []
    for path in daily_files:
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.name)
        if not match:
            continue
        date = match.group(1)
        title = read_title(path)
        entries.append(f"- {date} — [{title}]({path.as_posix()})")

    text = readme.read_text(encoding="utf-8")
    marker = "## Papers\n"
    if marker not in text:
        raise RuntimeError("README.md does not contain a '## Papers' section")

    before, after = text.split(marker, 1)
    trailing = ""
    next_heading = re.search(r"\n## ", after)
    if next_heading:
        trailing = after[next_heading.start() :]

    new_text = before + marker + "\n" + "\n".join(entries) + "\n" + trailing
    if new_text == text:
        return False

    readme.write_text(new_text, encoding="utf-8")
    return True


def close_pr(repo: str, number: int) -> None:
    run(["gh", "pr", "close", str(number), "--repo", repo])


def delete_branch(repo: str, branch: str) -> None:
    result = run(["git", "push", "origin", "--delete", branch], check=False)
    if result.returncode != 0:
        print(result.stderr.strip())
        print(f"Could not delete branch {branch}; continuing.")


def main() -> int:
    repo = github_repo()
    owner = repo.split("/", 1)[0]
    base = os.environ.get("TARGET_BRANCH", "main")

    run(["git", "config", "user.name", os.environ.get("GIT_AUTHOR_NAME", "daily-summary-bot")])
    run(["git", "config", "user.email", os.environ.get("GIT_AUTHOR_EMAIL", "daily-summary-bot@users.noreply.github.com")])

    if current_branch() != base:
        run(["git", "checkout", base])

    run(["git", "pull", "--ff-only", "origin", base])

    handled: list[dict] = []
    skipped: list[str] = []

    for pr in list_open_prs(repo, base):
        number = int(pr["number"])
        title = pr["title"]
        branch = pr["headRefName"]
        head_owner = owner_login(pr.get("headRepositoryOwner"))

        if head_owner != owner:
            skipped.append(f"#{number} {title}: fork PRs are not auto-integrated")
            continue

        ok, reason, daily_paths = is_daily_summary_pr(repo, pr)
        if not ok:
            skipped.append(f"#{number} {title}: {reason}")
            continue

        run(["git", "fetch", "origin", f"pull/{number}/head:pr-{number}"])
        changed = False
        for path in daily_paths:
            changed = checkout_daily_file(repo, number, path) or changed

        handled.append({"number": number, "title": title, "branch": branch, "changed": changed})

    readme_changed = rebuild_readme()

    status = output(["git", "status", "--porcelain"])
    if status:
        run(["git", "add", "README.md", "daily"])
        count = len([item for item in handled if item["changed"]])
        run(["git", "commit", "-m", f"Integrate {count} daily paper summary PRs"])
        run(["git", "push", "origin", base])
    else:
        print("No repository changes to commit.")

    for item in handled:
        close_pr(repo, item["number"])
        delete_branch(repo, item["branch"])

    print("\nHandled PRs:")
    for item in handled:
        print(f"- #{item['number']} {item['title']}")

    if skipped:
        print("\nSkipped PRs:")
        for item in skipped:
            print(f"- {item}")

    if not handled and not skipped and not readme_changed:
        print("No open PRs needed action.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise
