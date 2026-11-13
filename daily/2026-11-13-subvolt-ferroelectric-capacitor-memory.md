---
title: "Resolving the Kay–Dunn limit and the speed–endurance dilemma in ferroelectric Hf0.5Zr0.5O2 for DRAM-class sub-volt capacitors"
date: 2026-11-13
topic: semiconductors
tags: [semiconductors, memory, ferroelectrics, dram, hzo, device-engineering]
source: https://www.nature.com/articles/s41467-026-78705-4
---

# Resolving the Kay–Dunn limit and the speed–endurance dilemma in ferroelectric Hf0.5Zr0.5O2 for DRAM-class sub-volt capacitors

- Date: 2026-11-13
- Source: https://www.nature.com/articles/s41467-026-78705-4
- Topic: Semiconductors / memory devices
- Why it matters: It shows a path to a ferroelectric capacitor that switches fast at DRAM-like sub-volt voltages while also surviving far more read/write cycles than prior devices managed at those voltages, directly attacking a tradeoff that has limited ferroelectric memory as a DRAM alternative.

## Korean Summary

**한줄 요약**

서울대학교 연구팀이 중심이 된 연구진은 하프늄-지르코늄 산화물(Hf0.5Zr0.5O2, HZO) 강유전체 커패시터에서 전극 계면을 정밀하게 설계해, DRAM급의 낮은 전압(0.6~1V)에서도 빠른 분극 반전 속도와 긴 내구성을 동시에 달성했다고 발표했다. 이 논문은 2026년 10월 말 Nature Communications에 게재되었다.

**핵심 아이디어**

강유전체 메모리에서는 흔히 "속도-내구성 딜레마"가 존재한다. 더 빠르게 분극을 전환하려면 더 높은 전압이 필요한데, 전압이 높아지면 소자가 더 빨리 손상되어 내구성이 떨어진다. 이 연구는 강유전체 물질 자체를 바꾸는 대신 TiN 전극과 HZO 박막 사이의 계면을 조정해, 전압을 낮춰도 분극 반전이 느려지지 않도록 만들었다.

**무엇이 새로운가?**

- 전극 계면 공학만으로 0.6V에서 약 42.1ns, 1.0V에서 약 8.1ns의 분극 반전 속도를 달성.
- 20% 분극 손실 기준으로 0.6V에서 약 6000억(600 billion) 회, 1.0V에서 약 1조(1 trillion) 회의 스위칭 내구성을 확인하며 하드 브레이크다운이 관찰되지 않음.
- 초박막 HZO의 두께-보자력(coercive field) 스케일링 관계인 "Kay-Dunn 한계"를 재검토해, 유한 차단(finite-screening) 효과를 보정하면 지수가 약 -0.63으로 이론값(-2/3)에 가깝다는 것을 보임.
- 1트랜지스터-1커패시터(1T1C) 구조의 공통 플레이트 FeRAM(CP-FeRAM) 아키텍처를 제안하고 회로 시뮬레이션으로 읽기 동작을 평가.

**어떻게 작동하는가?**

연구팀은 5nm급 HZO 박막에 TiN 전극을 적용하면서, 전극의 플라즈마 처리 등으로 표면 구조와 화학적 특성을 조절했다. 이를 통해 전극-강유전체 계면에서 발생하는 전압 손실을 줄이고, 분극 반전에 필요한 핵생성(nucleation) 과정을 더 쉽게 일으킬 수 있도록 했다. 그 결과 낮은 전압에서도 충분한 구동력을 얻어 빠른 스위칭이 가능해졌고, 동시에 반복 스위칭에 따른 소자 손상도 줄어들어 내구성이 향상되었다. 이 메커니즘은 실제 소자에서 측정한 스위칭 시간과 반복 횟수, 그리고 Kay-Dunn 관계식에 대한 재해석으로 뒷받침된다.

**강점**

- 물질 자체의 큰 변경 없이 전극/계면 공학만으로 성능을 개선해, 기존 HZO 공정과의 호환성이 높을 가능성.
- 실제 소자 측정(스위칭 시간, 수조 회 단위의 사이클링 테스트)에 기반한 정량적 결과.
- DRAM 대체/보완 기술로서 구체적인 1T1C 메모리 아키텍처까지 제시.
- 삼성전자, 포항가속기연구소 등 산업·연구기관과의 협업으로 실용화 가능성에 대한 신뢰도 보강.

**한계**

- 제안된 CP-FeRAM 아키텍처는 아직 회로 시뮬레이션 단계이며, 실제 배열(array) 수준의 집적 및 양산 신뢰성은 검증되지 않음.
- "서브나노초" 수준의 극한 속도는 측정값이 아니라 핵생성 동역학 모델에 기반한 외삽(extrapolation)이라는 점에 유의해야 함.
- 보도자료와 2차 자료 간에 내구성 수치(사이클 수) 표기가 다소 엇갈려, 정확한 조건별 수치는 원문 확인이 필요함.
- 본 요약은 이 세션의 네트워크 정책상 해당 URL을 직접 불러올 수 없어, EurekAlert·semiengineering.com·techxplore 등 복수의 독립적인 2차 보도를 상호 대조하여 작성됨.

**알아둘 용어**

- 강유전체(Ferroelectric): 외부 전기장으로 분극 방향을 바꿀 수 있고, 전기장을 제거해도 분극 상태가 유지되는 물질.
- HZO (Hf0.5Zr0.5O2): 하프늄과 지르코늄 산화물을 혼합한 박막 강유전체 물질로, 기존 실리콘 반도체 공정과의 호환성이 높아 차세대 메모리 소재로 주목받음.
- 보자력(Coercive field): 강유전체의 분극 방향을 뒤집는 데 필요한 최소 전기장.
- Kay-Dunn 한계: 강유전체 박막의 두께가 얇아질수록 보자력이 일정한 지수 관계로 커진다는 경험적 스케일링 법칙.
- FeRAM (Ferroelectric RAM): 강유전체의 분극 상태를 이용해 데이터를 저장하는 비휘발성 메모리.
- 1T1C: 하나의 트랜지스터와 하나의 커패시터로 구성된 메모리 셀 구조(DRAM에서 흔히 쓰임).
- 내구성(Endurance): 메모리 소자가 손상 없이 견딜 수 있는 반복 읽기/쓰기(스위칭) 횟수.

**왜 주목할 만한가?**

DRAM 스케일링이 물리적 한계에 가까워지는 상황에서, 낮은 전압에서도 빠르고 내구성 있게 동작하는 강유전체 메모리는 DRAM의 유력한 대안 또는 보완 기술로 거론되어 왔다. 이 연구는 물질을 바꾸지 않고 전극 계면만 공학적으로 조정해 속도와 내구성을 동시에 끌어올렸다는 점에서, 기존 반도체 공정과의 호환성을 유지하면서 실용화 가능성을 높인 사례로 평가된다.

---

## English Summary

**One-line summary**

A team centered at Seoul National University engineered the electrode interface of a hafnium-zirconium oxide (Hf0.5Zr0.5O2, HZO) ferroelectric capacitor to achieve both fast polarization switching and high endurance at DRAM-class sub-volt voltages, a tradeoff that has historically limited ferroelectric memory. The paper was published in Nature Communications in late October 2026.

**Core idea**

Ferroelectric memory devices typically face a "speed-endurance dilemma": switching polarization faster requires higher voltage, but higher voltage accelerates device degradation and shortens endurance. Instead of changing the ferroelectric material itself, this work engineers the interface between the TiN electrode and the HZO thin film so that polarization switching stays fast even as the operating voltage is lowered.

**What is new?**

- Electrode-interface engineering alone yields polarization switching of about 42.1 ns at 0.6 V and about 8.1 ns at 1.0 V.
- Under a 20% polarization-loss endurance criterion, the devices sustained about 600 billion switching cycles at 0.6 V and about 1 trillion cycles at 1.0 V, with no hard electrical breakdown observed.
- The paper revisits the "Kay-Dunn limit," the empirical thickness-to-coercive-field scaling relation for ultrathin ferroelectric films, showing that after correcting for finite-screening effects the scaling exponent (~-0.63) is close to the theoretical -2/3 value.
- Proposes a common-plate FeRAM (CP-FeRAM) architecture using a 1-transistor-1-capacitor (1T1C) cell, with its read operation evaluated via circuit simulation.

**How does it work?**

The researchers fabricated ~5 nm HZO thin films with TiN electrodes, modifying the electrode's surface texture and chemistry (reportedly via plasma treatment) to reduce voltage loss at the electrode-ferroelectric interface. This interface engineering lowers the barrier for the nucleation process that initiates polarization reversal, so switching stays fast even when the applied voltage is reduced. Lower operating voltage in turn reduces the electrical stress that normally degrades the device over repeated cycling, improving endurance. The claims are backed by direct device measurements of switching time and cycling counts, plus a reanalysis of the Kay-Dunn scaling relation.

**Strengths**

- Improves performance mainly through electrode/interface engineering rather than a new material, suggesting compatibility with existing HZO process flows.
- Quantitative results from direct device measurements, including cycling tests reaching into the hundreds of billions to trillion-cycle range.
- Goes beyond a single device demonstration to propose a concrete 1T1C memory architecture (CP-FeRAM).
- Collaboration with Samsung Electronics and the Pohang Accelerator Laboratory lends some credibility to eventual manufacturability.

**Limitations**

- The proposed CP-FeRAM architecture has only been evaluated through circuit simulation; array-level integration and manufacturing-grade reliability remain unverified.
- Sub-nanosecond switching speeds mentioned in coverage are extrapolations from nucleation-kinetics models, not direct measurements.
- Secondary sources show minor inconsistencies in the exact endurance figures reported, so the precise numbers under each condition should be checked against the original paper.
- Due to this session's network policy, the source URL could not be fetched directly; this summary was cross-checked against multiple independent secondary reports (EurekAlert, semiengineering.com, techxplore) rather than the primary Nature Communications page itself.

**Terms to know**

- Ferroelectric: A material whose electric polarization can be switched by an external field and remains in that state after the field is removed.
- HZO (Hf0.5Zr0.5O2): A hafnium-zirconium oxide thin-film ferroelectric material valued for its compatibility with standard silicon semiconductor processes.
- Coercive field: The minimum electric field required to reverse a ferroelectric material's polarization direction.
- Kay-Dunn limit: An empirical scaling law describing how coercive field increases as ferroelectric film thickness decreases.
- FeRAM (Ferroelectric RAM): Non-volatile memory that stores data using a ferroelectric material's polarization state.
- 1T1C: A memory cell design using one transistor and one capacitor, the standard DRAM cell structure.
- Endurance: The number of read/write (switching) cycles a memory device can withstand before failing.

**Why it is worth watching**

As DRAM scaling approaches physical limits, ferroelectric memory that can switch fast and endure many cycles at low voltage has long been proposed as a DRAM alternative or complement. This work is notable for improving both speed and endurance simultaneously through electrode-interface engineering alone, without changing the base material, which keeps it closer to existing semiconductor manufacturing and makes practical adoption more plausible.

---

## My take

이 연구는 강유전체 메모리의 핵심 걸림돌이었던 속도-내구성 딜레마를 전극 계면 공학이라는 비교적 공정 친화적인 방법으로 완화했다는 점에서 의미가 있다. 다만 제시된 수치들은 단일 소자 수준의 측정이며, 실제 대규모 메모리 어레이로 확장했을 때의 균일성과 수율, 그리고 CP-FeRAM 아키텍처의 실제 동작 검증은 아직 이루어지지 않았다. 또한 이 요약은 네트워크 제약으로 원문을 직접 확인하지 못하고 복수의 2차 보도를 종합한 것이므로, 정확한 수치나 세부 조건은 원문 공개 시 재확인이 필요하다.

This work is notable for addressing the ferroelectric speed-endurance dilemma through a relatively process-friendly route (electrode-interface engineering) rather than a new material system. That said, the reported numbers are single-device measurements, and array-level uniformity, yield, and the actual operation of the proposed CP-FeRAM architecture have not yet been demonstrated. This summary was also compiled from multiple secondary reports rather than the primary source, since this session's network policy blocked direct access to the paper; exact figures and conditions should be re-verified against the original publication when accessible.
