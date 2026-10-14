---
title: "Quantifying and minimizing dissipation in a non-equilibrium phase transition"
date: 2026-10-14
topic: energy
tags: [energy, thermodynamics, computing, energy-efficiency, nonequilibrium-physics, liquid-crystals]
source: https://arxiv.org/abs/2511.12814
---

Quantifying and minimizing dissipation in a non-equilibrium phase transition

* Date: 2026-10-14
* Source: https://arxiv.org/abs/2511.12814
* Topic: Thermodynamics of computing / energy dissipation measurement
* Why it matters: Switching electronic and photonic devices between states always wastes some energy as heat, and that waste is normally only estimated indirectly; this paper demonstrates a way to measure that waste directly with extreme precision and then automatically search for control signals that cut it by roughly a factor of three, a method that could generalize to the switching elements inside future energy-efficient computing hardware.

## Korean Summary

**한줄 요약**

스탠퍼드대학교와 SLAC 국립가속기연구소 연구팀이 전압으로 유도되는 액정(liquid crystal)의 비평형 상전이(프레데릭스 전이) 과정에서 발생하는 에너지 손실(열 발산)을 약 10나노켈빈 온도 상승에 해당하는 정밀도로 직접 측정했습니다. 이 성과는 Physical Review Letters에 게재되었으며, 2026년 9월 Stanford News와 SLAC News를 통해 소개되었습니다.

**핵심 아이디어**

전자·광학 소자가 한 상태에서 다른 상태로 전환될 때마다 일정량의 에너지가 열로 낭비되는데, 지금까지는 이 손실을 소자 주변 온도 상승을 통해 간접적으로 추정하는 경우가 많았습니다. 이 연구팀은 액정 분자가 전압에 반응해 방향을 바꾸는 과정을 편광 광학 현미경으로 직접 추적함으로써, 에너지 손실 자체를 훨씬 더 정밀하게 측정할 수 있는 모델 시스템을 구축했습니다. 그리고 손실을 측정하는 데서 멈추지 않고, 구동 전압 파형을 자동으로 최적화해 손실을 실제로 줄이는 데까지 나아갔습니다.

**무엇이 새로운가?**

* 전압으로 유도되는 액정의 프레데릭스 전이에서 발생하는 에너지 손실을, 약 10나노켈빈 온도 상승에 해당하는 민감도로 직접 측정
* 상전이 속도에 따른 손실의 킵블-주렉(Kibble-Zurek) 스케일링과, 빠른 구동 속도에서 이 스케일링이 깨지는 현상을 실험적으로 확인하고 기존 이론과 비교
* 자동화된 실시간(in-situ) 최적화 절차를 통해 단순한 선형 전압 램프 대비 에너지 손실을 약 3배(보도에 따르면 60% 이상) 줄이는 구동 파형을 탐색
* 다체(many-body) 비평형 상전이계에서 손실을 직접 측정하면서 동시에 제어 프로토콜까지 최적화한 사례가 드물었다는 공백을 메움

**어떻게 작동하는가?**

1. 네마틱 액정 셀에 전압을 가해 분자 배향이 바뀌는 프레데릭스 전이를 유도합니다.
2. 전압을 올리고 내리는 동안 편광 광학 현미경으로 액정 분자의 회전을 실시간으로 관찰하고, 이를 통해 국소 온도 상승을 측정하는 기존 방식보다 훨씬 정밀하게 에너지 손실량을 계산합니다.
3. 상전이 구동 속도를 바꿔가며 손실이 이론적으로 예측된 킵블-주렉 스케일링을 따르는지, 그리고 어느 속도 영역에서 이 스케일링이 무너지는지를 측정합니다.
4. 자동화된 최적화 알고리즘이 전압 파형의 모양을 반복적으로 조정해가며 측정된 손실을 최소화하는 구동 프로토콜을 실시간으로 탐색합니다.
5. 최적화된 파형과 단순 선형 램프 파형을 비교해, 손실이 실제로 얼마나 줄었는지를 정량적으로 검증합니다.

**강점**

* 온도 상승을 간접적으로 추정하지 않고 에너지 손실을 직접, 매우 높은 정밀도로 측정하는 방법을 제시
* 측정에서 그치지 않고 실제로 손실을 줄이는 구동 프로토콜을 자동으로 찾아내는 최적화 루프까지 구현
* 액정이라는 다루기 쉬운 모델 시스템을 사용했지만, 전압으로 상태를 전환하는 다른 소자(메모리, 디스플레이, 스위치 등)에도 적용 가능한 일반적인 방법론을 제공
* 비평형 통계물리 이론(킵블-주렉 스케일링)과 실험 결과를 직접 대조할 수 있는 깨끗한 플랫폼을 제공

**한계**

* 실험은 액정이라는 특정 모델 시스템에서 수행된 것으로, 반도체 트랜지스터나 상변화 메모리 등 실제 컴퓨팅 소자에 동일한 손실 절감 효과가 적용되는지는 별도로 검증해야 함
* 보도에서 언급된 "60% 이상 손실 절감"이라는 수치와 논문에서 보고된 "약 3배 절감"이라는 수치의 정확한 비교 기준(최적화 전후 조건)은 원 논문의 세부 수치를 기준으로 확인할 필요가 있음
* 최적화에 사용된 구동 파형 탐색 절차가 다른 소자나 더 복잡한 다체계로 얼마나 빠르게/쉽게 일반화될 수 있는지는 아직 명확하지 않음
* 이 연구는 근본적인 측정 및 최적화 방법론을 제시한 기초 연구로, 실제 칩이나 디스플레이에 적용되어 에너지 절감 효과를 낸 사례는 아님

**알아둘 용어**

* 프레데릭스 전이(Fréedericksz transition): 외부 전기장이나 자기장이 특정 임계값을 넘으면 액정 분자의 배향이 갑자기 바뀌는 비평형 상전이 현상
* 킵블-주렉 스케일링(Kibble-Zurek scaling): 상전이가 얼마나 빠르게 진행되는지에 따라 결함 밀도나 에너지 손실이 어떻게 규칙적으로 변하는지를 설명하는 이론
* 비평형 상전이(Non-equilibrium phase transition): 계가 평형 상태에 도달하기 전에 외부에서 유한한 시간 안에 강제로 일으키는 상전이
* 에너지 손실(Dissipation): 시스템이 한 상태에서 다른 상태로 전환될 때 유용한 일로 쓰이지 못하고 열로 사라지는 에너지
* 실시간 최적화(In-situ optimization): 측정과 제어를 같은 실험 장비 안에서 반복하며, 결과를 즉시 반영해 제어 신호를 개선해 나가는 방식

**왜 주목할 만한가?**

컴퓨팅 소자가 소비하는 에너지 중 상당 부분은 상태를 전환할 때 열로 낭비되는데, 이 손실을 정밀하게 측정하고 줄이는 일반적인 방법이 많지 않았습니다. 이 연구는 비교적 다루기 쉬운 액정 시스템을 통해 손실을 나노켈빈 수준의 정밀도로 측정하고, 전압 파형만 바꿔 손실을 수 배 줄이는 것이 가능함을 보여주었다는 점에서, 데이터센터와 메모리·디스플레이 소자의 에너지 효율을 개선하려는 더 넓은 연구 흐름에 실질적인 도구를 제공합니다.

---

## English Summary

**One-line summary**

A team from Stanford University and SLAC National Accelerator Laboratory directly measured the heat dissipated during a voltage-driven, non-equilibrium phase transition in a liquid crystal, with a sensitivity equivalent to roughly a 10-nanokelvin temperature rise. The work was published in Physical Review Letters and covered by Stanford News and SLAC News in September 2026.

**Core idea**

Every time an electronic or photonic device switches between states, some energy is lost as heat, but that loss has usually been estimated indirectly from a small temperature rise rather than measured directly. The team built a model system — a liquid crystal cell whose molecules reorient under an applied voltage — and tracked that reorientation with a polarized optical microscope to measure dissipation far more precisely than conventional thermal methods. They then went a step further and used an automated optimization loop to actually reduce that dissipation by reshaping the driving voltage waveform.

**What is new?**

* Direct measurement of dissipation during the voltage-driven Fréedericksz transition in a liquid crystal, with sensitivity equivalent to about a 10-nanokelvin temperature rise
* Experimental observation of Kibble-Zurek scaling of dissipation with transition speed, and of where that scaling breaks down at fast driving rates, compared against existing theory
* An automated in-situ optimization procedure that searches over driving-voltage waveforms and finds protocols that cut dissipation by roughly a factor of three (reported elsewhere as a reduction of more than 60%) compared with a simple linear voltage ramp
* Fills a gap in which many-body non-equilibrium phase transitions had rarely had their dissipation both measured directly and actively minimized in the same experiment

**How does it work?**

1. A voltage is applied to a nematic liquid crystal cell, driving the Fréedericksz transition in which the molecules' orientation switches.
2. While the voltage is ramped up and down, a polarized optical microscope tracks the molecules' rotation in real time, from which the dissipated energy is calculated far more precisely than by inferring it from bulk temperature changes.
3. By varying how fast the transition is driven, the team checks whether dissipation follows the theoretically predicted Kibble-Zurek scaling, and identifies the regime where that scaling breaks down.
4. An automated optimization algorithm iteratively reshapes the voltage waveform, using the directly measured dissipation as feedback, to search for driving protocols that minimize energy loss.
5. The optimized waveform is compared against a simple linear ramp to quantify how much dissipation was actually saved.

**Strengths**

* Measures energy dissipation directly and with very high precision, instead of relying on indirect bulk-temperature estimates
* Goes beyond measurement to close the loop with an automated search that actually finds lower-dissipation control protocols
* Uses a convenient, well-controlled model system (liquid crystals) but demonstrates a methodology that is, in principle, transferable to other voltage-switched devices such as memory cells, displays, and other switches
* Provides a clean experimental platform for testing non-equilibrium statistical-physics predictions (Kibble-Zurek scaling) directly against measured dissipation

**Limitations**

* The experiment was performed in a specific liquid-crystal model system; whether the same reduction in dissipation transfers to real computing devices such as semiconductor transistors or phase-change memory still needs separate verification
* The exact relationship between the "roughly 3x" reduction reported in the paper and the ">60%" figure cited in secondary press coverage (and the precise before/after conditions behind each number) should be checked against the paper's own reported values
* It is not yet clear how quickly or easily the waveform-optimization procedure generalizes to other devices or to more complex many-body systems
* This is fundamental measurement-and-optimization methodology, not a demonstrated energy saving in an actual chip, memory cell, or display product

**Terms to know**

* Fréedericksz transition: a non-equilibrium phase transition in which a liquid crystal's molecular orientation abruptly changes once an applied electric or magnetic field crosses a threshold
* Kibble-Zurek scaling: a theoretical framework describing how defect density or dissipation scales with the speed at which a phase transition is driven
* Non-equilibrium phase transition: a phase transition forced to occur within a finite time, before the system can fully relax to equilibrium
* Dissipation: energy that is lost as heat rather than used as useful work when a system switches from one state to another
* In-situ optimization: an approach in which measurement and control happen within the same experimental setup, with results fed back immediately to improve the control signal

**Why it is worth watching**

A significant share of the energy computing devices consume is wasted as heat during state switching, and there have been few general methods to measure and reduce that waste precisely. By demonstrating nanokelvin-level dissipation measurement and a several-fold reduction achieved simply by reshaping a voltage waveform, this work offers a concrete tool for the broader effort to improve the energy efficiency of memory, display, and other switching elements used in computing hardware and data centers.

---

## My take

이 연구는 화려한 신소재나 새로운 소자를 제안한 것이 아니라, "에너지 손실을 얼마나 정밀하게 측정하고 줄일 수 있는가"라는 더 근본적인 문제에 답한 기초 연구에 가깝습니다. 액정이라는 다루기 쉬운 모델 시스템에서 나노켈빈 수준의 정밀도로 손실을 측정하고, 전압 파형만 바꿔 손실을 수 배 줄였다는 결과는 설득력이 있지만, 이것이 실제 반도체나 메모리 소자에 그대로 적용될지는 아직 열린 질문입니다. 그럼에도 측정과 최적화를 한 실험 루프 안에서 결합했다는 접근 방식 자체는 에너지 효율적인 컴퓨팅 하드웨어를 설계하려는 다른 연구에도 참고할 만한 방법론을 제공합니다.

This is less about a flashy new material or device and more about a fundamental methodological question: how precisely can energy dissipation be measured and then actually reduced? The demonstration — nanokelvin-level dissipation measurement in a tractable liquid-crystal system, followed by a several-fold reduction from reshaping the drive waveform alone — is convincing on its own terms, but whether it carries over to real semiconductor or memory devices remains an open question. Even so, the approach of closing the loop between direct dissipation measurement and automated optimization within a single experiment is a methodology other efforts to design energy-efficient computing hardware could reasonably build on.
