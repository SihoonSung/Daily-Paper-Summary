---
title: "IonStack Part II: GhostLock — A Stack Use-After-Free That Has Existed in All Linux Distributions for 15 Years"
date: 2026-07-13
topic: security
tags: [security, linux-kernel, vulnerability-research, use-after-free, privilege-escalation, CVE-2026-43499]
source: https://nebusec.ai/research/ionstack-part-2/
---

IonStack Part II: GhostLock — A Stack Use-After-Free That Has Existed in All Linux Distributions for 15 Years

* Date: 2026-07-13
* Source: https://nebusec.ai/research/ionstack-part-2/
* Topic: security (Linux kernel vulnerability research)
* Why it matters: A single stale pointer left behind by a kernel cleanup routine turns into a reliable, unprivileged root exploit on essentially every mainstream Linux distribution, and the bug has been silently present since 2011. It is a stark reminder that decade-old kernel code paths still hide critical, broadly exploitable flaws.

## Korean Summary

**한줄 요약**

보안 연구팀 VEGA(Nebula Security)가 리눅스 커널의 futex 우선순위 상속(priority-inheritance) 코드에서 2011년부터 존재해온 스택 use-after-free 취약점(CVE-2026-43499, 일명 "GhostLock")을 공개했습니다. 별도 권한 없이 로컬 코드를 실행할 수 있는 사용자가 약 5초, 97% 확률로 루트 권한을 획득하고 컨테이너를 탈출할 수 있습니다.

**핵심 아이디어**

리눅스 커널의 실시간 뮤텍스(rtmutex) 코드에 있는 `remove_waiter()`라는 정리(cleanup) 헬퍼 함수는 "자신이 정리하는 대기자(waiter)는 항상 현재 실행 중인 스레드 소유"라고 가정합니다. 그러나 `FUTEX_CMP_REQUEUE_PI` 재대기(requeue) 경로에서 커널이 교착 상태(deadlock)를 감지해 `-EDEADLK`로 롤백할 때는, 한 스레드가 잠들어 있는 다른 스레드를 대신해 정리 작업을 수행합니다. 이때 가정이 깨지면서 이미 해제된 스택 프레임을 가리키는 낡은(stale) 포인터가 남게 되고, 이것이 use-after-free로 이어집니다.

**무엇이 새로운가?**

* 2011년 5월(리눅스 2.6.39)에 도입되어 15년간 발견되지 않은 커널 버그를 규명
* `CONFIG_FUTEX_PI`만 켜져 있으면 발동 가능하며, 이는 사실상 모든 주요 배포판의 기본 설정
* 공개된 풀체인(full-chain) 익스플로잇이 약 5초, 97% 신뢰도로 루트 셸을 획득
* 동일 연구팀이 공개한 "IonStack" 체인의 후반부로, Firefox 샌드박스 탈출(CVE-2026-10702)과 결합하면 브라우저 코드 실행에서 시스템 루트까지 도달 가능
* Google kernelCTF 프로그램을 통해 포상금이 지급된 검증된 취약점

**어떻게 작동하는가?**

1. 공격자가 별도 권한 없이 로컬에서 코드를 실행할 수 있는 상태에서 시작합니다.
2. `futex` 시스템 호출로 우선순위 상속 뮤텍스에 대해 `FUTEX_CMP_REQUEUE_PI` 재대기를 유도하고, 교착 상태 감지 경로를 의도적으로 트리거해 `-EDEADLK` 롤백을 발생시킵니다.
3. 이 롤백 과정에서 `remove_waiter()`가 실행 중인 스레드가 아닌 잠든 다른 스레드의 대기자 구조체를 정리하면서, 이미 해제된 스택 메모리를 가리키는 포인터를 남깁니다.
4. 공격자는 해제된 스택 영역을 원하는 데이터로 덮어써(use-after-free 악용) 커널 내부 상태를 조작하고, 최종적으로 권한 상승 및 컨테이너 탈출을 달성합니다.
5. 패치는 상위 커밋(3bfdc63936dd)으로 병합되었고, AlmaLinux·CloudLinux 등 배포판이 긴급 커널 업데이트를 배포했습니다.

**강점**

* 취약점의 근본 원인(잘못된 소유권 가정)을 명확하고 재현 가능하게 규명
* 특수한 커널 설정 없이 기본 설정만으로 거의 모든 배포판에 영향을 미친다는 광범위성
* 다수의 배포판 벤더(AlmaLinux, CloudLinux 등)와 보안 매체를 통해 교차 검증됨
* 신속한 패치 발표와 명확한 커밋 참조로 실무 대응이 용이함

**한계**

* 이 글은 학술 논문이 아니라 보안 연구팀의 기술 공개(disclosure) 글이며, 동료 심사(peer review)를 거치지 않았습니다.
* 네트워크 정책 제약으로 원문 페이지를 직접 열람하여 재확인하지는 못했고, 여러 독립적인 매체(CloudLinux, AlmaLinux, TheHackerNews, TuxCare 등)의 보도를 교차 검증하는 방식으로 사실관계를 확인했습니다.
* 공개된 익스플로잇은 현재 arm64 안드로이드 기기에 특화되어 있으며, x86_64 리눅스용 코드는 문서화만 되어 있어 실제 야생 악용 확산 속도는 지켜봐야 합니다.
* 이미 패치가 나왔으므로 실제 위험은 각 시스템의 커널 업데이트 적용 속도에 달려 있습니다.

**알아둘 용어**

* **Use-after-free (UAF)**: 이미 해제된 메모리 영역을 계속 참조하여 발생하는 메모리 안전성 취약점.
* **Futex (fast userspace mutex)**: 사용자 공간과 커널 공간을 오가며 동작하는 경량 동기화 프리미티브.
* **우선순위 상속(Priority Inheritance, PI)**: 낮은 우선순위 스레드가 락을 쥐고 있을 때 일시적으로 우선순위를 높여 우선순위 역전을 방지하는 기법.
* **rtmutex**: 우선순위 상속을 지원하는 리눅스 커널의 실시간 뮤텍스 구현.
* **CVE**: 공개적으로 알려진 보안 취약점에 부여되는 표준 식별 번호 체계.
* **컨테이너 탈출(Container Escape)**: 컨테이너 내부에서 실행 중인 프로세스가 격리를 벗어나 호스트 시스템 권한을 획득하는 공격.

**왜 주목할 만한가?**

15년 전에 심어진 코드가 오늘날에도 거의 모든 리눅스 서버, 데스크톱, 안드로이드 기기, 클라우드 컨테이너 환경에 영향을 미칠 수 있다는 사실은 오래된 커널 코드에 대한 지속적인 보안 감사의 필요성을 보여줍니다. 특히 클라우드·컨테이너 환경이 보편화된 지금, 로컬 권한 상승이 컨테이너 탈출로 이어질 수 있다는 점에서 실무적 파급력이 큽니다.

---

## English Summary

**One-line summary**

Security research team VEGA (Nebula Security) disclosed GhostLock (CVE-2026-43499), a stack use-after-free in the Linux kernel's futex priority-inheritance code that has existed since 2011. An unprivileged local user can reach root and escape containers in roughly 5 seconds with about 97% reliability.

**Core idea**

A kernel cleanup helper called `remove_waiter()`, in the real-time mutex (rtmutex) code, assumes the futex waiter it is tearing down always belongs to the currently running thread. On the `FUTEX_CMP_REQUEUE_PI` requeue path, however, when the kernel detects a deadlock cycle and rolls back with `-EDEADLK`, one thread ends up cleaning up state on behalf of a different, sleeping thread. That broken assumption leaves a stale pointer into a stack frame the kernel has already freed — a classic use-after-free, but reachable from ordinary, unprivileged syscalls.

**What is new?**

* Roots out a kernel bug introduced in Linux 2.6.39 (May 2011) that went undetected for roughly 15 years.
* Requires nothing beyond `CONFIG_FUTEX_PI`, which is enabled by default on essentially every major Linux distribution.
* A published full-chain exploit reaches root in about 5 seconds with ~97% reliability.
* Forms the second half of the researchers' "IonStack" chain: combined with a separate Firefox sandbox-escape bug (CVE-2026-10702), it can carry attacker code from inside a browser all the way to host root.
* The finding was validated and rewarded through Google's kernelCTF bug-bounty program.

**How does it work?**

1. An attacker starts with the ability to run unprivileged local code (e.g., inside a sandboxed process or container).
2. Using futex syscalls, the attacker triggers a `FUTEX_CMP_REQUEUE_PI` requeue on a priority-inheritance mutex and deliberately induces the kernel's deadlock-detection path, forcing an `-EDEADLK` rollback.
3. During that rollback, `remove_waiter()` cleans up a waiter structure belonging to a different, sleeping thread rather than the currently running one, leaving a pointer into memory that has already been freed.
4. The attacker reclaims and overwrites the freed stack memory to manipulate kernel state, ultimately escalating to root and, in containerized environments, escaping to the host.
5. The fix landed upstream as commit 3bfdc63936dd, and downstream distributions (AlmaLinux, CloudLinux, and others) shipped emergency kernel updates shortly after disclosure.

**Strengths**

* Clearly identifies the root cause — a broken ownership assumption in cleanup code — in a way that is reproducible and technically precise.
* Extremely broad blast radius: no special kernel configuration is needed, and the vulnerable path is enabled by default almost everywhere.
* Cross-corroborated by multiple distribution vendors and security outlets (AlmaLinux, CloudLinux, TheHackerNews, TuxCare, and others).
* Rapid patch turnaround with a clear upstream commit reference makes remediation straightforward for administrators.

**Limitations**

* This is a security research disclosure, not a peer-reviewed academic paper.
* Due to this session's network access restrictions, the source page could not be directly re-fetched for a final check; the facts here were cross-verified against multiple independent secondary reports (CloudLinux, AlmaLinux, TheHackerNews, TuxCare) rather than a live fetch of the primary page.
* The publicly weaponized proof-of-concept is currently specific to arm64 Android devices; an x86_64 Linux exploit chain is described in the writeup but not yet confirmed widely deployed in the wild.
* Since a patch already exists, real-world risk now depends mainly on how quickly individual systems apply kernel updates.

**Terms to know**

* **Use-after-free (UAF)**: A memory-safety bug where a program keeps referencing memory after it has been freed.
* **Futex (fast userspace mutex)**: A lightweight synchronization primitive that mostly operates in userspace but falls back to the kernel for contention.
* **Priority inheritance (PI)**: A technique where a lower-priority thread holding a lock temporarily inherits a higher priority to prevent priority inversion.
* **rtmutex**: The Linux kernel's real-time mutex implementation, which supports priority inheritance.
* **CVE**: The standard public identifier system for known security vulnerabilities.
* **Container escape**: An attack where a process running inside a container breaks out of its isolation to gain access to the host system.

**Why it is worth watching**

That code planted 15 years ago can still endanger nearly every Linux server, desktop, Android device, and cloud container today underscores the ongoing need for security audits of old kernel code paths. With cloud and container deployments now ubiquitous, a local privilege-escalation bug that doubles as a container escape carries outsized practical consequences.

---

## My take

기술적으로 매우 명확하고 파급력이 큰 사례입니다. 다만 이 글은 동료 심사를 거친 학술 논문이 아니라 보안 연구팀의 기술 공개 자료이며, 이번 세션의 네트워크 제한으로 원문을 직접 재확인하지 못하고 여러 2차 보도를 교차 검증하는 데 그쳤다는 점은 밝혀둡니다. 그럼에도 다수의 독립적인 배포판 벤더가 동일한 CVE에 대해 패치를 배포했다는 사실은 신뢰도를 뒷받침합니다.

This is a technically clear and high-impact case. That said, it is a security disclosure rather than a peer-reviewed paper, and network restrictions in this session prevented a direct re-fetch of the primary source — verification here relies on cross-referencing multiple independent secondary reports. The fact that several distribution vendors independently shipped patches for the same CVE lends it credibility.
