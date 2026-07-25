---
title: "Experimental Demonstration of a Decentralized Electromagnetic Formation Flying Control Using Alternating Magnetic Field Forces"
date: 2026-07-25
topic: aerospace
tags: [aerospace, satellite-formation-flying, propellantless-propulsion, spacecraft-control, decentralized-control]
source: https://arxiv.org/abs/2601.05408
---

Experimental Demonstration of a Decentralized Electromagnetic Formation Flying Control Using Alternating Magnetic Field Forces

* Date: 2026-07-25
* Source: https://arxiv.org/abs/2601.05408
* Topic: aerospace
* Why it matters: It is the first experimental demonstration of decentralized, closed-loop control for three or more satellites flying in formation using only onboard electromagnets — no propellant at all — which is exactly the regime where prior electromagnetic formation flying work hit its hardest coupling problem.

## Korean Summary

**한줄 요약**

이 논문은 추진제(propellant) 없이 위성에 탑재된 전자석만으로 여러 위성의 상대 위치를 제어하는 "전자기 편대비행(Electromagnetic Formation Flying, EMFF)"에서, 위성 3대 이상을 대상으로 한 분산형(decentralized) 폐루프 제어를 실험적으로 시연한 첫 사례입니다. 저자는 켄터키대학교(University of Kentucky) 기계항공공학과 소속 Sumit S. Kamat, Ajin Sunny, T. Michael Seigler, Jesse B. Hoagg입니다.

**핵심 아이디어**

위성들이 전자석 코일에 전류를 흘려 서로 밀거나 당기는 자기력으로 편대 대형을 유지하면 추진제를 전혀 소모하지 않아도 됩니다. 문제는 위성이 2대일 때는 비교적 단순하지만, 3대 이상이 되면 모든 위성이 만드는 자기장이 서로 얽혀 특정 위성 쌍 사이에만 힘을 가하기가 어려워진다는 점입니다. 이 논문은 "교번 자기장력(Alternating Magnetic Field Forces, AMFF)" 기법으로 이 얽힘 문제를 풀고, 이를 실제 하드웨어 실험으로 검증합니다.

**무엇이 새로운가?**

* 위성 3대 이상을 대상으로 한 분산형 폐루프 EMFF 제어의 최초 실험적 시연.
* 각 위성이 자신의 전자석을 여러 개의 정현파(sinusoid) 합으로 구동하고, 특정 주파수를 오직 한 위성 쌍만 공유하도록 설계하여, 중앙 조정 장치 없이도 위성 쌍별로 힘을 독립적으로 제어.
* 지면 기반 테스트베드(선형 에어트랙 위의 전자기 구동 위성 3대)를 이용한 실험적 검증.
* 정착 시간(settling time) 30초 이내, 평균 정상상태 대형 오차 5mm 이하, 최대 오차 1cm 이하라는 구체적 성능 수치 제시.
* NASA 및 미 공군의 지원을 받은 연구로 보도됨.

**어떻게 작동하는가?**

1. 각 위성은 전자석 코일을 가지고 있으며, 코일에 전류를 흘려 자기 쌍극자(magnetic dipole)를 만듭니다.
2. 두 위성의 자기 쌍극자가 서로 다른 주파수로 진동하면 시간 평균 힘이 0이 되고, 같은 주파수로 진동해야만 0이 아닌 힘이 발생한다는 물리적 성질(AMFF)을 이용합니다.
3. 각 위성은 자신의 코일을 여러 주파수의 정현파 합으로 구동하되, 각 주파수를 오직 하나의 상대 위성과만 공유하도록 설정합니다.
4. 각 주파수 성분의 진폭을 조절함으로써, 특정 위성 쌍 사이에 원하는 힘만 선택적으로 가할 수 있어, 전체 위성 간 자기장 얽힘 문제를 분산적으로(즉 중앙 제어 없이) 풀 수 있습니다.
5. 이 제어 기법을 선형 에어트랙 위에 놓인 위성 3대로 구성된 실험 장치에 적용하여 폐루프로 대형을 형성하고 그 오차와 정착 시간을 측정합니다.

**강점**

* 추진제를 전혀 쓰지 않으므로 임무 수명이 연료가 아닌 전력 공급에만 좌우되어, 원리적으로 훨씬 오래 편대비행을 유지할 수 있습니다.
* 추진 시스템의 배기 플룸(plume)이 없어, 정밀 광학 관측이나 분산 우주망원경처럼 오염에 민감한 임무에 유리합니다.
* 분산형 제어 구조라 위성 대수가 늘어나도 중앙 컴퓨터가 모든 위성 상태를 실시간으로 알아야 할 필요가 없어 확장성이 좋습니다.
* 시뮬레이션이 아닌 실제 하드웨어 실험으로 검증했다는 점에서 이론적 제안보다 신뢰도가 높습니다.

**한계**

* 이 세션은 이번 실행에서 outbound 웹 페치(WebFetch)가 조직 정책상 차단되어 arXiv 원문이나 관련 저널 페이지를 직접 열어보지 못했습니다. 이 요약은 여러 차례의 검색 엔진 질의를 통해 확인된 초록, 저자, 소속, 수치 정보를 종합해 작성되었으며, 원문을 직접 읽고 재확인하지는 못했습니다.
* 실험은 지면 위 선형 에어트랙이라는 1차원(또는 저차원) 환경에서 이루어졌으며, 실제 우주의 3차원 자유낙하 환경에서도 동일한 성능이 나올지는 별도 검증이 필요합니다.
* 위성 대수가 늘어날수록 필요한 고유 주파수 쌍의 수도 늘어나므로, 대규모 편대(수십~수백 기)에서의 확장성은 이 논문만으로는 확인되지 않습니다.
* 전자기력은 거리 3~4제곱에 반비례해 급격히 약해지므로, 위성 간 거리가 멀어지면 필요한 전력과 코일 크기가 급격히 커질 수 있습니다.

**알아둘 용어**

* **전자기 편대비행(Electromagnetic Formation Flying, EMFF)**: 위성에 탑재된 전자석이 만드는 자기력만으로 여러 위성의 상대 위치를 제어하는 추진제 없는(propellantless) 편대비행 기법.
* **교번 자기장력(Alternating Magnetic Field Forces, AMFF)**: 자기 쌍극자를 특정 주파수로 진동시켜, 같은 주파수를 가진 쌍 사이에만 유효한 힘이 발생하도록 만드는 기법.
* **분산 제어(Decentralized control)**: 중앙 컴퓨터가 모든 개체의 상태를 알 필요 없이, 각 개체가 국소 정보만으로 스스로 제어 결정을 내리는 방식.
* **정착 시간(Settling time)**: 시스템이 목표 상태 근처의 허용 오차 범위 안에 들어오기까지 걸리는 시간.
* **선형 에어트랙(Linear air track)**: 압축 공기를 이용해 마찰을 거의 없앤 1차원 이동 실험 장치로, 우주의 무중력·무마찰 환경을 지상에서 근사하는 데 쓰임.

**왜 주목할 만한가?**

분산 우주망원경이나 위성 군집(swarm) 임무는 정밀한 상대 위치 유지가 핵심인데, 기존 추력기 기반 방식은 추진제 고갈과 배기 오염이라는 근본적 한계를 가집니다. 이 연구는 위성 3대 이상에서 발생하는 자기장 얽힘이라는, EMFF의 가장 어려운 문제를 분산 제어로 실험 검증했다는 점에서, 추진제 없는 정밀 편대비행이 실제 임무로 이어지기 위한 중요한 디딤돌로 볼 수 있습니다.

---

## English Summary

**One-line summary**

This paper reports the first experimental demonstration of decentralized, closed-loop electromagnetic formation flying (EMFF) control for three or more satellites, using only onboard electromagnets and no propellant. The authors — Sumit S. Kamat, Ajin Sunny, T. Michael Seigler, and Jesse B. Hoagg — are in the Department of Mechanical and Aerospace Engineering at the University of Kentucky.

**Core idea**

Satellites can hold formation by pushing and pulling on each other magnetically through onboard electromagnetic coils, consuming no propellant at all. This is relatively simple with two satellites, but with three or more, the magnetic fields from every satellite interact simultaneously, making it hard to apply a force to just one specific pair without a central controller that knows everyone's state. This paper uses Alternating Magnetic Field Forces (AMFF) to decouple those interactions and demonstrates the approach on real hardware.

**What is new?**

* The first experimental demonstration of decentralized, closed-loop EMFF control involving three or more satellites — the regime where the field-coupling problem first appears.
* Each satellite drives its coil with a sum of sinusoids, assigning each frequency to exactly one satellite pair, so pairwise forces can be commanded independently without a central coordinator.
* Validation on a ground-based testbed: three electromagnetically-actuated satellites on linear air tracks.
* Concrete performance numbers: settling time under 30 seconds, mean steady-state formation error under 5 mm, and maximum steady-state error under 1 cm.
* Reported as NASA- and US Air Force-backed research.

**How does it work?**

1. Each satellite carries an electromagnetic coil that generates a magnetic dipole when driven with current.
2. A physical property of alternating magnetic dipoles is exploited: two dipoles oscillating at different frequencies produce zero time-averaged force between them, while dipoles at the same frequency produce a nonzero net force (AMFF).
3. Each satellite drives its coil with a sum of sinusoids, where each individual frequency is shared with only one other satellite in the formation.
4. By modulating the amplitude of each frequency component, a satellite can command a force toward one specific neighbor without affecting its interaction with others — decoupling the multi-body magnetic coupling problem in a decentralized way.
5. This controller is implemented on a three-satellite testbed on linear air tracks, and closed-loop formation-keeping error and settling time are measured.

**Strengths**

* Propellant-free operation means mission life is limited only by available electrical power, not by fuel reserves, in principle enabling much longer formation-flying missions.
* No thruster exhaust plume, which matters for contamination-sensitive missions like distributed space telescopes or precision optical arrays.
* The decentralized architecture scales better than centralized schemes, since it does not require a central computer to track every satellite's state in real time.
* Validated on physical hardware rather than simulation alone, which is a stronger form of evidence than a purely theoretical or simulated result.

**Limitations**

* This session's outbound WebFetch access was blocked by organizational network policy during this run, so the arXiv page and any associated journal page could not be opened directly. This summary was assembled from details surfaced across multiple search-engine queries (abstract content, author list, affiliation, and reported numbers), not from a direct read of the full paper.
* The experiment was conducted on a ground-based, low-dimensional (linear air track) testbed; whether the same performance holds in a true 3D, free-fall orbital environment is not established by this test alone.
* The number of distinct frequencies needed grows with the number of satellite pairs, so scalability to much larger swarms (tens to hundreds of satellites) is not demonstrated here.
* Magnetic force falls off very steeply with distance (roughly as the fourth power), so required coil size and power would grow quickly as satellite separation increases.

**Terms to know**

* **Electromagnetic Formation Flying (EMFF)**: A propellantless formation-keeping approach where satellites control their relative positions using magnetic forces from onboard electromagnets instead of thrusters.
* **Alternating Magnetic Field Forces (AMFF)**: A technique that oscillates magnetic dipoles at chosen frequencies so that a nonzero net force arises only between dipoles sharing the same frequency.
* **Decentralized control**: A control architecture where each agent makes decisions from local information alone, without a central unit needing full knowledge of every agent's state.
* **Settling time**: The time required for a system to enter and stay within an acceptable error band around its target state.
* **Linear air track**: A near-frictionless one-dimensional test platform using a cushion of air, commonly used to approximate the drag-free environment of space in ground experiments.

**Why it is worth watching**

Distributed space telescopes and satellite swarm missions depend on precise, sustained relative positioning, but conventional thruster-based station-keeping is fundamentally limited by propellant depletion and plume contamination. By experimentally validating decentralized control through the hardest coupling regime of EMFF — three or more satellites — this work is a concrete step toward propellant-free precision formation flying becoming viable for real missions.

---

## My take

이 연구는 문제 설정이 명확하고(추진제 없는 편대비행의 다체 자기장 얽힘 문제), 이를 분산 제어로 실험까지 이어갔다는 점에서 견실한 진전으로 보입니다. 다만 이번 세션에서는 조직의 네트워크 정책으로 인해 arXiv 원문에 직접 접근하지 못해, 검색 엔진에 노출된 초록과 수치만으로 요약을 구성했습니다. 지상 테스트베드 결과가 실제 궤도 환경에서도 유지될지, 그리고 위성 수가 훨씬 많아졌을 때도 방식이 확장 가능한지는 원문과 후속 연구를 통해 추가로 확인이 필요합니다.

This work targets a well-defined problem — the multi-body magnetic coupling that makes propellant-free formation flying hard with three or more satellites — and backs its decentralized control scheme with a real hardware demonstration, which is a solid step forward. However, this session's network policy blocked direct WebFetch access, so this summary relies on abstract content and figures surfaced through search rather than a direct reading of the paper. Whether the ground-testbed results hold in an actual orbital environment, and whether the approach scales to much larger satellite swarms, remain open questions that would need the full paper and follow-up work to confirm.
