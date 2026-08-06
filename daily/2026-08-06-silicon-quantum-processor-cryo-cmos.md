---
title: "A digitally controlled silicon quantum processing unit"
date: 2026-08-06
topic: quantum-computing
tags: [quantum-computing, silicon-spin-qubits, cryo-cmos, quantum-error-correction, semiconductor]
source: https://www.hrl.com/news/2026/07/29/hrl-demonstrates-a-silicon-quantum-processor-that-runs-itself
---

A digitally controlled silicon quantum processing unit

* Date: 2026-08-06
* Source: https://www.hrl.com/news/2026/07/29/hrl-demonstrates-a-silicon-quantum-processor-that-runs-itself
* Topic: quantum-computing
* Why it matters: HRL Laboratories built a quantum processor that generates all of its own control signals and runs repeated rounds of error correction entirely inside the cryostat, with no real-time help from room-temperature electronics — directly attacking the "wiring bottleneck" that stands between today's small quantum chips and machines with thousands of qubits.

## Korean Summary

**한줄 요약**

HRL Laboratories(미국 캘리포니아 말리부)는 18큐비트 실리콘 스핀 큐비트 칩과, 극저온(4켈빈) 환경에서 동작하는 자체 개발 7000만 트랜지스터 CMOS 제어 칩을 하나로 통합해, 상온 전자장비의 실시간 개입 없이 칩 스스로 오류 정정(error correction)을 반복 수행하는 데 성공했습니다. 이 연구는 2026년 7월 29일 Nature(Vol. 655, Issue 8125) 커버 논문으로 게재되었습니다.

**핵심 아이디어**

기존 초전도·스핀 큐비트 양자 컴퓨터는 큐비트 자체는 극저온 냉동고(cryostat) 안에 있지만, 이를 제어하는 신호는 대부분 상온의 랙(rack)에 있는 전자장비에서 만들어져 수많은 배선(wiring)을 통해 냉동고 안으로 들어갑니다. 큐비트 수가 수천 개로 늘어나면 이 배선 수도 비례해서 늘어나야 하므로, 이는 대규모 양자 컴퓨터 구현을 가로막는 대표적인 "배선 병목(wiring bottleneck)" 문제로 꼽힙니다. 이 논문의 핵심 아이디어는 큐비트를 제어하는 시간 가변 신호(time-varying control signal)를 만드는 회로 자체를 극저온 환경 안으로 옮겨, 냉동고 밖 상온 전자장비에 대한 실시간 의존을 없애는 것입니다.

**무엇이 새로운가?**

* 18큐비트 exchange-only 실리콘 스핀 큐비트 칩, 4켈빈(약 영하 269도)에서 동작하는 7000만 트랜지스터급 맞춤형 CMOS 제어 칩, 그리고 296개 신호선을 가진 초전도 리본 케이블, 이렇게 별도로 제작된 세 개의 반도체 부품을 하나의 양자 처리 장치(QPU)로 통합.
* 큐비트를 제어하는 시간 가변 신호를 상온이 아니라 극저온 CMOS 컨트롤러가 냉동고 내부에서 직접 생성.
* 반복 부호(repetition code) 기반 오류 정정을 상온 전자장비의 실시간 개입 없이, 극저온 컨트롤러만으로 여러 라운드 연속 수행 — 이런 방식의 시연은 이번이 처음.
* 이 큐비트 종류(실리콘 스핀 큐비트) 기준으로 기존 시연 대비 약 10배 낮은 제어 오류율 달성.
* 오류 정정 부호에 큐비트를 추가할수록 오류율이 약 5배 억제되는 현상을 관측 — 이는 향후 양자 오류 정정이 큐비트 수 증가에 따라 실제로 작동함을 보여주는 규모 확장(scaling)의 핵심 신호.

**어떻게 작동하는가?**

1. 밀리켈빈(mK) 온도의 최하단 단(stage)에 18큐비트 exchange-only 실리콘 스핀 큐비트 칩을 배치합니다.
2. 그보다 약간 높은 4켈빈 단에 7000만 트랜지스터 규모의 맞춤형 CMOS 컨트롤러 칩을 배치해, 큐비트에 필요한 시간 가변 전압/신호를 그 자리에서 직접 생성합니다.
3. 두 칩은 296개의 신호선을 가진 초전도 리본 케이블로 연결되어, 신호를 전달하면서도 큐비트 단으로 유입되는 열을 최소화합니다.
4. 이렇게 통합된 시스템에 반복 부호 기반 양자 오류 정정 프로토콜을 실행시키되, 상온 전자장비가 매 사이클 실시간으로 개입하지 않고 극저온 컨트롤러가 자체적으로 판단·생성한 신호만으로 반복 라운드를 수행합니다.
5. 큐비트 수를 늘려가며 오류율 변화를 측정해, 오류 정정 부호가 커질수록 오류가 억제되는지(약 5배 감소) 확인합니다.

**강점**

* 큐비트 제어 전자장비를 극저온 환경 안으로 옮김으로써, 큐비트 수가 늘어날수록 기하급수적으로 늘어나는 상온-저온 간 배선 문제를 근본적으로 완화할 수 있는 방향을 제시.
* 오류 정정을 극저온 컨트롤러만으로 완전히 자율 수행한 최초 사례로, 실제 대규모 양자 컴퓨터의 제어 아키텍처에 직접적인 시사점을 줌.
* 기존 대비 약 10배 낮은 제어 오류율과, 큐비트 추가에 따른 약 5배 오류 억제라는 구체적 수치를 제시.
* 동료 심사를 거쳐 Nature 표지 논문으로 게재되어 신뢰도가 높음.
* 큐비트 칩, CMOS 컨트롤러, 극저온 배선까지 서로 다른 반도체 제조 공정을 통합했다는 점에서, 순수 물리학 실험을 넘어선 실질적 시스템 엔지니어링 성과.

**한계**

* 이 세션에서는 도구(네트워크) 제약으로 Nature 원문 페이지나 arXiv 버전을 직접 fetch하여 재확인하지 못했습니다. 이 요약은 HRL 공식 발표와 HPCwire, TheQuantumInsider, TechTimes, postquantum.com 등 여러 독립 매체 보도에서 반복적으로 일치한 저자, 소속, 수치(18큐비트, 7000만 트랜지스터, 4켈빈, 296개 신호선, 약 5배 오류 억제 등)를 교차 검증해 작성했으며, 논문 원문의 세부 실험 조건이나 실패 사례까지 전부 확인하지는 못했습니다.
* 큐비트 수가 18개로 여전히 소규모이며, 상용 양자 컴퓨터에 필요한 수천~수백만 큐비트 규모로 이 아키텍처가 그대로 확장될 수 있는지는 별도의 검증이 필요합니다.
* 4켈빈에서 동작하는 CMOS 컨트롤러 자체의 발열이 큐비트가 있는 밀리켈빈 단에 미치는 영향, 그리고 컨트롤러의 소비 전력이 커질 때의 냉각 부담은 추가로 다뤄야 할 과제로 보입니다.
* 이 발표 8일 전인 2026년 7월 23일, IBM이 Boeing과 GM으로부터 HRL Laboratories를 인수하는 계약을 체결했다고 발표된 바 있어, 이번 연구의 향후 활용 방향(IBM의 초전도 큐비트 로드맵과의 통합 여부 등)은 아직 불확실합니다.

**알아둘 용어**

* **스핀 큐비트(Spin qubit)**: 전자나 원자핵의 스핀 상태를 이용해 정보를 저장하는 큐비트로, 기존 반도체 제조 공정과 호환성이 높다는 장점이 있음.
* **CMOS 컨트롤러**: 큐비트에 인가할 전압·펄스 등 제어 신호를 만들어내는 회로로, 일반적으로 상온에 위치하지만 이 논문에서는 극저온(4K)에서 동작하도록 설계됨.
* **크라이오스탯(Cryostat)**: 큐비트를 절대영도에 가까운 극저온으로 유지하는 특수 냉동 장치.
* **배선 병목(Wiring bottleneck)**: 큐비트 수가 늘어날수록 상온-저온 간 제어 배선 수도 비례해 늘어나 규모 확장을 어렵게 만드는 문제.
* **반복 부호(Repetition code)**: 동일한 정보를 여러 큐비트에 중복 저장해 오류를 검출·정정하는 가장 단순한 형태의 양자 오류 정정 부호.
* **양자 오류 정정(Quantum error correction, QEC)**: 물리적 큐비트의 잡음과 오류로부터 논리적 큐비트의 정보를 보호하기 위한 절차로, 대규모 실용 양자 컴퓨터 구현의 필수 요소로 여겨짐.
* **초전도 리본 케이블**: 여러 신호선을 하나로 묶어 신호를 전달하면서도 열 유입을 최소화하도록 설계된 극저온용 배선.

**왜 주목할 만한가?**

양자 컴퓨터가 유용한 규모로 커지려면 결국 수천~수백만 개의 큐비트를 다뤄야 하는데, 지금처럼 큐비트마다 상온 전자장비까지 이어지는 배선을 계속 늘리는 방식은 물리적으로 한계에 부딪힙니다. 이 논문은 제어 전자장비 자체를 극저온 환경 안으로 옮기고, 오류 정정까지 그 안에서 자율적으로 수행하는 구체적인 아키텍처를 실증했다는 점에서, "큐비트 개수 늘리기" 경쟁을 넘어 "실제로 확장 가능한 시스템을 어떻게 지을 것인가"라는 공학적 질문에 답을 시도한 사례로 주목할 만합니다.

---

## English Summary

**One-line summary**

HRL Laboratories (Malibu, California) integrated an 18-qubit exchange-only silicon spin-qubit chip with a custom 70-million-transistor CMOS controller operating at 4 kelvin inside the same cryostat, and showed the system generating its own control signals and running repeated rounds of quantum error correction with no real-time involvement from room-temperature electronics. The work was published as the cover article of Nature (Vol. 655, Issue 8125) on July 29, 2026.

**Core idea**

In most superconducting and spin-qubit quantum computers today, the qubits sit in a cryostat, but the time-varying control signals that drive them are generated by room-temperature electronics and routed in through a large number of physical wires. As qubit counts grow toward the thousands, this wiring has to grow proportionally, creating a well-known "wiring bottleneck" that threatens to block further scaling. This paper's core idea is to move the circuitry that generates those time-varying control signals into the cryogenic environment itself, removing the real-time dependency on room-temperature hardware.

**What is new?**

* Integration of three separately fabricated semiconductor components into one quantum processing unit: an 18-qubit exchange-only silicon spin-qubit chip, a custom 70-million-transistor CMOS controller operating at 4 kelvin, and a 296-trace superconducting ribbon cable connecting them.
* The time-varying qubit control signals are generated directly inside the cryostat by the cryogenic CMOS controller, rather than at room temperature.
* Repeated rounds of repetition-code-based quantum error correction executed with no real-time involvement from room-temperature electronics — reportedly the first demonstration of this kind.
* Control errors roughly 10x lower than prior demonstrations for this qubit type.
* Error suppression of roughly 5x observed as more qubits were added to the error-correcting repetition code — a key scaling signature for quantum error correction.

**How does it work?**

1. An 18-qubit exchange-only silicon spin-qubit chip sits at the coldest, millikelvin stage of the cryostat.
2. A custom CMOS controller chip with about 70 million transistors sits at a warmer 4-kelvin stage, generating the time-varying voltages/pulses the qubits need directly on-site.
3. The two chips are connected by a 296-trace superconducting ribbon cable that carries signals between stages while minimizing heat flow into the qubit stage.
4. The integrated system runs a repetition-code quantum error correction protocol without room-temperature electronics intervening in real time each cycle — the cryogenic controller generates and manages the signals autonomously across repeated rounds.
5. Researchers vary the number of qubits in the code and measure how the error rate changes, confirming roughly fivefold error suppression as the code grows.

**Strengths**

* Moving qubit control electronics into the cryogenic environment directly addresses the wiring bottleneck that otherwise grows worse as qubit counts scale into the thousands.
* First reported demonstration of fully autonomous, cryogenic-controller-only quantum error correction, with direct implications for how large-scale quantum computers might actually be architected.
* Concrete, quantitative results: roughly 10x lower control error than prior work on this qubit type, and roughly 5x error suppression as the code scales.
* Peer-reviewed and published as a Nature cover article, lending it strong credibility.
* Represents genuine systems engineering — integrating distinct semiconductor fabrication processes (qubit chip, cryo-CMOS controller, cryogenic interconnect) into a working system — beyond a purely physics-focused result.

**Limitations**

* Due to network/tooling constraints in this session, the original Nature article page and any arXiv version could not be directly fetched for re-verification. This summary was built by cross-checking HRL's official announcement against multiple independent outlets (HPCwire, TheQuantumInsider, TechTimes, postquantum.com) that consistently reported the same figures (18 qubits, 70 million transistors, 4 kelvin, 296 traces, ~5x error suppression), but not every experimental detail or failure case in the full paper could be confirmed.
* The demonstration remains small-scale at 18 qubits; whether this architecture scales cleanly to the thousands or millions of qubits needed for practical quantum computing is not yet shown.
* How heat dissipated by the 4-kelvin CMOS controller affects the millikelvin qubit stage, and how cooling demands grow as controller power increases at larger scale, appear to be open engineering questions.
* Eight days before this paper appeared, on July 23, 2026, IBM announced a definitive agreement to acquire HRL Laboratories from Boeing and General Motors, so how this architecture will be used going forward (e.g., relative to IBM's superconducting-qubit roadmap) remains unclear.

**Terms to know**

* **Spin qubit**: A qubit that encodes information in the spin state of an electron or nucleus, notable for compatibility with existing semiconductor fabrication processes.
* **CMOS controller**: Circuitry that generates the voltage pulses and control signals applied to qubits; normally located at room temperature, but here designed to operate at 4 kelvin.
* **Cryostat**: A specialized refrigeration system that keeps qubits near absolute zero.
* **Wiring bottleneck**: The scaling problem where the number of room-temperature-to-cryogenic control wires grows proportionally with qubit count, becoming impractical at large scale.
* **Repetition code**: The simplest form of quantum error-correcting code, which stores the same logical information redundantly across multiple physical qubits to detect and correct errors.
* **Quantum error correction (QEC)**: Procedures that protect logical qubit information from physical qubit noise and errors, considered essential for large-scale, practical quantum computing.
* **Superconducting ribbon cable**: A cryogenic interconnect bundling many signal traces together while minimizing heat conducted into the coldest stage.

**Why it is worth watching**

For quantum computers to become useful at scale, they will eventually need to manage thousands to millions of qubits, and simply adding more room-temperature-to-cryostat wires per qubit does not scale. This paper demonstrates a concrete architecture that moves control electronics into the cryogenic environment and runs error correction autonomously there, making it a notable engineering answer to "how do we actually build a scalable system," not just "how do we add more qubits."

---

## My take

이 논문은 양자 컴퓨터 규모 확장의 실질적 걸림돌인 배선 문제를, 큐비트 제어 회로 자체를 극저온 환경 안으로 옮기는 방식으로 정면 공략했다는 점에서 공학적으로 설득력이 있습니다. 18큐비트라는 규모 자체는 여전히 작고, 이 아키텍처가 수천~수백만 큐비트로 그대로 확장되는지는 앞으로 더 지켜봐야 하지만, "오류 정정을 극저온 컨트롤러만으로 자율 수행"했다는 것은 실용적인 대규모 양자 컴퓨터를 어떻게 지을 것인가에 대한 구체적 답을 제시한 사례로서 의미가 있습니다. 다만 이번 세션에서는 네트워크 제약으로 Nature 원문을 직접 열람하지 못해 여러 2차 보도를 교차 검증하는 방식으로 작성했으며, IBM의 HRL 인수 발표 직후 나온 논문이라는 점도 향후 활용 방향에 변수로 남아 있습니다.

This paper makes an engineering-credible attack on the wiring problem that threatens quantum computer scaling, by physically relocating qubit control circuitry into the cryogenic environment. The 18-qubit scale is still modest, and whether this architecture cleanly extends to thousands or millions of qubits remains to be seen, but demonstrating fully autonomous, cryogenic-controller-only error correction is a concrete answer to how a scalable, practical quantum computer might actually be built. That said, network constraints in this session prevented direct access to the original Nature article, so this summary relies on cross-checked secondary reporting, and the fact that this result landed just after IBM's announced acquisition of HRL adds some uncertainty about how the work will be carried forward.
