---
title: "Evaluating Practical Enumeration and Blocking Attacks on the Snowflake Circumvention System"
date: 2026-09-16
topic: security
tags: [security, networking, censorship-circumvention, tor, privacy, measurement-study]
source: https://arxiv.org/abs/2609.12242
---

Evaluating Practical Enumeration and Blocking Attacks on the Snowflake Circumvention System

* Date: 2026-09-16
* Source: https://arxiv.org/abs/2609.12242
* Topic: Security / Networking
* Why it matters: Linden Chen, Ryan Sangha, Cecylia Bocovich, and Ram Sundara Raman run real-world attacks against Snowflake, the Tor Project's widely used anti-censorship proxy system, and show that a censor could enumerate tens of thousands of its proxy IPs and block a large share of them with very little collateral damage — a direct, practical threat to a tool millions of people in censored countries rely on.

## Korean Summary

**한줄 요약**

연구진은 Tor 프로젝트가 운영하는 검열 우회 시스템 "Snowflake"를 대상으로 실제 공격을 수행해, 악성 클라이언트가 프록시 IP를 대규모로 열거(enumeration)하고 이를 이용해 차단(blocking)할 수 있음을 실증했다. 2025년 5~6월 48일간의 실측에서 공격자는 약 1,000개 자율시스템(AS)에 속한 21,000여 개의 고유 프록시 IP를 열거했으며, 이 논문은 2026년 ACM CCS에 게재 승인되었다.

**핵심 아이디어**

Snowflake는 검열 국가의 사용자가 자원봉사자들이 운영하는 대량의 임시 WebRTC 프록시를 통해 인터넷 검열을 우회하도록 돕는 시스템으로, 보안성은 "공격자가 프록시 IP를 쉽게 열거할 수 없다"는 것과 "설령 열거하더라도 그 IP들을 차단하면 무고한 트래픽까지 광범위하게 막히는 부수 피해(collateral damage) 때문에 검열 당국이 차단을 꺼릴 것"이라는 두 가지 가정에 의존해왔다. 이 논문은 실제 악성 클라이언트처럼 행동하며 이 두 가정이 현실에서 얼마나 유효한지를 윤리적으로 제한된 실측과 대규모 시뮬레이션을 결합해 검증한다.

**무엇이 새로운가?**

* 실험실 시뮬레이션이 아니라 실제 Snowflake 인프라를 대상으로 한 48일간(2025년 5~6월)의 열거 공격을 수행해 21,000여 개의 고유 프록시 IP(약 1,000개 AS 소속)를 확보
* 관측된 AS 중 상위 1%만 차단해도 관측된 Snowflake 프록시의 30% 이상을 차단할 수 있는 반면, Tranco 상위 100대 도메인에는 영향이 0%, 상위 100만 도메인에는 약 2.5%만 영향을 미친다는 점을 정량화 — 즉 부수 피해가 기존에 가정했던 것보다 훨씬 작을 수 있음을 보임
* Snowflake 브로커(broker)의 "부하 인지형 매칭(load-aware matching)" 방식이, 특히 수요가 급증하는 시기(예: 2025년 6월 이란 검열 사태)에 안정적이고 고용량인 프록시를 공격자에게 더 일찍, 더 쉽게 노출시킨다는 부작용을 규명
* 프록시 처리량(churn, 교체 속도)이 열거·차단 공격의 효과를 시간에 따라 제한하는 핵심 변수임을 실측과 시뮬레이션 양쪽에서 확인
* 대규모 시뮬레이션을 통해 공격자 규모가 커질수록 열거·차단 성공률이 급격히 높아지는 반면, 프록시 교체 속도가 높을수록 차단 효과가 크게 감소함을 정량적으로 제시

**어떻게 작동하는가?**

연구팀은 실제로 검열 당국의 악성 클라이언트를 흉내 내는 실험을 설계했다. Snowflake 클라이언트처럼 브로커에 반복적으로 접속해 배정되는 프록시들의 IP 주소를 수집함으로써, 시간에 따라 얼마나 많은 고유 프록시가 노출되는지 측정했다(48일, 21,000여 개 IP, ~1,000개 AS). 이렇게 얻은 실측 데이터를 바탕으로, 네트워크 차단자가 "AS 단위로 트래픽을 차단"하는 시나리오를 시뮬레이션해 어떤 AS를 차단하면 얼마나 많은 프록시가 막히는지, 그리고 그 AS를 차단했을 때 같은 AS에 속한 정상 도메인(Tranco 목록 기준)들이 얼마나 부수적으로 피해를 입는지를 계산했다. 또한 대규모 시뮬레이션으로 공격자의 열거 규모와 프록시 교체 속도(churn)를 변수로 바꿔가며 장기적인 차단 효과를 추정했다.

**강점**

* 실제 배포된 시스템을 대상으로 한 윤리적으로 제한된 실측 공격이라는 점에서, 단순 이론적 취약점 제시를 넘어선 현실적 위협 평가를 제공
* 2026년 ACM CCS(컴퓨터·통신 보안 분야 최상위 학회 중 하나)에 게재 승인되어 학계의 엄정한 동료 심사를 거쳤을 가능성이 높음
* 부수 피해율까지 함께 정량화해, "차단이 비현실적"이라는 기존 방어 논리의 실제 강건성을 구체적 수치로 검증
* 2025년 6월 이란 검열 사태라는 실제 사건을 사례로 들어, 수요 급증 상황에서 방어 체계가 취약해지는 실질적 시나리오를 제시

**한계**

* 이 환경에서는 arXiv 원문 페이지에 직접 접근(fetch)할 수 없어, 검색 엔진에 노출된 초록과 2차 요약 정보를 교차 확인하는 방식으로 이 요약을 작성함 — 세부 실험 설정, 정확한 통계적 방법론, 논문이 제안하는 구체적 방어책은 원문 확인이 필요함
* 실측은 48일이라는 제한된 기간에 수행되었으며, Snowflake 운영진이 이미 대응책(예: 브로커 매칭 방식 변경, 레이트 리미팅 강화 등)을 적용했을 가능성이 있어 현재 시점의 실제 위험도는 달라졌을 수 있음
* 윤리적 고려에 따라 공격 강도를 제한했을 것으로 보이며, 실제 국가 수준 검열 당국이 동원할 수 있는 자원(대규모 병렬 접속, 장기간 관측 등)은 이보다 훨씬 클 수 있음

**알아둘 용어**

* Snowflake: Tor 프로젝트가 운영하는 검열 우회 시스템으로, 자원봉사자들의 브라우저가 WebRTC를 통해 임시 프록시 역할을 하여 검열 국가의 사용자가 Tor 네트워크에 접속하도록 돕는다
* 브로커(Broker): Snowflake 클라이언트와 이용 가능한 프록시를 연결(매칭)해주는 중개 서버
* 열거 공격(Enumeration Attack): 시스템이 사용하는 자원(여기서는 프록시 IP 주소)을 체계적으로 수집해 목록화하는 공격
* 부수 피해(Collateral Damage): 특정 대상을 차단하려는 조치가 의도치 않게 무고한 서비스·사용자에게까지 영향을 미치는 것
* 자율시스템(AS, Autonomous System): 인터넷에서 단일 라우팅 정책으로 관리되는 IP 주소 블록의 집합으로, 보통 하나의 ISP나 조직에 대응
* 프록시 교체(Churn): 프록시가 짧은 주기로 생성·소멸되며 새로운 IP로 교체되는 현상
* Tranco: 웹사이트 인기도 순위를 제공하는 연구용 도메인 랭킹 목록으로, 부수 피해 측정 시 기준으로 흔히 사용됨

**왜 주목할 만한가?**

Snowflake는 실제로 검열이 심한 국가의 활동가·언론인·일반 시민들이 인터넷 자유에 접근하기 위해 의존하는, 이미 폭넓게 배포된 실전 도구다. 이 연구는 그 방어 가정("열거가 어렵다", "차단은 부수 피해 때문에 비현실적이다")이 실제로는 생각보다 취약할 수 있음을 실측으로 보여줌으로써, 학술적 흥미를 넘어 실제 사용자의 안전과 직결되는 시의성 있는 결과를 제공한다. 동시에 Snowflake 운영진이 어떤 부분(브로커 매칭 방식, 프록시 교체 정책 등)을 강화해야 할지에 대한 구체적 단서도 함께 제공한다.

---

## English Summary

**One-line summary**

Linden Chen, Ryan Sangha, Cecylia Bocovich, and Ram Sundara Raman ran real, ethically bounded attacks against Snowflake — the Tor Project's widely deployed censorship-circumvention proxy system — and show that a censor can enumerate a large fraction of its proxy pool and block much of it with surprisingly little collateral damage. The work has been accepted to ACM CCS 2026.

**Core idea**

Snowflake helps users in censored countries reach the Tor network through a large, constantly changing pool of temporary WebRTC proxies run by volunteers. Its security has long rested on two assumptions: that an adversary cannot easily enumerate the IP addresses of these proxies, and that even if they could, blocking those IPs would cause unacceptable collateral damage to unrelated traffic sharing the same infrastructure. This paper tests both assumptions directly by acting as a malicious client and combining bounded real-world measurements with large-scale simulation.

**What is new?**

* A real (not simulated) 48-day enumeration attack against live Snowflake infrastructure (May–June 2025) that collected over 21,000 unique proxy IP addresses spanning nearly 1,000 autonomous systems (ASes)
* A quantified blocking analysis showing that blocking just the top 1% of observed ASes blocks more than 30% of observed Snowflake proxies, while affecting 0% of Tranco Top 100 domains and only about 2.5% of Top 1 million domains — much lower collateral damage than the system's threat model assumed
* Evidence that Snowflake's load-aware broker matching disproportionately exposes stable, high-capacity proxies to attackers early, especially during demand spikes such as the June 2025 Iran censorship event
* Confirmation, via both measurement and simulation, that proxy churn is the key factor limiting long-term enumeration and blocking effectiveness
* Simulation results showing that attacker scale sharply improves enumeration and blocking success, while higher proxy churn substantially reduces blocking effectiveness

**How does it work?**

The researchers built a client that repeatedly requests proxy assignments from the Snowflake broker, just as a real user's client would, and recorded every proxy IP address it was handed over 48 days, yielding roughly 21,000 unique IPs across about 1,000 ASes. Using this real data, they simulated a network-level censor that blocks entire autonomous systems rather than individual IPs, computing both how many proxies such a block would take down and how much collateral damage it would cause to legitimate domains (measured against the Tranco ranking) that happen to share the same ASes. They then extended this with large-scale simulation, varying attacker scale and proxy churn rate, to project enumeration and blocking effectiveness beyond what the 48-day measurement window could show directly.

**Strengths**

* Grounded in real, ethically bounded attacks against production Snowflake infrastructure rather than a purely theoretical model, giving concrete, current numbers
* Accepted to ACM CCS 2026, one of the top venues in computer and communications security, suggesting rigorous peer review
* Quantifies collateral damage alongside blocking effectiveness, directly stress-testing the "blocking is impractical" argument that circumvention systems have relied on
* Uses a real censorship event (Iran, June 2025) as a case study, showing how defenses can weaken precisely when demand — and thus stakes — are highest

**Limitations**

* The arXiv page could not be directly fetched in this environment, so this summary was written by cross-referencing search-engine snippets of the abstract and reported findings rather than the full paper text; exact experimental details, statistical methodology, and the authors' proposed mitigations should be verified against the original
* The real-world measurement window was limited to 48 days, and Snowflake's operators may have already changed broker matching or rate-limiting behavior in response, so current real-world risk could differ from what was measured
* Ethical constraints likely limited the scale of the real attack; a well-resourced nation-state censor could plausibly enumerate and probe far more aggressively than this study did

**Terms to know**

* Snowflake: a Tor Project censorship-circumvention system in which volunteers' browsers act as short-lived WebRTC proxies, helping users in censored regions reach the Tor network
* Broker: the server that matches Snowflake clients to available volunteer proxies
* Enumeration attack: systematically discovering and cataloging a system's resources — here, proxy IP addresses
* Collateral damage: unintended harm to innocent services or users caused by a blocking action aimed at something else
* Autonomous System (AS): a block of IP addresses under a single routing policy, typically corresponding to one ISP or organization
* Proxy churn: the rate at which proxies appear, disappear, and are replaced with new IP addresses
* Tranco: a research-oriented domain popularity ranking commonly used as a baseline for measuring collateral damage from network blocking

**Why it is worth watching**

Snowflake is a real, widely used tool that activists, journalists, and ordinary citizens in censored countries depend on for internet access. This paper matters because it moves beyond theory to show, with live measurement, that the defense's core assumptions may be weaker than believed — a result with direct implications for the safety of real users, not just academic interest. It also gives Snowflake's maintainers concrete targets for hardening, such as the broker's proxy-matching logic and churn policy.

---

## My take

이 논문은 화려한 신기술 제시보다는, 이미 수백만 명이 실제로 의존하는 검열 우회 도구의 방어 가정을 실측으로 검증했다는 점에서 실용적 가치가 크다. 다만 이 환경에서는 arXiv 원문에 직접 접근하지 못해 검색 결과의 초록과 보고된 수치를 교차 확인해 요약을 작성했으므로, 세부 실험 방법론과 논문이 제안하는 구체적 방어책은 원문 확인을 권장한다. 부수 피해가 예상보다 작다는 결과는 검열 우회 커뮤니티 전체에 실질적인 경고 신호이며, Snowflake 운영진의 후속 대응 여부를 계속 지켜볼 가치가 있다.

This paper's value lies less in flashy new technology and more in empirically testing the defense assumptions of a censorship-circumvention tool that real people already depend on. This summary was written by cross-referencing search-engine snippets of the abstract and reported findings rather than the full arXiv text, so readers should verify the exact experimental methodology and proposed mitigations against the source. The finding that collateral damage is smaller than expected is a genuine warning sign for the circumvention community, and it's worth watching how Snowflake's maintainers respond.
