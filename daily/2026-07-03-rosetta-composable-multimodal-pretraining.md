---
title: "Rosetta: Composable Native Multimodal Pretraining"
date: 2026-07-03
topic: AI
tags: [AI, multimodal, pretraining, mixture-of-experts, catastrophic-forgetting, continual-learning]
source: https://arxiv.org/abs/2607.00293
---

# Rosetta: Composable Native Multimodal Pretraining

* Date: 2026-07-01
* Source: https://arxiv.org/abs/2607.00293
* Topic: AI
* Why it matters: Building AI systems that handle text, images, and other modalities without forgetting prior capabilities is a key unsolved problem; Rosetta proposes a new modular pretraining framework and a gradient-conflict resolution technique that lets models absorb new modalities while preserving what they already know.

## Korean Summary

**한줄 요약**

Rosetta는 기존 MoE 및 MoT 아키텍처에서 발생하는 파국적 망각(catastrophic forgetting) 문제를 해결하기 위해 제안된 조합 가능한 멀티모달 프리트레이닝 프레임워크다. 핵심 지식을 글로벌 공유 전문가(global shared expert)에 보존하고, 모달리티별 능력을 플러그인 전문가(plug-and-play expert)에 분산시키는 모듈식 설계를 채택한다. 새로운 모달리티를 추가할 때 발생하는 그레이디언트 충돌을 MAOP(Momentum-Anchored Orthogonal Projection)로 억제하여, 언어 이해와 시각 이해 능력을 유지하면서도 이미지 생성 등 새로운 능력을 확장할 수 있다.

**핵심 아이디어**

멀티모달 AI 모델은 텍스트 이해(이산적 분류 목표)와 이미지 생성(연속적 생성 목표)처럼 성격이 다른 목표를 동시에 학습하면 그레이디언트 충돌이 발생한다. 이 충돌은 기존에 잘 수행하던 과제를 잊어버리는 파국적 망각으로 이어진다. Rosetta는 두 가지 방법으로 이 문제를 해결한다. 첫째, 글로벌 공유 전문가가 핵심 지식을 유지하고 모달리티 전용 플러그인 전문가가 각 양식의 특수 능력을 담당하는 모듈식 MoE 구조를 사용한다. 둘째, MAOP 기법으로 새 모달리티 학습 시 기존 지식을 손상시키는 그레이디언트 성분만 선택적으로 제거한다.

**무엇이 새로운가?**

- **모듈식 MoE 설계**: 핵심 지식을 담은 글로벌 공유 전문가와 모달리티별 플러그인 전문가를 분리하여 조합 가능한 확장성 확보
- **MAOP (Momentum-Anchored Orthogonal Projection)**: 옵티마이저의 모멘텀 상태를 암묵적인 시맨틱 앵커로 활용해 새 모달리티의 충돌 그레이디언트를 선택적으로 중화
- **기존 MoE/MoT 대비 우위 증명**: 표준 MoE와 MoT(Mixture-of-Transformers) 아키텍처가 모달리티 추가 시 파국적 망각을 겪는 반면 Rosetta는 기존 능력을 유지함을 실험으로 검증
- **교차 모달 시너지 발현**: 단순히 기존 능력을 보존하는 데 그치지 않고 모달리티 조합으로 새로운 시너지 효과가 나타남
- **새로운 생성 태스크의 빠른 수렴**: 플러그인 전문가 덕분에 새 모달리티 학습 시 수렴 속도가 향상됨

**어떻게 작동하는가?**

1. **글로벌 공유 전문가**: Transformer 내 FFN 층에 항상 활성화되는 공유 전문가를 배치하여 언어, 시각 등 공통 지식을 보존한다.
2. **플러그인 전문가**: 각 모달리티(예: 이미지 생성)에 특화된 전문가를 별도로 두고, 해당 모달리티 입력이 들어올 때만 활성화되어 기존 지식과의 충돌을 구조적으로 줄인다.
3. **MAOP 그레이디언트 제어**: 새 모달리티를 추가하는 학습 시, 옵티마이저가 추적하는 모멘텀 벡터를 참조해 기존 공유 전문가 파라미터의 업데이트 방향에서 충돌 성분을 직교 투영(orthogonal projection)으로 제거한다. 시너지를 낼 수 있는 그레이디언트 성분은 보존되어 교차 모달 학습이 가능하다.
4. **평가**: 표준 MoE 및 MoT 기준 모델과 비교하여 언어 이해, 시각 이해, 이미지 생성 벤치마크에서 평가하며 파국적 망각 여부를 측정한다.

**강점**

- 새 모달리티 추가 시 기존 능력 손실 없이 확장 가능한 실용적 설계
- MAOP는 별도 아키텍처 변경 없이 옵티마이저 상태를 재활용하는 경량 기법
- 글로벌/플러그인 전문가 분리로 모달리티 간 책임이 명확해져 해석 가능성 향상
- Tencent Hunyuan의 실무 인프라를 바탕으로 한 연구로, 실용화 가능성이 높음

**한계**

- 구체적인 벤치마크 수치와 비교 결과가 아직 공개 문헌에서 충분히 검증되지 않음 (preprint 단계)
- 모달리티 수가 늘어날수록 플러그인 전문가 수 증가에 따른 모델 크기 문제가 발생할 수 있음
- MAOP의 직교 투영 계산 비용이 대규모 학습에서 어느 정도 오버헤드를 초래하는지 불명확
- 오디오, 비디오 등 추가 모달리티까지 확장한 결과는 현재 논문에서 명시적으로 제시되지 않음

**알아둘 용어**

- **파국적 망각 (Catastrophic Forgetting)**: 새로운 지식을 학습할 때 기존에 습득한 지식이 급격히 손실되는 신경망 현상
- **MoE (Mixture-of-Experts)**: 여러 전문가 서브네트워크 중 입력에 따라 일부만 선택적으로 활성화하는 희소 아키텍처
- **MoT (Mixture-of-Transformers)**: 모달리티마다 독립적인 Transformer 블록을 배치해 구조적으로 분리하는 방식
- **MAOP (Momentum-Anchored Orthogonal Projection)**: 옵티마이저 모멘텀을 의미론적 앵커로 삼아 충돌 그레이디언트를 직교 투영으로 제거하는 기법
- **직교 투영 (Orthogonal Projection)**: 벡터를 다른 벡터 방향에서 수직인 성분만 남기는 선형대수 연산; 여기서는 기존 지식을 손상시키는 방향의 그레이디언트를 제거하는 데 사용
- **플러그인 전문가 (Plug-and-play Expert)**: 기존 모델에 탈착 가능한 모듈식 전문가로, 새 모달리티 추가 시 본체를 건드리지 않고 삽입 가능
- **교차 모달 시너지 (Cross-modal Synergy)**: 서로 다른 모달리티를 함께 학습할 때 각 모달리티의 성능이 단독 학습보다 향상되는 효과

**왜 주목할 만한가?**

AI 모델이 텍스트, 이미지, 오디오, 비디오 등 점점 더 많은 양식을 처리해야 하는 시대에 파국적 망각은 멀티모달 AI 개발의 핵심 장벽이다. 기존 대형 모델들은 새 모달리티를 추가할 때 종종 처음부터 재학습하거나, 기존 능력 저하를 감수해야 했다. Rosetta는 MAOP와 모듈식 전문가 설계로 이 문제를 구조적으로 해결하여, 멀티모달 AI의 점진적·지속적 확장을 가능하게 한다는 점에서 범용 AI 구축 로드맵에 중요한 기여를 한다.

---

## English Summary

**One-line summary**

Rosetta is a composable native multimodal pretraining framework from HKUST and Tencent Hunyuan that solves catastrophic forgetting when expanding a model with new modalities. It separates core foundational knowledge in global shared experts from modality-specific plug-and-play experts, and introduces Momentum-Anchored Orthogonal Projection (MAOP) to neutralize gradient conflicts during new modality integration.

**Core idea**

Multimodal AI models must simultaneously handle discrete understanding objectives (e.g., language classification) and continuous generative objectives (e.g., image generation). These conflicting gradient directions cause representation overwriting, where learning one capability degrades another — a problem known as catastrophic forgetting. Existing architectures including standard MoE and Mixture-of-Transformers (MoT) are vulnerable. Rosetta addresses this with two complementary ideas: (1) a modular expert structure that structurally separates foundational and modality-specific knowledge, and (2) MAOP, which actively monitors and filters out only the harmful gradient components during training.

**What is new?**

- **Modular MoE design**: Global shared experts preserve cross-modal foundational knowledge; plug-and-play experts handle each modality's specialized capabilities independently
- **MAOP (Momentum-Anchored Orthogonal Projection)**: Uses the optimizer's accumulated momentum vector as a semantic anchor to identify and remove conflicting gradient components from new modalities while keeping synergistic ones
- **Empirical proof of forgetting in existing approaches**: Demonstrates that standard MoE and MoT architectures both suffer significant catastrophic forgetting under native multimodal pretraining
- **Cross-modal synergy**: Beyond mere forgetting prevention, Rosetta enables newly composed modalities to positively reinforce each other
- **Faster convergence on new generative tasks**: The plug-in expert structure speeds up adaptation when adding new modalities

**How does it work?**

1. **Global shared experts**: A fixed set of always-active experts within the FFN layers retains general-purpose representations shared across modalities (language, vision understanding, etc.).
2. **Plug-and-play experts**: Each modality has its own dedicated experts that activate only on modality-specific inputs. Adding a new modality means inserting new plug-in experts without touching the shared core.
3. **MAOP gradient filtering**: When training on new modality data, MAOP reads the current momentum state of the optimizer (which reflects the accumulated update directions for existing knowledge) and uses orthogonal projection to remove the component of new-modality gradients that conflicts with existing directions. Synergistic gradient components are preserved, enabling positive transfer.
4. **Evaluation**: The framework is benchmarked against standard MoE and MoT baselines on language understanding, visual understanding, and image generation tasks, measuring both capability retention and cross-modal improvement.

**Strengths**

- Plug-in expert design allows modular, non-destructive expansion — new modalities do not require retraining the whole model
- MAOP is lightweight; it reuses the optimizer's existing momentum state rather than requiring separate reference models or complex conflict detection modules
- Structural separation between global and modality-specific experts improves interpretability and reduces interference
- Backed by Tencent Hunyuan, a large-scale practical deployment environment, suggesting feasibility at industrial scale

**Limitations**

- Results are from a preprint and have not yet undergone full peer review
- Scaling to many modalities (audio, video, code, etc.) could inflate model size as each new modality adds plug-in experts
- The computational overhead of MAOP's orthogonal projection at scale is not thoroughly characterized
- The paper does not yet report results on a broad set of modalities beyond the text-image pair evaluated
- It is unclear how MAOP interacts with low-rank or quantized training settings common in production

**Terms to know**

- **Catastrophic forgetting**: The tendency of neural networks to lose previously learned knowledge when trained on new tasks
- **MoE (Mixture-of-Experts)**: A sparse architecture where only a subset of expert sub-networks activates per input, enabling large model capacity with lower per-token compute
- **MoT (Mixture-of-Transformers)**: An architecture variant that assigns separate Transformer blocks to different modalities for structural isolation
- **MAOP (Momentum-Anchored Orthogonal Projection)**: A gradient management technique that projects new-modality gradient components orthogonal to the momentum direction, canceling interference while preserving synergy
- **Orthogonal projection**: A linear algebra operation that extracts the component of one vector perpendicular to another; used here to isolate and remove conflicting gradient directions
- **Plug-and-play expert**: A modular expert module that can be inserted into an existing model without modifying its core parameters
- **Cross-modal synergy**: Performance gains that arise specifically from training multiple modalities together, where each benefits from the other's representation

**Why it is worth watching**

As AI systems are expected to natively handle an expanding set of modalities — text, images, audio, video, code, and beyond — catastrophic forgetting is one of the most stubborn practical blockers to building general-purpose models. Today, adding a new modality often forces a full retraining from scratch or accepts degraded performance on existing tasks. Rosetta's modular expert design and MAOP technique offer a principled, architecture-level solution to this problem. If the results hold up under broader evaluation, this approach could become an important component in how multimodal foundation models are designed and extended at scale.

**My take**

Rosetta targets a genuine and important failure mode in multimodal AI. The MAOP idea is technically elegant — repurposing the momentum vector already computed by the optimizer as a semantic anchor, rather than requiring a separate mechanism, is a frugal design choice. That said, the paper is a preprint and the evaluation scope appears focused on text-image modalities; whether MAOP scales gracefully to three or more modalities with heterogeneous gradient dynamics remains to be seen. Worth tracking as a serious approach to compositional multimodal pretraining.

로제타는 멀티모달 AI의 실질적인 장애물인 파국적 망각을 정면으로 다루는 연구다. MAOP 아이디어는 기술적으로 우아하다 — 옵티마이저가 이미 계산하는 모멘텀 벡터를 의미론적 앵커로 재활용하는 방식은 별도 메커니즘이 불필요한 절약적 설계다. 다만 이 논문은 프리프린트 단계이며 텍스트-이미지 조합에 집중된 평가를 제시하고 있어, 세 가지 이상의 이질적인 모달리티로 확장될 때 MAOP가 얼마나 잘 작동하는지는 추가 검증이 필요하다.
