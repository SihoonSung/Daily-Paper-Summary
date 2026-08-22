---
title: "An entangling gate for dual-rail erasure qubits"
date: 2026-08-22
topic: quantum-computing
tags: [quantum-computing, superconducting-qubits, erasure-qubits, quantum-error-correction, dual-rail-qubits]
source: https://www.nature.com/articles/s41586-026-10822-y
---

An entangling gate for dual-rail erasure qubits

* Date: 2026-08-22
* Source: https://www.nature.com/articles/s41586-026-10822-y
* Topic: quantum-computing
* Why it matters: The team demonstrated a fast, ~99.9%-fidelity two-qubit gate between superconducting "dual-rail" qubits that turns most physical errors into easily-detected erasures rather than hidden bit/phase flips — a design choice that, if it scales, could cut the number of physical qubits needed per logical qubit for fault-tolerant quantum computing.

## Korean Summary

**한줄 요약**

2026년 8월 5일 Nature에 게재된 이 논문은 초전도 "듀얼레일(dual-rail)" 큐비트 두 개 사이에서 동작하는 얽힘 게이트(entangling gate)를 시연했습니다. 이 게이트는 약 500나노초 만에 약 99.9%의 물리적 충실도(fidelity)를 달성했으며, 발생하는 오류의 대부분을 "삭제(erasure)"라는, 검출하기 쉬운 형태로 만드는 것이 핵심입니다. 이 연구는 원래 Quantum Circuits Inc.에서 수행되었고, 2026년 1월 D-Wave가 이 회사를 인수하면서 D-Wave 명의의 첫 게이트 모델 동료심사 논문으로 발표되었습니다.

**핵심 아이디어**

초전도 큐비트에서 발생하는 오류에는 크게 두 종류가 있습니다. 하나는 위치는 알지만 어떤 오류인지는 모르는 "삭제(erasure, 소실)" 오류이고, 다른 하나는 언제 어디서 발생했는지 알기 어려운 비트반전(bit-flip)·위상반전(phase-flip) 오류입니다. 후자는 양자 오류 정정에서 다루기가 훨씬 어렵고 비용이 큽니다. 듀얼레일 큐비트는 하나의 논리적 큐비트 정보를 두 개의 공동(cavity) 모드에 나누어 저장하고, 시스템 전체의 여기(excitation) 총합이 보존되도록 설계함으로써, 광자 손실 같은 흔한 오류가 발생하면 이를 "숨겨진 오류"가 아니라 "검출 가능한 삭제"로 바꿔버립니다. 이 논문은 이런 듀얼레일 큐비트 두 개 사이에서 얽힘을 만드는 2큐비트 게이트를 구현하면서도 이 "오류 위계(error hierarchy)"를 그대로 유지할 수 있음을 실험으로 보여줍니다.

**무엇이 새로운가?**

* 튜너블 트랜스몬(tunable transmon) 커플러로 연결된 두 개의 듀얼레일 공동 큐비트(dual-rail cavity qubit) 사이에서 스왑-대기-스왑(Swap–Wait–Swap, SWS) 방식의 제어위상(controlled-phase, CZ) 게이트를 시연.
* 약 500나노초의 빠른 게이트 시간과 약 99.9%의 전체 물리적 충실도를 동시에 달성.
* 게이트당 삭제(erasure) 발생률 약 0.5%, 사후선택(post-selection) 이후 남는 파울리(Pauli) 오류율은 0.1% 미만으로 측정.
* 비트반전 오류는 100만분의 1 수준까지 억제되어, 잔여 오류의 대부분이 위상반전(dephasing) 오류로 남는다는 것을 확인 — 즉 오류 위계가 2큐비트 게이트에서도 유지됨을 입증.
* D-Wave가 인수한 Quantum Circuits Inc.의 연구 성과가 D-Wave 명의로 발표된 첫 게이트 모델(gate-model) 동료심사 논문.

**어떻게 작동하는가?**

1. 듀얼레일 큐비트는 하나의 논리 정보를 두 개의 마이크로파 공동 모드에 나누어 저장하며, 전체 여기 수가 0이나 2가 아니라 항상 1로 보존되도록 설계됩니다.
2. 두 개의 이런 큐비트를 튜너블 트랜스몬 커플러로 연결해, 필요할 때만 큐비트 간 상호작용을 켤 수 있도록 합니다.
3. 스왑-대기-스왑(SWS) 시퀀스를 이용해 두 큐비트 사이에 제어위상(CZ) 게이트를 구현합니다: 먼저 정보를 트랜스몬 커플러로 스왑해 넣고, 정해진 시간 동안 대기하며 위상을 축적시킨 뒤, 다시 스왑해 원래 큐비트로 되돌립니다.
4. 게이트가 끝난 후 각 큐비트의 여기 수를 측정해, 만약 여기가 사라졌다면(광자 손실) 이를 "삭제 이벤트"로 표시하고 해당 결과를 사후선택으로 걸러냅니다.
5. 살아남은(삭제되지 않은) 결과들만 모아 게이트의 파울리 오류율(비트반전·위상반전)을 별도로 측정함으로써, 오류 대부분이 검출 가능한 삭제로 나타나고 검출 불가능한 파울리 오류는 매우 낮은 수준으로 유지됨을 확인합니다.

**강점**

* 500나노초라는 빠른 게이트 시간과 99.9% 충실도를 동시에 달성해, 속도와 정확도 사이의 트레이드오프에서 실용적인 지점을 보여줌.
* 2큐비트 게이트 단계에서도 "삭제가 지배적이고 파울리 오류는 희귀하다"는 듀얼레일 아키텍처의 핵심 전제를 실측 데이터로 검증.
* D-Wave 시뮬레이션에 따르면 이런 오류 위계를 활용하면 오류 정정 부호의 거리(code distance)를 한 단계 늘릴 때마다 논리 오류율을 최대 약 10배까지 줄일 수 있어, 기존 초전도 큐비트 대비 필요한 물리적 큐비트 수(하드웨어 오버헤드)를 줄일 잠재력이 있음.
* Nature에 동료심사를 거쳐 게재되었고, D-Wave·TheQuantumInsider·HPCwire·Quantum Computing Report 등 다수의 독립 매체가 수치(약 99.9% 충실도, 500나노초, 삭제율 약 0.5%)를 일관되게 보도해 신뢰도가 뒷받침됨.

**한계**

* 이 세션은 네트워크 제약으로 Nature 원문 페이지를 직접 fetch하여 재확인하지 못했습니다. 이 요약은 D-Wave 공식 발표와 TheQuantumInsider, HPCwire, Quantum Computing Report, NextPlatform 등 여러 독립 매체 보도에서 반복적으로 일치한 수치와 설명을 교차 검증해 작성했으며, 논문 원문의 세부 실험 조건까지 전부 확인하지는 못했습니다.
* 이번 시연은 큐비트 2개 사이의 게이트 수준이며, 논문에서 제시한 "코드 거리당 최대 10배 오류 억제" 수치는 완벽한 삭제 검출과 측정 잡음 없음을 가정한 시뮬레이션 결과로, 실제 단일 큐비트 게이트 오류·불완전한 삭제 검출·측정 오류·유휴 잡음을 반영하면 이 값은 낮아질 것으로 예상됩니다.
* 초전도 큐비트 전반의 근본적 제약인 짧은 T1(에너지 완화 시간)이 여전히 병목으로 남아 있으며, 이 연구의 핵심 실험 자체는 D-Wave의 2026년 1월 Quantum Circuits Inc. 인수 이전에 수행되어 2025년 3월 프리프린트, 2025년 5월 Nature 투고를 거쳐 이번에 게재된 것으로, "최신 연구"라기보다는 "최근에 공개된 기존 성과"에 가깝습니다.

**알아둘 용어**

* **듀얼레일 큐비트(Dual-rail qubit)**: 하나의 논리 정보를 두 개의 물리적 모드(예: 두 개의 마이크로파 공동)에 나누어 저장해, 광자 손실 같은 흔한 오류를 검출 가능한 삭제로 바꾸도록 설계된 큐비트.
* **삭제 오류(Erasure error)**: 오류가 발생한 위치는 알지만 정확히 어떤 오류인지는 모르는 경우로, 위치를 모르는 일반 오류보다 훨씬 다루기 쉬움.
* **파울리 오류(Pauli error)**: 비트반전·위상반전처럼 위치도 종류도 사전에 알 수 없는 오류로, 양자 오류 정정에서 가장 다루기 어려운 오류 유형.
* **제어위상 게이트(Controlled-phase/CZ gate)**: 두 큐비트 사이에 얽힘을 만드는 대표적인 2큐비트 게이트.
* **트랜스몬 커플러(Transmon coupler)**: 두 큐비트 사이의 상호작용 세기를 필요할 때만 조절할 수 있게 해주는 보조 초전도 회로 소자.
* **사후선택(Post-selection)**: 측정 결과 중 특정 조건(여기서는 삭제가 발생하지 않은 경우)을 만족하는 데이터만 골라 분석하는 기법.
* **논리 오류율(Logical error rate)**: 여러 물리적 큐비트를 묶어 만든 하나의 논리 큐비트에서 실제로 정보 손실이 발생할 확률로, 오류 정정 성능의 핵심 지표.

**왜 주목할 만한가?**

대규모 오류 정정 양자 컴퓨터를 만들려면 물리적 큐비트 수가 논리 큐비트당 수백~수천 개까지 늘어날 수 있다는 것이 현재 가장 큰 걸림돌 중 하나입니다. 이 논문은 "오류를 아예 줄이기"보다 "오류를 검출하기 쉬운 형태로 바꾸기"라는 접근이 2큐비트 게이트 단계에서도 유효함을 실측으로 보여주었다는 점에서, 물리적 큐비트 오버헤드를 낮출 수 있는 구체적 경로 중 하나로 주목받고 있습니다. 다만 이는 인수합병을 통해 최근 공개된 기존 연구 성과라는 점, 그리고 시뮬레이션 수치와 실제 대규모 시스템 성능 사이에는 여전히 간극이 있을 수 있다는 점을 함께 감안할 필요가 있습니다.

---

## English Summary

**One-line summary**

Published in Nature on August 5, 2026, this paper demonstrates an entangling gate between two superconducting "dual-rail" qubits that reaches roughly 99.9% physical fidelity in about 500 nanoseconds, while converting most of the errors it produces into easily-detected "erasures" rather than hidden bit- or phase-flip errors. The underlying work was originally done at Quantum Circuits Inc., which D-Wave acquired in January 2026, making this the first gate-model peer-reviewed paper published under the D-Wave name.

**Core idea**

Superconducting qubits suffer from two broad categories of error: erasures, where you know an error happened and roughly where, but not what it was, and Pauli errors (bit-flips, phase-flips), where you know neither the location nor the type in advance. Pauli errors are far more expensive to correct. Dual-rail qubits store one logical bit of information across two cavity modes and are engineered so the total number of excitations in the system is conserved; a common failure like photon loss then shows up as a detectable erasure instead of a silent error. This paper shows that a two-qubit entangling gate between such dual-rail qubits can be built while preserving that favorable "error hierarchy."

**What is new?**

* Demonstration of a Swap–Wait–Swap (SWS) controlled-phase (CZ) gate between two dual-rail cavity qubits, linked through a tunable transmon coupler.
* Simultaneous achievement of a fast ~500-nanosecond gate time and ~99.9% overall physical fidelity.
* Measured erasure rate of about 0.5% per gate, with post-selected residual Pauli error below 0.1%.
* Bit-flip errors suppressed to roughly the one-in-a-million level, with dephasing left as the dominant residual error — confirming the error hierarchy holds at the two-qubit-gate level, not just for single qubits.
* The first gate-model, peer-reviewed result published under the D-Wave banner, stemming from its acquisition of Quantum Circuits Inc.

**How does it work?**

1. Each dual-rail qubit encodes one logical bit across two microwave cavity modes, engineered so the total excitation number stays fixed at one rather than zero or two.
2. Two such qubits are connected through a tunable transmon coupler that can switch their interaction on only when needed.
3. A Swap–Wait–Swap sequence implements the CZ gate: information is swapped into the transmon coupler, held there to accumulate a controlled phase, then swapped back into the original qubits.
4. After the gate, each qubit's excitation count is checked; if an excitation is missing (photon loss), that run is flagged as an erasure and discarded via post-selection.
5. The surviving, non-erased results are analyzed separately to measure the gate's Pauli error rate, confirming that most errors show up as detectable erasures while undetectable bit/phase-flip errors remain rare.

**Strengths**

* Achieves a fast (~500 ns) gate time and high (~99.9%) fidelity simultaneously, showing a practical operating point rather than trading one for the other.
* Provides direct experimental evidence, at the two-qubit-gate level, for the core premise of the dual-rail architecture: that erasures dominate and Pauli errors stay rare.
* Per D-Wave's simulations, exploiting this error hierarchy could reduce the logical error rate by up to roughly 10x per increment in error-correction code distance, pointing to lower hardware overhead than conventional superconducting-qubit approaches.
* Peer-reviewed in Nature, with figures (≈99.9% fidelity, ≈500 ns gate time, ≈0.5% erasure rate) consistently corroborated across independent outlets (TheQuantumInsider, HPCwire, Quantum Computing Report, NextPlatform).

**Limitations**

* Due to network/tooling constraints in this session, the original Nature article page could not be directly fetched for re-verification. This summary was built by cross-checking D-Wave's official materials against multiple independent outlets that consistently reported the same figures and description, but not every experimental detail in the full paper could be confirmed.
* The demonstration is at the two-qubit level; the widely cited "up to 10x logical error reduction per code-distance increment" figure comes from simulations assuming perfect erasure detection and no measurement noise — realistic single-qubit gate errors, imperfect erasure checks, measurement errors, and idling noise are expected to lower this number.
* Short T1 (energy relaxation) times remain a fundamental bottleneck for superconducting qubits generally, and the core experiments here predate D-Wave's involvement: the work originated at Quantum Circuits Inc., with a March 2025 preprint and a May 2025 Nature submission, so this is a recently-published existing result rather than brand-new research.

**Terms to know**

* **Dual-rail qubit**: A qubit that encodes one logical bit across two physical modes (e.g., two microwave cavities), designed so common failures like photon loss become detectable erasures rather than silent errors.
* **Erasure error**: An error whose location is known but whose exact nature is not — much easier to correct than an error whose location is also unknown.
* **Pauli error**: Bit-flip or phase-flip errors whose location and type are both unknown in advance, the hardest category for quantum error correction to handle.
* **Controlled-phase (CZ) gate**: A standard two-qubit gate used to generate entanglement between qubits.
* **Transmon coupler**: An auxiliary superconducting circuit element used to turn the interaction between two qubits on only when needed.
* **Post-selection**: A technique that discards or separately analyzes measurement outcomes based on whether a specific condition (here, no erasure) was met.
* **Logical error rate**: The probability that a logical qubit, built from many physical qubits under an error-correcting code, still loses information — the key performance metric for error correction.

**Why it is worth watching**

One of the biggest obstacles to large-scale, error-corrected quantum computing is that current architectures may need hundreds to thousands of physical qubits per logical qubit. This paper offers concrete, two-qubit-gate-level evidence for an alternative strategy — engineering errors to be detectable rather than just trying to reduce their rate — which could translate into meaningfully lower hardware overhead if it holds up at larger scale. It is worth reading with the caveat that the headline scaling numbers are simulation-based and the underlying experiment is a recently-published existing result surfaced through an acquisition, not a brand-new demonstration.

---

## My take

이 논문은 "오류를 줄인다"가 아니라 "오류를 검출하기 쉬운 형태로 만든다"는 전략이 2큐비트 게이트 단계에서도 실제로 성립함을 구체적 수치(약 99.9% 충실도, 500나노초, 삭제율 약 0.5%)로 보여준다는 점에서 공학적으로 흥미롭습니다. 다만 코드 거리당 최대 10배 오류 억제라는 수치는 이상적인 가정 하의 시뮬레이션이고, 실험 자체도 D-Wave의 최근 인수 이전에 이미 수행된 성과가 뒤늦게 공개된 것이라는 점은 감안해서 읽을 필요가 있습니다. 네트워크 제약으로 이번 세션에서 Nature 원문을 직접 확인하지 못했다는 한계도 함께 밝혀둡니다.

This paper is engineering-interesting because it puts concrete numbers (~99.9% fidelity, ~500 ns, ~0.5% erasure rate) behind the idea that making errors detectable, rather than simply rarer, can work at the two-qubit-gate level. That said, the headline "up to 10x per code-distance increment" figure is a best-case simulation, and the underlying experiment itself predates D-Wave's acquisition of the team that ran it, so this is more "a strong existing result surfacing now" than a brand-new breakthrough. As noted above, network constraints in this session also meant the original Nature page could not be directly verified.
