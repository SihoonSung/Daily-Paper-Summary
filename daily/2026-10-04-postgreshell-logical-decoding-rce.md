---
title: "PostGREShell: A 12-Year-Old PostgreSQL Logical-Decoding Flaw Enabling Replication-to-RCE Privilege Escalation (CVE-2026-6471)"
date: 2026-10-04
topic: security
tags: [security, postgresql, cve, privilege-escalation, database, vulnerability-research]
source: https://www.postgresql.org/support/security/CVE-2026-6471/
---

# PostGREShell: A 12-Year-Old PostgreSQL Logical-Decoding Flaw Enabling Replication-to-RCE Privilege Escalation (CVE-2026-6471)

- Date: 2026-10-04
- Source: https://www.postgresql.org/support/security/CVE-2026-6471/ (research write-up: https://cyera.com/research/postgreshell-the-database-powering-much-of-the-internet-had-an-open-door-for-12-years)
- Topic: Security (database / privilege escalation)
- Why it matters: A non-superuser account with only the REPLICATION privilege could get arbitrary code execution on the PostgreSQL server itself, a privilege-boundary bug that sat unnoticed in every supported PostgreSQL branch for about 12 years and affects one of the world's most widely deployed open-source databases.

## Korean Summary

**한줄 요약**

보안 연구팀 Cyera Research(연구자 Vladimir Tokarev)는 PostgreSQL의 "logical decoding(논리적 디코딩)" 기능에서 REPLICATION 권한만 가진 저권한 계정이 서버에서 임의 코드를 실행할 수 있는 취약점(CVE-2026-6471, 별칭 "PostGREShell")을 발견했다. 이 취약점은 2014년 PostgreSQL 9.4부터 존재해 약 12년간 패치되지 않은 채 남아 있었다.

**핵심 아이디어**

PostgreSQL의 논리적 디코딩 기능은 클라이언트가 복제 슬롯을 만들 때 WAL(Write-Ahead Log)을 변환해 줄 "output plugin"을 이름으로 지정하게 해준다. 문제는 CREATE_REPLICATION_SLOT 명령에 전달된 플러그인 이름이 검증 없이 곧바로 서버의 동적 라이브러리 로더로 전달된다는 점이다. 즉 REPLICATION 권한만 있으면 수퍼유저가 아니어도 PostgreSQL 프로세스가 접근 가능한 임의의 공유 라이브러리 파일을 "플러그인"인 척 지정해 서버에 로드시킬 수 있다.

**무엇이 새로운가?**

- REPLICATION 권한을 "낮은 권한"으로 취급해 온 오랜 운영 관행이 사실은 사실상 코드 실행 권한과 동급이었음을 입증했다.
- 백업/복제 계정이 윈도우에서는 UNC 경로(SMB)를, 리눅스/맥OS에서는 NFS 자동마운트나 기존 쓰기 가능 경로를 이용해 임의 라이브러리를 로드시키는 구체적 공격 경로를 제시했다.
- 코드 실행 이후 카탈로그 테이블을 조작해 완전한 수퍼유저 권한으로 에스컬레이션하고, 서버 재시작 후에도 살아남는 영속적 백도어를 심을 수 있음을 보였다.
- PostgreSQL 14~18의 지원되는 모든 메이저 브랜치에 동일하게 영향을 미친다는 점을 확인했다.
- 수정 방안으로 출력 플러그인을 관리자가 승인한 목록으로 제한하는 새 서버 설정(output_plugin_libraries)을 도입했다.

**어떻게 작동하는가?**

1. 공격자는 REPLICATION 권한(또는 그에 준하는 백업/복제용 역할)을 가진 계정으로 로그인한다.
2. CREATE_REPLICATION_SLOT 명령을 보내면서 output plugin 이름에 자신이 통제하는 공유 라이브러리 경로(또는 이름)를 지정한다.
3. 서버는 이 이름을 검증 없이 동적 라이브러리 로더에 넘겨 해당 파일을 로드·실행한다.
4. 로드된 코드는 PostgreSQL 서버 프로세스를 구동하는 OS 계정 권한으로 실행되며, 이를 발판 삼아 카탈로그를 조작해 PostgreSQL 수퍼유저 권한으로 승격하고 영속적 접근 수단을 설치할 수 있다.
5. PostgreSQL 프로젝트는 2026년 8월 보안 릴리스(18.6, 17.11, 16.15, 15.19, 14.24)에서 output_plugin_libraries 설정을 추가해, 관리자가 허용한 플러그인(기본값: pgoutput, test_decoding)만 로드되도록 제한했다.

**강점**

- 영향 범위가 매우 넓다: PostgreSQL은 수만 개 조직(넷플릭스, 인스타그램, 스포티파이, 우버 등 포함)이 사용하는 대표적 오픈소스 DB이며, 지원되는 모든 메이저 버전이 영향을 받는다.
- 공격 경로가 구체적이고 재현 가능하게 설명되어 있어, 방어자가 즉시 패치 우선순위와 완화책(권한 재점검, 네트워크 공유 경로 제한 등)을 세울 수 있다.
- 패치와 함께 설계 수준의 방어(허용 목록 기반 output_plugin_libraries)가 도입되어 향후 유사한 플러그인 로딩 경로의 재발을 줄인다.
- 플랫폼(윈도우·리눅스·맥OS)을 가리지 않고 통용되는 공격 패턴을 식별했다.

**한계**

- 공격을 수행하려면 여전히 REPLICATION 권한을 가진 유효한 계정이 필요하므로, 완전히 미인증 상태의 원격 공격자가 바로 악용할 수 있는 취약점은 아니다.
- NFS 자동마운트나 SMB UNC 경로를 통한 악용은 서버의 네트워크/파일시스템 구성에 따라 난이도가 달라질 수 있다.
- 패치가 나온 지 한 달 남짓이므로, 실제 환경에서의 패치 적용률이나 구버전 방치 서버 규모는 아직 충분히 파악되지 않았다.
- 보도에 사용된 세부 수치(예: "39,000개 이상 기업 사용")는 연구팀의 자체 집계이며 독립적으로 검증되지는 않았다.

**알아둘 용어**

- Logical decoding(논리적 디코딩): PostgreSQL의 WAL(Write-Ahead Log)을 애플리케이션이 소비할 수 있는 형식으로 변환해 변경 데이터를 스트리밍하는 기능.
- Output plugin: 논리적 디코딩 결과를 원하는 형식으로 바꿔주는 서버 측 공유 라이브러리 모듈.
- REPLICATION privilege: 복제 슬롯 생성, WAL 스트리밍 등 복제 관련 작업을 수행할 수 있는 PostgreSQL 역할 속성으로, 전통적으로 수퍼유저보다 낮은 권한으로 간주되어 왔다.
- Replication slot: 복제 클라이언트가 WAL의 특정 위치를 추적·보존하도록 서버에 등록하는 객체.
- Privilege escalation(권한 상승): 낮은 권한의 계정이 의도되지 않은 방식으로 더 높은 권한(여기서는 서버 코드 실행 및 수퍼유저)을 획득하는 것.
- CVSS: 취약점의 심각도를 0~10 점수로 나타내는 공통 평가 체계(이 취약점은 7.2, High).

**왜 주목할 만한가?**

데이터베이스 복제·백업 계정은 많은 조직에서 "낮은 권한"으로 취급되어 다수의 서비스 계정, CI/CD 파이프라인, 모니터링 도구 등에 폭넓게 부여되어 있다. 이 취약점은 그런 계정 하나만 탈취되면 전체 데이터베이스 서버를 완전히 장악할 수 있었음을 보여주며, 12년간 발견되지 않았다는 사실은 널리 쓰이는 핵심 인프라 소프트웨어라도 권한 경계 가정이 틀릴 수 있음을 환기시킨다. 이미 공개 패치가 나온 상태이므로, 운영 중인 PostgreSQL 서버의 즉각적인 업데이트와 복제 권한 재검토가 필요하다.

---

## English Summary

**One-line summary**

Security researchers at Cyera Research (Vladimir Tokarev) disclosed CVE-2026-6471, nicknamed "PostGREShell": a PostgreSQL logical-decoding flaw that lets a non-superuser account holding only the REPLICATION privilege get the server to load and execute arbitrary code. The bug had existed since PostgreSQL 9.4 in 2014, roughly 12 years, across every currently supported major version.

**Core idea**

PostgreSQL's logical decoding feature converts the write-ahead log (WAL) into a consumable change stream via a server-side "output plugin," whose name a client supplies when creating a replication slot. The flaw is that the plugin name passed in a CREATE_REPLICATION_SLOT command is handed directly to the server's dynamic-library loader without adequate validation — so any account with REPLICATION privilege, not just a superuser, can point that name at an arbitrary shared library file reachable to the OS account running PostgreSQL and have the server load it.

**What is new?**

- Shows that the REPLICATION privilege, long treated operationally as "low privilege," is effectively equivalent to code-execution privilege on the server.
- Documents concrete exploitation paths: UNC paths over SMB on Windows, and NFS automounts or existing writable paths on Linux/macOS, to get a malicious library loaded.
- Demonstrates escalation beyond code execution: once code runs with the OS account's privileges, catalog tables can be modified to grant full PostgreSQL superuser and install backdoors that survive server restarts.
- Confirms the issue affects every supported major branch, PostgreSQL 14 through 18, before the August 2026 security releases.
- Introduces the fix's defense-in-depth mechanism: a new `output_plugin_libraries` setting that restricts logical-decoding clients to an administrator-approved allow-list (default: `pgoutput`, `test_decoding`).

**How does it work?**

1. An attacker authenticates with an account that has the REPLICATION role attribute (or an equivalent backup/replication role) — not superuser.
2. They issue a CREATE_REPLICATION_SLOT command specifying an output plugin name pointing at a shared library file they control.
3. The server passes this unvalidated name straight to its dynamic-library loader, which loads and executes the file.
4. The loaded code runs with the privileges of the OS account hosting the PostgreSQL server process; from there, catalog-table manipulation can escalate to full database superuser and plant persistent backdoors.
5. PostgreSQL's August 2026 security releases (18.6, 17.11, 16.15, 15.19, 14.24) add the `output_plugin_libraries` setting so only admin-approved plugins can be loaded this way.

**Strengths**

- Very broad real-world exposure: PostgreSQL is used across tens of thousands of organizations, reportedly including Netflix, Instagram, Spotify, and Uber, and every currently supported major version was affected.
- The exploitation path is described concretely and reproducibly, letting defenders prioritize patching and mitigations (reviewing replication-role grants, restricting network file-share access) immediately.
- The fix pairs a patch with a structural, allow-list-based defense (`output_plugin_libraries`) rather than a narrow one-off fix, reducing the chance of similar plugin-loading issues recurring.
- Identifies attack patterns that generalize across Windows, Linux, and macOS deployments.

**Limitations**

- Exploitation still requires a valid account with REPLICATION privilege, so it is not a pre-authentication, fully remote vulnerability.
- Practical exploitability via NFS automounts or SMB UNC paths depends on how a given server's network and filesystem are configured, so real-world ease of attack varies.
- The patch is only about a month old at the time of this summary, so real-world patch-adoption rates and the number of still-exposed servers are not yet well characterized.
- Figures cited in coverage (e.g., "39,000+ companies") come from the researchers' own framing and have not been independently verified here.

**Terms to know**

- Logical decoding: A PostgreSQL feature that converts the write-ahead log (WAL) into a consumable stream of data changes for downstream clients.
- Output plugin: A server-side shared-library module that formats logical-decoding output into a desired representation.
- REPLICATION privilege: A PostgreSQL role attribute permitting replication-related actions such as creating replication slots and streaming WAL; traditionally treated as lower-privilege than superuser.
- Replication slot: A server-side object that tracks and retains WAL position on behalf of a replication client.
- Privilege escalation: Gaining higher, unintended privileges (here, server code execution and database superuser) from a lower-privileged starting point.
- CVSS: Common Vulnerability Scoring System, a 0–10 severity scale (this issue scored 7.2, rated High).

**Why it is worth watching**

Replication and backup accounts are commonly treated as low-risk and are widely granted to service accounts, CI/CD pipelines, and monitoring tools. This disclosure shows that compromising just one such account could have meant full takeover of the underlying database server, and the fact that it went unnoticed for roughly 12 years in such widely used infrastructure software is a reminder that privilege-boundary assumptions in mature, heavily audited open-source projects can still be wrong. With patches already available, it is an immediate, practical call to update PostgreSQL deployments and re-audit who holds replication privileges.

---

## My take

이번 사례는 "복제/백업 권한은 안전하다"는 오래된 운영 관행이 실제로는 암묵적인 신뢰 가정이었을 뿐, 코드 수준에서 검증된 적이 없었다는 점을 보여준다. 패치가 이미 배포되었고 완화 방법(권한 재검토, output_plugin_libraries 설정)도 명확하므로 실무적 가치가 크지만, 12년이나 지속된 점을 고려하면 비슷한 "암묵적으로 안전하다고 여겨지는 권한" 영역이 다른 데이터베이스나 미들웨어에도 남아 있을 가능성을 시사한다.

This case illustrates that the long-standing assumption "replication/backup privilege is safe" was really just an implicit trust assumption that had never been rigorously validated in code. The fix and mitigations are already available and clearly actionable, making this highly practical, but the fact that it persisted for 12 years suggests similar "implicitly trusted privilege" gaps may still exist in other databases or middleware.
