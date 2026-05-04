---
title: "Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture"
date: 2026-05-02
topic: quantum computing
tags: [quantum computing, fault tolerance, error correction, trapped ions, LDPC, hardware, architecture]
source: https://arxiv.org/abs/2604.19481
---

Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture

* Date: 2026-05-02
* Source: https://arxiv.org/abs/2604.19481
* Topic: Quantum Computing / Fault-Tolerant Architecture
* Why it matters: IonQ proposes the first end-to-end, buildable blueprint for a fault-tolerant trapped-ion quantum computer that can execute millions of logical operations on hundreds of error-corrected qubits using as few as 2,514 physical qubits, bridging the gap between today's noisy hardware and practically useful quantum computation.

## Korean Summary

**한줄 요약**

IonQ의 연구팀이 오류 수정이 완전히 적용된 포획 이온 양자 컴퓨터의 처음부터 끝까지 실제로 만들 수 있는 설계도를 공개했다. 2,514개의 물리 큐비트만으로 110개의 논리 큐비트를 구성하고 하루 약 100만 번의 T 게이트를 실행할 수 있으며, 약 10,000개 물리 큐비트로 화학적 정밀도의 양자 시뮬레이션이 가능하다고 분석한다.

**핵심 아이디어**

양자 컴퓨터의 실제 활용을 막는 가장 큰 장벽은 오류다. 물리 큐비트는 외부 환경의 간섭을 받아 연산이 금방 틀어지기 때문에, 여러 물리 큐비트를 묶어 하나의 "논리 큐비트"를 만드는 양자 오류 수정(QEC)이 필수다. 그러나 기존 표면 코드(Surface Code) 기반 설계는 논리 큐비트 1개에 수천~수만 개의 물리 큐비트가 필요해 규모 확장이 어렵다. Walking Cat 아키텍처는 통신 분야에서 쓰이는 LDPC(저밀도 패리티 검사) 코드를 양자 오류 수정에 적용하고, 포획 이온의 이동(이온 셔틀링)을 1급 설계 요소로 활용함으로써 훨씬 적은 물리 큐비트로 동일한 수준의 내결함성을 달성한다.

**무엇이 새로운가?**

- **완전 스택 설계도**: 컴파일러, QEC 프로토콜, 마이크로 아키텍처, 디코더, 시뮬레이션을 포함한 처음부터 끝까지 통합된 청사진을 공개
- **LDPC 코드 기반 QEC**: 표면 코드 대신 코드 거리 대비 인코딩 효율이 높은 LDPC 코드 전용 아키텍처를 설계
- **캣 팩토리(Cat Factory) 개념**: 논리 연산에 필요한 "캣 상태(Cat State)"를 전용 팩토리에서 생성·분배하는 모듈식 자원 공급 방식 도입
- **세 가지 코드 인스턴스**: 단순(Simple), 고속(Fast, [[70,6,9]] 코드), 고밀도(Dense, [[102,22,9]] 코드) 세 가지 실현 가능한 구성 제시
- **HMRS 설계 원칙**: 계층성(Hierarchy), 모듈성(Modularity), 규칙성(Regularity), 단순성(Simplicity)을 고전 컴퓨터 아키텍처 원칙에서 차용해 양자 컴퓨터 설계에 적용

**어떻게 작동하는가?**

1. **물리 기반**: QCCD(양자 전하 결합 소자) 칩에 포획 이온을 가두고, 99.99% 이상 충실도의 2큐비트 게이트와 이온 이동(셔틀링) 기능을 활용한다.
2. **LDPC 코드 적용**: 물리 큐비트들을 [[70,6,9]] 또는 [[102,22,9]] 코드로 묶어 논리 큐비트를 만든다. 코드 [[n,k,d]]는 n개 물리 큐비트로 k개 논리 큐비트를 인코딩하며 거리 d를 가짐을 의미한다.
3. **이온 셔틀링**: LDPC 코드는 최근접 이웃 이상의 큐비트 연결성이 필요한데, 포획 이온 시스템은 이온을 물리적으로 이동시켜 이를 자연스럽게 해결한다. 이 이동이 아키텍처 이름의 "Walking" 부분이다.
4. **캣 상태 생성**: 전용 "캣 팩토리"가 오류 감지에 사용하는 캣 상태를 지속적으로 생성한다. 캣 상태는 슈뢰딩거의 고양이처럼 두 상태의 중첩을 이용해 논리 게이트를 수행하는 양자 자원이다. 이것이 "Cat" 부분이다.
5. **오류 검출 및 수정**: 캣 상태를 측정해 오류를 감지하되, 연산 자체는 무너뜨리지 않는다. 디코더가 오류 패턴을 빠르게 분석해 수정 연산을 적용한다.
6. **논리 연산 실행**: 수정된 논리 큐비트 위에서 양자 알고리즘을 실행한다. 고밀도 인스턴스에서는 2,514개 물리 큐비트로 110개 논리 큐비트를 구성하고 하루 약 100만 번의 T 게이트를 처리한다.
7. **규모 확장**: 약 10,000개 물리 큐비트 수준에서 Heisenberg 해밀토니안 시뮬레이션을 화학적 정밀도로 약 1개월 내에 수행할 수 있다고 분석한다.

**강점**

- 이론이 아닌 실제로 만들 수 있는 수준의 구체적 설계로, 기존 실험에서 이미 입증된 하드웨어 성능을 전제로 함
- LDPC 코드 적용으로 동일한 내결함성 수준에서 물리 큐비트 수를 표면 코드 대비 크게 절감
- 모듈식 설계(HMRS)로 구성 요소 간 인터페이스가 명확해 제작·검증이 용이
- 컴파일러부터 디코더까지 전체 소프트웨어 스택을 함께 설계해 즉시 구현 가능성을 높임
- 이온 셔틀링이라는 포획 이온 시스템 고유의 강점을 최대한 활용

**한계**

- 아직 설계도이며 실제 구축 및 실험적 검증은 이루어지지 않음
- 2,514개 이상의 이온을 안정적으로 QCCD 칩에서 운영하는 것은 현재 수준에서 주요 공학적 도전 과제
- 99.99% 2큐비트 게이트 충실도를 대규모로 일관되게 달성해야 한다는 요건이 있으며, 이를 확장된 규모에서 유지하기는 아직 어려움
- 오류 수정 임계값 이하의 실제 운영 조건 확보에 대한 검증 필요
- 실용적 양자 우위를 달성하기까지의 시간표는 불확실

**알아둘 용어**

- **내결함성 양자 컴퓨팅 (Fault-Tolerant Quantum Computing, FTQC)**: 물리 큐비트 오류가 발생해도 전체 연산 결과가 보호되도록 양자 오류 수정을 실행하는 양자 컴퓨팅 방식
- **LDPC 코드 (Low-Density Parity-Check Code)**: 저밀도 패리티 검사 코드. 고전 통신에서 쓰이던 오류 정정 코드로, 양자 오류 수정에 적용하면 표면 코드 대비 물리 큐비트 오버헤드가 낮음
- **캣 상태 (Cat State)**: 중첩과 얽힘을 이용한 특수 양자 상태로, 논리 게이트 수행에 필요한 자원 상태. "슈뢰딩거의 고양이"에서 유래
- **QCCD (Quantum Charge-Coupled Device)**: 이온을 전기장 포텐셜로 가두고 이동시키는 포획 이온 하드웨어 플랫폼
- **이온 셔틀링 (Ion Shuttling)**: 포획 이온 시스템에서 이온을 물리적으로 이동시켜 원거리 큐비트 간 연결성을 구현하는 방법
- **논리 큐비트 (Logical Qubit)**: 여러 물리 큐비트로 오류 수정을 포함하여 인코딩된 가상의 오류-내성 큐비트
- **T 게이트 (T Gate)**: 비-클리퍼드(Non-Clifford) 양자 게이트로, 양자 계산의 보편성을 완성하는 핵심 게이트이며 오류 수정 비용이 가장 높음

**왜 주목할 만한가?**

양자 컴퓨터가 실제로 유용해지려면 내결함성이 필수적이지만, "어떻게 만드는가"에 대한 구체적이고 완전한 설계도는 지금까지 드물었다. Walking Cat 아키텍처는 기존 실험실 수준의 하드웨어 성능에서 출발해, 수천 개 물리 큐비트로 수백 개 논리 큐비트와 수백만 번의 논리 연산을 처리하는 실현 가능한 경로를 제시한다. 화학 시뮬레이션, 암호 해독, 최적화 등 양자 우위가 기대되는 응용 분야에서 실질적인 타임라인을 제시한 최초의 종합 청사진 중 하나다.

---

## English Summary

**One-line summary**

IonQ's Walking Cat architecture is a complete, buildable blueprint for a fault-tolerant trapped-ion quantum computer that uses Low-Density Parity-Check (LDPC) codes and cat states to run hundreds of logical qubits and millions of logical gate operations using only a few thousand physical qubits. It is the first end-to-end design—covering compiler, error-correction protocols, micro-architecture, decoder, and simulation—intended to bridge the gap between today's noisy intermediate-scale quantum hardware and genuinely useful quantum computation.

**Core idea**

The central barrier to useful quantum computing is noise: physical qubits degrade rapidly, so multiple physical qubits must be grouped into a single error-corrected "logical qubit" via quantum error correction (QEC). The dominant QEC approach, the surface code, requires thousands of physical qubits per logical qubit, making large-scale fault-tolerant machines impractical in the near term. The Walking Cat architecture replaces surface codes with LDPC codes—long used in classical communications—which encode more logical qubits per physical qubit at the same distance. It then exploits trapped-ion hardware's unique ability to physically shuttle ions around a chip to satisfy the long-range connectivity that LDPC codes require.

**What is new?**

- **Full-stack blueprint**: A single paper covers the entire system—compiler, QEC protocol, micro-architecture, decoder, and hardware simulations—in actionable detail
- **LDPC-based QEC for trapped ions**: Entire architecture designed around modern LDPC codes rather than surface codes, achieving significantly lower physical-qubit overhead
- **Cat factory abstraction**: A dedicated module produces "cat states" continuously and ships them to where logical operations need them, making the design cleanly modular
- **Three concrete code instances**: Simple (single LDPC code), Fast ([[70,6,9]] with Clifford-frame tracking), and Dense ([[102,22,9]] encoding 22 logical qubits per memory block)
- **HMRS design principles**: Hierarchy, Modularity, Regularity, and Simplicity—borrowed from classical computer architecture—applied systematically to the quantum stack

**How does it work?**

1. **Hardware platform**: A QCCD (quantum charge-coupled device) chip traps ions using electric fields. Current QCCD systems can achieve two-qubit gate fidelity above 99.99% and support controlled ion movement.
2. **LDPC encoding**: Physical qubits are grouped into LDPC code blocks. The notation [[n,k,d]] means n physical qubits encode k logical qubits with code distance d. The dense instance uses [[102,22,9]], encoding 22 logical qubits per block.
3. **Ion shuttling for connectivity**: LDPC codes require multi-hop qubit interactions. Trapped-ion systems naturally provide this by physically moving ions across the chip—this is the "Walking" in the name.
4. **Cat state generation**: A dedicated "cat factory" module continuously produces cat states—quantum superpositions used as resources for fault-tolerant logical measurements that detect errors without collapsing the computation. This is the "Cat" in the name.
5. **Error detection and correction**: Cat states probe the logical qubits for errors. A fast classical decoder analyzes error syndromes and applies corrections, keeping the computation on track.
6. **Logical computation**: Algorithms execute on the corrected logical qubits. The dense instance runs ~1 million T gates per day on 110 logical qubits with only 2,514 physical qubits.
7. **Scaling**: At approximately 10,000 physical qubits, the architecture is estimated to simulate the Heisenberg Hamiltonian at chemical accuracy in roughly one month—a potentially commercially relevant computation.

**Strengths**

- Designed around hardware capabilities already demonstrated in the lab, not theoretical future devices
- LDPC codes provide substantially lower physical-qubit overhead than surface codes at the same error-correction distance
- HMRS modularity keeps component interfaces clean, making the machine easier to build and verify incrementally
- Full software stack (compiler to decoder) designed together, avoiding the common gap between QEC theory and practical implementation
- Ion shuttling as a first-class primitive turns a trapped-ion constraint into a design advantage

**Limitations**

- The paper is a blueprint, not a built machine; experimental validation at scale is still needed
- Operating thousands of ions stably in a QCCD chip simultaneously is a substantial unsolved engineering problem
- The design requires sustained 99.99% two-qubit gate fidelity at scale, which has not yet been routinely demonstrated for large ion registers
- Error thresholds must be met in practice under realistic noise, not just in simulation
- Timelines for building such a machine are not specified, and remain uncertain

**Terms to know**

- **Fault-tolerant quantum computing (FTQC)**: A mode of quantum computation in which quantum error correction is actively applied, protecting the result even when individual physical qubits fail
- **LDPC code (Low-Density Parity-Check code)**: An error-correcting code originally from classical communications, characterized by sparse parity-check matrices; its quantum analog encodes more logical qubits per physical qubit than surface codes
- **Cat state**: A quantum superposition used as a resource state for fault-tolerant logical measurements; named after Schrödinger's cat thought experiment
- **QCCD (Quantum Charge-Coupled Device)**: A trapped-ion hardware platform that confines ions in electric-field traps and can shuttle them between different zones on a chip
- **Ion shuttling**: Moving trapped ions physically around a chip to enable two-qubit gates between non-neighboring ions, providing any-to-any connectivity
- **Logical qubit**: An error-protected qubit encoded across multiple physical qubits via a quantum error-correcting code
- **T gate**: A non-Clifford quantum gate essential for universal quantum computation; the most expensive gate to implement fault-tolerantly, and thus a key unit for measuring algorithmic cost

**Why it is worth watching**

Fault-tolerant quantum computing has long been treated as a distant goal whose architecture was underspecified. The Walking Cat paper is one of the first full-stack, end-to-end designs from a major quantum hardware company that lays out a concrete, buildable path. The qubit counts it targets—a few thousand to around ten thousand physical qubits—are within realistic reach of near-term hardware roadmaps. If the claimed performance holds under experimental conditions, quantum simulations relevant to drug discovery, materials science, and cryptanalysis could become accessible far sooner than current timelines suggest.

**My take**

Walking Cat 아키텍처는 양자 컴퓨팅이 "언제가 될 것이다"라는 막연한 기대에서 "이렇게 만들면 된다"는 구체적 공학 문서로 전환하는 중요한 이정표다. LDPC 코드와 이온 셔틀링의 조합은 설득력 있으며, HMRS 원칙은 실제 제작·검증을 고려한 현실적 설계 철학을 반영한다. 다만 규모 확대 시 하드웨어 충실도 유지라는 근본적인 공학 문제가 남아 있으며, 실제 작동하는 시스템 구축까지의 간극은 여전히 상당하다.

The Walking Cat architecture is a meaningful transition from quantum computing as a vague future promise to a concrete engineering document. The combination of LDPC codes and ion shuttling is technically coherent, and the HMRS design principles reflect genuinely practical engineering thinking. The key uncertainty remains whether hardware fidelity can be maintained as ion counts scale—a gap that only experimental hardware will close.
