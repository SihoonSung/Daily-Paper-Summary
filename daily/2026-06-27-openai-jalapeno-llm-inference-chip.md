---
title: "OpenAI and Broadcom Unveil Jalapeño: A Custom LLM-Optimized Intelligence Processor"
date: 2026-06-27
topic: semiconductor
tags: [semiconductor, AI-inference, custom-chip, ASIC, LLM, hardware, OpenAI, Broadcom, HBM, inference-acceleration]
source: https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
---

# OpenAI and Broadcom Unveil Jalapeño: A Custom LLM-Optimized Intelligence Processor

* Date: 2026-06-27
* Source: https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
* Topic: Semiconductor / AI Inference Hardware
* Why it matters: OpenAI는 범용 GPU에 대한 의존에서 벗어나 처음으로 자체 설계 AI 추론 전용 칩 Jalapeño를 Broadcom과 공동으로 발표했다. 이 칩은 LLM 추론의 구체적인 연산 패턴에 맞게 메모리, 연산, 네트워킹을 처음부터 최적화하여 현재 GPU 대비 약 50% 낮은 추론 비용을 목표로 하며, AI 컴퓨팅 인프라의 수직 통합 경쟁을 본격화한다.

---

## Korean Summary

**한줄 요약**

OpenAI와 Broadcom이 2026년 6월 24일, LLM 추론 전용으로 설계된 맞춤형 ASIC(Application-Specific Integrated Circuit) Jalapeño를 공개했다. 레티클 크기에 달하는 대형 다이, 8개의 HBM 스택, Broadcom의 대규모 네트워킹 기술을 결합하여 현재 GPU 기반 클러스터 대비 약 50% 저렴한 토큰 당 추론 비용을 목표로 하며, OpenAI 자체 모델을 활용한 설계 가속으로 단 9개월 만에 테이프아웃(tape-out)에 성공했다.

**핵심 아이디어**

기존 AI 추론 클러스터는 엔비디아 GPU처럼 학습과 추론 모두에 사용할 수 있는 범용 가속기로 운영된다. 범용 GPU는 유연하지만, LLM 추론에는 필요하지 않은 연산 기능에도 전력과 면적을 소비하며, 특히 메모리 대역폭·데이터 이동·네트워킹 측면에서 LLM 추론의 실제 병목을 직접 해결하지 못한다. Jalapeño는 이 문제를 ASIC 방식으로 해결한다. LLM 추론의 핵심인 대규모 행렬 곱(matrix multiplication)에 최적화된 시스톨릭 어레이(systolic array), HBM 스택을 통한 고대역폭 메모리, Broadcom의 SerDes 및 Tomahawk 6 네트워킹으로 수천 개의 칩이 하나의 통합 패브릭으로 동작하도록 설계되어 이론적 피크 성능에 훨씬 가까운 실제 활용률을 달성한다.

**무엇이 새로운가?**

- **OpenAI 최초의 자체 설계 실리콘**: 구글(TPU), 아마존(Trainium), 마이크로소프트(Maia) 등 주요 AI 기업들이 이미 자체 칩을 보유한 가운데, OpenAI가 마지막으로 수직 통합에 합류하며 Broadcom과 공동 개발한 첫 번째 추론 전용 프로세서
- **추론 특화 아키텍처**: 학습 재활용 칩이나 범용 AI 프로세서가 아닌, LLM 추론 커널·메모리 이동 패턴·네트워킹 패턴에 맞게 처음부터 설계된 목적형 ASIC
- **레티클 크기 대형 다이**: 다이 면적이 EUV 리소그래피 장비의 레티클 한계(약 858mm²)에 근접한 약 840mm²로, 최대 연산 밀도를 추구
- **AI 보조 칩 설계**: OpenAI의 자체 모델을 설계·최적화 과정에 직접 활용하여, 초기 설계부터 테이프아웃까지 단 9개월이라는 이례적으로 짧은 개발 주기 달성
- **Broadcom 네트워킹 통합**: Broadcom의 SerDes 기술과 Tomahawk 6(1.6 Tbps 처리량)를 통해 수천 개의 Jalapeño 칩이 단일 논리적 추론 패브릭으로 동작하는 대규모 확장성 제공

**어떻게 작동하는가?**

1. **시스톨릭 어레이 행렬 연산**: LLM 추론에서 가장 많은 연산을 차지하는 행렬 곱(주의(attention) 연산, FFN 레이어 등)을 시스톨릭 어레이—처리 요소들이 리드미컬하게 데이터를 전달하는 격자 구조—로 처리한다. 이 구조는 재사용 패턴이 반복적인 밀집 행렬 곱에 특히 적합하다.
2. **8스택 HBM 고대역폭 메모리**: 8개의 HBM 스택이 컴퓨트 다이 주위에 배치되어 메모리 대역폭을 극대화하고 KV 캐시 및 모델 가중치 로딩의 병목을 완화한다. 패키지 내 HBM 통합으로 외부 DRAM 대비 레이턴시가 크게 감소한다.
3. **데이터 이동 최소화 설계**: 아키텍처 전반이 컴퓨트, 메모리, 네트워킹 자원 간 균형을 유지하며 데이터 이동을 최소화하도록 공동 설계되어 이론적 피크 성능에 훨씬 가까운 실제 활용률을 달성한다.
4. **Broadcom SerDes + Tomahawk 6 스케일아웃**: Broadcom의 고속 직렬화/역직렬화(SerDes) 기술과 Tomahawk 6 네트워킹 칩(1.6 Tbps)을 통해 수천 개의 Jalapeño 칩이 낮은 레이턴시로 연결되어 초대형 모델의 분산 추론을 가능하게 한다.
5. **소프트웨어-하드웨어 공동 설계**: OpenAI의 연구팀이 실제 프로덕션 LLM 추론 커널과 서빙 패턴을 분석하여 하드웨어 설계에 반영하고, Broadcom의 실리콘 구현 전문성과 결합했다. OpenAI 자체 모델이 설계 탐색 및 최적화 일부를 자동화했다.
6. **엔지니어링 샘플 검증**: GPT-5.3-Codex-Spark를 포함한 ML 워크로드가 목표 주파수 및 전력에서 실험실 내 엔지니어링 샘플 위에서 실행 중이며, 2026년 말 초기 양산 배치를 목표로 한다.

**강점**

- LLM 추론에 특화된 목적형 ASIC는 범용 GPU 대비 동일 전력에서 더 높은 처리량 달성 가능
- HBM 스택 내장으로 메모리 대역폭 제한을 완화하고 대형 모델 추론 시 KV 캐시 병목 감소
- AI 보조 설계로 개발 속도가 대폭 단축되어 미래 칩 설계 프로세스의 새로운 선례 제시
- Broadcom의 네트워킹 기술 통합으로 대규모 분산 추론 스택 전체의 최적화 가능
- OpenAI의 엔비디아 의존도 감소로 인한 구조적 비용 절감 가능성

**한계**

- 상세 사양(TFLOPS, 전력, 확정된 공정 노드, 메모리 용량)은 공식적으로 미공개 — 일부 스펙은 웨이퍼 이미지 분석에서 추정
- ASIC는 GPU 대비 유연성이 낮아 새로운 모델 아키텍처 등장 시 적응이 어려울 수 있음
- 현재는 추론 전용이며 학습에는 사용 불가 — 학습용 NVIDIA GPU 의존도는 유지됨
- 초기 배치 규모와 실제 프로덕션 성능은 2026년 말까지 검증 필요
- 자체 실리콘 운영·소프트웨어 스택 유지에 따른 엔지니어링 부담 증가

**알아둘 용어**

- **ASIC(Application-Specific Integrated Circuit, 주문형 집적회로)**: 특정 작업에 최적화된 맞춤형 반도체. GPU보다 특정 워크로드에서 전력 효율이 높지만 유연성이 낮다.
- **HBM(High Bandwidth Memory, 고대역폭 메모리)**: 3D 스택 구조의 고속 DRAM. GDDR6 등 기존 메모리 대비 대역폭이 수배~수십배 높아 AI 추론의 메모리 병목을 완화한다.
- **시스톨릭 어레이(Systolic Array)**: 처리 요소들이 규칙적인 리듬으로 데이터를 인접 셀에 전달하는 격자형 컴퓨팅 구조. 밀집 행렬 곱에 특히 효율적이며 구글 TPU에도 채택된 설계다.
- **레티클 크기 다이(Reticle-Limited Die)**: EUV 리소그래피 장비가 한 번의 노광으로 처리할 수 있는 최대 면적(약 858mm²)에 근접한 대형 반도체 다이. 단일 칩으로 최대 연산 집적도를 추구한다.
- **SerDes(Serializer/Deserializer, 직렬화/역직렬화)**: 고속 직렬 데이터를 병렬로 변환하거나 그 반대를 수행하는 인터페이스 기술. 칩 간 고속 통신의 핵심 요소.
- **Tomahawk 6**: Broadcom의 최신 이더넷 스위치 칩으로 1.6 Tbps 처리량을 지원. AI 클러스터 내 칩 간 대규모 데이터 교환을 가능하게 한다.
- **테이프아웃(Tape-out)**: 반도체 설계의 최종 단계로, 완성된 회로 레이아웃을 제조 공장(파운드리)에 제출하는 시점. 이후 실제 웨이퍼 제작이 시작된다.

**왜 주목할 만한가?**

AI 추론 비용은 생성형 AI 서비스의 수익성을 결정하는 핵심 변수이며, 이 비용의 대부분이 GPU 하드웨어와 전력 소비에서 발생한다. 구글(TPU), 아마존(Trainium), 마이크로소프트(Maia)에 이어 OpenAI가 자체 추론 실리콘을 갖추게 되면, AI 컴퓨팅 시장의 수직 통합이 주요 플레이어 전반으로 확산됨을 의미한다. 더 주목할 점은 설계 과정에 AI를 적극 활용하여 9개월이라는 이례적으로 짧은 개발 주기를 달성했다는 것으로, AI가 자신의 다음 세대 하드웨어를 설계하는 재귀적 가속의 첫 번째 사례가 되었다.

---

## English Summary

**One-line summary**

On June 24, 2026, OpenAI and Broadcom unveiled Jalapeño, OpenAI's first custom AI inference chip — a reticle-sized ASIC co-designed from scratch for LLM inference, featuring 8 HBM stacks, a systolic array architecture, and Broadcom-scale networking. Engineering samples are already running production LLM workloads, with initial deployment targeted for late 2026 at roughly 50% lower token cost than current GPU-based clusters.

**Core idea**

Large language model inference has a fundamentally different computational profile from training: it is memory-bandwidth-bound rather than compute-bound, dominated by sequential token generation rather than parallel batch processing, and critically dependent on the efficiency of data movement between compute and memory. General-purpose GPUs — designed to handle both training and inference and a wide variety of workloads — carry architectural overhead that does not benefit LLM inference and cannot be optimized away through software alone. Jalapeño is an ASIC purpose-built around the specific kernels, memory access patterns, and networking requirements of LLM inference, with the goal of achieving realized utilization much closer to theoretical peak performance and dramatically lower cost per output token.

**What is new?**

- **OpenAI's first custom silicon**: OpenAI is the last major AI hyperscaler to vertically integrate into silicon (joining Google's TPU, Amazon's Trainium, and Microsoft's Maia), marking a structural shift in how frontier AI inference infrastructure is built
- **Inference-first ASIC design**: A purpose-built inference processor designed around specific LLM inference kernels, memory access patterns, and serving requirements — not a repurposed training accelerator or general-purpose AI chip
- **Reticle-limited die**: An ~840mm² ASIC approaching the maximum die size achievable with EUV lithography (~858mm²), maximizing on-chip compute density in a single package
- **AI-assisted chip design**: OpenAI's own models were used to accelerate parts of the chip design and optimization process, enabling an unusually fast nine-month cycle from initial design to tape-out
- **Integrated Broadcom scale-out networking**: Broadcom's SerDes technology and Tomahawk 6 networking (1.6 Tbps) are tightly integrated into the inference stack, enabling thousands of Jalapeño ASICs to operate as a unified logical fabric for distributed LLM inference

**How does it work?**

1. **Systolic array for matrix multiplication**: The core compute engine is a systolic array — a grid of processing elements that pass data between cells in rhythmic lockstep — which is well-suited to the dense matrix multiplications (attention layers, feed-forward layers) that dominate LLM inference compute.
2. **8-stack HBM for high-bandwidth memory**: Eight HBM stacks are arranged tightly around the compute die on the package, providing high memory bandwidth to keep the compute elements fed during token generation and to reduce KV cache and weight-loading bottlenecks.
3. **Data movement minimization**: The architecture co-designs compute, memory, and networking resources to minimize unnecessary data movement between subsystems, pushing realized utilization significantly closer to theoretical peak performance than a general-purpose GPU running the same workload.
4. **Broadcom SerDes + Tomahawk 6 scale-out**: Broadcom's high-speed serializer/deserializer (SerDes) interfaces and Tomahawk 6 switching silicon (1.6 Tbps throughput) enable thousands of Jalapeño chips to interconnect with low latency, supporting distributed inference of models too large for a single chip.
5. **Software-hardware co-design**: OpenAI's researchers analyzed production LLM inference kernels and serving patterns to inform hardware architectural decisions; Broadcom contributed silicon implementation expertise. OpenAI's models automated parts of the design space exploration and optimization.
6. **Engineering sample validation**: Engineering samples are already running ML workloads — including GPT-5.3-Codex-Spark — at production target frequency and power in the lab. Early results show better performance per watt than current state-of-the-art, with mass deployment targeted for late 2026.

**Strengths**

- Purpose-built inference ASICs can substantially outperform general-purpose GPUs in performance per watt for LLM-specific workloads
- HBM integration directly addresses the memory-bandwidth bottleneck that limits LLM inference throughput on conventional hardware
- AI-assisted chip design sets a precedent for significantly compressed hardware development timelines
- Integration of Broadcom networking technology at the chip level allows the full inference stack — not just the accelerator — to be co-optimized
- Structural cost reduction of ~50% per inference token, if achieved at scale, would materially change the economics of deploying frontier AI

**Limitations**

- Detailed specifications (TFLOPS, power draw, confirmed process node, exact memory capacity and bandwidth) were not officially disclosed; some figures are inferred from die imagery analysis
- ASICs are less flexible than GPUs — adapting to significantly new model architectures (e.g., new attention variants, different sparsity patterns) may require new chip generations
- Jalapeño is inference-only; OpenAI remains dependent on NVIDIA hardware for model training
- Actual production-scale performance and cost claims require validation against real deployment data, expected in late 2026 or 2027
- Maintaining a custom silicon stack introduces significant ongoing engineering and software complexity

**Terms to know**

- **ASIC (Application-Specific Integrated Circuit)**: A chip custom-designed for one specific task rather than general use. Less flexible than a GPU but potentially far more efficient for the target workload.
- **HBM (High Bandwidth Memory)**: 3D-stacked DRAM that sits directly on or adjacent to the chip package, offering memory bandwidth several times higher than conventional GDDR memory. Critical for memory-bandwidth-bound workloads like LLM inference.
- **Systolic array**: A grid of processing elements where data flows between neighboring cells in a regular rhythmic pattern. Highly efficient for dense matrix multiplication, which makes up the majority of LLM inference compute; also used in Google's TPUs.
- **Reticle-limited die**: A semiconductor die whose area approaches the maximum exposure field of an EUV lithography system (~858mm²). Maximizes transistor count and on-chip bandwidth in a single piece of silicon.
- **KV cache**: The key-value cache used during autoregressive LLM token generation to avoid recomputing attention over previously generated tokens. Its size and access speed are major inference bottlenecks.
- **SerDes (Serializer/Deserializer)**: High-speed interface circuitry that converts parallel data to serial form for transmission across chips or boards and back. The foundation of inter-chip communication in AI compute clusters.
- **Tape-out**: The final step in semiconductor design where the completed circuit layout is submitted to the fab for manufacturing. "Nine months to tape-out" means nine months from design start to manufacturing submission.

**Why it is worth watching**

The cost of inference — not training — is now the dominant operating expense for deployed AI products. Every major cloud provider that builds frontier models has moved toward custom silicon to reduce this cost and break dependence on NVIDIA GPUs: Google with TPUs since 2016, Amazon with Trainium, Microsoft with Maia. OpenAI's Jalapeño announcement signals that the era of frontier AI companies relying entirely on merchant silicon is over. The nine-month development cycle enabled by AI-assisted design is equally significant: if AI tools can compress chip design timelines this dramatically, the cadence of hardware innovation for AI could itself accelerate. Whether Jalapeño's performance claims hold at production scale will be the real test, but the architectural bet — that LLM inference is a distinct and stable enough workload to justify a purpose-built ASIC — appears well-founded.

**My take**

Jalapeño가 OpenAI에 특별한 이유는 단순히 첫 번째 자체 칩이기 때문만이 아니다. 9개월이라는 개발 기간, AI 보조 설계의 적극적 활용, 그리고 추론 특화라는 단일 목적에 집중한 설계 철학이 결합되어 있다는 점에서, 이것은 AI 기업이 자신의 하드웨어 운명을 스스로 통제하기 시작한 전환점으로 볼 수 있다. 다만 공식 성능 수치가 아직 없고 ASIC의 구조적 유연성 부족이라는 리스크는 실제 배포 결과가 나올 때까지 유보적으로 봐야 한다.

Jalapeño matters beyond being OpenAI's "first chip" because it combines three things at once: a credible architectural thesis (LLM inference is stable enough to deserve a purpose-built ASIC), a compressed development timeline that AI tools made possible, and a clear economic motivation (reducing per-token cost to sustain profitability at scale). The lack of official performance numbers is a reason for appropriate skepticism, and ASIC inflexibility remains a real architectural risk as model designs continue to evolve. But the directional bet — that purpose-built inference silicon will be necessary for any frontier AI company at scale — looks correct.
