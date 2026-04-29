---
title: "Accelerating Speculative Decoding with Block Diffusion Draft Trees"
date: 2026-04-29
topic: AI
tags: [AI, speculative-decoding, inference-efficiency, diffusion-models, LLM, block-diffusion, inference]
source: https://arxiv.org/abs/2604.12989
---

Accelerating Speculative Decoding with Block Diffusion Draft Trees

* Date: 2026-04-29
* Source: https://arxiv.org/abs/2604.12989
* Topic: AI / Inference Efficiency
* Why it matters: Speculative decoding is one of the most practical ways to speed up LLM inference without sacrificing output quality; DDTree significantly advances the state of the art by combining block diffusion draft models with tree-based multi-path verification, achieving speedups of up to 7.5× over standard autoregressive decoding on reasoning-heavy tasks.

## Korean Summary

**한줄 요약**

DDTree는 블록 확산(block diffusion) 드래프터 모델이 출력하는 위치별 확률 분포를 활용해 추론 트리(draft tree)를 구성하고, 이를 단 한 번의 타깃 모델 순전파로 검증함으로써 기존 DFlash보다 더 많은 토큰을 라운드당 수락한다. 이스라엘 테크니온(Technion)에서 2026년 4월 제출된 이 논문은 EAGLE-3 같은 자기회귀 드래프터 기반 방법보다 뛰어난 성능을 보이며, 수학 추론(MATH) 등 집약적인 태스크에서 표준 자기회귀 디코딩 대비 최대 7.5배의 속도 향상을 보고한다.

**핵심 아이디어**

투기적 디코딩(speculative decoding)은 소형 드래프트 모델이 여러 토큰을 미리 제안하고 대형 타깃 모델이 이를 병렬로 검증하는 방식이다. DFlash(선행 연구)는 블록 확산 모델을 드래프터로 사용해 단 한 번의 순전파로 블록 전체를 생성하고 EAGLE-3를 능가했지만, 매 라운드마다 단일 후보 시퀀스만 검증한다는 한계가 있다. DDTree는 블록 확산 드래프터가 각 위치에 대해 전체 어휘 확률 분포를 출력한다는 점을 이용해, 가장 높은 결합 확률을 가진 경로들로 이루어진 드래프트 트리를 구성하고, 이 트리 전체를 단 한 번의 타깃 모델 순전파로 검증해 라운드당 수락 길이를 늘린다.

**무엇이 새로운가?**

- 블록 확산 드래프터의 위치별 확률 분포를 이용한 드래프트 트리 구성이라는 새로운 접근법
- 고정된 노드 예산(node budget) 내에서 결합 확률 기준으로 최적 경로를 선택하는 best-first 힙(heap) 알고리즘
- 조상-전용(ancestor-only) 어텐션 마스크를 이용한 드래프트 트리 전체의 단일 패스 검증
- 단일 후보 시퀀스만 검증하는 vanilla DFlash 대비 추가 속도 향상 (코드·수학 태스크에서 ~10–15%)
- 수학·추론 집약적 태스크에서 표준 자기회귀 대비 최대 7.5× 속도 향상; GitHub 공개 및 Apple Silicon(MLX) 포팅 버전 제공

**어떻게 작동하는가?**

1. **블록 확산 드래프팅**: DFlash 드래프터(블록 확산 언어 모델)가 단 하나의 순전파로 드래프트 블록 내 각 위치에 대한 어휘 확률 분포를 출력한다. 자기회귀 드래프터처럼 토큰을 순차적으로 생성하지 않아도 되어 매우 빠르다.
2. **트리 구성(best-first heap)**: 위치별 분포를 바탕으로, 각 후보 경로의 결합 확률을 기준으로 best-first 힙 알고리즘을 사용해 고정된 노드 수 예산 내에서 트리를 구성한다. 가장 높은 확률을 가진 토큰 조합들이 트리 노드로 선택된다.
3. **트리 검증(조상-전용 어텐션)**: 구성된 드래프트 트리를 단 한 번의 타깃 모델 순전파로 검증한다. 트리 내 각 노드는 자신의 조상 노드들만 어텐션하므로 복수의 후보 경로를 동시에 처리할 수 있다.
4. **수락 및 반복**: 드래프트 트리에서 타깃 모델이 수락하는 가장 긴 접두사(prefix)를 채택하고, 다음 라운드로 진행한다. 라운드당 수락 길이가 늘어나면 전체 토큰 생성 속도가 향상된다.

**강점**

- 자기회귀 드래프터 기반 EAGLE-3를 능가하는 블록 확산 드래프터의 장점을 그대로 유지하면서, 트리 기반 검증으로 추가 이득 확보
- 드래프터나 타깃 모델을 재훈련하지 않고 기존 DFlash 드래프터 위에 바로 적용 가능
- GitHub 공개 및 Apple Silicon(MLX) 포팅 버전 제공으로 접근성 높음
- 수학·추론 집약적 태스크에서 특히 높은 수락률과 속도 향상; vLLM 통합 논의 진행 중

**한계**

- 속도 향상 폭은 태스크 유형과 드래프터-타깃 일치도에 크게 의존 (수학: ~7.5×, 일반 대화: ~3.3×)
- 블록 확산 드래프터가 현재 공개된 모델 패밀리가 제한적 (예: Qwen 3.5 계열)
- 최적 노드 예산(256~512)을 넘어서면 트리 구성 비용이 이득을 초과해 효율 감소 가능
- 새로운 타깃 모델에 맞는 블록 확산 드래프터를 별도로 훈련하는 비용은 여전히 필요

**알아둘 용어**

- **투기적 디코딩(Speculative Decoding)**: 소형 드래프트 모델이 여러 토큰을 제안하고 대형 타깃 모델이 한 번의 순전파로 이를 병렬 검증하는 LLM 추론 가속 기법
- **블록 확산 언어 모델(Block Diffusion LM)**: 마스킹된 확산(masked diffusion) 기반 비자기회귀 언어 모델; 한 번의 순전파로 토큰 블록 전체의 위치별 확률 분포를 출력
- **드래프트 트리(Draft Tree)**: 투기적 디코딩에서 단일 경로 대신 여러 후보 시퀀스를 트리 구조로 구성해 한 번에 검증하는 방식
- **EAGLE-3**: 학습된 특징 예측(feature prediction)과 트리 구조 초안을 결합한 자기회귀 드래프터 기반 최강 투기적 디코딩 방법 중 하나
- **DFlash**: 블록 확산 모델을 드래프터로 사용하는 투기적 디코딩 방법; DDTree의 직접적인 전신이며 EAGLE-3를 능가
- **조상-전용 어텐션 마스크(Ancestor-Only Attention Mask)**: 트리 기반 검증에서 각 토큰이 트리 상의 부모·조상 노드만 어텐션하도록 제한하는 마스크; 복수의 트리 경로를 단일 패스로 처리 가능하게 함
- **수락 길이(Acceptance Length)**: 투기적 디코딩 한 라운드에서 타깃 모델이 수락하는 드래프트 토큰 수; 이 값이 클수록 전체 생성 속도가 빠름

**왜 주목할 만한가?**

LLM 추론 비용 절감은 2026년 AI 인프라의 핵심 과제이며, 투기적 디코딩은 출력 품질 저하 없이 추론 속도를 높이는 가장 실용적인 방법 중 하나다. DDTree는 최근 등장한 블록 확산 드래프터의 강점에 트리 기반 다중 경로 검증을 결합해, 기존 방법들보다 효율적으로 더 많은 토큰을 수락한다. GitHub 공개 코드 및 vLLM 통합 추진(issue #40809)을 통해 실제 서빙 스택에 미치는 영향도 빠르게 확산될 전망이다.

---

## English Summary

**One-line summary**

DDTree (Diffusion Draft Tree) is a speculative decoding method that builds a tree of high-probability token continuations from a block diffusion drafter's per-position output distributions, verifies the entire tree in a single target model forward pass, and achieves speedups of up to 7.5× over standard autoregressive decoding — improving over both EAGLE-3 and vanilla DFlash without retraining either model.

**Core idea**

Speculative decoding uses a small draft model to propose k tokens at once, then verifies all k in parallel with a single target model forward pass, gaining multiple tokens per round instead of one. DFlash (the predecessor) replaced autoregressive drafters with block diffusion models that output full per-position distributions in a single pass, already outperforming EAGLE-3. But vanilla DFlash still verifies only one draft trajectory per round. DDTree fixes this: since block diffusion produces a full probability distribution over the vocabulary at every position, those distributions can be used to construct a tree of the most probable token combinations. The entire tree is verified in one pass using an ancestor-only attention mask, and the longest matching prefix is accepted, raising the expected tokens accepted per round.

**What is new?**

- First method to construct a speculative draft tree directly from a block diffusion model's per-position output distributions
- Best-first heap algorithm for tree node selection under a fixed budget, maximizing joint probability of candidate paths
- Ancestor-only attention mask enabling single-pass verification of the full draft tree
- Up to ~10–15% additional speedup over vanilla DFlash from increased per-round acceptance length
- Up to 7.5× speedup over autoregressive decoding on MATH-500; 3.3× on Alpaca; open-source release with Apple Silicon (MLX) port

**How does it work?**

1. **Block diffusion drafting**: The DFlash block diffusion drafter performs a single forward pass and outputs a probability distribution over the full vocabulary at each position in the draft block — not just one token per position, unlike autoregressive drafters.
2. **Tree construction (best-first heap)**: Under a fixed node budget, DDTree greedily builds a tree by expanding nodes in order of descending joint probability. A best-first heap selects which branches to expand next, filling the budget with the paths most likely to be accepted by the target model.
3. **Single-pass tree verification**: The entire draft tree is verified in one target model forward pass using an ancestor-only attention mask — each token attends only to its ancestors in the tree, allowing multiple candidate paths to be evaluated simultaneously and efficiently.
4. **Acceptance**: The longest prefix of the draft tree that the target model accepts (under the standard speculative decoding criterion) is committed. Accepting longer prefixes per round means fewer total rounds to generate a full response.

**Strengths**

- Inherits all advantages of block diffusion drafters (parallel block generation, state-of-the-art acceptance rates) while extracting additional speedup through tree exploration
- No retraining of the drafter or target model required; applies directly on top of existing DFlash drafters
- Open-source GitHub implementation; Apple Silicon (MLX) port also available
- Particularly effective on reasoning-heavy tasks (math, code) where drafter and target distributions are well-aligned; vLLM integration is in active development (issue #40809)

**Limitations**

- Speedup is highly task-dependent: up to 7.5× on MATH but around 3.3× on conversational tasks like Alpaca
- Block diffusion drafters are currently only available for select model families (e.g., Qwen 3.5); broader model coverage requires training new drafters
- Node budget must be tuned carefully; budgets above ~512 can reduce efficiency as tree construction cost outpaces acceptance gains
- Training a block diffusion drafter for a new target model remains a separate, non-trivial effort

**Terms to know**

- **Speculative decoding**: An LLM inference acceleration technique in which a small draft model proposes candidate tokens and a large target model verifies all of them in parallel, yielding multiple tokens per target model forward pass.
- **Block diffusion language model**: A non-autoregressive language model based on masked diffusion; generates a block of tokens in a fixed number of diffusion steps (far fewer than L autoregressive steps), outputting per-position vocabulary distributions in a single pass.
- **Draft tree**: A tree-structured set of candidate token continuations where each path from root to leaf is a candidate sequence; the entire tree is verified in one target model pass via a specialized attention mask.
- **EAGLE-3**: A leading autoregressive speculative decoding method combining learned feature prediction with tree-structured drafting to maximize acceptance rates.
- **DFlash**: Block Diffusion for Flash Speculative Decoding — the direct predecessor to DDTree; uses block diffusion as the drafter but verifies only a single trajectory per round.
- **Ancestor-only attention mask**: An attention mask used in tree verification that restricts each token to attend only to its ancestors in the draft tree, enabling simultaneous evaluation of multiple candidate paths in one forward pass.
- **Acceptance length**: The number of draft tokens accepted by the target model per speculative decoding round; higher acceptance length means fewer rounds and faster end-to-end generation.

**Why it is worth watching**

LLM inference cost is one of the most pressing practical concerns in AI deployment, and speculative decoding is the leading approach to reducing it without any loss in output quality. DDTree represents a clean, zero-retraining improvement over the current state of the art by extracting value from information that block diffusion drafters already produce — the per-position probability distributions — to verify more candidates per round. With an active vLLM integration effort and an open-source codebase, DDTree has a direct path into real production serving infrastructure, and as block diffusion drafters become available for more model families, its impact will broaden.

**My take**

DDTree의 기여는 명확하고 실용적이다. 블록 확산 드래프터가 이미 위치별 확률 분포를 자연스럽게 제공한다는 사실을 이용해 추가 훈련 없이 트리를 구성한다는 아이디어는 우아하며, 수학적 복잡도보다는 엔지니어링 창의성에 가까운 기여다. 그만큼 즉각적으로 실용화될 가능성이 높다. 다만 속도 향상 폭이 태스크 종류와 드래프터 가용성에 크게 의존하므로, 블록 확산 드래프터 생태계가 얼마나 빠르게 확장되느냐가 이 방법의 장기적 영향력을 좌우할 것이다.

DDTree's contribution is practical and well-motivated. The insight that block diffusion drafters already produce per-position distributions — information wasted by vanilla DFlash — and that those distributions can be directly turned into a speculation tree via a simple heap algorithm is elegant. It is more an engineering innovation than a theoretical breakthrough, but that is precisely what makes it immediately deployable. The key constraint is that the method's impact depends on the availability of block diffusion drafters for the target model in question; as the ecosystem expands beyond the current Qwen 3.5 family, DDTree will become broadly applicable to production LLM serving.
