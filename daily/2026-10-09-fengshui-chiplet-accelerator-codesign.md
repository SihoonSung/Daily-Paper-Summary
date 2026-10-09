---
title: "Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign"
date: 2026-10-09
topic: semiconductors
tags: [semiconductors, chiplets, computer-architecture, hardware-codesign, ai-accelerators]
source: https://arxiv.org/abs/2609.10970
---

Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign

- Date: 2026-10-09
- Source: https://arxiv.org/abs/2609.10970
- Topic: semiconductors (chiplet-based hardware co-design)
- Why it matters: University of Michigan researchers (accepted to MICRO 2026) show that jointly designing a small reusable pool of chiplets together with the custom accelerators built from them can match near-fully-custom chip efficiency while sharing non-recurring engineering costs across many applications — a concrete answer to the rising cost of building bespoke AI hardware.

## Korean Summary

**한줄 요약**

미시간대학교 연구진이 칩렛(chiplet) 풀 구성과 이를 조합해 만드는 맞춤형 가속기(BASIC) 설계를 하나의 문제로 동시에 최적화하는 프레임워크 "Fengshui"를 제안했다. 단 8개의 칩렛만으로 동질적(homogeneous) 가속기 대비 에너지, 에너지-비용, 에너지-지연 등 여러 지표에서 큰 개선을 달성했으며, 이 연구는 MICRO 2026에 채택되었다.

**핵심 아이디어**

완전히 맞춤화된 주문형 반도체(ASIC)는 성능은 좋지만 설계·제조에 드는 비용(NRE)이 매우 크다. 칩렛을 재사용하면 이 비용을 여러 응용에 분산시킬 수 있지만, 문제는 순환적이다 — 어떤 칩렛을 만들어야 할지는 그 칩렛들로 만들어질 가속기의 품질에 좌우되고, 가속기의 품질은 다시 어떤 칩렛이 존재하느냐에 좌우된다. Fengshui는 이 두 문제를 분리하지 않고 함께 최적화함으로써 이 순환성을 정면으로 다룬다.

**무엇이 새로운가?**

- 재사용 가능한 칩렛 풀 선택과 개별 연산자 단위 맞춤형 가속기(BASIC) 조합을 하나의 공동 최적화 문제로 정식화
- 대리모델 기반 진화 최적화(surrogate-assisted evolutionary optimization)로 칩렛 풀을 선정하고, 별도의 진화적 탐색으로 연산자 단위 가속기 구성을 조합
- 네트워크 스위치, 프로세싱-인-메모리(PIM) 유닛, 다양한 마이크로아키텍처의 가속기를 포함한 단 8개의 칩렛만으로 동질적 가속기 대비 에너지 48.5%, 에너지-비용 곱 88.1%, 에너지-지연 곱 93.0%, 에너지-지연-비용 곱 97.8% 감소를 보고
- 제약 없는 완전 이종(heterogeneous) 맞춤 설계 대비 성능 차이를 4.1% 이내로 좁힘
- 데이터센터 LLM 서빙과 엣지 자율주행 인지(perception) 두 가지 실제 응용 시나리오에서 각각 최대 16.8%, 12.0%의 에너지 절감을 실증

**어떻게 작동하는가?**

1. 네트워크 스위치, PIM 유닛, 여러 마이크로아키텍처의 연산 가속기 등 후보 칩렛들의 설계 공간을 정의
2. 대리모델(surrogate model)을 활용한 진화 알고리즘으로, 다양한 응용에 걸쳐 재사용될 소규모 칩렛 풀을 탐색·선정
3. 선정된 칩렛 풀을 바탕으로, 별도의 진화적 탐색을 통해 특정 연산자(operator) 단위로 칩렛들을 조합한 맞춤형 가속기(BASIC) 설계를 구성
4. 완성된 설계를 동질적 가속기, 제약 없는 완전 이종 설계와 비교해 에너지, 지연, 비용 지표를 평가
5. 데이터센터 LLM 추론 서빙과 엣지 자율주행 인지라는 서로 다른 두 실제 워크로드에 적용해 일반화 가능성을 검증

**강점**

- 칩렛 생태계 구축과 가속기 설계라는 상호 의존적인 두 문제를 분리하지 않고 함께 최적화한 점이 실무적으로 의미 있음
- 단 8개의 칩렛이라는 작은 풀로도 완전 맞춤 설계에 근접한 효율(4.1% 이내 차이)을 달성해, 재사용을 통한 NRE 비용 절감의 실질적 가능성을 제시
- 데이터센터와 엣지라는 성격이 다른 두 워크로드에서 모두 개선을 확인해 일반성에 대한 근거를 일부 확보
- 깃허브와 Zenodo에 코드·아티팩트를 공개해 재현성을 높임
- MICRO 2026(컴퓨터 아키텍처 분야 최상위 학회)에 채택되어 동료 평가를 통과

**한계**

- 보고된 수치는 특정 8개 칩렛 풀과 특정 비교 기준(동질적 가속기) 대비 결과로, 다른 응용 영역이나 더 큰 칩렛 풀로 일반화되는지는 추가 검증이 필요
- 현재까지는 시뮬레이션·탐색 기반 설계 결과이며, 실제 실리콘으로 제작되어 측정된 수치인지는 원문 확인이 필요
- 칩렛 간 패키징, 인터커넥트, 열 관리 등 물리적 통합의 실제 난이도는 이 설계 공간 탐색 프레임워크만으로는 충분히 드러나지 않을 수 있음
- 탐색에 사용된 대리모델과 진화 알고리즘의 계산 비용, 그리고 새로운 응용이 추가될 때 전체 프레임워크를 다시 돌려야 하는 정도는 논문만으로 완전히 파악하기 어려움

**알아둘 용어**

- 칩렛(Chiplet): 하나의 큰 칩을 여러 개의 작은 다이(die)로 나누어 제작한 뒤 패키징 단계에서 결합하는 반도체 설계 단위
- 비반복 설계비용(Non-Recurring Engineering, NRE): 칩을 처음 설계하고 제조 공정을 셋업하는 데 드는, 생산량과 무관한 일회성 비용
- BASIC(Bespoke Application-Specific IC): 특정 응용에 맞춰 칩렛들을 조합해 만든 맞춤형 주문형 반도체
- 프로세싱-인-메모리(Processing-in-Memory, PIM): 메모리 내부 또는 근접한 위치에서 연산을 수행해 데이터 이동을 줄이는 하드웨어 구조
- 대리모델 기반 진화 최적화(Surrogate-assisted evolutionary optimization): 실제 평가 비용이 큰 설계를 빠른 근사 모델(대리모델)로 대신 평가하며 진화 알고리즘으로 탐색하는 방법
- 에너지-지연-비용 곱(Energy-Delay-Cost Product): 에너지, 지연시간, 비용을 함께 곱해 하드웨어 설계의 종합적 효율을 비교하는 지표

**왜 주목할 만한가?**

AI 반도체 수요 급증으로 맞춤형 가속기 수요도 늘고 있지만, 응용마다 완전히 새로운 칩을 설계하는 것은 비용 면에서 지속 가능하지 않다. 이 연구는 재사용 가능한 칩렛 생태계와 맞춤형 가속기 설계를 함께 최적화함으로써, 적은 수의 칩렛으로도 완전 맞춤 설계에 가까운 효율을 낼 수 있음을 구체적 수치로 보여준 점에서, 반도체 설계 비용 문제에 대한 실용적 방향을 제시한다.

---

## English Summary

**One-line summary**

Researchers at the University of Michigan (accepted to MICRO 2026) propose Fengshui, a framework that jointly optimizes which chiplets to build and how to compose them into bespoke accelerators (BASICs), rather than treating these as separate problems. Using just 8 chiplets, Fengshui-generated designs come within 4.1% of unconstrained fully-custom designs while cutting energy and cost metrics sharply relative to homogeneous accelerators.

**Core idea**

Fully custom ASICs offer the best performance but carry large non-recurring engineering (NRE) costs. Chiplets let that cost be amortized by reusing the same small dies across many designs, but deciding which chiplets to build is circular: a chiplet pool's value depends on the accelerators eventually built from it, and accelerator quality depends on which chiplets already exist. Fengshui tackles this circularity directly by co-optimizing chiplet-pool selection and accelerator composition together instead of solving them separately.

**What is new?**

- Formulates chiplet-pool selection and operator-level bespoke accelerator (BASIC) composition as a single joint optimization problem
- Uses surrogate-assisted evolutionary optimization to select a reusable chiplet pool, paired with a separate evolutionary search to compose operator-level accelerators from that pool
- With only 8 chiplets — including network switches, processing-in-memory (PIM) units, and accelerators of different microarchitectures — reports energy, energy-cost product, energy-delay product, and energy-delay-cost product reductions of 48.5%, 88.1%, 93.0%, and 97.8% respectively versus homogeneous accelerators
- Comes within 4.1% of unconstrained, fully heterogeneous custom designs despite the small, reusable chiplet set
- Demonstrates energy reductions of up to 16.8% (datacenter LLM serving) and 12.0% (edge autonomous-vehicle perception) on two distinct real-world workloads

**How does it work?**

1. Define a design space of candidate chiplets — network switches, PIM units, and accelerators with different microarchitectures
2. Run a surrogate-assisted evolutionary search to select a small chiplet pool meant to be reused across many downstream applications
3. Given that chiplet pool, run a separate evolutionary search to compose operator-level bespoke accelerator designs (BASICs) for specific workloads
4. Compare the resulting designs against homogeneous accelerators and against unconstrained fully-heterogeneous custom designs on energy, delay, and cost metrics
5. Validate generality by applying the same framework to two very different real workloads: datacenter LLM inference serving and edge autonomous-vehicle perception

**Strengths**

- Directly addresses the circular dependency between chiplet-ecosystem design and accelerator design instead of treating them as independent steps
- Shows that a small pool of just 8 chiplets can approach fully-custom efficiency (within 4.1%), giving a concrete, quantified case for cost amortization through reuse
- Validated on two workloads with very different characteristics (datacenter vs. edge), providing some evidence of generality
- Released code and artifacts on GitHub and Zenodo, supporting reproducibility
- Peer-reviewed and accepted at MICRO 2026, a top-tier computer architecture venue

**Limitations**

- Reported numbers are specific to one 8-chiplet configuration and to homogeneous-accelerator baselines; generalization to other application domains or larger chiplet pools needs further validation
- Results appear to be from simulation and design-space search; whether any design was fabricated and measured in silicon is unclear from available summaries and would need checking against the full paper
- Physical integration challenges — chiplet packaging, interconnect overhead, thermal management — may not be fully captured by this design-space exploration framework alone
- The computational cost of the surrogate models and evolutionary search, and how much of the pipeline must re-run as new applications are added, is not fully clear from secondary sources

**Terms to know**

- Chiplet: a small, separately fabricated die that is combined with others at the packaging stage to form a larger functional chip
- Non-recurring engineering (NRE) cost: the one-time cost of designing a chip and setting up its manufacturing process, independent of production volume
- BASIC (Bespoke Application-Specific IC): a custom accelerator assembled from a pool of chiplets to fit a specific application
- Processing-in-memory (PIM): a hardware architecture that performs computation inside or very close to memory to reduce data movement
- Surrogate-assisted evolutionary optimization: an evolutionary search technique that uses a fast approximate model to evaluate candidate designs, avoiding costly exact evaluation at every step
- Energy-delay-cost product: a composite metric multiplying energy, latency, and cost together to compare the overall efficiency of hardware designs

**Why it is worth watching**

As demand for AI hardware drives more application-specific accelerator designs, the cost of building a fully custom chip for every use case is becoming unsustainable. This work offers a concrete, quantified path — co-designing a small, reusable chiplet ecosystem alongside the accelerators built from it — that approaches full-custom efficiency while spreading design costs across many applications, making it a practical direction for the semiconductor industry's cost problem.

---

## My take

이 논문의 강점은 "칩렛을 재사용하면 좋다"는 직관을 넘어, 칩렛 풀 설계와 가속기 설계를 하나의 최적화 문제로 묶어 구체적 수치(완전 맞춤 설계 대비 4.1% 이내 차이)로 그 가능성을 보여준 점이다. 다만 공개된 요약 정보만으로는 실제 실리콘 제작·검증 여부와 더 넓은 응용·칩렛 풀로의 일반화 가능성을 확인하기 어려워, MICRO 2026 발표 이후 전체 논문과 공개된 아티팩트를 직접 확인하는 것이 좋겠다.

This paper's strength is moving beyond the general intuition that "chiplet reuse helps" to a concrete, quantified demonstration (within 4.1% of fully custom designs) by framing chiplet-pool design and accelerator design as one joint optimization. That said, based on available secondary summaries alone it's hard to confirm whether any design was fabricated and measured in silicon, or how well the approach generalizes to broader applications and larger chiplet pools — worth checking the full paper and released artifacts directly once the MICRO 2026 presentation materials are out.
