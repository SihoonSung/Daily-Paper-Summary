---
title: "Viscoelastic nanomechanical devices for neuromorphic information processing"
date: 2026-09-27
topic: computing
tags: [neuromorphic-computing, nanomechanics, polymer-electronics, edge-computing, in-materio-computing]
source: https://doi.org/10.1126/sciadv.aeg9893
---

Viscoelastic nanomechanical devices for neuromorphic information processing

* Date: 2026-09-27
* Source: https://doi.org/10.1126/sciadv.aeg9893
* Topic: computing (neuromorphic hardware / in-materio computing)
* Why it matters: The device performs neuron-like signal processing directly through the physical mechanics of a nanometer-thin polymer, folding memory and computation into a single simple component instead of separate transistor circuits — a promising route to much lower-power edge and wearable computing.

## Korean Summary

**한줄 요약**

MIT 연구진이 나노미터 두께의 점탄성(viscoelastic) 고분자 필름을 이용해 생물학적 뉴런의 발화(firing) 거동을 모사하는 나노기계 소자를 개발했습니다. 이 소자는 별도의 메모리 회로 없이 재료 자체의 물리적 성질만으로 정보를 기억하고 처리합니다.

**핵심 아이디어**

일반적인 뉴로모픽 칩은 여러 개의 트랜지스터와 커패시터를 조합해 뉴런의 발화 특성을 흉내 냅니다. 이 논문은 대신 폴리디메틸실록산(PDMS) 같은 점탄성 고분자가 압력을 받은 뒤 원래 모양으로 서서히 돌아가는 "기계적 기억" 성질을 이용해, 전압에 따라 변하는 나노 스케일 전자 터널링 접합 하나만으로 뉴런과 유사한 시간 의존적 전기 반응을 만들어냅니다.

**무엇이 새로운가?**

* 전기적 회로가 아니라 재료의 점탄성 역학 자체를 계산 요소로 사용하는 "인-머티리오(in-materio)" 컴퓨팅 방식을 제시
* 나노미터 두께의 얇은 PDMS 박막으로 구성된 전기기계적 터널링 접합을 인공 뉴런으로 시연
* 전하가 누적되어 임계값을 넘으면 발화하고, 이후 이완(relax)되며 초기화되는 생물학적 뉴런과 유사한 거동을 재현
* 계산 기능이 소자 자체의 물성에 내재되어 있어 필요한 부품 수를 크게 줄임

**어떻게 작동하는가?**

소자는 나노미터 두께의 점탄성 고분자 필름을 포함한 전기기계적 터널링 접합으로 구성됩니다. 전압을 인가하면 고분자 필름이 미세하게 압축·변형되고, 점탄성 때문에 이 변형은 힘이 사라진 뒤에도 즉시 회복되지 않고 시간에 따라 서서히 풀립니다. 이 지연된 기계적 회복이 터널링 전류(전기 저항)에 비선형적이고 시간에 의존하는 변화를 만들어내며, 전하나 전압이 누적되어 임계값을 넘으면 소자가 "발화"하고 이후 다시 이완되어 원상태로 돌아가는 뉴런 유사 반응을 구현합니다.

**강점**

* 별도의 메모리 소자나 복잡한 회로 없이 하나의 나노 소자로 기억과 연산 기능을 동시에 구현
* 소형화·저전력화에 유리해 웨어러블 헬스 기기, 엣지 컴퓨팅, 로봇 등에 적용 가능성 제시
* 재료의 내재적 물성을 활용하므로 확장 가능한 플랫폼으로 발전할 잠재력 보유

**한계**

* 아직 초기 단계의 개별 소자 시연으로, 대규모 어레이 집적이나 실제 신경망 학습 알고리즘 적용 여부는 검증되지 않음
* 점탄성 고분자의 장기 안정성, 반복 사용에 따른 열화(fatigue), 온도 민감성 등은 추가 검증이 필요
* 기존 CMOS 기반 뉴로모픽 칩 대비 처리 속도나 신뢰성에서 아직 실용적 우위를 입증하지 못함

**알아둘 용어**

* 뉴로모픽 컴퓨팅(Neuromorphic computing): 생물학적 뇌와 뉴런의 동작 방식을 모사해 정보를 처리하는 컴퓨팅 방식
* 점탄성(Viscoelasticity): 물질이 탄성(즉각 복원)과 점성(서서히 복원)을 동시에 갖는 성질
* 인-머티리오 컴퓨팅(In-materio computing): 별도의 회로 설계 없이 재료 자체의 물리적 동역학을 계산에 직접 활용하는 접근
* 터널링 접합(Tunneling junction): 두 전극 사이 매우 얇은 절연/유전체 층을 전자가 양자역학적으로 통과하는 구조
* 폴리디메틸실록산(PDMS): 유연하고 점탄성이 있는 대표적인 실리콘 기반 고분자 소재
* 엣지 컴퓨팅(Edge computing): 데이터를 중앙 서버가 아닌 기기 자체(현장)에서 처리하는 방식

**왜 주목할 만한가?**

AI 연산 수요가 급증하면서 저전력·소형 뉴로모픽 하드웨어에 대한 관심이 커지고 있습니다. 이 연구는 복잡한 반도체 회로 대신 단순한 고분자 소재의 물리적 성질만으로 뉴런 유사 기능을 구현할 수 있음을 보여줌으로써, 웨어러블·엣지 기기용 초저전력 컴퓨팅 소자 설계에 새로운 방향을 제시합니다.

---

## English Summary

**One-line summary**

MIT researchers built a nanomechanical device made from a nanometer-thin viscoelastic polymer film that mimics the firing behavior of a biological neuron. The device stores and processes information using only the material's own physical mechanics, without a separate memory circuit.

**Core idea**

Conventional neuromorphic chips reproduce neuron-like firing using combinations of transistors and capacitors. This work instead exploits the "mechanical memory" of a viscoelastic polymer such as PDMS — which slowly returns to its original shape after being compressed — to generate a neuron-like, time-dependent electrical response from a single voltage-tunable nanoscale electromechanical tunneling junction.

**What is new?**

* Introduces an "in-materio" computing approach that uses a material's own viscoelastic mechanics as the computational element, rather than dedicated circuitry
* Demonstrates an artificial neuron built from an electromechanical tunneling junction containing a nanometer-thin PDMS film
* Reproduces neuron-like dynamics: charge/voltage accumulates to a threshold, the device "fires," then relaxes back to its resting state
* Embeds the computing function directly in the intrinsic material property, sharply reducing the number of components needed

**How does it work?**

The device is an electromechanical tunneling junction built around a nanometer-thin viscoelastic polymer film. Applying a voltage slightly compresses/deforms the polymer; because the material is viscoelastic, that deformation does not spring back instantly once the force is removed but relaxes gradually over time. This delayed mechanical recovery produces a nonlinear, time-dependent change in the tunneling current (resistance), so that accumulated charge or voltage crossing a threshold causes the device to "fire," after which it relaxes back toward its original state — closely mirroring how a biological neuron fires and resets.

**Strengths**

* Combines memory and computation in a single nanoscale device, without a separate memory element or complex supporting circuitry
* Favorable for miniaturization and low power use, with potential applications in wearable health devices, edge computing, and robotics
* Exploits an intrinsic material property, suggesting a potentially scalable platform for future hardware

**Limitations**

* Still an early-stage demonstration of an individual device; integration into large arrays and compatibility with practical neural-network training algorithms remain unverified
* Long-term stability, fatigue under repeated use, and temperature sensitivity of the viscoelastic polymer need further characterization
* Has not yet demonstrated a practical advantage in speed or reliability over established CMOS-based neuromorphic chips

**Terms to know**

* Neuromorphic computing: computing approaches that mimic how biological brains and neurons process information
* Viscoelasticity: a material property combining elastic (instant) and viscous (gradual) recovery from deformation
* In-materio computing: an approach that uses a material's own physical dynamics directly for computation, rather than dedicated circuit design
* Tunneling junction: a structure where electrons quantum-mechanically tunnel through an extremely thin insulating/dielectric layer between two electrodes
* PDMS (polydimethylsiloxane): a flexible, viscoelastic silicone-based polymer commonly used in soft devices
* Edge computing: processing data locally on a device rather than sending it to a central server

**Why it is worth watching**

As demand for AI computation grows, so does interest in low-power, compact neuromorphic hardware. This work shows that neuron-like functionality can emerge from the physical properties of a simple polymer rather than complex semiconductor circuitry, pointing to a new design direction for ultra-low-power computing in wearable and edge devices.

---

## My take

이 연구는 아직 단일 소자 수준의 초기 시연이지만, "회로가 아니라 재료로 계산한다"는 인-머티리오 컴퓨팅의 방향성을 명확한 물리적 메커니즘(점탄성 이완)으로 보여준 점이 흥미롭습니다. 다만 대규모 집적, 소자 간 편차, 장기 내구성 검증 없이는 실용화까지는 거리가 있어 보이며, 과대 해석을 경계할 필요가 있습니다.

This is an early, single-device demonstration, but it makes a clean physical case (viscoelastic relaxation) for the broader "compute with the material, not the circuit" direction in in-materio computing. Without evidence of large-scale integration, device-to-device variability control, and long-term durability, practical deployment remains distant, so the result is best read as a promising proof of concept rather than a near-term technology.
