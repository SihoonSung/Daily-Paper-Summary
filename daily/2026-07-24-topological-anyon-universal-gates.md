---
title: "Universal gates from braiding and fusing anyons on quantum hardware"
date: 2026-07-24
topic: quantum-computing
tags: [quantum-computing, topological-quantum-computing, non-abelian-anyons, trapped-ions, quantum-error-correction, fault-tolerance, quantinuum]
source: https://www.nature.com/articles/s41586-026-10709-y
---

Universal gates from braiding and fusing anyons on quantum hardware

* Date: 2026-07-24
* Source: https://www.nature.com/articles/s41586-026-10709-y
* Topic: Quantum Computing / Topological Quantum Computing
* Why it matters: The team built the first complete "universal" set of quantum gates out of braiding and fusing non-Abelian anyons on real hardware, and used it to directly prepare a fault-tolerance resource state (a "magic state") that normally requires an extremely resource-hungry purification process — a potential lever for cutting the overhead of error-corrected quantum computers.

## Korean Summary

**한줄 요약**

Quantinuum, 시카고대학교 프리츠커 분자공학대학원(UChicago PME), 하버드대학교, 스토니브룩대학교 공동 연구진이 Quantinuum의 54큐비트 포획 이온 프로세서 H2 위에서 비아벨(non-Abelian) 애니온의 "땋기(braiding)"와 "융합(fusion)"을 결합해 범용 양자 게이트 집합을 구현하고, 이를 이용해 결함허용 계산에 필요한 "마법 상태(magic state)"를 위상학적으로 직접 준비했다고 Nature에 2026년 7월 15일 발표했다.

**핵심 아이디어**

위상 양자컴퓨팅은 양자 정보를 개별 입자가 아니라 여러 입자로 이루어진 계의 전역적·위상학적 성질에 저장해, 국소적 잡음에 상대적으로 둔감하게 만드는 접근법이다. 그러나 실제로 임의의 양자 계산을 수행하려면 애니온을 이리저리 움직이는 "땋기" 연산만으로는 부족하고, 특정 종류의 위상 질서(topological order)가 이론적으로 "범용(universal)" 게이트 집합을 지원해야 한다. 이 논문은 가장 작은 비아벨 군인 S3의 양자 이중군(quantum double)에 해당하는 위상 질서 상태를 54개의 물리 큐비트로 준비하고, 땋기 연산과 애니온 융합 결과의 측정을 함께 사용하면 이 "최소 비아벨" 위상 질서만으로도 범용 계산이 가능함을 실험적으로 보였다.

**무엇이 새로운가?**

* 최소 비아벨 군인 S3의 위상 질서를 54큐비트 규모로 준비하고, 3준위 정보(큐트리트, qutrit)를 비국소적인 애니온 융합 공간에 인코딩
* 땋기(엔탱글링 연산)와 애니온 전하 측정(융합)이라는 서로 다른 두 연산을 결합해 범용 위상 게이트 집합과 판독(readout)을 함께 구현
* 애니온 융합을 계산의 기본 연산(primitive)으로 취급함으로써, 이전에는 범용성이 불확실했던 "최소 비아벨" 위상 질서도 범용 계산에 쓸 수 있음을 증명
* 자원 소모가 매우 큰 마법 상태 증류(magic state distillation) 과정 없이, 위상학적 연산만으로 마법 상태를 직접 준비
* 2024년 같은 팀이 처음으로 비아벨 애니온의 생성·조작을 시연한 후속 연구로, "생성"에서 "범용 계산"으로 성과를 확장

**어떻게 작동하는가?**

1. **위상 질서 상태 준비**: Quantinuum H2 포획 이온 프로세서의 54개 큐비트를 이용해 적응형 회로(adaptive circuit)로 S3 양자 이중군의 바닥상태 파동함수를 준비한다.
2. **정보 인코딩**: 계산에 쓰일 정보(큐트리트)를 특정 입자의 국소적 상태가 아니라, 비아벨 플럭스들의 비국소적 융합 공간에 인코딩한다.
3. **땋기 연산**: 애니온에 해당하는 여기(excitation)들을 서로 교환하는 순서를 제어해 얽힘 게이트를 구현한다. 결과가 교환 순서에 의존하기 때문에 국소적 잡음에 어느 정도 저항력을 갖는다.
4. **융합 측정**: 두 애니온을 합치고 그 결과(어떤 전하가 나오는지)를 측정하는 "융합"을 두 번째 연산으로 사용해, 땋기만으로는 얻을 수 없는 게이트와 판독을 추가한다.
5. **마법 상태 준비**: 위 두 연산을 조합해 결함허용 계산의 핵심 자원인 마법 상태를 위상학적 방식으로 직접 만들어낸다.

**강점**

* 특정 이론적 조건 하에서 "최소" 비아벨 위상 질서만으로도 범용 계산이 가능함을 실제 하드웨어에서 시연
* 자원 소모가 큰 마법 상태 증류를 우회할 수 있는 대안적 경로를 실험적으로 제시 — 마법 상태 증류는 결함허용 양자컴퓨팅에서 물리적 큐비트와 제어 자원의 상당 부분(추정치에 따라 최대 약 90%)을 소모하는 병목으로 꼽힘
* Quantinuum, 시카고대, 하버드대, 스토니브룩대 등 위상 물질 및 양자 하드웨어 분야의 여러 그룹이 공동 참여한 연구로 이론과 실험이 긴밀히 결합
* 2024년 비아벨 애니온 생성 시연에 이은 명확한 후속 성과로, 위상 양자컴퓨팅 로드맵의 진전을 보여줌

**한계**

* 이번 시연은 트랩된 이온을 이용해 회로적으로(디지털 방식으로) 위상 질서 파동함수를 "시뮬레이션"한 것으로, 애니온이 자연적인 위상 물질 속에서 본질적으로 보호되는 유한 에너지 여기(intrinsic excitation)는 아니다 — 즉 진정한 물리적 위상 보호와는 구별되는 "회로 기반 구현"이라는 점에 유의해야 한다
* 관련 선행 연구들에 따르면 이런 디지털 구현에서의 땋기 통계는 전반적인 위상(phase)까지만 잘 정의되는 "사영적(projective)" 비아벨 통계이며, 연속적인 비파괴 안정자(stabilizer) 측정을 동반한 엄밀한 의미의 오류 수정 결함허용성은 아직 이 실험에 포함되지 않았다
* 54큐비트, 최소 비아벨 군(S3)이라는 소규모·개념 증명 단계로, 대규모 결함허용 계산으로의 확장성은 별도로 검증되어야 한다
* 본 요약은 논문 원문 전체에 직접 접근하지 못한 채 Nature 초록 페이지 접근 실패, 언론 보도(phys.org, UChicago PME 보도자료, 전문 매체) 및 저자들의 관련 이전 발표 자료에 기반해 작성되었다

**알아둘 용어**

* 비아벨 애니온(non-Abelian anyon): 2차원(또는 유효 2차원) 계에서 나타나는 준입자로, 서로 교환하는 순서에 따라 결과가 달라지는 특이한 통계를 갖는다
* 위상 질서(topological order): 국소적 성질이 아니라 전역적·위상학적 구조에 정보가 저장되는 양자 다체계의 상태로, 국소 잡음에 상대적으로 강건하다
* 땋기(braiding): 애니온들을 공간(및 시간)에서 서로 교환하는 연산으로, 그 순서 자체가 양자 게이트로 작동한다
* 융합(fusion): 두 개 이상의 애니온을 결합해 그 결과로 나오는 입자 종류(전하)를 측정하는 연산
* 마법 상태(magic state): 결함허용 양자컴퓨팅에서 범용 게이트 집합을 완성하기 위해 필요한 특별한 자원 상태로, 통상 값비싼 증류 과정을 거쳐 얻는다
* 마법 상태 증류(magic state distillation): 노이즈가 있는 여러 개의 저품질 마법 상태를 결합해 소수의 고품질 마법 상태로 정제하는 과정으로, 물리적 큐비트를 대량으로 소모한다
* 큐트리트(qutrit): 0, 1, 2의 세 가지 상태를 가질 수 있는 양자정보 단위로, 두 상태만 갖는 일반 큐비트를 확장한 개념

**왜 주목할 만한가?**

결함허용 양자컴퓨팅의 가장 큰 병목 중 하나는 마법 상태 증류에 필요한 막대한 자원 오버헤드다. 이 논문은 애니온의 땋기와 융합을 함께 활용하면 비교적 단순한 위상 질서만으로도 범용 계산과 마법 상태의 직접 준비가 가능함을 실제 하드웨어에서 보여줌으로써, 오버헤드를 줄이는 대안적 설계 방향에 실험적 근거를 더했다. 다만 이는 개념 증명 단계이며, "디지털로 구현된 위상 질서"와 "물리적으로 본질적인 위상 보호"의 구분을 명확히 인지할 필요가 있다.

---

## English Summary

**One-line summary**

A collaboration between Quantinuum, the University of Chicago Pritzker School of Molecular Engineering (UChicago PME), Harvard University, and Stony Brook University demonstrated, on Quantinuum's 54-qubit H2 trapped-ion processor, a universal gate set built from braiding and fusing non-Abelian anyons, and used it to topologically prepare a "magic state" needed for fault-tolerant computation. The work was published in Nature on July 15, 2026.

**Core idea**

Topological quantum computing stores quantum information in the global, topological properties of a many-body system rather than in individual particles, making it relatively insensitive to local noise. But performing arbitrary computations requires more than moving ("braiding") anyons around — the underlying topological order has to be theoretically capable of supporting a full "universal" gate set. This paper prepares the ground-state wavefunction of the quantum double of S3 — the smallest non-Abelian group — on 54 physical qubits, and shows that combining braiding with measurement of anyon fusion outcomes makes even this "minimally non-Abelian" topological order universal for computation.

**What is new?**

* Preparation of S3 topological order (the smallest non-Abelian group) at 54-qubit scale, encoding three-level information (qutrits) in the nonlocal fusion space of non-Abelian fluxes
* Combining two distinct operations — braiding (an entangling operation) and measurement of anyon fusion outcomes (charge measurement) — to realize a universal topological gate set plus readout
* Treating anyon fusion as a computational primitive, proving that even "minimally" non-Abelian topological orders (whose universality was previously unclear) can be made universal
* Topologically preparing a magic state directly, without the resource-intensive magic state distillation process normally required
* A direct follow-up to the same team's 2024 demonstration of creating and manipulating non-Abelian anyons, extending the result from "creation" to "universal computation"

**How does it work?**

1. **Prepare the topological state**: Using an adaptive circuit on Quantinuum's 54-qubit H2 trapped-ion processor, the team prepares the ground-state wavefunction of the S3 quantum double.
2. **Encode information**: Computational information (qutrits) is encoded not in any single particle's local state, but in the nonlocal fusion space of non-Abelian flux excitations.
3. **Braiding**: Controlling the order in which anyon-like excitations are exchanged implements entangling gates; because the outcome depends on exchange order, this provides some inherent resistance to local noise.
4. **Fusion measurement**: Merging two anyons and measuring the resulting charge — "fusion" — serves as a second operation that provides gates and readout capabilities braiding alone cannot.
5. **Magic state preparation**: Combining braiding and fusion, the team topologically prepares a magic state, a key resource for fault-tolerant computation.

**Strengths**

* Demonstrates on real hardware that even a "minimally" non-Abelian topological order can support universal computation under the right combination of operations
* Provides an experimental alternative pathway to bypass costly magic state distillation, which is widely considered the most expensive bottleneck in fault-tolerant quantum computing — estimates suggest it can consume up to roughly 90% of a machine's physical qubit and control resources
* Brings together multiple leading groups in topological matter and quantum hardware (Quantinuum, UChicago, Harvard, Stony Brook), tightly coupling theory and experiment
* A clear, incremental follow-up to the team's 2024 non-Abelian anyon creation result, showing concrete progress on the topological quantum computing roadmap

**Limitations**

* The demonstration is a circuit-based ("digital") preparation of a topologically ordered wavefunction on trapped ions, not anyons as intrinsic, finite-energy excitations of a naturally topologically ordered physical medium — this is an important distinction from true physical topological protection
* Related prior work on digital anyon simulations notes that braiding statistics in such implementations are only well-defined up to an overall phase ("projective" non-Abelian statistics), and that strict fault-tolerant protection — which requires continuous, non-destructive stabilizer measurements during braiding — was not part of this kind of experiment
* This is a small-scale, proof-of-concept demonstration (54 qubits, the smallest non-Abelian group S3); scaling to large, fault-tolerant computations remains to be shown
* This summary was written without direct access to the full paper text — the Nature abstract page could not be reached in this session, so the summary relies on press coverage (phys.org, UChicago PME's press release), specialist quantum-computing outlets, and the authors' related prior publications

**Terms to know**

* Non-Abelian anyon: A quasiparticle arising in two-dimensional (or effectively two-dimensional) quantum systems whose exchange statistics depend on the order in which particles are swapped
* Topological order: A phase of a quantum many-body system in which information is stored in global, topological structure rather than local properties, giving it relative robustness to local noise
* Braiding: The operation of exchanging anyons in space (and time); the exchange sequence itself acts as a quantum gate
* Fusion: The operation of combining two or more anyons and measuring which particle type (charge) results
* Magic state: A special resource state required, together with a limited native gate set, to complete a universal gate set in fault-tolerant quantum computing; normally obtained through costly distillation
* Magic state distillation: A process that combines many noisy, low-quality magic states to produce fewer high-quality ones, consuming large numbers of physical qubits
* Qutrit: A unit of quantum information with three possible states (0, 1, 2), generalizing the two-state qubit

**Why it is worth watching**

One of the biggest bottlenecks in fault-tolerant quantum computing is the enormous resource overhead of magic state distillation. By showing on real hardware that combining anyon braiding with fusion enables universal computation and direct magic-state preparation using a relatively simple, minimally non-Abelian topological order, this work adds experimental grounding to an alternative design direction aimed at reducing that overhead. It remains a proof-of-concept, though, and the distinction between a "digitally realized" topological order and physically intrinsic topological protection is important to keep in mind.

---

## My take

이 논문은 위상 양자컴퓨팅 로드맵에서 "애니온을 만들고 조작할 수 있다"는 이전 단계에서 "실제로 범용 계산에 쓸 수 있고, 값비싼 마법 상태 증류까지 우회할 수 있다"는 단계로 넘어간 의미 있는 진전이다. 다만 이는 트랩된 이온 위에서 회로적으로 위상 질서를 구현한 개념 증명이며, 물리적으로 본질적인 위상 보호를 갖는 하드웨어(예: 마요라나 기반 큐비트)와는 구분해서 이해할 필요가 있다. 또한 본 요약은 논문 원문에 직접 접근하지 못한 채 언론 보도와 저자들의 이전 발표에 의존해 작성되었으므로, 세부 수치나 조건은 원문 확인이 필요하다.

This paper marks a meaningful step in the topological quantum computing roadmap — moving from "we can create and manipulate anyons" to "this minimally non-Abelian order supports universal computation and can even bypass expensive magic state distillation." That said, it remains a proof-of-concept realized as a digital circuit on trapped ions, and should be understood as distinct from hardware with intrinsic physical topological protection (such as Majorana-based qubit efforts). This summary also could not draw on the full original paper — the Nature page was unreachable in this session — and instead relies on press coverage and the authors' earlier publications, so readers should verify specific figures and conditions against the primary source.
