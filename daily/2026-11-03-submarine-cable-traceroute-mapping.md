---
title: "Calypso's Voyage: Charting Traceroute Paths Through Submarine Cables"
date: 2026-11-03
topic: networking
tags: [networking, internet-infrastructure, submarine-cables, network-measurement, resilience, systems]
source: https://aqualab.cs.northwestern.edu/publication/2026/cwang-imc26
---

Calypso's Voyage: Charting Traceroute Paths Through Submarine Cables

* Date: 2026-11-03
* Source: https://aqualab.cs.northwestern.edu/publication/2026/cwang-imc26
* Topic: Networking (internet measurement / critical infrastructure)
* Why it matters: Submarine cables carry the bulk of intercontinental internet traffic, but nobody outside cable operators has a reliable, scalable way to know which internet paths actually depend on which physical cables; this work gives researchers and policymakers a traceroute-based tool to expose those hidden dependencies without needing proprietary cable-operator data.

## Korean Summary

**한줄 요약**

노스웨스턴 대학교 AQUA Lab과 공동 연구진이 일반적인 traceroute(경로 추적) 데이터만으로 인터넷 트래픽이 어떤 해저 케이블을 실제로 지나는지 지도화하는 Calypso 프레임워크를 확장한 논문을 2026년 ACM 인터넷 측정 컨퍼런스(IMC 2026, 10월 12~16일, 독일 카를스루에)에서 발표했다. 이 논문은 2025년 SIGCOMM 단편 논문으로 처음 소개된 Calypso 아이디어를 전문가 검증, 장애 사례 분석, 지역별 사례 연구로 확장한 완결판 시스템 논문이다.

**핵심 아이디어**

해저 케이블 운영사의 비공개 데이터 없이도, 전 세계에 이미 깔려 있는 공개 traceroute 측정 인프라(RIPE Atlas, CAIDA Ark 등)를 활용해 특정 인터넷 경로가 어떤 해저 케이블을 지나는지 역으로 추론하고, 그 케이블이 전체 인터넷 트래픽에서 얼마나 중요한지를 정량화하는 것이 핵심 아이디어다.

**무엇이 새로운가?**

* traceroute 경로를 실제 해저 케이블 지도에 매핑하는 Calypso 프레임워크를 시스템 수준으로 완성.
* 특정 해저 케이블에 얼마나 많은 경로가 의존하는지를 나타내는 "Route Stress"라는 새로운 지표 도입.
* 전문가 검증(expert validation), 실제 장애(failure) 사례 분석, 지역별 사례 연구를 통한 다각도 검증.
* 해저 케이블망(SCN)을 물리적·지정학적 위협이 커지는 핵심 인프라로 규정하고, 기존 방법들이 해상도와 신뢰성이 부족하다는 점을 지적하며 이를 보완.
* 선행 연구(SIGCOMM 2025, "Threading the Ocean")에서는 약 70만 건의 traceroute를 분석해 남아프리카의 ACE, WACS 등 특정 케이블이 유독 높은 Route Stress를 보인다는 결과를 제시한 바 있음.

**어떻게 작동하는가?**

전 세계 관측점에서 수집된 traceroute 데이터를 입력으로 받아, 각 홉(hop)이 어떤 해저 구간을 지나는지 추정한 뒤, 이를 실제 해저 케이블 지도(케이블 경로, 상륙 지점 정보)와 대조해 각 traceroute 경로를 특정 케이블에 할당한다. 이렇게 매핑된 대량의 경로 데이터를 집계해, 전체 경로 중 특정 케이블에 의존하는 비율을 Route Stress로 계산한다. 이 값이 높을수록 해당 케이블에 장애가 발생했을 때 영향받는 트래픽이 많다는 뜻이며, 실제 장애 사례와 비교해 지표의 타당성을 검증한다.

**강점**

* 케이블 운영사의 비공개 데이터 없이도 공개 측정 인프라만으로 해저 케이블 의존도를 추정할 수 있어 접근성이 높음.
* 단일 사례가 아니라 전문가 검증, 실제 장애, 지역 사례 연구라는 세 가지 방식으로 결과를 교차 검증.
* 해저 케이블 복원력(resilience) 정책 논의나 리스크 분석에 바로 활용 가능한 실용적 지표(Route Stress)를 제공.
* SIGCOMM 2025 단편 논문에서 IMC 2026 정식 논문으로 발전하며 방법론이 누적적으로 검증됨.

**한계**

* traceroute는 왕복 경로가 비대칭적일 수 있어, 특정 구간이 실제로 어떤 케이블을 지나는지 완벽하게 특정하기 어려운 근본적 불확실성이 있다.
* 공개 측정 플랫폼의 관측점 분포가 불균등해, 관측점이 적은 지역의 케이블 의존도는 과소 또는 과대 추정될 수 있다.
* Route Stress는 트래픽 경로 의존도를 보여주는 상대적 지표일 뿐, 케이블의 물리적 손상 위험이나 지정학적 위협까지 직접 측정하지는 않는다.
* 이 요약은 이 세션의 네트워크 정책상 ACM 디지털 라이브러리나 논문 원문 PDF에 직접 접속해 확인하지 못했고, 저자들의 연구실(AQUA Lab) 공개 페이지, 선행 SIGCOMM 2025 논문 정보, IMC 2026 프로그램 관련 검색 결과를 교차 확인해 작성되었다. 정량적 수치는 선행 논문에서 확인된 것 외에는 직접 검증하지 못했다.

**알아둘 용어**

* Traceroute: 인터넷 상에서 데이터가 출발지에서 목적지까지 거쳐가는 네트워크 경로(라우터 목록)를 추적하는 도구.
* 해저 케이블망(Submarine Cable Network, SCN): 대륙 간 인터넷 트래픽 대부분을 실어 나르는 해저에 매설된 광케이블들의 네트워크.
* Route Stress: 전체 인터넷 경로 중 특정 해저 케이블에 의존하는 경로의 비율로, 그 케이블의 상대적 중요도를 나타내는 지표.
* 관측점(Vantage Point): traceroute 같은 네트워크 측정을 수행하는 지리적으로 분산된 측정 지점.
* 복원력(Resilience): 네트워크 인프라가 장애나 공격을 겪은 뒤에도 기능을 유지하거나 빠르게 회복하는 능력.

**왜 주목할 만한가?**

최근 해저 케이블 절단·손상 사건이 늘면서 인터넷 인프라의 물리적 취약성에 대한 우려가 커지고 있는데, 이 연구는 누구나 접근 가능한 공개 측정 데이터만으로 "어떤 케이블이 끊기면 어떤 트래픽이 영향을 받는가"를 정량적으로 추정할 수 있는 실용적 도구를 제시한다. 이는 학계뿐 아니라 정책 결정자나 네트워크 운영자가 리스크를 평가하는 데도 바로 쓰일 수 있는 접근이다.

---

## English Summary

**One-line summary**

Researchers from Northwestern University's AQUA Lab and collaborators presented an extended version of their Calypso framework at ACM IMC 2026 (October 12-16, 2026, Karlsruhe, Germany), which maps internet traceroute paths onto the physical submarine cables they actually traverse using only public measurement data. The paper builds on a 2025 SIGCOMM short paper that introduced the core idea, adding expert validation, real-world failure analysis, and regional case studies.

**Core idea**

Without access to proprietary cable-operator data, the method reuses already-deployed public traceroute measurement infrastructure (such as RIPE Atlas and CAIDA Ark) to infer which submarine cable a given internet path likely crosses, and then quantifies how much of overall internet traffic depends on that specific cable.

**What is new?**

* A fully developed system version of the Calypso framework for mapping traceroute paths to physical submarine cables.
* A new metric, "Route Stress," that estimates a cable's relative importance based on the share of measured routes that depend on it.
* Validation through three complementary angles: expert review, analysis of real cable failure events, and regional case studies.
* Framing of the submarine cable network as critical infrastructure facing growing physical and geopolitical threats, and addressing the resolution and reliability limits of prior mapping methods.
* Builds on the predecessor SIGCOMM 2025 short paper ("Threading the Ocean"), which analyzed roughly 700,000 traceroutes and found especially high Route Stress for specific cables in South Africa, such as ACE and WACS.

**How does it work?**

The system takes traceroute data collected from globally distributed vantage points, estimates which submarine segment each hop likely crosses, and cross-references this against real submarine cable route and landing-point data to assign each traceroute path to a specific cable. Aggregating this mapping across a large volume of paths produces the Route Stress score — the fraction of all measured routes that rely on a given cable — and the authors validate this score against documented real-world cable failures.

**Strengths**

* Estimates submarine cable dependency using only publicly available measurement infrastructure, without needing proprietary operator data.
* Cross-validates findings through three independent angles rather than a single case study: expert review, real failures, and regional analysis.
* Produces a concrete, actionable metric (Route Stress) directly usable in resilience planning and infrastructure risk assessment.
* Methodology has matured cumulatively from a SIGCOMM 2025 short paper into a full IMC 2026 system paper.

**Limitations**

* Traceroute paths can be asymmetric, so there is inherent uncertainty in pinpointing exactly which cable a given segment crosses.
* Public measurement platforms have uneven vantage point coverage, which can over- or under-estimate dependency on cables in less-monitored regions.
* Route Stress is a relative traffic-dependency indicator, not a direct measure of a cable's physical damage risk or exposure to geopolitical threats.
* This session's network policy blocked direct access to the ACM Digital Library entry and the full paper PDF, so this summary relies on cross-checked web search results — the authors' AQUA Lab publication page, details from the predecessor SIGCOMM 2025 paper, and IMC 2026 program references — rather than a direct read of the full text. Quantitative figures beyond those confirmed in the predecessor paper were not independently verified.

**Terms to know**

* Traceroute: A network diagnostic tool that traces the sequence of routers a packet passes through from source to destination.
* Submarine Cable Network (SCN): The network of undersea fiber-optic cables that carries most intercontinental internet traffic.
* Route Stress: A metric measuring the fraction of internet routes that depend on a specific submarine cable, indicating its relative criticality.
* Vantage point: A geographically distributed measurement point used to run network probes like traceroute.
* Resilience: An infrastructure's ability to maintain function or recover quickly after a disruption or attack.

**Why it is worth watching**

As incidents of submarine cable damage and disruption draw growing attention to the physical fragility of internet infrastructure, this work offers a practical, reproducible way to estimate which traffic is at risk if a given cable fails, using only publicly available data. That makes it immediately useful not just to researchers but to policymakers and network operators assessing infrastructure risk.

---

## My take

이 논문은 화려한 신기술보다는 기존에 공개된 측정 데이터를 창의적으로 재활용해 실질적인 인프라 리스크 분석 도구를 만든 사례에 가깝다. Route Stress라는 지표 자체는 단순하지만, 전문가 검증과 실제 장애 사례로 뒷받침한 점이 신뢰도를 높인다. 다만 이 요약은 논문 원문이 아니라 저자 공개 페이지와 선행 논문, 학회 프로그램 정보를 교차 확인해 작성된 것이므로, IMC 2026 버전에서 추가된 구체적인 정량 결과는 원문 확인 전까지 보수적으로 받아들이는 것이 적절하다.

This paper is less about a flashy new technique and more about creatively repurposing already-public measurement data into a practical infrastructure risk-assessment tool. The Route Stress metric itself is simple, but grounding it in expert validation and real failure events adds credibility. That said, since this summary was built by cross-checking the authors' public page, the predecessor paper, and conference program references rather than reading the IMC 2026 full text directly, any new quantitative results specific to this extended version should be treated cautiously until the primary source can be reviewed.
