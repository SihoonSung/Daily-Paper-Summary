---
title: "Long Context Pre-Training with Lighthouse Attention"
date: 2026-05-17
topic: AI
tags: [AI, LLM, attention, long-context, pre-training, efficiency, hierarchical-attention, Nous-Research]
source: https://arxiv.org/abs/2605.06554
---

# Long Context Pre-Training with Lighthouse Attention

* Date: 2026-05-17
* Source: https://arxiv.org/abs/2605.06554
* Topic: AI / Efficient Training / Attention Mechanisms
* Why it matters: Training causal transformers at very long context lengths (98K–512K tokens) is dominated by the quadratic cost of standard attention; Lighthouse Attention cuts the forward+backward pass to 1/17 the cost at 512K context on a single B200 GPU, without a custom sparse kernel, and the resulting model matches or exceeds the quality of a fully dense-attention baseline after a brief recovery phase.

## Korean Summary

**한줄 요약**

Nous Research의 Lighthouse Attention은 훈련 전용 계층적(hierarchical) 어텐션 알고리즘으로, Q·K·V를 다단계 피라미드(pyramid)로 압축한 뒤 중요도 높은 토큰만 선별하여 표준 SDPA를 실행함으로써 98K 컨텍스트에서 1.4–1.7× 훈련 속도 향상을 달성한다. 훈련이 끝나면 잠깐의 전체 어텐션 복원(recovery) 단계를 거쳐 표준 풀 어텐션 모델을 생성하므로, 추론 환경에는 아무런 변경이 필요 없다.

**핵심 아이디어**

긴 컨텍스트 LLM 사전훈련의 가장 큰 병목은 표준 스케일드-닷-프로덕트 어텐션(SDPA)의 O(N²) 연산·메모리 복잡도다. Lighthouse Attention은 이를 "훈련 중에만" 교체하는 전략을 취한다. Q·K·V 행렬을 동시에 평균 풀링(average pooling)하여 L단계 피라미드를 만들고, 각 피라미드 항목의 중요도를 ℓ₂ 노름으로 채점한 뒤, 상위 k개 항목만 선택하여 SDPA를 수행한다. 이 선택 과정이 기울기 없이(gradient-free) 동작하므로 역전파가 복잡해지지 않는다. 훈련 대부분을 이 방식으로 진행한 뒤, 마지막 짧은 단계에서 전체 SDPA로 복원하면 표준 풀 어텐션 체크포인트를 얻는다.

**무엇이 새로운가?**

- 훈련 전용(training-only) 계층적 어텐션: 추론 코드·커널 변경 없이 사전훈련 비용만 줄임
- Q·K·V를 동시에 대칭 압축(symmetrical compression)하여 인과성(causality)을 보존하면서 병렬성을 극대화
- 파라미터 없는 ℓ₂ 노름 스코어링과 계층 간 max-pooling 점수 전파로 별도 학습 없이 중요 토큰 선별
- 커스텀 희소 어텐션 커널이나 직통 추정기(straight-through estimator) 없이 구현
- 512K 컨텍스트에서 단일 B200 GPU 기준 순방향 21×, 순방향+역방향 17.3× 속도 향상

**어떻게 작동하는가?**

1. **피라미드 구성**: Q, K, V 각각을 평균 풀링으로 L단계 피라미드로 압축한다. 풀링 인수 p일 때 ℓ단계는 N/pˡ개 토큰을 가진다. 가장 조악한(coarsest) 단계는 모든 기반 위치를 반드시 포함한다.
2. **채점(Scoring)**: 각 피라미드 항목에 대해 헤드별 ℓ₂ 노름으로 쿼리 점수·키 점수 두 스칼라를 계산한다. 상위 단계는 하위 단계 점수의 max-pooling으로 점수를 상속받아, 조악한 스팬이 그 안의 가장 중요한 토큰 점수를 반영한다.
3. **상위 k 선택**: 융합된(fused) 청크 비토닉(chunked-bitonic) 상위-k 커널이 모든 피라미드 단계를 통틀어 k개 항목을 선택한다.
4. **희소 어텐션 연산**: 선택된 k개 토큰에 대해서만 표준 SDPA를 실행한다. 이 과정이 전체 N²보다 훨씬 작다.
5. **2단계 훈련**: 전체 훈련의 대부분(약 10,000 스텝)은 Lighthouse Attention으로 진행하고, 마지막 짧은 단계(약 6,000 스텝)에서 전체 SDPA로 교체해 체크포인트를 표준 풀 어텐션 모델로 복원한다.

**강점**

- **추론 변경 불필요**: 훈련이 끝나면 완전한 표준 풀 어텐션 모델이 생성되므로 배포 인프라를 바꿀 필요가 없음
- **커스텀 커널 불필요**: 기존 PyTorch SDPA 위에서 동작하므로 하드웨어별 커스텀 구현 부담이 없음
- **안정적인 역전파**: 기울기 없는 선택 덕분에 직통 추정기나 복잡한 스파스 역전파가 필요 없어 훈련이 안정적
- **컨텍스트 병렬화 호환**: CP=2, DP=4 등 기존 컨텍스트 병렬화 설정과 함께 사용 가능
- **오픈소스**: 코드가 GitHub에 공개되어 있으며 PyTorch Torchtitan 기반으로 쉽게 적용 가능

**한계**

- 추론 속도 향상 없음: 훈련 단계의 비용만 줄이며, 배포된 모델의 추론 속도는 변하지 않음
- 소규모 실험 위주 검증: 논문의 실험은 비교적 작은 모델 규모에서 이루어졌으며, 수백억 파라미터 이상의 대규모 사전훈련에서의 효과는 아직 검증되지 않음
- 2단계 훈련 관리: 복원 단계로의 전환 시점 설정 등 훈련 파이프라인이 단일 단계보다 복잡해짐
- B200 GPU 최적화: 현재 구현은 CUDA 12.8 및 B200에 최적화되어 있으며 다른 하드웨어에서의 성능은 검증이 필요
- 상위-k 하이퍼파라미터 민감도: k값, 풀링 인수, 계층 수 등 추가 하이퍼파라미터 튜닝이 필요

**알아둘 용어**

- **스케일드-닷-프로덕트 어텐션(SDPA, Scaled Dot-Product Attention)**: 트랜스포머의 핵심 연산으로, Q·K 내적 점수를 소프트맥스로 정규화한 후 V에 가중합하는 방식. 시퀀스 길이 N에 대해 O(N²) 복잡도를 가진다.
- **계층적 어텐션(Hierarchical Attention)**: 입력 시퀀스를 여러 해상도(resolution)의 피라미드 구조로 압축하여, 전체 토큰 대신 중요도 높은 일부만 선택해 어텐션을 수행하는 접근법.
- **피라미드 압축(Pyramid Compression)**: 평균 풀링으로 시퀀스를 점차 줄여 다단계 요약 표현을 만드는 것. 각 단계는 상위 단계보다 더 많은 원래 토큰을 집약한다.
- **직통 추정기(Straight-Through Estimator)**: 불연속(discrete) 선택 연산을 역전파 가능하게 근사하는 기법. Lighthouse Attention은 이를 사용하지 않는다.
- **컨텍스트 병렬화(Context Parallelism)**: 긴 시퀀스를 여러 GPU에 분할하여 처리하는 분산 훈련 전략.
- **복원 단계(Recovery Phase)**: Lighthouse Attention 훈련 후, 짧은 기간 동안 전체 SDPA로 전환하여 표준 풀 어텐션 모델로 파인튜닝하는 마지막 단계.
- **비토닉 정렬(Bitonic Sort)**: 병렬 하드웨어(GPU)에서 효율적으로 상위-k 선택을 수행하기 위해 쓰이는 정렬 알고리즘.

**왜 주목할 만한가?**

긴 컨텍스트(128K, 512K, 1M 토큰 이상) LLM 훈련은 현재 AI 개발에서 가장 비용이 높은 과제 중 하나다. O(N²) 어텐션 때문에 컨텍스트 길이가 2배 늘면 어텐션 비용이 4배 증가한다. Lighthouse Attention은 훈련 속도를 17배 이상 높이면서도 최종 모델 품질을 유지하며, 커스텀 커널이나 추론 변경 없이 적용할 수 있다는 점에서 실용성이 높다. 특히 "훈련 전용" 설계는 배포 인프라를 변경하지 않으면서 훈련 비용만 줄일 수 있는 매우 실용적인 전략이다.

---

## English Summary

**One-line summary**

Lighthouse Attention is a training-only, selection-based hierarchical attention from Nous Research that compresses Q, K, and V into a multi-level pyramid, selects the top-K most important tokens via gradient-free scoring, and runs standard SDPA on only those tokens — delivering a 17× forward+backward speedup at 512K context with no custom kernels and no inference-time changes.

**Core idea**

Training causal transformers at very long context lengths is dominated by the quadratic O(N²) cost of standard scaled dot-product attention (SDPA). Lighthouse Attention replaces SDPA during most of pre-training with a hierarchical mechanism: Q, K, and V are simultaneously average-pooled into an L-level pyramid, each entry is scored using parameter-free per-head ℓ₂ norms, and a top-K kernel selects the most informative tokens across all pyramid levels. Only these selected tokens enter SDPA. Because the selection is gradient-free, backpropagation remains simple and stable. After the majority of training, a brief recovery phase switches back to full SDPA, converting the checkpoint into a standard full-attention model. The final model requires no special inference kernel or modified serving stack.

**What is new?**

- Training-only hierarchical attention: the resulting checkpoint is a standard full-attention model; no inference-side changes are needed
- Symmetrical compression: Q, K, and V are pooled simultaneously, preserving causal ordering while maximizing GPU parallelism
- Parameter-free scoring via per-head ℓ₂ norms with max-pooling score inheritance across pyramid levels
- No custom sparse attention kernel and no straight-through estimator required — the selection is gradient-free
- 21× faster forward pass and 17.3× faster forward+backward pass at 512K context on a single B200 GPU, with no loss in final model quality

**How does it work?**

1. **Pyramid construction**: Q, K, and V are average-pooled into an L-level hierarchy with pooling factor p. Level ℓ has N/pˡ tokens. The coarsest level is always retained in full so every base position has at least one representative.
2. **Scoring**: Each pyramid entry gets two scalar scores from its per-head ℓ₂ norm — one query score, one key score. Coarser levels inherit scores from finer levels via max-pooling, so a coarse span carries the score of its strongest token.
3. **Top-K selection**: A fused chunked-bitonic top-K kernel selects k entries jointly across all pyramid levels in a single efficient pass.
4. **Sparse attention**: Full SDPA runs on only the selected k tokens rather than the full N, reducing compute and memory dramatically.
5. **Two-stage training**: Stage 1 (majority of training, ~10K steps) uses Lighthouse Attention. Stage 2 (~6K steps) resumes with full SDPA to recover a standard full-attention model with matching or better quality than a dense baseline trained from scratch.

**Strengths**

- **No inference changes**: The final checkpoint is a standard full-attention model; deployment infrastructure is unchanged
- **No custom kernels**: Runs on top of standard PyTorch SDPA; hardware-specific kernel engineering is not required
- **Stable training**: Gradient-free selection avoids the instability of straight-through estimators or complex sparse backward passes
- **Context-parallel compatible**: Works alongside existing context-parallelism strategies (e.g., CP=2, DP=4)
- **Open source**: Code released on GitHub, implemented as a patch over PyTorch Torchtitan

**Limitations**

- **No inference speedup**: Training cost is reduced but the deployed model's inference speed is unchanged
- **Small-scale validation so far**: Experiments were conducted at relatively modest model sizes; effectiveness at tens of billions of parameters has not yet been demonstrated
- **Two-stage pipeline complexity**: Managing the switch from Lighthouse to full SDPA at the right training step adds pipeline overhead compared to single-stage training
- **B200-optimized implementation**: The current code targets CUDA 12.8 and NVIDIA B200; performance on other hardware is unverified
- **Additional hyperparameters**: Top-K budget, pooling factor, and number of hierarchy levels all require tuning

**Terms to know**

- **Scaled dot-product attention (SDPA)**: The core Transformer operation that computes attention scores as softmax(QKᵀ / √d) · V, with O(N²) compute and memory in sequence length N.
- **Hierarchical attention**: An attention variant that compresses the sequence into multiple resolution levels, attending only to the most important token representatives rather than all tokens.
- **Pyramid compression**: Average-pooling a sequence into progressively coarser levels; each coarser level summarizes an increasing number of original tokens.
- **Straight-through estimator**: A technique for backpropagating through discrete selections by approximating the gradient; Lighthouse Attention avoids this by making selection gradient-free.
- **Context parallelism**: A distributed training strategy that splits long sequences across multiple GPUs to handle lengths that exceed single-device memory.
- **Recovery phase**: The short final training stage where Lighthouse Attention is removed and full SDPA is restored, producing a standard full-attention model checkpoint.
- **Bitonic sort**: A parallel sorting algorithm well-suited to GPU execution, used here to efficiently perform top-K selection across pyramid levels.

**Why it is worth watching**

Long-context LLM pre-training (128K, 512K, and beyond) is one of the most computationally expensive challenges in current AI development. Doubling context length quadruples the attention cost, making trillion-token long-context pre-training prohibitively expensive. Lighthouse Attention reduces training wall-clock time by over an order of magnitude at extreme context lengths, with no sacrifice in final model quality and no changes to how the model is deployed or served. The training-only design is particularly practical: labs can simply swap in Lighthouse Attention for the pre-training run and recover a drop-in full-attention model at the end. As context windows continue to grow toward millions of tokens, efficient training algorithms like this will become increasingly important infrastructure.

**My take**

훈련 비용만 줄이고 추론에는 영향을 주지 않는 "훈련 전용" 설계는 실용성 측면에서 매우 영리한 선택이다. 17배 이상의 속도 향상은 인상적이지만, 아직 소규모 실험 결과이므로 수십억 파라미터 규모의 실제 사전훈련에서의 안정성과 품질 유지 여부가 향후 핵심 검증 과제다.

The training-only design — reducing pre-training cost without touching inference — is a pragmatic engineering choice. The 17× speedup figures are striking, but they come from smaller-scale experiments; whether quality and stability hold at tens of billions of parameters in a full production pre-training run is the key open question.
