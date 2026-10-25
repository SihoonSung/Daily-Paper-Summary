---
title: "Revealing New Leakage Paths in GAAFETs using Predictive First-Principles Simulations"
date: 2026-10-25
topic: semiconductors
tags: [semiconductors, transistors, GAAFET, device-physics, chip-scaling, quantum-transport]
source: https://arxiv.org/abs/2610.14298
---

Revealing New Leakage Paths in GAAFETs using Predictive First-Principles Simulations

- Date: 2026-10-25
- Source: https://arxiv.org/abs/2610.14298
- Topic: Semiconductors (transistor device physics)
- Why it matters: As chipmakers move below the 2 nm node with gate-all-around transistors (GAAFETs), stray leakage currents quietly erode the power and performance gains that scaling is supposed to deliver; this paper uses first-principles quantum simulation to pinpoint exactly where one such leakage path originates, which is a prerequisite for ever fixing it.

## Korean Summary

**한줄 요약**

미국 샌디아국립연구소와 룩셈부르크과학기술연구소(LIST) 연구진은 차세대 트랜지스터 구조인 GAAFET(Gate-All-Around FET)에서 게이트에 음전압을 걸었을 때 오히려 전류가 늘어나는 이상 누설 현상의 원인을 양자 수송 시뮬레이션으로 밝혀냈다. 이 누설은 고유전율(high-k) 게이트 절연막을 통한 게이트-드레인 터널링에서 비롯된다는 것을 공간적으로 직접 보여준 것이 핵심이다.

**핵심 아이디어**

기존 측정 데이터에서는 GAAFET를 완전히 끈(음의 게이트 전압) 상태로 만들수록 전류가 지수적으로 줄어야 하는데, 어느 지점부터는 오히려 전류가 다시 증가하는 비정상적인 현상이 관찰되었다. 연구팀은 이 현상이 드레인에 의해 유도된 유전막 장벽 낮춤(Drain-Induced Dielectric Barrier Lowering, DIDBL) 효과로 인해 게이트에서 주입된 전자가 고유전율 절연막을 뚫고 드레인으로 직접 터널링하기 때문이라고 보고, 이를 1차 원리(first-principles) 양자 수송 시뮬레이션으로 검증했다.

**무엇이 새로운가?**

- 기존의 2단자(소스-드레인) NEGF(비평형 그린함수) 시뮬레이션으로는 게이트를 통한 누설 경로 자체를 재현할 수 없었는데, 이 연구는 소스·드레인·게이트를 모두 전류가 흐르는 양자역학적 단자로 취급하는 다단자(multi-terminal) 프레임워크를 사용했다.
- Contact Block Reduction(CBR) 기법을 전하 자기일관(charge self-consistent) 방식으로 적용해, 소자 내부의 국소 전류 밀도를 공간적으로 직접 계산해냈다.
- 그 결과 게이트에서 주입된 전하가 드레인 쪽 장벽이 가장 많이 낮아진 영역 근처에서 고유전율 절연막을 뚫고 터널링한 뒤 드레인으로 수집된다는 것을 시뮬레이션으로 직접 보여주었다.
- 기존에 실험적으로만 제기되었던 DIDBL 가설(2026년 3월 공개된 선행 연구, arXiv:2603.21015)을 제1원리 시뮬레이션으로 뒷받침하고 그 공간적 경로까지 규명했다.

**어떻게 작동하는가?**

1. 측정 데이터에서 음의 게이트 전압 영역에서 드레인 전류가 이론과 다르게 증가하는 현상을 포착한다.
2. 이를 설명하기 위해 소스, 드레인, 게이트를 각각 독립적인 전류 단자로 취급하는 다단자 양자 수송 모델을 구성한다.
3. CBR 기반 NEGF 방법으로 전하 분포를 자기일관적으로 계산하여, 게이트-절연막-드레인 구조 내부의 국소 전류 밀도 지도를 얻는다.
4. 계산 결과 전류가 게이트의 드레인 쪽 끝부분에 집중되어 고유전율 절연막을 관통한다는 것을 확인한다.

**강점**

- 기존 2단자 모델의 한계를 넘어, 게이트를 포함한 3단자 모두에서 전류 경로를 추적할 수 있는 시뮬레이션 프레임워크를 제시했다.
- 실험으로만 추정되던 누설 메커니즘을 양자역학적 제1원리 계산으로 직접 시각화·검증했다.
- 국가연구소와 반도체 연구기관의 협업으로, 산업계가 실제로 마주치는 스케일링 한계 문제를 다룬다.

**한계**

- 이 논문은 시뮬레이션을 통한 메커니즘 규명에 집중하며, 이 누설을 줄이기 위한 구체적인 소자 설계 개선책을 제시하지는 않는 것으로 보인다(공개된 초록 수준에서는 확인되지 않음).
- 구체적인 누설 전류 수치나 시뮬레이션에 사용된 정확한 소자 치수 등 정량적 세부사항은 이번 조사에서 확인하지 못했으며, 원문 전체를 읽어야 확정할 수 있다.
- 아직 동료 심사를 거치지 않은 아카이브 프리프린트(2026년 10월 9일 제출)이다.

**알아둘 용어**

- GAAFET (Gate-All-Around FET): 게이트가 채널을 사방에서 감싸는 차세대 트랜지스터 구조로, FinFET의 후속 기술이며 2nm급 이하 최신 반도체 공정에 쓰인다.
- DIDBL (Drain-Induced Dielectric Barrier Lowering): 드레인 전압이 게이트 절연막의 터널링 장벽을 낮춰 누설을 유발하는 현상.
- NEGF (Non-Equilibrium Green's Function): 나노 소자 내부의 양자역학적 전자 수송을 계산하는 표준 시뮬레이션 기법.
- CBR (Contact Block Reduction): NEGF 계산에서 여러 전류 단자를 효율적으로 다루기 위한 수치 기법.
- 고유전율(high-k) 절연막: 누설 전류를 줄이기 위해 기존 실리콘 산화막 대신 쓰이는 유전율이 높은 게이트 절연 물질.

**왜 주목할 만한가?**

트랜지스터가 2nm 이하로 작아질수록 예상치 못한 누설 경로가 전력 효율과 성능 향상을 갉아먹는 핵심 걸림돌이 된다. 이 연구는 그 원인을 추측이 아니라 양자역학적 시뮬레이션으로 정확히 짚어낸 사례로, 향후 반도체 설계자들이 이런 누설을 억제할 설계 변경을 찾는 데 기초가 될 수 있다.

---

## English Summary

**One-line summary**

Researchers from Sandia National Laboratories and the Luxembourg Institute of Science and Technology (LIST) used first-principles quantum transport simulations to pinpoint the physical origin of an anomalous leakage current in gate-all-around field-effect transistors (GAAFETs), the transistor architecture used in the most advanced chips today. They show that the leakage comes from carriers tunneling through the high-k gate dielectric directly into the drain.

**Core idea**

Measurements of GAAFETs show that, instead of decaying exponentially as the gate voltage is pushed more negative (i.e., as the device is turned off harder), the drain current unexpectedly rises again at sufficiently negative gate voltages. The authors attribute this to Drain-Induced Dielectric Barrier Lowering (DIDBL): the drain bias lowers the tunneling barrier in the gate's high-k dielectric, letting gate-injected carriers tunnel straight through to the drain. This paper verifies and spatially resolves that mechanism using first-principles quantum simulation.

**What is new?**

- Conventional two-terminal (source-drain) Non-Equilibrium Green's Function (NEGF) simulations cannot reproduce gate-related leakage paths at all. This work instead builds a multi-terminal framework that treats the source, drain, and gate as current-carrying quantum-mechanical contacts simultaneously.
- It applies the Contact Block Reduction (CBR) method in a charge-self-consistent way to compute the spatially resolved local current density throughout the 3D device structure.
- The simulation directly shows that gate-injected carriers tunnel through the high-k dielectric preferentially near the drain side of the gate, where the DIDBL effect lowers the barrier the most, and are then collected by the drain.
- It provides first-principles confirmation and spatial localization of the DIDBL leakage hypothesis that an earlier 2026 paper from the same group (arXiv:2603.21015) had proposed from device measurements alone.

**How does it work?**

1. Start from experimental observations that drain current in GAAFETs rises anomalously, rather than falling, at sufficiently negative gate voltages.
2. Build a multi-terminal quantum transport model that treats source, drain, and gate each as independent current-carrying contacts.
3. Run charge-self-consistent NEGF simulations using the CBR method to compute a spatially resolved map of local current density inside the gate-dielectric-channel structure.
4. Identify that the simulated current concentrates near the drain-side edge of the gate, tunneling through the high-k dielectric — matching the hypothesized DIDBL mechanism.

**Strengths**

- Goes beyond the limits of standard two-terminal device simulations by tracking current through all three terminals, including the gate.
- Turns a previously inferred (measurement-based) leakage hypothesis into a directly visualized, first-principles quantum-mechanical result.
- A collaboration between a national lab and a semiconductor research institute, tackling a scaling problem the chip industry is actually running into at advanced nodes.

**Limitations**

- The paper appears to focus on diagnosing the mechanism rather than proposing a concrete device fix or mitigation strategy; this could not be confirmed beyond the available abstract-level summary.
- Specific quantitative figures — exact leakage current values or the precise device dimensions simulated — could not be confirmed from the sources available for this summary and would require reading the full paper.
- This is an arXiv preprint (submitted October 9, 2026) that has not yet been confirmed as peer-reviewed.

**Terms to know**

- GAAFET (Gate-All-Around FET): A transistor design where the gate wraps around the channel on all sides; the successor to FinFET, used in leading-edge sub-2nm chip manufacturing.
- DIDBL (Drain-Induced Dielectric Barrier Lowering): A mechanism where drain bias lowers the tunneling barrier in the gate dielectric, causing leakage.
- NEGF (Non-Equilibrium Green's Function): A standard quantum-mechanical method for simulating electron transport in nanoscale devices.
- CBR (Contact Block Reduction): A numerical technique for efficiently handling multiple current-carrying terminals in NEGF simulations.
- High-k dielectric: A gate insulator material with a high dielectric constant, used in modern transistors in place of silicon oxide to reduce certain leakage paths.

**Why it is worth watching**

As transistors scale below 2 nm, unexpected leakage pathways become a central obstacle to the power and performance gains that scaling is meant to deliver. This work replaces guesswork with a first-principles quantum simulation that precisely localizes one such leakage path, which is the kind of mechanistic understanding chip designers need before they can suppress it.

---

## My take

이 논문은 화려한 신기술이라기보다, 반도체 스케일링이 한계에 다가가면서 점점 중요해지는 "미세 누설 메커니즘"을 정교한 양자 시뮬레이션으로 규명한 기초 연구에 가깝다. 실질적인 소자 설계 개선책이나 정량적 성능 수치가 아직 공개 요약 수준에서는 확인되지 않아, 당장의 산업적 파급력을 판단하기는 어렵다. 다만 2nm 이하 공정의 실제 걸림돌을 다루고, 기존 시뮬레이션 기법의 한계(게이트 누설을 재현하지 못하는 문제)를 해결한 방법론적 기여는 명확하다.

This is less a flashy new technology than a careful piece of mechanistic groundwork, using quantum simulation to pin down a leakage pathway that matters more and more as transistor scaling approaches its physical limits. Without confirmed quantitative results or a proposed fix at the abstract level, its near-term industrial impact is hard to judge. Still, it tackles a real bottleneck in sub-2nm manufacturing and makes a clear methodological contribution by overcoming a known limitation of standard transport simulations (their inability to capture gate leakage at all).
