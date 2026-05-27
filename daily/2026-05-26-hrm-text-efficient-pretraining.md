---
title: "HRM-Text: Efficient Pretraining Beyond Scaling"
date: 2026-05-26
topic: AI
tags: [AI, pretraining, architecture, recurrent-networks, efficient-training, LLM, non-transformer, hierarchical]
source: https://arxiv.org/abs/2605.20613
---

# HRM-Text: Efficient Pretraining Beyond Scaling

* Date: 2026-05-26
* Source: https://arxiv.org/abs/2605.20613
* Topic: AI / Efficient Pretraining
* Why it matters: The current LLM pretraining paradigm requires trillions of tokens and millions of dollars of compute, creating an enormous barrier for most researchers. HRM-Text demonstrates that a 1B-parameter non-transformer model, trained on only 40 billion tokens for roughly $1,500, can match the benchmark performance of 2–7B parameter models trained at hundreds of times the cost, by replacing the transformer with a brain-inspired hierarchical recurrent architecture and switching from raw-text pretraining to a task-completion objective.

## Korean Summary

**한줄 요약**

HRM-Text는 트랜스포머를 대신해 뇌의 전두두정엽(frontoparietal) 루프에서 영감을 얻은 계층적 순환 모델(HRM)을 사용하고, 원시 텍스트 대신 지시-응답 쌍으로만 학습함으로써, 1B 파라미터 모델을 약 170만 원($1,500)에 처음부터 훈련해 2~7B 규모 오픈 모델과 경쟁하는 성능을 달성한 효율적 사전 학습 프레임워크다.

**핵심 아이디어**

기존 LLM 사전 학습은 수조 개의 인터넷 텍스트 토큰과 막대한 컴퓨팅 비용에 의존하는 구조적 한계가 있다. HRM-Text는 두 가지를 동시에 바꾼다. 첫째, 트랜스포머 대신 계층적 순환 모델(HRM)을 사용해 '느린 전략 모듈(H)'과 '빠른 실행 모듈(L)'이 서로 다른 시간 척도에서 상호작용하도록 설계한다—이는 뇌의 서로 다른 주파수로 동기화되는 두 영역과 유사하다. 둘째, 원시 텍스트 사전 학습을 포기하고, 지시-응답 쌍을 이용한 태스크 완성(task-completion) 목표 함수와 PrefixLM 마스킹으로만 학습한다. 이 두 가지 변화의 조합이 100배 이상의 학습 효율성을 가능하게 한다.

**무엇이 새로운가?**

- **비트랜스포머 사전 학습 모델**: H(전략)·L(실행) 두 모듈이 상호작용하는 계층적 순환 구조를 설계해 트랜스포머 없이 경쟁력 있는 언어 모델을 처음부터 학습
- **태스크 완성 목표**: 원시 인터넷 텍스트 대신 지시-응답 쌍만으로 학습. 노이즈 많은 웹 데이터 없이 깨끗한 학습 신호만 사용
- **MagicNorm**: 깊은 순환 구조에서 발생하는 학습 불안정성(기울기 소실/폭발)을 해결하기 위해 고안한 정규화 기법
- **Warmup deep credit assignment**: 깊은 시간 순환에서 오류 신호를 효과적으로 전파하기 위한 학습률 워밍업 전략
- **극단적 효율성**: 표준 기준선 대비 130~600배 적은 연산량, 150~900배 적은 학습 토큰으로 2~7B 모델 수준 달성

**어떻게 작동하는가?**

1. **HRM 구조**: H 모듈은 긴 시간 척도에서 전략적·맥락적 표현을 유지하고, L 모듈은 짧은 시간 척도에서 토큰 수준의 세부 처리를 담당. 두 모듈이 서로 정보를 교환하며 계층적 처리
2. **PrefixLM 마스킹**: 지시(prefix) 부분에는 양방향 어텐션(bidirectional)을, 응답(response) 부분에는 단방향 인과 어텐션(causal)을 적용해 입력 맥락을 완전히 활용하면서 응답은 자기회귀적으로 생성
3. **학습 안정화**: MagicNorm을 통해 순환 레이어 간 활성값 크기를 제어하고, warmup deep credit assignment로 긴 순환 경로의 기울기 전파를 보완
4. **데이터 전략**: 수조 토큰의 원시 웹 크롤을 사용하지 않고, 정제된 지시-응답 쌍 40B 토큰만으로 학습. FlashAttention 3 커널과 FSDP2 분산 학습으로 실제 훈련 진행
5. **추론**: 학습된 HRM-Text는 표준 자기회귀 방식으로 텍스트를 생성하며, 기존 추론 런타임과 호환 가능

**강점**

- 1B 모델 학습 비용이 약 $1,500(16× H100, 46시간)으로 개인 연구자도 처음부터 언어 모델을 사전 학습 가능
- GSM8k 84.7%, MATH 56.5%, MMLU 60.7%, ARC-C 81.9% 등 주요 벤치마크에서 2~7B 오픈 모델과 경쟁하는 실질적 수치
- 코드, 모델 가중치(HuggingFace)가 오픈 소스로 공개되어 재현·확장 가능
- 트랜스포머의 이차 어텐션 복잡도 의존성에서 벗어날 가능성 제시
- 노이즈 있는 원시 텍스트 정제 파이프라인이 불필요해 데이터 준비 비용 절감

**한계**

- 아직 소규모(1B) 모델에서만 검증되었으며, 수십억~수백억 파라미터 규모에서도 동일한 효율성이 유지되는지 미확인
- 태스크 완성 목표로만 학습해 훈련 데이터 밖 광범위한 일반 지식 커버리지가 표준 사전 학습보다 제한적일 가능성
- HRM 구조의 깊은 순환 계산이 트랜스포머 대비 실제 추론 레이턴시 측면에서 얼마나 경쟁력이 있는지 충분히 평가되지 않음
- 기존 트랜스포머 기반 인프라(서빙, 파인튜닝 도구)와의 호환성이 즉각적이지 않을 수 있음
- HellaSwag 63.4%는 비슷한 크기의 트랜스포머 모델과 비교해 다소 낮으며, 일반 언어 이해 벤치마크에서의 성능 격차 분석이 필요

**알아둘 용어**

- **계층적 순환 모델 (Hierarchical Recurrent Model, HRM)**: 서로 다른 추상 수준과 시간 척도에서 동작하는 복수의 순환 모듈을 계층적으로 결합한 신경망 구조
- **PrefixLM**: 입력의 접두사(prefix) 부분은 양방향 어텐션으로 처리하고 생성 부분은 인과 어텐션으로 처리하는 언어 모델링 방식
- **태스크 완성 목표 (Task-Completion Objective)**: 원시 텍스트 예측 대신 특정 지시에 대한 올바른 응답을 생성하는 것을 학습 목표로 삼는 방식
- **MagicNorm**: 깊은 순환 네트워크에서 중간 레이어의 활성값 스케일을 안정화하기 위해 저자들이 고안한 정규화 기법
- **Warmup deep credit assignment**: 긴 순환 경로를 통해 오류 신호가 효과적으로 전파되도록 학습률을 단계적으로 높이는 전략
- **전두두정엽 루프 (Frontoparietal Loop)**: 뇌에서 전두엽과 두정엽이 서로 다른 시간 척도로 상호작용하는 신경 회로로, 전략적 계획과 세부 실행을 통합하는 것으로 알려짐
- **FSDP2 (Fully Sharded Data Parallel 2)**: PyTorch의 분산 학습 기법으로, 모델 파라미터를 여러 GPU에 분산 저장해 메모리 효율을 높이는 방식

**왜 주목할 만한가?**

LLM 사전 학습의 진입 장벽은 지난 수년간 계속 높아져, 사실상 대형 기술기업과 일부 대형 연구소만이 기반 모델을 처음부터 학습할 수 있는 상황이 되었다. HRM-Text는 이 전제에 직접적으로 도전한다: 트랜스포머 스케일링 법칙이 아닌 아키텍처와 학습 목표의 공동 설계를 통해, 개인 연구자 수준의 예산으로 2~7B 오픈 모델과 경쟁하는 기반 모델을 처음부터 학습할 수 있음을 실제로 보여준다. 이는 비트랜스포머 아키텍처의 실용성에 대한 강력한 증거이자, 사전 학습 연구를 다시 넓은 연구 공동체에 열어줄 수 있는 가능성을 가진다.

---

## English Summary

**One-line summary**

HRM-Text is a 1B-parameter language model that replaces the transformer with a brain-inspired Hierarchical Recurrent Model (HRM) and trains exclusively on instruction-response pairs, achieving competitive performance with 2–7B open models using 130–600× less compute and 150–900× less data, at a training cost of roughly $1,500.

**Core idea**

Standard LLM pretraining demands trillions of tokens and millions of dollars of compute — a barrier that concentrates foundational model research in a small number of institutions. HRM-Text challenges this by simultaneously changing two things: the architecture and the training objective. Instead of a transformer, it uses an HRM that splits computation into a slow H module (strategic, long-range context) and a fast L module (execution, token-level detail), inspired by the multi-timescale organization of the brain's frontoparietal loop. Instead of next-token prediction on raw web text, it trains exclusively on curated instruction-response pairs using a task-completion objective with PrefixLM masking. The combination achieves dramatic efficiency gains without sacrificing benchmark coverage.

**What is new?**

- **Non-transformer foundation model**: A hierarchical recurrent architecture with interacting slow (H) and fast (L) modules achieves competitive language model pretraining entirely without transformers
- **Task-completion pretraining**: Replaces noisy raw web-text prediction with a clean instruction-response objective, eliminating the need for trillion-token internet corpora
- **MagicNorm**: A normalization technique designed to stabilize training in deep recurrent networks, preventing gradient explosion and vanishing over long recurrent paths
- **Warmup deep credit assignment**: A training schedule that gradually increases learning rate to improve gradient flow through long temporal dependencies in the recurrent structure
- **Accessible training cost**: A 1B model trains from scratch in ~46 hours on 16 H100 GPUs for approximately $1,500, with a 0.6B variant achievable for ~$800

**How does it work?**

1. **HRM structure**: The H module operates at a coarser timescale, maintaining strategic, long-range representations. The L module operates at the token level, handling local execution detail. The two modules exchange information hierarchically at each step
2. **PrefixLM masking**: The prompt (prefix) region uses bidirectional attention to fully encode context; the response region uses causal attention for autoregressive generation. Sequences are packed using PrefixLM sequence packing for training efficiency
3. **Training stabilization**: MagicNorm controls activation magnitudes across recurrent layers; warmup deep credit assignment schedules gradient flow through the deep recurrence
4. **Data strategy**: Training uses only 40B unique tokens of curated instruction-response pairs — no raw web crawl, no deduplication pipeline over trillions of documents. FlashAttention 3 kernels and PyTorch FSDP2 enable efficient distributed training
5. **Inference**: The trained model generates text autoregressively in standard fashion; the HRM architecture is compatible with existing inference frameworks

**Strengths**

- Concrete $1,500 training cost for a competitive 1B model makes foundational LLM research accessible to individual researchers and small labs
- Strong benchmark numbers: GSM8k 84.7%, MATH 56.5%, MMLU 60.7%, ARC-C 81.9%, DROP 82.2%, competitive with models 2–7× larger
- Fully open source: code and model weights (HuggingFace) are publicly available for reproduction and extension
- Avoids the trillion-token raw-text data pipeline entirely, reducing data preparation costs alongside compute costs
- Provides a concrete empirical proof point that non-transformer architectures can serve as viable pretraining foundations

**Limitations**

- Only validated at 1B scale; whether the efficiency advantage holds at 10B–100B parameters is unknown
- Training exclusively on instruction-response pairs may limit breadth of general world knowledge compared to web-scale pretraining
- HellaSwag (63.4%) is notably lower than transformer models of similar size, suggesting potential gaps in commonsense language understanding
- Recurrent inference has different latency and batching characteristics than attention-based models; production serving implications are not fully characterized
- Compatibility with the existing transformer-centric fine-tuning and serving ecosystem (LoRA, vLLM, etc.) requires additional engineering

**Terms to know**

- **Hierarchical Recurrent Model (HRM)**: A neural architecture combining multiple recurrent modules at different levels of abstraction and timescales, allowing slow strategic processing and fast execution processing to coexist
- **PrefixLM**: A language modeling variant that applies bidirectional attention over an input prefix and causal attention for the output, allowing full context awareness during generation conditioning
- **Task-completion objective**: Training a language model to complete structured instruction-response pairs rather than predicting the next token in unstructured raw text
- **MagicNorm**: A normalization method introduced in this paper to stabilize activation magnitudes in deeply recurrent networks
- **Warmup deep credit assignment**: A training schedule that ramps up learning rate to progressively strengthen gradient signals propagating through long recurrent temporal paths
- **Frontoparietal loop**: A brain circuit connecting the frontal and parietal cortex, believed to integrate strategic planning (slow) with sensorimotor execution (fast) at different oscillation frequencies — the biological analogy for HRM's two-module design
- **FSDP2 (Fully Sharded Data Parallel 2)**: A PyTorch distributed training strategy that shards model parameters across GPUs to reduce per-device memory usage, enabling training of large models on commodity hardware

**Why it is worth watching**

The cost and compute barrier to foundational LLM research has grown large enough that most academic groups and small organizations cannot participate. HRM-Text is a direct, empirical challenge to this situation: by co-designing a non-transformer architecture and a cleaner training objective, it shows that competitive language model pretraining is achievable at a cost that individual researchers can afford. Whether or not HRM ultimately scales to match the largest transformers, this result validates that the transformer-plus-trillion-tokens paradigm is not the only viable path, and it reopens foundational pretraining as a research problem accessible to the broader community.

**My take**

HRM-Text의 핵심 기여는 단순한 아키텍처 교체가 아니라, 아키텍처와 학습 목표를 함께 재설계함으로써 사전 학습의 근본적인 효율성 장벽을 낮춘 데 있다. 결과 수치가 설득력 있고 코드가 공개되어 있어 재현 및 검증이 가능하다. 다만 1B 이상의 스케일 검증과 범용 언어 이해 벤치마크에서의 격차는 향후 과제로 남아 있으며, 트랜스포머 기반 생태계와의 통합 경로도 명확하지 않다.

HRM-Text makes a compelling empirical argument that the compute-intensive transformer pretraining paradigm is not a hard requirement for building capable language models. The numbers are credible, the code is open, and the cost claim ($1,500) is concrete enough to verify. The key open question is whether the efficiency advantage persists at larger scale — if it does, this represents a genuine architectural shift worth following closely; if it does not, it still stands as a useful proof of concept for sample-efficient pretraining research.
