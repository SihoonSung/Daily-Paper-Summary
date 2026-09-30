---
title: "Monolithic 3D Integration of Atomic-Layer-Deposited Oxide Semiconductors on 200-mm Silicon Wafers"
date: 2026-09-30
topic: semiconductors
tags: [semiconductors, 3d-integration, oxide-semiconductor, chip-fabrication, beol, computing-in-memory]
source: https://doi.org/10.1038/s41565-026-02276-0
---

Monolithic 3D Integration of Atomic-Layer-Deposited Oxide Semiconductors on 200-mm Silicon Wafers

- Date: 2026-09-30
- Source: https://doi.org/10.1038/s41565-026-02276-0 (preprint: https://arxiv.org/abs/2608.09508)
- Topic: semiconductors (3D chip integration)
- Why it matters: Purdue researchers stacked three tiers of transistors directly on top of one another on full 200-mm silicon wafers using a low-temperature, CMOS-compatible process, fabricating over 100,000 working devices with high uniformity — a concrete step toward true monolithic 3D chips that pack more compute into the same footprint without the wiring bottlenecks of today's stacked-chip packaging.

## Korean Summary

**한줄 요약**

퍼듀대학교 연구진이 원자층증착(ALD) 산화물 반도체인 산화인듐(InOx)을 이용해 200mm 실리콘 웨이퍼 위에 트랜지스터 3개 층을 곧바로 쌓아 올리는 웨이퍼 스케일 모놀리식 3차원(M3D) 집적을 시연했다. 10만 개가 넘는 소자를 제작해 높은 균일성과 작동 회로를 확인했으며, 이를 이용해 거대언어모델(LLM) 연산에 특화된 4층 컴퓨팅-인-메모리(CIM) 가속기까지 구현했다.

**핵심 아이디어**

기존 3D 칩 적층 기술(예: 실리콘관통전극, TSV)은 완성된 칩들을 따로 만든 뒤 본딩하는 방식이라 층 사이 배선 밀도와 정렬 정밀도에 한계가 있다. 반면 모놀리식 3D 집적은 아래층 회로 위에 새로운 반도체 층을 직접 증착·가공해 쌓아 올리는 방식으로, 훨씬 촘촘한 층간 연결이 가능하다. 문제는 새 층을 만들 때 필요한 고온 공정이 이미 완성된 아래층의 구리 배선과 트랜지스터를 손상시킨다는 점인데, 이 논문은 약 225°C의 저온 원자층증착으로 산화인듐 박막을 균일하게 증착함으로써 이 문제를 해결했다.

**무엇이 새로운가?**

- 200mm 실리콘 웨이퍼 전체에 강유전체(ferroelectric), 증가형(enhancement-mode), 감소형(depletion-mode) 산화인듐 전계효과트랜지스터 3개 층을 모놀리식으로 집적
- 10만 개 이상의 소자를 웨이퍼 스케일로 제작해 대규모 통계적 균일성 입증 (문턱전압 표준편차 최저 0.04V)
- 평균 전자 이동도 최대 91.6 cm²/V·s 달성과 함께 층을 넘나드는(cross-tier) 완전 동작 회로 구현
- 약 225°C의 저온·BEOL(후공정) 호환 ALD 공정으로, 기존 하부 배선·트랜지스터를 손상시키지 않고 새 반도체 층을 그 위에 직접 형성
- 이 플랫폼으로 4층 3D 컴퓨팅-인-메모리(CIM) 가속기를 제작해 LLM 워크로드에서 2D 기준 대비 1.4~2.9배 속도 향상과 에너지-지연 곱 개선을 실증

**어떻게 작동하는가?**

1. 실리콘 CMOS 로직이 형성된 200mm 웨이퍼 위에 원자층증착(ALD)으로 나노미터 두께의 산화인듐(InOx) 박막을 저온(약 225°C)에서 균일하게 증착
2. 이 박막을 패터닝해 강유전체, 증가형, 감소형 등 다양한 특성의 전계효과트랜지스터를 한 층에 제작
3. 이미 만들어진 층 위에 절연층을 형성한 뒤, 같은 저온 ALD 공정을 반복해 두 번째, 세 번째 트랜지스터 층을 순차적으로 적층 — 각 단계가 하부 층에 열 손상을 주지 않음
4. 층 간 비아(via)로 각 티어의 트랜지스터를 전기적으로 연결해 층을 넘나드는 회로와 4층 컴퓨팅-인-메모리 가속기 구조를 완성
5. 커스텀 InOx 공정설계키트(PDK)를 이용해 이 가속기를 LLM 연산 시뮬레이션에 적용, 2D(단층) 기준 설계 대비 속도와 에너지 효율을 측정·비교

**강점**

- 실험실 규모 데모가 아니라 상용 파운드리 표준인 200mm 웨이퍼 전체에서 재현성을 입증한 것이 실용화 가능성을 크게 높임
- 저온 공정이라 기존 실리콘 CMOS 후공정(BEOL)과 호환되어, 완전히 새로운 제조 인프라 없이 기존 팹에 도입할 여지가 있음
- 10만 개 이상 소자의 통계로 균일성을 정량화해 신뢰성 근거를 제시
- 메모리와 연산을 물리적으로 가깝게 배치하는 컴퓨팅-인-메모리 구조로 AI 가속기의 데이터 이동 병목을 직접 겨냥

**한계**

- 산화인듐 기반 트랜지스터의 이동도(91.6 cm²/V·s)는 실리콘 대비 높은 편이지만, 최고 성능 실리콘/화합물 반도체 트랜지스터에는 아직 못 미칠 수 있음
- 3개 층 집적은 시연되었으나, 상용 적층 메모리 수준(수십 층)까지 확장 시 수율·정렬·방열 문제는 별도로 검증 필요
- 장기 신뢰성(열화, 바이어스 스트레스 내구성)과 대량 양산 시 수율에 대한 데이터는 이번 논문만으로는 충분히 확인되지 않음
- 4층 CIM 가속기의 성능 향상(1.4~2.9배)은 특정 LLM 워크로드·비교 기준에서의 결과로, 일반화 가능성은 추가 검증이 필요

**알아둘 용어**

- 모놀리식 3D 집적(Monolithic 3D, M3D): 완성된 칩들을 접합하는 대신, 하나의 기판 위에 반도체 층을 순차적으로 직접 증착·가공해 쌓는 3차원 집적 방식
- 원자층증착(Atomic Layer Deposition, ALD): 원자 단위 두께로 박막을 한 층씩 정밀하게 쌓아 올리는 저온 증착 공정
- 후공정 호환(BEOL-compatible): 이미 만들어진 배선·트랜지스터 층에 열 손상을 주지 않을 만큼 낮은 온도에서 이루어져, 반도체 후공정 단계에 도입할 수 있는 공정 특성
- 산화인듐(Indium Oxide, InOx): 얇은 막으로도 높은 전자 이동도를 보이는 산화물 반도체 소재
- 컴퓨팅-인-메모리(Computing-in-Memory, CIM): 메모리 소자 안에서 직접 연산을 수행해 데이터를 멀리 이동시키지 않아도 되게 하는 컴퓨팅 구조
- 문턱전압(Threshold voltage): 트랜지스터가 켜지기 시작하는 게이트 전압으로, 그 편차가 작을수록 소자 균일성이 높음

**왜 주목할 만한가?**

AI 반도체 수요가 급증하면서 더 많은 트랜지스터를 같은 면적에 채워 넣는 3차원 집적이 업계의 핵심 과제로 떠오르고 있다. 이 연구는 실험실 수준을 넘어 표준 200mm 웨이퍼에서 저온·후공정 호환 공정으로 다층 트랜지스터를 안정적으로 쌓을 수 있음을 대규모로 입증했다는 점에서, 향후 3D 로직-메모리 통합 칩 제조 방식에 실질적인 참고 사례가 될 수 있다.

---

## English Summary

**One-line summary**

Researchers at Purdue University demonstrated wafer-scale monolithic 3D (M3D) integration of three transistor tiers made of atomic-layer-deposited indium oxide (InOx) on full 200-mm silicon wafers, fabricating over 100,000 devices and building a four-tier computing-in-memory (CIM) accelerator for large-language-model workloads on top of the platform.

**Core idea**

Conventional 3D chip stacking (e.g., through-silicon vias) bonds separately manufactured chips together, which limits how densely the layers can be interconnected. Monolithic 3D integration instead deposits and processes new semiconductor layers directly on top of already-finished circuitry, enabling much denser inter-layer connections — but the high temperatures normally needed to form new transistor layers would damage the copper wiring and devices already built below. This paper solves that problem by depositing indium oxide thin films uniformly at a low temperature (~225°C) using atomic layer deposition, keeping the process compatible with existing back-end-of-line (BEOL) fabrication.

**What is new?**

- Monolithically stacks three tiers of indium oxide field-effect transistors — ferroelectric, enhancement-mode, and depletion-mode — across a full 200-mm silicon wafer
- Fabricates over 100,000 devices at wafer scale, demonstrating statistical uniformity (threshold-voltage standard deviation as low as 0.04 V)
- Achieves average electron mobility up to 91.6 cm²V⁻¹s⁻¹ along with fully functional cross-tier circuits
- Uses a ~225°C, BEOL-compatible ALD process so each new layer avoids damaging the finished circuitry underneath it
- Builds a four-tier 3D computing-in-memory (CIM) accelerator on this platform, delivering 1.4×–2.9× speedup and comparable energy-delay-product improvements over 2D baselines on LLM workloads

**How does it work?**

1. Start with a 200-mm silicon wafer carrying finished CMOS logic, then deposit a nanometer-thin indium oxide (InOx) film uniformly at low temperature (~225°C) via atomic layer deposition
2. Pattern this film into field-effect transistors with different characteristics (ferroelectric, enhancement-mode, depletion-mode) to form one device tier
3. Form an insulating layer over that tier and repeat the same low-temperature ALD process to build a second and then a third transistor tier, each step avoiding thermal damage to the layers below
4. Connect the tiers electrically through inter-tier vias to realize functional cross-tier circuits and a four-tier computing-in-memory accelerator architecture
5. Use a custom InOx process design kit (PDK) to simulate this accelerator on large-language-model workloads, comparing speed and energy efficiency against conventional 2D (single-tier) baselines

**Strengths**

- Demonstrated at full 200-mm wafer scale rather than a small lab sample, which is directly relevant to how commercial foundries operate
- Low process temperature keeps it compatible with existing silicon CMOS back-end-of-line flow, suggesting a path to adoption without entirely new fab infrastructure
- Statistical evidence from over 100,000 devices gives a concrete, quantified basis for uniformity and reliability claims
- The computing-in-memory architecture directly targets the data-movement bottleneck that limits today's AI accelerators by placing memory and compute physically close together

**Limitations**

- The mobility of indium oxide transistors (91.6 cm²V⁻¹s⁻¹), while high for an oxide semiconductor, may still trail the best silicon or compound-semiconductor transistors
- Only three tiers were demonstrated; scaling to the dozens of layers used in commercial 3D memory would raise separate yield, alignment, and thermal-management challenges that remain to be verified
- Long-term reliability (degradation, bias-stress endurance) and yield under mass production are not fully established by this single study
- The reported 1.4×–2.9× accelerator speedup is specific to the LLM workloads and 2D baselines tested, so how broadly it generalizes needs further validation

**Terms to know**

- Monolithic 3D (M3D) integration: stacking semiconductor layers by depositing and processing them directly on a single substrate, rather than bonding separately fabricated chips together
- Atomic layer deposition (ALD): a low-temperature thin-film deposition technique that builds up material one atomic layer at a time with precise thickness control
- BEOL-compatible: a process gentle enough (low temperature) to avoid damaging the interconnects and transistors already fabricated in earlier back-end-of-line steps
- Indium oxide (InOx): an oxide semiconductor material that can achieve relatively high electron mobility even as an ultra-thin film
- Computing-in-memory (CIM): a computing architecture that performs computation directly within memory elements to reduce data movement between memory and processor
- Threshold voltage: the gate voltage at which a transistor turns on; a smaller variation across devices indicates higher fabrication uniformity

**Why it is worth watching**

As demand for AI hardware pushes the industry toward packing more transistors into the same chip footprint, this work shows — at full production wafer scale rather than in a small lab demo — that multiple transistor tiers can be reliably stacked using a low-temperature, BEOL-compatible process. That combination of scale, uniformity data, and a working multi-tier accelerator makes it a concrete reference point for how future 3D logic-memory chips might actually be manufactured.

---

## My take

이 연구의 가장 인상적인 부분은 "될 것 같다"는 개념 증명이 아니라, 실제 200mm 웨이퍼 전체와 10만 개가 넘는 소자로 균일성을 통계적으로 보여줬다는 점이다. 다만 3개 층 집적과 소규모 CIM 가속기 시연이 실제 상용 3D 로직-메모리 칩 양산으로 이어지려면 층수 확장, 방열, 장기 신뢰성 등에서 갈 길이 남아 있어, 아직은 유망한 플랫폼 검증 단계로 보는 것이 정확하다.

The most striking part of this work is not a "this should work in principle" demo, but statistically grounded uniformity data from a full 200-mm wafer and over 100,000 devices. That said, turning three-tier integration and a small-scale CIM accelerator demo into an actual commercial 3D logic-memory chip will still require progress on scaling tier count, thermal management, and long-term reliability — so it is best read as a strong platform validation step rather than a finished manufacturing solution.
