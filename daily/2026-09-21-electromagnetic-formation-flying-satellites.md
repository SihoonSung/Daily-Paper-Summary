---
title: "Experimental Demonstration of a Decentralized Electromagnetic Formation Flying Control Using Alternating Magnetic Field Forces"
date: 2026-09-21
topic: aerospace
tags: [aerospace, satellites, propulsion, formation-flying, spacecraft, propellantless]
source: https://arxiv.org/abs/2601.05408
---

Experimental Demonstration of a Decentralized Electromagnetic Formation Flying Control Using Alternating Magnetic Field Forces

* Date: 2026-09-21
* Source: https://arxiv.org/abs/2601.05408
* Topic: Aerospace / Spacecraft Propulsion
* Why it matters: The paper demonstrates, for the first time with three satellites, a decentralized control scheme that lets satellites hold formation using only onboard electromagnets instead of thruster propellant — a step toward propellantless satellite clusters for future space telescopes and interferometers.

## Korean Summary

**한줄 요약**

켄터키대학교(University of Kentucky) 기계·항공우주공학과 연구진이 발표한 이 논문은, 추진제(propellant) 없이 전자석만으로 여러 위성의 상대 위치를 제어하는 "전자기 편대비행(Electromagnetic Formation Flying, EMFF)" 기술을 3기의 위성으로 실험 검증했다. NASA, 미국 국립과학재단(NSF), 미 공군과학연구소(AFOSR)의 지원을 받았으며, 2026년 9월 학술지 Aerospace Science and Technology에 게재될 예정으로 보도되었다.

**핵심 아이디어**

EMFF는 위성마다 실린 코일에 전류를 흘려 자기 쌍극자 모멘트를 만들고, 이 자기장들이 서로 밀고 당기는 힘으로 위성 간 상대 위치를 조정하는 방식이다. 문제는 위성이 3기 이상이 되면 한 위성의 자석이 다른 모든 위성과 동시에 상호작용해 힘이 복잡하게 얽힌다는 점이다. 이 논문은 이를 풀기 위해 "교번 자기장력(Alternating Magnetic Field Forces, AMFF)" 기법을 사용해, 각 위성 쌍(pair)에만 고유하게 작용하는 힘을 만들어낸다.

**무엇이 새로운가?**

* 위성 쌍마다 서로 다른 고유 주파수의 사인파 전류를 조합해 자석을 구동함으로써, 같은 주파수를 가진 쌍끼리만 0이 아닌 시간평균 힘이 발생하도록 설계(AMFF)
* 이를 통해 여러 위성이 동시에 상호작용해도 각 쌍 사이의 힘을 사실상 독립적으로(디커플링) 제어 가능
* 중앙 제어 없이 각 위성이 자체적으로 제어를 수행하는 탈중앙화(decentralized) 폐루프(closed-loop) 제어를 구현
* 저자들에 따르면 3기 이상의 위성을 대상으로 AMFF 기반 제어(개루프·폐루프 포함)를 실험적으로 보인 첫 사례
* 저마찰 선형 공기트랙(air track) 위에 놓인 3기의 전자기 구동 위성 모형으로 실제 실험 검증을 수행

**어떻게 작동하는가?**

각 위성에는 전자기 코일이 실려 있고, 이 코일에 흐르는 전류로 자기 쌍극자 모멘트를 만든다. 두 자석이 같은 주파수로 진동(예: 사인파)하면 시간에 대해 평균을 낸 상호작용력이 0이 아니게 되고, 서로 다른 주파수로 진동하면 평균 힘이 0에 가까워진다는 물리적 성질을 이용한다. 연구진은 각 위성의 전자기 구동 신호를 "여러 사인파의 합"으로 구성하되, 특정 위성 쌍에는 그 쌍만의 고유 주파수를 배정하고 그 사인파의 진폭을 조절해 그 쌍 사이에서 원하는 힘을 만들어낸다. 이렇게 하면 위성이 늘어나도 각 쌍의 힘 제어가 서로 간섭하지 않아, 중앙 컴퓨터 없이 각 위성이 자기 정보만으로 제어 명령을 계산하는 탈중앙화 제어가 가능해진다. 연구진은 이 방식을 3기의 위성 모형(저마찰 공기트랙 위에서 움직이는 지상 테스트베드)에 적용해 폐루프 제어 실험을 수행했다.

**강점**

* 추진제를 전혀 쓰지 않는 위성 간 상대 위치 제어 개념을 실제 다중 위성 실험으로 입증
* 위성이 늘어나도 계산·제어가 얽히지 않도록 하는 실용적인 디커플링 기법 제시
* 중앙집중식이 아닌 탈중앙화 제어라 확장성과 견고성 면에서 유리할 수 있음
* NASA·NSF·공군 등 복수 기관의 지원을 받은 연구로, 실제 우주 임무 적용 가능성을 염두에 둔 것으로 보임

**한계**

* 이 요약은 이 세션의 네트워크 환경 제약으로 arXiv 초록 페이지, ScienceDirect 게재 정보, 외부 보도(The Debrief) 등 검색으로 확인 가능한 내용을 종합해 작성했으며, 논문 원문 PDF 전체를 직접 열람하지는 못했다. 세부 수치나 실험 조건은 원문 확인이 필요하다.
* 실험은 지상의 저마찰 공기트랙(선형 이동만 가능한 2D에 가까운 환경) 위에서 이루어진 것으로 보이며, 실제 우주 공간의 3차원 자유낙하 환경, 지구 자기장의 영향, 장거리 통신 지연 등은 그대로 반영되지 않았을 가능성이 있다.
* 3기 위성 규모의 실증이므로, 더 많은 위성으로 이루어진 대규모 편대(예: 수십~수백 기)로 확장했을 때도 같은 방식이 유효한지는 추가 검증이 필요하다.
* 전자기력은 거리가 멀어질수록 급격히 약해지는 특성이 있어, EMFF가 적용 가능한 위성 간 거리(대략 수십 미터 이내로 알려짐)에는 근본적인 제약이 있다.

**알아둘 용어**

* 전자기 편대비행(EMFF, Electromagnetic Formation Flying): 위성에 실린 전자석 코일로 만든 자기장을 이용해, 추진제 소모 없이 위성 간 상대 위치를 제어하는 방식
* 교번 자기장력(AMFF, Alternating Magnetic Field Forces): 서로 다른 위성 쌍에 고유 주파수를 배정해, 특정 쌍 사이에만 유효한 힘이 작용하도록 자석 구동 신호를 설계하는 기법
* 탈중앙화 제어(decentralized control): 중앙 컴퓨터가 전체를 통제하는 대신, 각 개체(위성)가 자체 정보로 스스로 제어 명령을 계산하는 방식
* 자기 쌍극자 모멘트(magnetic dipole moment): 전류가 흐르는 코일이 만들어내는 자석의 세기를 나타내는 물리량
* 추진제(propellant): 로켓·위성 추력기가 추력을 내기 위해 소모하는 연료·가스 등의 물질
* 희박 개구 배열(sparse aperture array): 여러 개의 작은 망원경(위성)을 넓게 배치해 마치 하나의 거대한 망원경처럼 동작시키는 방식

**왜 주목할 만한가?**

우주망원경, 간섭계, 중력파 검출기처럼 여러 위성이 정밀한 대형을 유지해야 하는 임무는 늘어나는 추세지만, 추진제 기반 추력기는 연료가 소진되면 임무 수명이 끝나고, 추력기 배기가스가 민감한 광학 장비를 오염시킬 위험도 있다. 이 연구는 추진제를 전혀 쓰지 않는 EMFF 방식을, 여러 위성이 동시에 상호작용하는 현실적인 상황(3기 이상)에서도 계산이 얽히지 않게 제어할 수 있는 실용적인 해법을 제시했다는 점에서, 아직 초기 단계이지만 향후 분산 우주 임무 설계에 참고할 만한 결과다.

---

## English Summary

**One-line summary**

Researchers from the University of Kentucky's Department of Mechanical and Aerospace Engineering demonstrated, with a three-satellite ground testbed, a decentralized control scheme for Electromagnetic Formation Flying (EMFF) — controlling satellites' relative positions using only onboard electromagnets, without any propellant. The work, supported by NASA, the National Science Foundation, and the Air Force Office of Scientific Research, is reported to appear in the September 2026 issue of Aerospace Science and Technology.

**Core idea**

EMFF controls the relative positions of satellites in a cluster by running current through onboard coils to create magnetic dipole moments, whose mutual attraction/repulsion generates control forces — no propellant needed. The catch is that once there are three or more satellites, each satellite's magnet interacts with every other satellite's magnet simultaneously, coupling the forces together in a way that is hard to control. This paper addresses that coupling problem using a technique called Alternating Magnetic Field Forces (AMFF), which makes the force between each pair of satellites effectively independent of the others.

**What is new?**

* Uses AMFF: each satellite's electromagnet is driven by a sum of sinusoids, where each sinusoid's frequency is unique to one satellite pair, so a nonzero time-averaged force arises only between magnets oscillating at the same frequency
* This lets the force on each pair be modulated (via that sinusoid's amplitude) essentially independently, decoupling the control problem even as more satellites are added
* Implements fully decentralized closed-loop control, where each satellite computes its own control commands without a central coordinator
* Per the authors, this is the first experimental demonstration of AMFF-based control (open- or closed-loop) with three or more satellites
* Validated experimentally with three electromagnetically actuated satellite models on a low-friction linear air-track testbed

**How does it work?**

Each satellite carries an electromagnetic coil that produces a magnetic dipole moment proportional to its drive current. The physics exploited is that two magnets oscillating (e.g., sinusoidally) at the same frequency produce a nonzero time-averaged interaction force, while magnets oscillating at different frequencies produce a time-averaged force close to zero. The researchers assign each satellite pair its own unique frequency and drive every satellite's coil with the sum of the sinusoids needed for all of its pairwise interactions, adjusting each sinusoid's amplitude to achieve the desired force for that specific pair. Because the pairwise forces are decoupled this way, each satellite can compute and apply its own control action locally, without needing a central controller to solve for the whole formation at once. The team implemented and tested this closed-loop, decentralized scheme on a three-satellite ground testbed using low-friction linear air tracks to approximate frictionless motion.

**Strengths**

* Demonstrates propellant-free relative-position control experimentally with more than two satellites, not just in simulation
* Offers a practical decoupling technique that keeps the control problem tractable as the number of satellites grows
* Decentralized (rather than centralized) control is generally more scalable and robust to single points of failure
* Backed by NASA, NSF, and AFOSR, suggesting the work is aimed at eventual real-mission relevance rather than a purely academic exercise

**Limitations**

* Because of network access constraints in this session, this summary was compiled from the arXiv abstract page, the ScienceDirect listing, and secondary press coverage (The Debrief), rather than a full read of the published PDF; readers should verify exact figures and experimental conditions against the primary source
* The demonstration used a ground-based, low-friction linear air-track setup, which approximates frictionless 1D/2D motion but does not fully replicate the 3D free-fall environment, Earth's magnetic field, or communication latencies of actual orbit
* The experiment involved three satellites; whether the same decentralized AMFF approach scales cleanly to much larger formations (tens to hundreds of satellites) remains to be shown
* Electromagnetic forces fall off sharply with distance, so EMFF is inherently limited to relatively short inter-satellite separations (reportedly on the order of tens of meters), which constrains the missions it can support

**Terms to know**

* Electromagnetic Formation Flying (EMFF): controlling the relative positions of satellites in a cluster using magnetic fields from onboard electromagnets, instead of propellant-based thrusters
* Alternating Magnetic Field Forces (AMFF): a technique that assigns each satellite pair a unique oscillation frequency so that only magnets sharing a frequency produce a net force, decoupling multi-satellite interactions
* Decentralized control: a control architecture where each agent (satellite) computes its own commands locally, rather than relying on a central coordinator
* Magnetic dipole moment: the physical quantity describing the strength and orientation of the magnetic field produced by a current-carrying coil
* Propellant: the fuel or gas a thruster consumes to generate thrust, which is finite and limits a spacecraft's operational lifetime
* Sparse aperture array: a configuration of multiple small telescopes (satellites) spaced apart to jointly act like one much larger telescope

**Why it is worth watching**

Missions requiring precise multi-satellite formations — space telescopes, interferometers, gravity-wave detectors — are becoming more common, but propellant-based thrusters cap mission life once fuel runs out and can contaminate sensitive optics with exhaust. This work shows a practical way to keep EMFF's propellant-free control tractable once more than two satellites are involved, which is an early but concrete step toward distributed spacecraft missions that don't depend on fuel for station-keeping.

---

## My take

이 연구는 완전히 새로운 물리 원리를 제시한 것은 아니며, EMFF 자체는 2000년대 초 MIT SPHERES 연구 등에서부터 논의되어 온 개념이다. 다만 위성이 3기 이상일 때 발생하는 자기력 간의 얽힘 문제를 AMFF라는 비교적 단순하고 구현 가능한 방법으로 풀고, 이를 지상 테스트베드에서 탈중앙화 폐루프 제어로 실제 시연했다는 점은 실용적인 진전이다. 다만 지상의 저마찰 공기트랙 실험과 실제 궤도 환경 사이에는 여전히 큰 격차가 있고, EMFF 자체가 짧은 위성 간 거리에서만 유효하다는 물리적 한계도 있어, 이 결과가 실제 우주 임무로 이어지려면 더 많은 검증 단계가 필요해 보인다.

This is not a fundamentally new physical concept — EMFF itself has been studied since projects like MIT's SPHERES in the early 2000s. The concrete contribution here is a relatively simple, implementable way (AMFF) to untangle the pairwise magnetic coupling that appears once a formation has three or more satellites, backed by an actual decentralized closed-loop demonstration rather than simulation alone. That said, there remains a substantial gap between a low-friction ground testbed and real orbital conditions, and EMFF's short effective range is a hard physical constraint on which missions it can serve — so translating this into an operational space mission would require several more validation steps.
