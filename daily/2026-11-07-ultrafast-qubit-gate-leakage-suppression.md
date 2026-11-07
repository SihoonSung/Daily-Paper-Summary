---
title: "Ultrafast single-qubit gates through multi-photon transition removal"
date: 2026-11-07
topic: quantum-computing
tags: [quantum-computing, superconducting-qubits, transmon, pulse-shaping, gate-fidelity, quantum-error-correction]
source: https://www.nature.com/articles/s41467-026-78373-4
---

Ultrafast single-qubit gates through multi-photon transition removal

* Date: 2026-11-07
* Source: https://www.nature.com/articles/s41467-026-78373-4
* Topic: quantum-computing
* Why it matters: Faster, more accurate single-qubit gates directly reduce the error budget that quantum error correction has to absorb, which is one of the main obstacles standing between today's noisy superconducting quantum processors and fault-tolerant quantum computing.

## Korean Summary

**한줄 요약**

독일 Forschungszentrum Jülich, RWTH Aachen University, University of Cologne 연구진이 초전도 트랜스몬(transmon) 큐비트에서 6.8나노초 만에 99.98% 이상의 정확도를 가지는 단일 큐비트 게이트를 구현했다고 발표했다. 이는 펄스 모양을 더 정교하게 설계해 원치 않는 고차 전이(leakage)를 억제함으로써 달성한 결과다.

**핵심 아이디어**

초전도 큐비트를 빠르게 제어하려면 짧고 강한 마이크로파 펄스를 써야 하는데, 펄스가 짧아질수록 큐비트가 계산에 사용하지 않는 상위 에너지 준위로 새어나가는 "누설(leakage)" 오류가 커진다. 기존에는 DRAG(Derivative Removal by Adiabatic Gate)라는 펄스 보정 기법으로 이 문제를 줄여왔지만, 더 짧은 펄스에서는 DRAG만으로 억제되지 않는 다광자(multi-photon) 전이가 새로운 오류원이 된다. 이 논문은 DRAG를 재귀적으로 두 번 적용하는 R2D라는 보정 기법을 제안해 이 다광자 전이까지 추가로 억제했다.

**무엇이 새로운가?**

* DRAG를 한 단계 더 확장한 "R2D(이중 재귀 DRAG)" 펄스 보정 기법을 제시했다.
* 단일 고립 트랜스몬 큐비트에서 6.8나노초의 매우 짧은 게이트 시간에 99.98%를 넘는 충실도(fidelity)를 달성했다.
* 두 가지 기본 게이트 연산에서 각각 99.981%, 99.989%의 정확도를 보고했다.
* 게이트당 누설 오류를 2.0×10⁻⁵ 미만으로 낮췄으며, 기존 DRAG 대비 원치 않는 다광자 전이를 20배 이상 줄였다고 보고했다.

**어떻게 작동하는가?**

1. Jülich의 헬름홀츠 나노 시설(Helmholtz Nano Facility)에서 제작한 초전도 트랜스몬 큐비트를 사용한다.
2. 큐비트를 짧은 시간에 제어하기 위해 강한 마이크로파 펄스를 인가하되, 펄스의 위상과 진폭을 DRAG 방식으로 1차 보정한다.
3. 여기에 더해, 더 높은 에너지 준위로의 다광자 전이를 억제하도록 보정을 한 번 더 재귀적으로 적용하는 R2D 기법을 더한다.
4. 보정된 펄스를 이용해 두 가지 기본 단일 큐비트 연산을 수행하고, 각 연산의 충실도와 누설 오류를 측정해 성능을 검증한다.

**강점**

* 초전도 큐비트 플랫폼(IBM, Google 등이 사용하는 것과 같은 계열)에 비교적 쉽게 적용 가능한 순수 펄스 설계 기법으로, 하드웨어 자체를 바꿀 필요가 없다.
* 게이트 속도와 정확도를 동시에 개선해, 양자 오류 정정에 필요한 물리 큐비트 수와 오버헤드를 줄일 잠재력이 있다.
* 기존 표준 기법인 DRAG와 직접 비교해 정량적인 개선폭(20배 이상의 누설 억제)을 제시했다.

**한계**

* 실험은 단일 고립 트랜스몬 큐비트 하나에서만 수행되었으며, 여러 큐비트로 이루어진 실제 프로세서나 2큐비트 게이트에서도 같은 개선이 유지되는지는 아직 검증되지 않았다.
* 저자 명단과 세부 수치 일부는 2차 보도자료를 통해 확인한 것으로, Nature Communications 원문의 모든 세부 조건(온도, 큐비트 설계 변형 등)까지 확인하지는 못했다.
* 다른 큐비트 플랫폼(스핀 큐비트, 이온트랩 등)에 이 기법이 그대로 적용될지는 불확실하다.

**알아둘 용어**

* **트랜스몬(transmon)**: 널리 쓰이는 초전도 큐비트의 한 종류로, 전하 잡음에 덜 민감하도록 설계된 조셉슨 접합 기반 회로.
* **DRAG(Derivative Removal by Adiabatic Gate)**: 짧은 펄스로 큐비트를 제어할 때 발생하는 누설 오류를 줄이기 위해 펄스 파형에 보정항을 추가하는 표준 기법.
* **누설(leakage)**: 큐비트가 0/1 두 계산 상태를 벗어나 상위 에너지 준위로 빠져나가는 오류.
* **충실도(fidelity)**: 실제 수행된 양자 연산이 이상적인 목표 연산과 얼마나 일치하는지를 나타내는 척도.
* **다광자 전이(multi-photon transition)**: 하나의 펄스가 여러 광자를 흡수한 것과 같은 효과를 내 더 높은 에너지 준위로 건너뛰는 원치 않는 전이.
* **양자 오류 정정(quantum error correction)**: 물리적 큐비트의 오류를 여러 큐비트로 중복 인코딩해 논리적으로 정정하는 기법으로, 물리 게이트의 오류율이 낮을수록 필요한 자원이 줄어든다.

**왜 주목할 만한가?**

현재 초전도 큐비트 기반 양자컴퓨터들의 가장 큰 병목 중 하나는 게이트 오류율이며, 이는 오류 정정에 필요한 물리 큐비트 수를 기하급수적으로 늘리는 원인이다. 이 연구처럼 하드웨어 변경 없이 펄스 설계만으로 속도와 정확도를 동시에 개선할 수 있다면, IBM이나 Google 등이 쓰는 기존 초전도 큐비트 칩에도 비교적 빠르게 적용될 수 있어 실질적인 파급력이 크다.

---

## English Summary

**One-line summary**

Physicists from Forschungszentrum Jülich, RWTH Aachen University, and the University of Cologne report single-qubit gates on a superconducting transmon qubit running in just 6.8 nanoseconds with fidelities above 99.98%, achieved by extending standard pulse-shaping to suppress higher-order "leakage" errors that normal corrections miss.

**Core idea**

Controlling a superconducting qubit quickly requires short, strong microwave pulses, but shorter pulses increase "leakage" — unwanted population of energy levels outside the computational 0/1 subspace. The standard fix, DRAG (Derivative Removal by Adiabatic Gate), corrects much of this, but at very short gate times a residual source of error remains: multi-photon transitions to levels beyond the nearest excited state, which plain DRAG does not fully suppress. The paper introduces R2D, a doubly recursive extension of DRAG, to additionally cancel these multi-photon transitions.

**What is new?**

* A new pulse-shaping correction, R2D (recursive double DRAG), that extends the standard DRAG technique to suppress multi-photon leakage.
* Single-qubit gates on an isolated transmon qubit at a 6.8 ns gate duration with fidelity above 99.98%.
* Reported fidelities of 99.981% and 99.989% for two fundamental single-qubit operations.
* Per-gate leakage error reduced to below 2.0 × 10⁻⁵, with unwanted multi-photon transitions cut by more than 20-fold compared with standard DRAG.

**How does it work?**

1. The team uses a superconducting transmon qubit fabricated at the Helmholtz Nano Facility at Forschungszentrum Jülich.
2. Short microwave pulses drive the qubit; their envelope is first corrected using standard DRAG to cancel first-order leakage.
3. A second, recursive correction (R2D) is layered on top to specifically suppress multi-photon transitions to higher energy levels that DRAG alone leaves behind.
4. The corrected pulses are used to perform two fundamental single-qubit operations, with gate fidelity and leakage measured to validate performance.

**Strengths**

* A purely pulse-level technique applicable to the same superconducting qubit architectures used by companies like IBM and Google, without requiring new hardware.
* Simultaneously improves gate speed and accuracy, which could reduce the physical-qubit overhead needed for quantum error correction.
* Provides a direct, quantified comparison against the widely used DRAG baseline (over 20x less leakage).

**Limitations**

* Demonstrated on a single, isolated transmon qubit; it remains to be shown whether the same gains hold in multi-qubit processors or extend to two-qubit gates.
* Some details, including author names, were confirmed through secondary press coverage (press releases and specialist outlets) rather than the full Nature Communications text, since not every experimental detail could be independently verified.
* It is unclear whether the R2D approach transfers directly to other qubit modalities, such as spin qubits or trapped ions.

**Terms to know**

* **Transmon**: A widely used type of superconducting qubit based on a Josephson-junction circuit, designed to be less sensitive to charge noise.
* **DRAG (Derivative Removal by Adiabatic Gate)**: A standard pulse-shaping correction that reduces leakage errors caused by driving a qubit with short, fast pulses.
* **Leakage**: An error in which a qubit escapes its intended 0/1 computational subspace into higher energy levels.
* **Fidelity**: A measure of how closely an actual quantum operation matches its ideal target operation.
* **Multi-photon transition**: An unwanted transition in which a pulse effectively drives the qubit to a much higher energy level, as if multiple photons were absorbed at once.
* **Quantum error correction**: Encoding one logical qubit across many physical qubits to correct errors; lower physical gate error rates reduce the resources this requires.

**Why it is worth watching**

Gate error is one of the biggest bottlenecks for superconducting quantum computers, since it drives the (often exponential) resource overhead needed for error correction. A pulse-level fix like this, which needs no new hardware, could in principle be adopted relatively quickly on existing superconducting qubit chips such as those built by IBM and Google.

---

## My take

이 결과는 새로운 하드웨어나 큐비트 설계 없이 펄스 제어 알고리즘만으로 게이트 속도와 정확도를 동시에 개선했다는 점에서 실용적 가치가 크다. 다만 단일 큐비트 하나에서의 고립된 실험 결과이므로, 여러 큐비트가 상호작용하는 실제 프로세서나 2큐비트 게이트로 확장될 때도 동일한 개선이 유지되는지가 다음 검증 단계가 될 것이다. 수치들은 1차 논문 원문이 아닌 신뢰할 만한 2차 보도(물리학 전문 매체, 연구기관 보도자료)를 통해 교차 확인한 것임을 밝혀둔다.

This result is practically significant because it improves both gate speed and fidelity purely through pulse-control software, without new hardware or qubit redesign. However, since it was demonstrated on a single isolated qubit, the next key test is whether the same leakage suppression holds up in multi-qubit processors and for two-qubit gates. Note that the specific figures here were cross-checked through reputable secondary science-press coverage and institutional press releases rather than a direct read of the primary Nature Communications text.
