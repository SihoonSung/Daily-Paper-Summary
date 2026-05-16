---
title: "Federation of Experts: Communication Efficient Distributed Inference for Large Language Models"
date: 2026-05-10
topic: AI
tags: [AI, inference, MoE, distributed-systems, communication-efficiency, expert-parallelism, LLM-serving]
source: https://arxiv.org/abs/2605.06206
---

Federation of Experts: Communication Efficient Distributed Inference for Large Language Models

* Date: 2026-05-10
* Source: https://arxiv.org/abs/2605.06206
* Topic: AI / Distributed Inference / Systems
* Why it matters: Mixture-of-Experts (MoE) is now the dominant architecture for large-scale LLMs, but distributed inference requires expensive all-to-all network communication to route tokens to remote experts. This paper introduces Federation of Experts (FoE), a new MoE architecture that structurally guarantees tokens are always processed locally, eliminating cross-GPU all-to-all communication entirely on a single node and reducing it to fast intra-node links on multi-node deployments—cutting end-to-end inference latency by up to 1.95× with no degradation in model quality.

## Korean Summary

**한줄 요약**

MoE(Mixture-of-Experts) 모델의 분산 추론에서 발생하는 all-to-all 통신 병목을 구조적으로 제거하는 새로운 아키텍처 Federation of Experts(FoE)를 스탠퍼드 대학교 연구팀이 제안했다. FoE는 MoE 블록을 KV 헤드 단위의 클러스터로 재구성해, 모든 토큰이 자신이 머무는 GPU 내 전문가에게만 라우팅되도록 보장함으로써 Local Activation Rate(LAR)를 구조적으로 1.0으로 고정한다. 1B·7B 모델 실험에서 LongBench 기준 최대 1.95배의 지연 감소와 동등한 생성 품질을 달성한다.

**핵심 아이디어**

MoE 모델은 각 토큰을 소수의 전문가(expert)에만 라우팅해 활성화 파라미터를 줄이지만, 분산 환경에서는 라우팅된 전문가가 다른 GPU에 있을 경우 토큰을 네트워크를 통해 전송해야 한다. 이 all-to-all 통신은 GPU 수가 늘어날수록 네트워크를 경유하는 토큰 비율—Local Activation Rate(LAR)의 역수—이 선형적으로 증가해 점점 심각한 지연 병목이 된다. FoE는 MoE 레이어를 KV 어텐션 헤드 수와 일치하는 클러스터로 분할하고, 각 클러스터의 전문가들을 동일 GPU에 배치한다. 어텐션 후 잔차를 클러스터 간에 합산하여 다음 MoE 블록의 라우팅 입력으로 쓰는 방식으로, 아키텍처 수준에서 LAR = 1.0을 보장한다.

**무엇이 새로운가?**

- **구조적 LAR 보장**: 기존 MoE가 실행 시점에야 LAR을 결정하는 것과 달리, FoE는 전문가-GPU 매핑을 아키텍처 설계 단계에서 확정해 LAR = 1.0을 수학적으로 보장
- **클러스터-KV 헤드 결합**: MoE 전문가 그룹을 어텐션 KV 헤드 하나씩 담당하도록 재구조화함으로써, 어텐션과 FFN 레이어의 통신 패턴을 통합 설계
- **단일 노드 all-to-all 완전 제거**: 단일 노드에서는 모든 전문가가 같은 노드 내에 있으므로 all-to-all 통신이 원천적으로 발생하지 않음
- **멀티 노드 통신 국소화**: 멀티 노드에서도 all-to-all이 고속 인트라-노드 패브릭(NVLink 등) 내에만 머물게 되어, 저속 크로스-노드 링크(InfiniBand)를 통한 통신을 제거
- **약 10배 통신량 절감**: 기존 MoE 대비 통신 볼륨이 10배 수준으로 감소, LongBench에서 최대 1.95배 레이턴시 단축

**어떻게 작동하는가?**

1. **클러스터 분할**: MoE 레이어를 K개의 클러스터로 나눈다(K = KV 헤드 수). 각 클러스터는 전체 전문가 풀의 1/K를 담당하며, 해당 전문가들은 동일 GPU에 배치된다.
2. **어텐션-전문가 결합**: 각 클러스터는 담당 KV 헤드로 어텐션 연산을 수행한 뒤, 해당 클러스터 내 전문가들로만 토큰을 라우팅한다. 이 과정에서 GPU 간 토큰 이동이 없다.
3. **잔차 집계**: 클러스터별 어텐션·FFN 연산 완료 후, 잔차 출력을 all-reduce(합산)로 합친다. 이 합산 트래픽은 작은 스칼라-레벨 데이터이며, 멀티 노드에서도 인트라-노드 링크로 처리된다.
4. **다음 블록 라우팅 입력**: 합산된 잔차가 다음 트랜스포머 블록의 라우팅 입력이 되어, 전체 레이어 스택에서 이 패턴이 반복된다.
5. **균일 부하 분산**: 각 클러스터가 동수의 전문가를 담당하고 어텐션 헤드와 1:1 대응되므로, GPU 간 부하가 구조적으로 균등하게 분배된다.

**강점**

- 통신 병목 구조적 해결: 런타임 스케줄링이나 토큰 드롭 없이 아키텍처 설계만으로 all-to-all 통신을 제거 또는 국소화
- 품질 보존: 1B·7B 모델 실험에서 동일 크기 표준 MoE와 동등한 제로샷 정확도를 유지
- 확장성 개선: GPU 수가 늘어도 LAR이 하락하지 않아, 대규모 클러스터로의 확장이 선형적으로 유리
- LongBench 기준 최대 1.95배 레이턴시 단축—동일 하드웨어에서 처리량 또는 응답 시간 대폭 개선
- 기존 MoE 설계 원칙과 호환: 어텐션·FFN 구조를 근본적으로 바꾸지 않고 레이어 내 클러스터링만 변경

**한계**

- 1B·7B 규모 모델에서만 검증—수백B 파라미터 이상의 초대형 모델로의 일반화는 미확인
- KV 헤드 수와 클러스터 수를 일치시키는 설계 원칙이 멀티-헤드-어텐션(MHA)이 아닌 GQA/MQA 등 변형 어텐션에서 어떻게 작동하는지 논문에서 상세히 다루지 않음
- 클러스터 내 균일 부하가 라우팅 불균형(특정 전문가에 토큰이 몰리는 현상)에 얼마나 취약한지 추가 분석 필요
- 사전 학습(pretraining)이 아닌 추론 단계에 초점—FoE 구조로 처음부터 학습한 모델이 존재하지 않으면 배포가 어려울 수 있음
- 아직 커뮤니티 검증 및 대규모 프로덕션 배포 사례가 없음

**알아둘 용어**

- **MoE (Mixture of Experts, 전문가 혼합)**: 각 토큰을 전체 파라미터 중 소수의 "전문가" 서브-네트워크에만 라우팅해, 모델 총 파라미터는 크게 유지하면서 연산량은 줄이는 아키텍처; DeepSeek, Mixtral, GPT-4(추정) 등 주요 LLM이 채택
- **all-to-all 통신**: 분산 컴퓨팅에서 모든 프로세스(GPU)가 다른 모든 프로세스와 데이터를 교환하는 집합적 통신 패턴; MoE 라우팅에서 토큰이 원격 전문가로 이동할 때 발생
- **LAR (Local Activation Rate, 국소 활성화율)**: 전체 전문가 선택 중 같은 GPU 내 전문가에게 라우팅된 비율; 1.0이면 모든 토큰이 네트워크 전송 없이 로컬에서 처리됨
- **전문가 병렬성 (Expert Parallelism)**: 서로 다른 전문가를 서로 다른 GPU에 분산 배치해 MoE를 다중 GPU로 스케일아웃하는 방법
- **인트라-노드 패브릭 (Intra-node fabric)**: 동일 물리 서버 내 GPU들을 연결하는 고속 링크(예: NVLink, NVSwitch); 크로스-노드 InfiniBand보다 훨씬 높은 대역폭을 제공
- **KV 헤드 (Key-Value heads)**: 어텐션 메커니즘에서 키(K)와 값(V) 프로젝션을 담당하는 헤드 그룹; GQA/MQA 모델에서는 쿼리 헤드보다 수가 적어 메모리를 절감
- **LongBench**: 긴 컨텍스트 이해와 다양한 추론 과제를 평가하는 다국어 벤치마크; 본 논문의 지연 시간 비교에 사용됨

**왜 주목할 만한가?**

MoE는 이미 프로덕션 LLM의 지배적 아키텍처가 되었고, 이를 여러 GPU에 분산 배치해 서빙하는 것이 표준이 되고 있다. 그러나 all-to-all 통신 비용은 클러스터 규모와 함께 선형적으로 증가해, 수십~수백 GPU 규모에서 심각한 병목이 된다. FoE는 하드웨어 업그레이드나 새로운 통신 라이브러리 없이, 아키텍처 설계 변경만으로 이 병목을 제거한다. 1.95배의 레이턴시 감소는 동일 서빙 비용에서 거의 두 배의 처리량을 의미하며, 실시간 추론 서비스에서는 즉각적인 사용자 경험 향상으로 이어진다. 스탠퍼드의 Philip Levis(네트워킹·시스템 분야 저명 연구자)와 Azalia Mirhoseini(MoE 공동 창안자)가 참여한 것도 신뢰도를 높인다.

---

## English Summary

**One-line summary**

Distributed inference of Mixture-of-Experts LLMs is bottlenecked by all-to-all communication that routes tokens to remote experts across GPUs—Federation of Experts (FoE), proposed by researchers at Stanford, redesigns the MoE layer into clusters tied to individual KV attention heads so that every token is always processed by a local expert, structurally guaranteeing a Local Activation Rate of 1.0 and achieving up to 1.95× lower end-to-end inference latency on LongBench with no quality loss.

**Core idea**

MoE models activate only a small subset of experts per token, but in a distributed setting those experts may reside on different GPUs, forcing all-to-all communication that sends token embeddings over the network. As the number of GPUs grows, the fraction of tokens that must travel across the network increases, making this communication the dominant inference bottleneck. FoE addresses this at the architectural level: it partitions the MoE experts into clusters equal in number to the KV attention heads, assigns each cluster exclusively to one GPU, and routes tokens only to experts within the local cluster. Post-attention residuals are then summed across clusters via a small all-reduce operation confined to the fast intra-node fabric. This design structurally locks the Local Activation Rate (LAR) at 1.0, eliminating all-to-all communication entirely on a single node and restricting it to intra-node links on multi-node deployments.

**What is new?**

- **Structural LAR guarantee**: Unlike standard MoE where LAR degrades as the cluster scales, FoE guarantees LAR = 1.0 by construction—all expert selections are resolved without network transfer
- **Cluster-KV head co-design**: MoE expert groups are coupled to attention KV heads one-to-one, unifying the communication patterns of attention and FFN layers into a coherent local-first design
- **Single-node all-to-all elimination**: On a single node, no all-to-all communication occurs at all, since every expert in a cluster sits on the same GPU
- **Multi-node communication localization**: Across nodes, any remaining all-to-all traffic is confined to high-bandwidth intra-node links (e.g., NVLink), avoiding slow cross-node InfiniBand communication
- **~10× communication volume reduction and up to 1.95× latency improvement**: Empirically demonstrated on LongBench with 1B and 7B models at comparable quality to standard MoE baselines

**How does it work?**

1. **Cluster partitioning**: The MoE layer is divided into K clusters, where K equals the number of KV attention heads. Each cluster owns 1/K of the total experts and all those experts are co-located on a single GPU.
2. **Local attention and routing**: Each cluster performs attention using its dedicated KV head, then routes tokens only to its local experts. No tokens cross GPU boundaries during this step.
3. **Residual aggregation**: After each cluster completes its attention and FFN computation, residuals are summed across clusters via an all-reduce. This all-reduce carries lightweight scalar-level data and remains within the intra-node fabric.
4. **Next-block input**: The aggregated residual feeds the routing logic for the next transformer block, and the pattern repeats across all layers.
5. **Uniform load balancing**: Because each cluster owns an equal share of experts and is tied to one KV head, token load is structurally balanced across GPUs without dynamic load balancing heuristics.

**Strengths**

- Eliminates the primary distributed MoE inference bottleneck through architecture, not runtime heuristics
- Quality preserved: zero-shot accuracy on 1B and 7B FoE models matches equivalently-sized standard MoE baselines
- Scales favorably: LAR remains at 1.0 regardless of how many GPUs are added, unlike standard MoE where LAR falls linearly
- Up to 1.95× latency reduction on LongBench—nearly double the throughput for the same hardware
- Structurally enforces uniform load distribution, removing the need for expert-load-balancing auxiliary losses

**Limitations**

- Validated at 1B and 7B scale; generalization to hundreds-of-billion-parameter frontier models is unconfirmed
- The cluster-KV head pairing assumes a specific relationship between attention head count and expert groups; behavior under multi-query attention (MQA) or grouped-query attention (GQA) variants is not fully analyzed
- Sensitivity to routing imbalance (tokens clustering to specific experts within a cluster) requires further study
- FoE is designed for inference; it is unclear how easy it is to retrain or fine-tune existing standard MoE checkpoints in the FoE layout
- No large-scale production deployment results yet; real-world network topology effects (congestion, variable bandwidth) are not assessed

**Terms to know**

- **MoE (Mixture of Experts)**: An architecture that routes each token to a small subset of "expert" sub-networks, keeping total parameters large while activating only a fraction per forward pass; adopted by DeepSeek, Mixtral, and other major LLMs
- **All-to-all communication**: A collective communication pattern where every process (GPU) exchanges data with every other process; the dominant bottleneck in distributed MoE routing when experts are spread across GPUs
- **LAR (Local Activation Rate)**: The fraction of expert selections resolved without cross-GPU data transfer; a LAR of 1.0 means all routing is handled locally, eliminating network latency entirely
- **Expert parallelism**: A distributed training/inference strategy that places different experts on different GPUs to scale MoE models across hardware
- **Intra-node fabric**: High-bandwidth interconnects within a single physical server (e.g., NVLink, NVSwitch), much faster than cross-node InfiniBand links; FoE exploits this hierarchy
- **KV heads**: The key and value projection heads in attention; in GQA/MQA architectures, fewer KV heads are used than query heads to save memory—FoE co-designs expert clusters around this structure
- **LongBench**: A multilingual long-context understanding benchmark used in this paper to measure end-to-end latency and generation quality

**Why it is worth watching**

MoE has become the dominant architecture for frontier LLMs, and distributed serving across tens to hundreds of GPUs is now standard practice for commercial deployments. The all-to-all communication tax grows proportionally with cluster size, making it an increasingly severe bottleneck as models scale. FoE removes this bottleneck through an architectural decision—no new hardware, no new communication libraries—and the 1.95× latency improvement translates directly to halved serving costs or doubled throughput on the same infrastructure. The involvement of Azalia Mirhoseini (a co-inventor of MoE) and Philip Levis (a prominent systems and networking researcher at Stanford) lends strong credibility to both the design and the analysis. If the approach generalizes to larger model scales, it could significantly reduce the infrastructure cost of serving the next generation of MoE LLMs.

**My take**

FoE가 제시하는 "통신 병목을 아키텍처 설계로 사전에 제거"하는 접근은 개념적으로 깔끔하고 실용적이다. LAR = 1.0을 구조적으로 보장한다는 아이디어는 런타임 스케줄링에 의존하는 기존 방법보다 훨씬 강력한 보장을 제공한다. 1B·7B 실험 결과는 품질 손실 없는 레이턴시 단축을 보여주지만, 실제 프론티어 모델(70B 이상)에서의 검증과 GQA/MQA와의 호환성이 이 접근의 범용성을 결정하는 핵심 미결 과제다.

FoE is architecturally elegant: it solves the all-to-all communication problem by making remote routing structurally impossible rather than trying to minimize it at runtime. The LAR = 1.0 guarantee is a stronger promise than any dynamic scheduling heuristic can offer. The 1.95× speedup is practically meaningful, and the quality parity at 1B and 7B is encouraging. The main open question is scale: frontier MoE models are dramatically larger and often use non-standard attention configurations, and whether the cluster-KV head co-design holds up there will determine how broadly deployable FoE becomes.
