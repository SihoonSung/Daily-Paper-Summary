---
title: "Optimal Control Drives Ultrafast and Energy-Efficient Magnetization Switching in Van der Waals Magnets"
date: 2026-09-10
topic: semiconductors
tags: [semiconductors, spintronics, mram, memory-technology, van-der-waals-magnets, energy-efficient-computing]
source: https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202523059
---

Optimal Control Drives Ultrafast and Energy-Efficient Magnetization Switching in Van der Waals Magnets

- Date: 2026-09-10
- Source: https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202523059
- Topic: semiconductors (spintronic memory)
- Why it matters: It shows that mathematically optimized magnetic-field pulses, rather than blunt fixed pulses, can flip magnetic memory bits up to two orders of magnitude more efficiently, pointing to a path toward memory technology that could sharply cut the energy cost of data storage and AI computing.

## Korean Summary

**한줄 요약**

에든버러 대학교 연구진이 최적 제어 이론(optimal control theory)을 이용해 반데르발스(van der Waals) 자성 물질의 자화 방향을 피코초(ps) 단위로, 기존 방식보다 최대 100배 적은 에너지로 뒤집는 방법을 시뮬레이션으로 제시했다. 이는 다음 세대 자기저항 메모리(MRAM)의 에너지 효율을 획기적으로 높일 수 있는 새로운 설계 원리다.

**핵심 아이디어**

기존 자기 메모리는 정해진 형태의 자기장이나 전류 펄스를 강하게 걸어 자화 방향을 강제로 뒤집는 방식이라 에너지 손실이 크다. 이 논문은 목표 상태에 도달하기 위한 가장 효율적인 경로를 수학적으로 계산하는 최적 제어 이론을 적용해, 물질의 감쇠(damping)와 자기 이방성(anisotropy) 같은 고유 특성에 맞춰 정교하게 모양이 설계된 자기장 펄스를 만들어냈다. 이렇게 하면 훨씬 적은 에너지로도 빠르고 확실하게 자화를 반전시킬 수 있다.

**무엇이 새로운가?**

- 최적 제어 이론을 반데르발스 자성 소재(Fe3GaTe2, Fe3GeTe2, CrSBr) 세 종류에 적용해 시뮬레이션으로 검증
- 균일한 스핀 회전을 1~10피코초 안에 완료 (기존 스핀-전달 토크·스핀-궤도 토크 방식과 비슷하거나 더 빠른 속도)
- 스위칭 에너지가 0.94~9.7나노줄로, 기존 자기장 방식(42.8~91.2나노줄)보다 최대 2자릿수(최대 약 100배) 낮음
- 필요한 자기장 세기도 기존 방식보다 10배 이상 작음
- 이론적으로는 펨토줄(fJ) 수준까지 에너지를 낮춰 DRAM, STT-MRAM, SOT-MRAM 등 기존·차세대 메모리 기술보다 우수할 잠재력 제시

**어떻게 작동하는가?**

1. 목표: 특정 반데르발스 자성 물질의 자화 벡터를 초기 상태에서 반대 방향(반전된 상태)으로 옮기는 것
2. 물질의 감쇠 계수, 자기 이방성 등 물성 매개변수를 반영한 스핀 동역학 모델(예: Landau-Lifshitz-Gilbert 방정식 계열)을 구성
3. 최적 제어 이론으로 "에너지를 최소화하면서 정해진 시간 안에 목표 상태에 도달"하는 자기장 펄스의 시간에 따른 파형을 계산
4. 이렇게 설계된 비정형(non-uniform) 펄스를 시뮬레이션에 적용해 스위칭 속도와 에너지 소모를 측정
5. 기존의 고정된 형태(구형파 등) 펄스를 사용한 경우와 비교해 성능 향상 폭을 정량화

**강점**

- 특정 물질에만 국한되지 않고 여러 반데르발스 자성체에 적용 가능한 일반적 설계 프레임워크
- 속도(피코초)와 에너지 효율(나노줄~펨토줄) 두 마리 토끼를 동시에 달성
- 이론상 에너지 소모의 물리적 하한선인 란다우어 한계(Landauer limit)에 더 가까이 접근할 수 있음을 시사
- 데이터센터·AI 연산의 급증하는 메모리 에너지 수요 문제에 직접적으로 대응하는 실용적 방향 제시

**한계**

- 현재까지는 컴퓨터 시뮬레이션 결과이며, 실제 소자에서의 실험적 검증은 아직 이루어지지 않음
- 정교하게 시간에 따라 변하는 자기장 펄스를 실제 칩 수준에서 값싸고 정밀하게 생성할 수 있는 하드웨어 기술이 별도로 필요
- 열 요동, 소자 간 편차 등 실제 제조 환경에서 발생하는 변수는 시뮬레이션에 충분히 반영되지 않았을 수 있음
- 상용화까지는 소자 집적, 신뢰성, 반복 내구성 등 추가 검증이 필요

**알아둘 용어**

- 반데르발스 자성체(van der Waals magnet): 층상 구조를 가지며 얇은 층으로 쉽게 박리할 수 있는 자성을 띠는 물질
- 최적 제어 이론(optimal control theory): 주어진 제약 조건 하에서 목표를 가장 효율적으로 달성하는 입력(제어) 신호를 수학적으로 찾는 이론
- MRAM(자기저항 메모리): 자화 방향으로 0과 1을 저장하는 비휘발성 메모리 기술
- STT/SOT(스핀-전달/스핀-궤도 토크): 전류를 이용해 자화 방향을 바꾸는 기존 MRAM 스위칭 방식
- 란다우어 한계(Landauer limit): 1비트의 정보를 처리(삭제)하는 데 필요한 최소 에너지에 대한 열역학적 하한선
- 자기 이방성(anisotropy): 자성체가 특정 방향으로 자화되기 쉬운 성질

**왜 주목할 만한가?**

AI와 데이터센터의 확산으로 메모리 연산의 전력 소비가 빠르게 커지는 상황에서, 이 연구는 하드웨어 자체를 바꾸지 않고도(펄스 파형 설계만으로) 메모리 스위칭 에너지를 획기적으로 낮출 수 있다는 가능성을 제시한다. 아직 시뮬레이션 단계지만, 최적 제어라는 수학적 도구를 스핀트로닉스에 접목한 접근은 향후 초저전력 메모리 설계의 새로운 기준이 될 수 있다.

---

## English Summary

**One-line summary**

Researchers at the University of Edinburgh used optimal control theory to design precisely shaped magnetic-field pulses that flip the magnetization of van der Waals magnetic materials within picoseconds while using up to two orders of magnitude less energy than conventional switching methods, in simulation.

**Core idea**

Today's magnetic memory technologies switch magnetization using fixed, "blunt-force" current or field pulses, which wastes energy. This paper instead applies optimal control theory — a mathematical framework for finding the most efficient way to steer a system to a target state — to compute custom, time-varying magnetic-field waveforms tailored to a material's own damping and anisotropy properties, achieving fast, reliable switching at a fraction of the energy cost.

**What is new?**

- Applies optimal control theory to three representative van der Waals magnets (Fe3GaTe2, Fe3GeTe2, CrSBr) in simulation
- Achieves uniform spin-rotation switching within 1-10 picoseconds, matching or beating conventional spin-transfer-torque (STT) and spin-orbit-torque (SOT) switching speeds
- Cuts switching energy to 0.94-9.7 nanojoules, up to about two orders of magnitude below conventional field-pulse protocols (42.8-91.2 nanojoules)
- Requires field amplitudes more than tenfold smaller than standard approaches
- Suggests femtojoule-scale switching is achievable by exploiting material-specific parameters, potentially surpassing DRAM, STT-MRAM, and emerging SOT-MRAM

**How does it work?**

1. Define the goal: reverse the magnetization vector of a van der Waals magnetic material from an initial to a target (flipped) orientation
2. Build a spin-dynamics model (based on equations such as the Landau-Lifshitz-Gilbert framework) incorporating the material's damping coefficient and magnetic anisotropy
3. Use optimal control theory to compute the time-dependent magnetic-field waveform that reaches the target state within a set time while minimizing energy
4. Simulate the resulting non-uniform pulse and measure switching speed and energy consumption
5. Compare against fixed-shape (e.g., square-wave) pulses used in conventional protocols to quantify the improvement

**Strengths**

- A general design framework applicable across multiple van der Waals magnetic materials, not tied to one specific compound
- Simultaneously achieves high switching speed (picoseconds) and high energy efficiency (nanojoule to femtojoule range)
- Suggests a path toward approaching the Landauer limit, the fundamental thermodynamic floor on the energy needed to process one bit
- Offers a concrete, practical direction for addressing the rapidly growing memory-energy demands of data centers and AI workloads

**Limitations**

- Results are currently based on computer simulation; experimental validation in real devices has not yet been reported
- Generating precisely shaped, time-varying field pulses cheaply and accurately at the chip level requires separate hardware advances
- Simulations may not fully capture real-world manufacturing variability such as thermal fluctuations and device-to-device variation
- Further work on integration, reliability, and endurance is needed before this could become a commercial memory technology

**Terms to know**

- Van der Waals magnet: a layered magnetic material that can be easily exfoliated into thin, atomically precise layers
- Optimal control theory: a mathematical framework for finding the input signal that most efficiently drives a system to a desired state under given constraints
- MRAM (magnetoresistive random-access memory): non-volatile memory that stores bits as magnetization direction
- STT/SOT (spin-transfer/spin-orbit torque): conventional current-driven mechanisms used to switch magnetization in today's MRAM
- Landauer limit: the thermodynamic lower bound on the energy required to process (erase) one bit of information
- Anisotropy: a material property describing a magnet's preference to align along particular directions

**Why it is worth watching**

As AI and data-center growth drives memory energy consumption sharply upward, this work shows that switching energy can potentially be slashed dramatically through smarter pulse design alone, without necessarily requiring new materials or device architectures. While still simulation-based, borrowing optimal control — a tool more familiar from quantum control and robotics — for spintronic memory design points to a promising new direction for ultra-low-power memory.

---

## My take

이 연구는 아직 시뮬레이션 단계이지만, 접근 방식 자체가 참신하다. 소재나 소자 구조를 바꾸는 대신 "펄스를 어떻게 설계하느냐"라는 소프트웨어적 최적화만으로 에너지 효율을 크게 높일 수 있다는 점은 실용적 파급력이 크다. 다만 실제 칩에서 이런 정교한 펄스를 값싸게 구현할 수 있는지, 그리고 실험적으로 재현되는지는 아직 확인되지 않았으므로, 상용화까지는 상당한 검증 기간이 필요해 보인다.

This work is still simulation-only, but the approach itself is genuinely fresh: rather than inventing new materials or device structures, it shows that a purely algorithmic optimization of the pulse waveform can deliver large energy-efficiency gains, which is a practically appealing angle. The open questions are whether such precisely shaped pulses can be generated cheaply on real chips and whether the predicted gains hold up experimentally — so meaningful validation is still needed before this could move toward commercial memory technology.
