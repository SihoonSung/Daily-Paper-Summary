---
title: "Single-Period Floquet Control of Bosonic Codes with Quantum Lattice Gates"
date: 2026-09-13
topic: quantum-computing
tags: [quantum-computing, bosonic-codes, floquet-engineering, superconducting-qubits, quantum-error-correction]
source: https://arxiv.org/abs/2601.08782
---

Single-Period Floquet Control of Bosonic Codes with Quantum Lattice Gates

- Date: 2026-09-13
- Source: https://arxiv.org/abs/2601.08782
- Topic: quantum computing (bosonic error-correcting codes)
- Why it matters: Chalmers University of Technology and Tianjin University researchers show that bosonic error-correcting codewords and logical gates — normally built up over thousands of slow driving cycles — can instead be synthesized in a single driving period, cutting the operation time by more than 1,000x and pointing toward a practical route to fault-tolerant superconducting quantum processors.

## Korean Summary

**한줄 요약**

스웨덴 찰머스 공과대학과 중국 톈진대학 공동 연구진이 "양자 격자 게이트(Quantum Lattice Gates, QLG)"라는 방법을 이용해, 초전도 회로에서 보소닉(bosonic) 오류 정정 코드 상태와 논리 게이트를 단 한 번의 구동 주기 안에 만들어내는 방법을 Physical Review Letters에 발표했다. 기존에는 이런 코드 상태를 준비하려면 수천 번의 느린 단열(adiabatic) 구동 주기가 필요했는데, 이번 방법은 이를 1000배 이상 단축시켰다.

**핵심 아이디어**

초전도 큐비트를 만들 때, 하나의 마이크로파 공진기(연속변수 보소닉 모드) 안에 정보를 인코딩하는 "보소닉 코드"(binomial, cat, GKP 코드 등)를 쓰면 하드웨어 효율이 높아진다. 문제는 진공 상태에서 이런 특수한 코드 상태를 정확히 만들어내고, 그 위에서 논리 게이트를 수행하는 과정이 매우 느리고 여러 단계의 점진적(adiabatic) 구동을 필요로 한다는 점이다. 이 논문은 조셉슨 접합의 비섭동적(non-perturbative) 비선형성과 비가환 푸리에 변환(Noncommutative Fourier Transformation, NcFT)을 결합해, 원하는 임의의 유니터리 변환을 처음부터 "단일 주기" 안에서 해석적·결정론적으로 합성하는 플로케(Floquet) 제어 기법을 제시한다.

**무엇이 새로운가?**

- 진공 상태에서 시작해 이항(Binomial), 고양이(Cat), GKP 보소닉 코드워드를 한 번의 구동 주기 안에서 준비하는 방법을 제시 (오차율 10^-3 이하)
- 아다마르(H), 위상(S), π/8(T) 게이트를 포함한 범용 단일 큐비트 논리 게이트 세트를 마이크로초 단위 시간 안에 평균 오류율 약 10^-3 수준으로 구현
- 최적 펄스 엔지니어링(Optimal Pulse Engineering, OPE)과 결합해 기존 다중 주기 단열 구동 대비 연산 속도를 1000배 이상 향상
- 힐베르트 공간 차원(D)에 대해 선형적으로 확장 가능한 구조로, 실제 하드웨어에 적용 가능한 청사진 제시
- 스웨덴 WACQT(Wallenberg Centre for Quantum Technology)가 구축 중인 100큐비트급 초전도 양자 프로세서를 겨냥한 실용적 설계

**어떻게 작동하는가?**

1. 목표로 하는 코드 상태 또는 논리 게이트에 해당하는 유니터리 변환을 수학적으로 먼저 구성
2. 이 유니터리를 조셉슨 접합의 강한 비선형성을 활용하는 "양자 격자 게이트"들의 연쇄로 분해
3. 비가환 푸리에 변환을 이용해 이 게이트 연쇄를 단일 플로케 구동 주기 안에 압축해 넣음
4. 최적 펄스 엔지니어링으로 실제 마이크로파 펄스 파형을 다듬어 목표 상태·게이트에 대한 충실도(fidelity)를 높임
5. 시뮬레이션을 통해 진공에서 시작한 코드워드 준비와 논리 게이트 수행의 오류율, 소요 시간을 기존 다중 주기 단열 방식과 비교해 검증

**강점**

- 기존 방법 대비 1000배 이상의 속도 향상은 결맞음 시간이 짧은 초전도 큐비트에서 오류 노출 시간을 크게 줄여줌
- 여러 대표적 보소닉 코드(binomial, cat, GKP)와 범용 논리 게이트 세트 모두에 적용 가능함을 시뮬레이션으로 보임
- 힐베르트 공간 차원에 선형적으로 확장되어 더 큰 코드 공간에도 원리적으로 적용 가능
- 실제 건설 중인 100큐비트급 초전도 프로세서(WACQT)를 염두에 둔 하드웨어 호환 설계

**한계**

- 현재 결과는 이론·수치 시뮬레이션 기반이며, 실제 초전도 회로에서의 실험적 구현과 검증은 아직 이루어지지 않음
- 제시된 오류율(약 10^-3)은 완전한 결함 허용(fault-tolerant) 양자 계산 문턱값에는 근접하지만, 실제 잡음이 있는 하드웨어에서 동일한 성능이 재현될지는 불확실
- 조셉슨 접합의 비선형성과 정밀한 펄스 제어에 크게 의존하므로, 실제 소자의 제작 편차나 잡음에 얼마나 민감한지에 대한 분석이 더 필요
- 단일 큐비트 논리 게이트에 초점을 맞추고 있어, 다중 큐비트 얽힘 게이트로의 확장성은 후속 연구 과제로 남음

**알아둘 용어**

- 보소닉 코드(bosonic code): 하나의 연속변수 보소닉 모드(예: 마이크로파 공진기) 안에 양자 정보를 인코딩해 오류에 강하게 만드는 오류 정정 코드
- 플로케 제어(Floquet control): 시간에 따라 주기적으로 변하는 구동을 가해 원하는 양자 상태나 게이트를 만들어내는 제어 기법
- 양자 격자 게이트(Quantum Lattice Gates, QLG): 조셉슨 접합의 비선형성을 이용해 만든, 보소닉 코드 상태 조작에 특화된 기본 게이트 단위
- GKP 코드: 위치·운동량 격자 구조를 이용해 오류를 정정하는 대표적인 연속변수 보소닉 오류 정정 코드
- 결함 허용 양자 계산(fault-tolerant quantum computing): 개별 연산의 오류가 있어도 전체 계산 결과의 신뢰성을 보장할 수 있도록 설계된 양자 계산 방식

**왜 주목할 만한가?**

초전도 큐비트는 결맞음 시간이 짧기 때문에, 코드 상태 준비와 게이트 연산에 걸리는 시간을 줄이는 것 자체가 오류율을 낮추는 핵심 전략이다. 이 연구는 수천 주기가 필요하던 연산을 단일 주기로 압축함으로써, 보소닉 코드 기반 결함 허용 양자 컴퓨팅을 실용화하는 데 중요한 걸림돌 하나를 이론적으로 해소했다는 점에서 주목할 만하다. 다만 아직 시뮬레이션 단계이므로, 실제 하드웨어에서의 검증이 다음 단계로 필요하다.

---

## English Summary

**One-line summary**

Researchers from Chalmers University of Technology (Sweden) and Tianjin University (China) published a method in Physical Review Letters that synthesizes bosonic error-correcting code states and logical gates in superconducting circuits within a single Floquet driving period, instead of the thousands of adiabatic driving cycles previously required, achieving more than a 1,000x speedup.

**Core idea**

Encoding quantum information in a single continuous-variable bosonic mode (such as a microwave cavity) using "bosonic codes" — binomial, cat, and GKP codes among them — is hardware-efficient, but preparing these special code states from vacuum and performing logical gates on them has traditionally required slow, multi-period adiabatic driving. This paper introduces an analytical, deterministic Floquet control method — called Quantum Lattice Gates (QLGs) — that combines the non-perturbative nonlinearity of Josephson junctions with Noncommutative Fourier Transformations (NcFT) to synthesize an arbitrary target unitary directly from vacuum within a single driving period.

**What is new?**

- A method to prepare Binomial, Cat, and GKP bosonic codewords from the vacuum state within a single driving period, with infidelities below 10^-3
- A universal single-qubit logical gate set (Hadamard, Phase, and π/8 gates) implemented within microsecond timescales at average gate errors around 10^-3
- Combined with Optimal Pulse Engineering (OPE) to boost operation speed by more than 1,000x compared to existing multi-period adiabatic driving
- A scheme that scales linearly with Hilbert-space dimension D, offering a hardware-compatible blueprint rather than a purely abstract result
- A design explicitly aimed at the 100-qubit superconducting quantum processor under construction at Sweden's Wallenberg Centre for Quantum Technology (WACQT)

**How does it work?**

1. Mathematically construct the target unitary transformation corresponding to the desired code state or logical gate
2. Decompose this unitary into a sequence of "quantum lattice gates" that exploit the strong nonlinearity of Josephson junctions
3. Use Noncommutative Fourier Transformations to compress this gate sequence into a single Floquet driving period
4. Refine the actual microwave pulse waveforms with Optimal Pulse Engineering to maximize fidelity for the target state or gate
5. Validate via simulation that codeword preparation and logical gate performance — in error rate and execution time — outperform existing multi-period adiabatic approaches

**Strengths**

- A speedup of more than 1,000x substantially reduces the time superconducting qubits (with their short coherence times) are exposed to error during an operation
- Demonstrated in simulation across multiple representative bosonic codes (binomial, cat, GKP) and a full universal logical gate set, not just a single special case
- Scales linearly with Hilbert-space dimension, suggesting applicability to larger code spaces in principle
- Designed with a real, under-construction 100-qubit superconducting processor (WACQT) in mind, rather than as a purely abstract proposal

**Limitations**

- The results are theoretical and numerical; experimental implementation and verification on real superconducting hardware has not yet been reported
- The reported error rates (~10^-3) are close to but not conclusively below fault-tolerance thresholds under realistic noise, so real-hardware performance remains to be confirmed
- The method depends heavily on precise control of Josephson junction nonlinearity and pulse shaping, and its sensitivity to fabrication variation and hardware noise needs further analysis
- The demonstrated gates are single-qubit logical operations; extending the approach to multi-qubit entangling gates is left for future work

**Terms to know**

- Bosonic code: a quantum error-correcting code that encodes information in a single continuous-variable bosonic mode, such as a microwave cavity
- Floquet control: a control technique that applies a periodically time-varying drive to steer a quantum system toward a target state or gate
- Quantum Lattice Gates (QLG): elementary gate building blocks, based on Josephson junction nonlinearity, used to manipulate bosonic code states
- GKP code: a continuous-variable bosonic error-correcting code that encodes information using a lattice structure in position and momentum
- Fault-tolerant quantum computing: a computing approach designed so that overall computation remains reliable despite errors in individual operations

**Why it is worth watching**

Because superconducting qubits have short coherence times, shortening the time needed for state preparation and gate operations is itself a core strategy for reducing error rates. By compressing operations that used to require thousands of driving cycles into a single cycle, this work theoretically removes one significant obstacle to making bosonic-code-based fault-tolerant quantum computing practical. It remains at the simulation stage, so experimental validation on real hardware is the necessary next step.

---

## My take

이 연구는 아직 시뮬레이션 단계이지만, 초전도 양자 컴퓨팅에서 오랫동안 병목이었던 "느린 코드 상태 준비"라는 문제를 정면으로 겨냥했고, 실제 건설 중인 100큐비트급 하드웨어(WACQT)를 목표로 설계했다는 점에서 구체성이 높다. 1000배라는 속도 향상 수치가 인상적이지만, 결국 관건은 조셉슨 접합의 제작 편차와 실제 잡음 환경에서도 이 정밀한 펄스 제어가 그대로 재현되는지이며, 실험적 검증이 뒤따라야 이 방법의 실용적 가치를 제대로 평가할 수 있을 것이다.

This work is still at the simulation stage, but it directly targets the long-standing bottleneck of slow bosonic code-state preparation in superconducting quantum computing, and its design is concrete enough to target a real, under-construction 100-qubit processor (WACQT). The 1,000x speedup figure is striking, but the real test will be whether this precise pulse control survives fabrication variation and realistic noise on actual hardware — experimental validation will be needed to properly assess its practical value.
