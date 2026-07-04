---
title: "Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training"
date: 2026-07-04
topic: AI
tags: [AI, LLM, reinforcement-learning, post-training, transformer, efficiency, RLVR, GRPO]
source: https://arxiv.org/abs/2607.01232
---

# Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

* Date: 2026-07-01
* Source: https://arxiv.org/abs/2607.01232
* Topic: AI
* Why it matters: This paper reveals that RL post-training gains in large language models are concentrated in a small subset of transformer layers, meaning training just one layer can match or exceed full-parameter RL training — a finding with significant implications for compute efficiency and our understanding of how RL shapes language models.

## Korean Summary

**한줄 요약**

대형 언어 모델의 강화학습(RL) 파인튜닝에서, 전체 파라미터를 학습시키는 대신 단 하나의 트랜스포머 레이어만 학습해도 전체 성능 향상의 대부분(최대 114%)을 회복할 수 있다는 사실이 밝혀졌다. RL 적응(adaptation)이 소수의 레이어에 집중된다는 이 구조적 특성은 기존 가정을 뒤집는 중요한 발견이다.

**핵심 아이디어**

기존의 RL 후훈련(post-training)은 모든 트랜스포머 레이어의 파라미터를 업데이트한다는 전제하에 진행되었다. 이 논문은 레이어별 기여도를 체계적으로 측정해 보면, RL 이득의 대부분이 소수의 특정 레이어(주로 중간 부분)에 집중되어 있음을 보여준다. 따라서 가장 기여도가 높은 단일 레이어만 훈련해도 전체 파라미터 RL과 대등하거나 더 나은 성능을 낼 수 있다.

**무엇이 새로운가?**

* **레이어 기여도(Layer Contribution)** 라는 새로운 지표를 도입하여, 각 레이어를 단독으로 훈련했을 때 전체 RL 이득의 몇 %를 회복하는지를 정량화했다.
* 단일 레이어 훈련으로 전체 RL 성능의 최대 114%를 회복할 수 있으며, 가장 낮은 레이어는 30% 미만에 그친다는 사실을 발견했다.
* 높은 기여도의 레이어는 트랜스포머 스택의 **중간 부분**에 집중되고, 입출력 끝단의 레이어는 기여도가 낮음을 규명했다.
* 레이어 기여도 순위가 서로 다른 데이터셋, 태스크, 모델 패밀리, RL 알고리즘에 걸쳐 강하게 상관되어 있음을 보였다.
* Qwen3, Qwen2.5 계열 7개 모델, GRPO·GiGPO·Dr. GRPO 3가지 RL 알고리즘, 수학 추론·코드 생성·에이전트 의사결정 등 다양한 도메인에서 실험을 통해 주장을 검증했다.

**어떻게 작동하는가?**

1. **설정**: 사전학습된 LLM을 준비하고, 특정 레이어 하나를 선택하여 그 레이어의 파라미터만 훈련 가능(trainable)으로 설정한다. 나머지 레이어는 모두 동결(frozen) 상태로 둔다.
2. **레이어 기여도 측정**: 각 레이어를 단독으로 RL 훈련하고, 전체 파라미터 RL 훈련 대비 성능 향상 비율을 측정하여 "레이어 기여도"로 정의한다.
3. **분포 분석**: 여러 모델, 태스크, 알고리즘에 걸쳐 레이어별 기여도 분포를 분석하면, 중간 레이어들이 일관되게 높은 기여도를 보인다.
4. **단일 최고 레이어 훈련**: 가장 기여도가 높은 레이어를 선택해 단독으로 훈련하면, 전체 파라미터 RL과 대등하거나 더 나은 성능을 달성할 수 있다.
5. **일반화 검증**: 이 패턴은 모델 크기, RL 알고리즘, 도메인이 바뀌어도 안정적으로 유지된다.

**강점**

* 대규모 실험(7개 모델, 3개 RL 알고리즘, 다수 도메인)으로 강한 일반화를 입증함.
* 단일 레이어 훈련으로 메모리와 연산 비용을 대폭 절감할 수 있는 실용적 방법론을 제시함.
* RL 적응이 어느 레이어에서 일어나는지에 대한 기계론적 이해(mechanistic understanding)를 제공함.
* 기존 RL 알고리즘(GRPO 등)을 그대로 사용하면서 훈련 범위만 줄이는 방식이라 적용이 간단함.

**한계**

* 현재는 Qwen 계열 모델에만 실험이 집중되어 있어, 다른 모델 패밀리(Llama, Mistral 등)에서도 동일한 패턴이 나타나는지 추가 검증이 필요하다.
* 어떤 레이어가 최고 기여도를 가지는지 사전에(without searching) 예측하는 방법이 아직 명확히 제시되지 않았다.
* 단일 레이어 훈련이 RL 알고리즘과 어떻게 상호작용하는지의 이론적 설명이 아직 부족하다.
* 매우 어려운 롱-호라이즌(long-horizon) 태스크나 도메인 이동(domain shift) 상황에서의 성능은 검증이 필요하다.

**알아둘 용어**

* **RL 후훈련 (RL Post-training)**: 사전학습된 LLM에 강화학습을 적용해 특정 능력(추론, 코드 생성 등)을 향상시키는 과정.
* **GRPO (Group Relative Policy Optimization)**: 그룹 내 상대적 보상을 활용하는 LLM 강화학습 알고리즘. DeepSeek-R1에서 유명해졌다.
* **레이어 기여도 (Layer Contribution)**: 단일 레이어를 훈련했을 때 전체 RL 이득의 몇 %를 회복하는지를 나타내는 지표.
* **파라미터 동결 (Parameter Freezing)**: 특정 레이어의 파라미터를 훈련 중 변경하지 않고 고정하는 방법.
* **RLVR (Reinforcement Learning from Verifiable Rewards)**: 정답 확인이 가능한 태스크(수학, 코드 등)에서 검증 가능한 보상을 이용하는 RL 방식.
* **트랜스포머 스택 (Transformer Stack)**: 여러 트랜스포머 레이어가 순차적으로 쌓인 구조.
* **GiGPO, Dr. GRPO**: GRPO의 변형 알고리즘으로, 각각 인스턴스 수준 기준선과 다양한 강인화 기법을 도입한 것.

**왜 주목할 만한가?**

RL 후훈련은 최신 추론 모델(reasoning model)의 핵심 기술이지만 연산 비용이 높다. 이 논문은 RL 이득이 소수 레이어에 집중된다는 구조적 사실을 밝혀 훈련 비용을 획기적으로 줄일 수 있는 방향을 제시한다. 나아가 RL이 LLM의 어느 부분을 변화시키는지에 대한 기계론적 이해를 높여, 향후 더 효율적인 RL 알고리즘 설계에 기여할 것으로 기대된다.

---

## English Summary

**One-line summary**

Training only a single transformer layer during RL post-training can recover most, and sometimes exceed all, of the gains from full-parameter RL training — revealing that RL adaptation in LLMs is concentrated in a small subset of middle-stack layers.

**Core idea**

Standard RL post-training updates every parameter in a language model uniformly. This paper challenges that by measuring how much each individual transformer layer contributes to RL improvement when trained in isolation. The result: a handful of middle-stack layers account for nearly all the gains, and training just the single best layer can match or beat full-parameter RL. This rewrites how we think about what RL post-training actually changes in a model.

**What is new?**

* Introduces **layer contribution**, a scalar metric measuring the fraction of full-parameter RL gains recovered when a single layer is trained in isolation.
* Demonstrates that the best individual layers recover up to **114% of full-parameter RL gains**, while the weakest recover less than 30%.
* Shows that high-contribution layers are consistently located in the **middle of the transformer stack**, not at the input or output ends.
* Demonstrates that layer contribution rankings are **strongly correlated** across different datasets, tasks, model families, and RL algorithms.
* Validates findings across 7 models from the Qwen3 and Qwen2.5 families, 3 RL algorithms (GRPO, GiGPO, Dr. GRPO), and tasks spanning mathematical reasoning, code generation, and agentic decision-making.

**How does it work?**

1. **Setup**: Take a pretrained LLM and select one transformer layer to be trainable; freeze all remaining layers.
2. **Layer contribution measurement**: Apply RL training with only the selected layer's parameters unfrozen, then measure the performance improvement as a fraction of what full-parameter RL achieves. Repeat for every layer in the model.
3. **Pattern analysis**: Across models, tasks, and algorithms, the layer-wise contribution distribution consistently shows a peak in the middle layers and a sharp drop at both ends of the stack.
4. **Single best layer training**: Selecting and training the single highest-contributing layer in isolation produces performance matching or exceeding full-parameter RL.
5. **Generalization check**: The pattern holds across different model sizes, RL algorithm variants, and task domains, indicating a stable structural property rather than an artifact.

**Strengths**

* Large-scale empirical validation across multiple model families, RL algorithms, and task domains makes the finding highly credible.
* Directly practical: single-layer RL training drastically reduces memory and compute requirements, with no change to the RL algorithm itself.
* Provides mechanistic insight into where RL adaptation happens inside a transformer, advancing interpretability of post-training.
* Straightforward to apply — just freeze all layers except the identified key layer and run existing RL pipelines.

**Limitations**

* Experiments are limited to Qwen3 and Qwen2.5 families; whether the pattern holds for Llama, Mistral, or other architectures needs further verification.
* The paper does not yet provide a principled method for predicting which specific layer will be highest-contributing without running a search.
* A theoretical explanation for why middle-stack layers dominate RL adaptation is still lacking.
* Performance on very long-horizon tasks or significant out-of-distribution settings is not fully explored.

**Terms to know**

* **RL post-training**: Applying reinforcement learning to a pretrained LLM to improve specific capabilities such as reasoning, coding, or instruction following.
* **GRPO (Group Relative Policy Optimization)**: An RL algorithm for LLMs that uses relative rewards within a group of outputs; popularized by DeepSeek-R1.
* **Layer contribution**: The fraction of full-parameter RL improvement recovered when a single layer is trained in isolation — the paper's core metric.
* **Parameter freezing**: Keeping all but a select set of parameters fixed during training so only those parameters are updated.
* **RLVR (Reinforcement Learning from Verifiable Rewards)**: RL training using rewards derived from verifiable task outcomes, common in math and code settings.
* **GiGPO / Dr. GRPO**: Variants of GRPO incorporating instance-level baselines and additional robustness techniques.
* **Transformer stack**: The sequential arrangement of transformer layers that constitutes the core of a modern LLM.

**Why it is worth watching**

RL post-training has become the defining technique for modern reasoning models, but it is computationally expensive. This paper shows that the expense may be largely unnecessary: most RL gains are concentrated in a small fraction of the model's layers. If this holds broadly, the field could shift toward selective-layer RL training, cutting training costs substantially while preserving gains. The mechanistic insight — that middle-stack layers are the primary site of RL adaptation — also opens new questions about interpretability and the design of more targeted post-training methods.

**My take**

이 발견은 단순히 "효율화" 이상의 의미를 가진다. RL이 어디서 무엇을 바꾸는지에 대한 이해를 심화시키며, 지금까지 "블랙박스"처럼 다뤄졌던 RL 후훈련의 내부 작동 방식을 조금 더 투명하게 만들어 준다. 다만 이 패턴이 더 다양한 모델 아키텍처와 더 어려운 태스크에서도 성립하는지 추가 검증이 필요하며, "어떤 레이어를 고를지"를 탐색 없이 결정하는 방법이 확립되어야 실용적 가치가 완결될 것이다.

This finding matters beyond efficiency. It sheds light on where and how RL reshapes a language model, making the post-training process more interpretable. The immediate practical payoff — drastically cheaper RL training — is real, but the deeper value is the mechanistic picture it starts to build. Whether the pattern extends to other model families and harder tasks, and whether we can predict the best layer without a full search, are the critical open questions that will determine how widely this insight can be applied.
