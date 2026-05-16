---
title: "Solve the Loop: Attractor Models for Language and Reasoning"
date: 2026-05-16
topic: AI
tags: [AI, LLM, architecture, reasoning, fixed-point, implicit-differentiation, looped-models, efficiency]
source: https://arxiv.org/abs/2605.12466
---

# Solve the Loop: Attractor Models for Language and Reasoning

* Date: 2026-05-16
* Source: https://arxiv.org/abs/2605.12466
* Topic: AI / Architecture / Reasoning
* Why it matters: Looped Transformers can compute more deeply without growing model size, but have been hampered by training instability and fixed recurrence depth; Attractor Models solve both problems with a fixed-point formulation that gives constant training memory and adaptive iteration depth, while achieving 46.6% perplexity gains over standard Transformers and solving puzzles where GPT o3 fails.

## Korean Summary

**한줄 요약**

USC 연구진이 제안한 Attractor Models는 트랜스포머의 반복 연산을 고정점 방정식(fixed-point equation)으로 재정식화하여, 암묵적 미분(implicit differentiation)으로 기울기를 구함으로써 훈련 메모리를 깊이와 무관하게 일정하게 유지한다. 표준 트랜스포머 대비 최대 46.6% 퍼플렉시티(perplexity) 개선과 19.7% 다운스트림 정확도 향상을 달성했으며, 27M 파라미터 모델이 Claude와 GPT o3가 실패하는 Sudoku-Extreme에서 91.4%를 달성했다.

**핵심 아이디어**

루프 트랜스포머(Looped Transformer)는 동일한 레이어 블록을 여러 번 반복 실행해 파라미터 수를 늘리지 않고 연산 깊이를 키우는 접근법이다. 기존 방식은 반복 횟수를 사전에 고정해야 하고, 모든 반복에 걸쳐 키-값(KV) 캐시나 은닉 상태를 저장해야 하므로 훈련 메모리가 깊이에 비례해 늘어난다. Attractor Models는 이를 다르게 풀어낸다: 비재귀적 백본(backbone) 모듈이 초기 출력 임베딩을 제안하면, 어트랙터(attractor) 모듈이 이 임베딩의 고정점을 반복 풀이로 찾아낸다. 고정점에서는 추가 반복을 해도 출력이 변하지 않으므로, 기울기는 암묵적 미분(implicit differentiation)으로 고정점 방정식을 한 번만 풀어 얻을 수 있어 역전파 경로가 반복 횟수와 무관해진다.

**무엇이 새로운가?**

- 루프 연산을 명시적 순환이 아닌 고정점 탐색 문제로 재정식화하여, 훈련 메모리가 유효 깊이와 무관하게 일정하도록 구조화한 최초의 언어 모델 아키텍처
- 암묵적 미분을 통한 기울기 계산: 역방향 패스가 반복 횟수에 비례하지 않아 역전파 불안정성이 없음
- 수렴 조건에 따라 반복 횟수를 적응적으로 결정하는 가변 깊이(adaptive depth) 추론
- **균형 내면화(equilibrium internalization)**: 고정점 훈련의 부산물로 모델의 초기 출력 임베딩이 자연스럽게 균형점 근처에 놓이게 되어, 추론 시 어트랙터 모듈을 제거해도 성능 저하가 거의 없는 현상
- 770M 어트랙터 모델이 2배 더 많은 토큰으로 학습된 1.3B 트랜스포머를 능가하는 파라미터 효율

**어떻게 작동하는가?**

1. **백본 처리**: 입력 토큰 시퀀스를 비재귀적(non-recurrent) 트랜스포머 백본에 통과시켜 초기 출력 임베딩 제안(proposal) `z⁰`을 생성한다.
2. **고정점 탐색**: 어트랙터 모듈 `f`가 `z = f(z, x)` 형태의 고정점 방정식을 반복 풀이한다. 즉, 현재 임베딩을 입력과 결합해 새로운 임베딩을 생성하는 과정을 `z`가 수렴할 때까지 반복한다.
3. **적응적 중단**: 연속된 반복 간 변화량이 특정 기준치 이하로 떨어지면 반복을 멈추어, 쉬운 예제는 적은 반복으로, 어려운 예제는 더 많은 반복으로 처리한다.
4. **암묵적 미분**: 학습 시 고정점 조건 `z* = f(z*, x)`를 이용해 기울기를 수치적으로 직접 구한다. 구체적으로, `(I - ∂f/∂z)ᵀ`을 선형 풀이기로 푸는 한 번의 연산으로 역전파를 대체하므로, 실제 반복 횟수와 무관하게 메모리가 일정하다.
5. **디코딩**: 수렴된 균형 임베딩(equilibrium embedding) `z*`를 표준 언어 모델 헤드에 통과시켜 최종 토큰 분포를 생성한다.

**강점**

- **메모리 효율**: 훈련 메모리가 반복 횟수에 비례하지 않아, 루프 깊이를 크게 키워도 GPU 메모리 부담이 없음
- **훈련 안정성**: 암묵적 미분은 기울기 소실/폭발 문제를 구조적으로 방지함
- **파라미터 효율**: 더 적은 파라미터로 더 큰 모델에 필적하는 성능
- **적응적 계산**: 입력 난이도에 따라 자동으로 연산량을 조절
- **추론 경량화**: 균형 내면화 덕분에 어트랙터 모듈을 추론 시 생략 가능, 표준 트랜스포머처럼 빠르게 실행 가능
- **구조화된 추론**: 27M 파라미터 모델이 1000개의 예시만으로 프런티어 LLM이 실패하는 Sudoku-Extreme(91.4%)과 Maze-Hard(93.1%)를 해결

**한계**

- 어트랙터 모듈의 고정점 수렴이 항상 보장되지 않으며, 특정 입력에서 진동하거나 느리게 수렴할 가능성 존재
- 암묵적 미분을 위한 선형 풀이기 실행이 추가적인 연산 오버헤드를 발생시킴
- 구조화된 추론(Sudoku, 미로) 벤치마크 중심의 평가로, 자연어 생성이나 대화 등 다양한 실제 태스크에서의 성능 검증 부족
- 백본과 어트랙터 두 모듈의 하이퍼파라미터 조정이 표준 트랜스포머보다 복잡
- 대규모 학습(수백억 토큰 이상)에서의 장기 안정성과 스케일링 법칙이 아직 충분히 연구되지 않음

**알아둘 용어**

- **고정점(Fixed Point)**: 함수 `f`에 대해 `f(z) = z`를 만족하는 점. 어트랙터 모델은 이 방정식의 해 `z*`를 출력 임베딩으로 사용한다.
- **암묵적 미분(Implicit Differentiation)**: 방정식으로 암시적으로 정의된 함수의 기울기를 역방향 패스 없이 수치적으로 구하는 기법.
- **루프 트랜스포머(Looped Transformer)**: 동일한 레이어 블록을 K번 반복 실행하여 파라미터 수를 고정한 채 유효 깊이를 늘리는 아키텍처.
- **균형 내면화(Equilibrium Internalization)**: 고정점 훈련의 결과로 모델의 초기 제안 `z⁰`이 자연스럽게 균형점에 가깝게 학습되는 현상.
- **유효 깊이(Effective Depth)**: 파라미터 수가 동일할 때 실제로 수행되는 연산 레이어의 총 횟수.
- **어트랙터(Attractor)**: 동역학 시스템에서 시간이 지남에 따라 계가 수렴하는 상태나 경로. 이 논문에서는 모델의 반복 연산이 수렴하는 임베딩을 의미.
- **퍼플렉시티(Perplexity)**: 언어 모델의 예측 불확실성을 나타내는 지표로, 낮을수록 더 좋은 모델.

**왜 주목할 만한가?**

루프 언어 모델은 "같은 파라미터로 더 깊이 생각하는" 아이디어로 오래전부터 주목받았지만, 훈련 불안정성과 메모리 폭증 문제로 실용화가 어려웠다. Attractor Models는 이 두 장벽을 고정점 이론과 암묵적 미분이라는 수학적 도구로 우아하게 해결한다. 특히 27M 소형 모델이 GPT o3 같은 대형 모델이 실패하는 논리 퍼즐을 거의 완벽하게 풀어낸다는 결과는, 크기가 아닌 계산 방식이 추론 성능의 핵심일 수 있다는 가능성을 보여준다.

---

## English Summary

**One-line summary**

Attractor Models reframe looped Transformer computation as a fixed-point problem solved with implicit differentiation, achieving constant training memory regardless of effective depth, a 46.6% perplexity improvement over standard Transformers, and near-perfect performance on hard reasoning puzzles that defeat GPT o3 and Claude.

**Core idea**

Looped Transformers repeat the same layer block multiple times to get deeper computation without adding parameters — but existing approaches must store hidden states or KV caches across every iteration, so memory grows linearly with depth, and gradients are unstable over long loops. Attractor Models change the formulation entirely: a non-recurrent backbone first produces a rough output embedding, then an attractor module refines it by solving the fixed-point equation `z = f(z, x)` until `z` converges. Because the gradient at convergence comes from the fixed-point condition via implicit differentiation — a single linear solve of `(I - ∂f/∂z)ᵀ` — backpropagation does not need to unroll through iterations at all, keeping training memory constant and gradients well-behaved.

**What is new?**

- First language model architecture to treat recurrent depth as a fixed-point problem, making training memory independent of effective depth via implicit differentiation
- Adaptive iteration depth at inference: the model runs until convergence rather than a fixed number of steps, automatically allocating more compute to harder inputs
- **Equilibrium internalization**: as a side effect of fixed-point training, the backbone learns to place its initial proposal near the fixed point, so the attractor module can be dropped at inference with minimal quality loss
- 770M Attractor Model outperforms a 1.3B Transformer trained on twice as many tokens
- 27M-parameter model achieves 91.4% on Sudoku-Extreme and 93.1% on Maze-Hard with ~1000 training examples, while frontier models like Claude and GPT o3 fail completely on these tasks

**How does it work?**

1. **Backbone pass**: The input token sequence goes through a standard non-recurrent Transformer backbone that produces an initial output embedding proposal `z⁰`.
2. **Fixed-point iteration**: The attractor module `f` repeatedly applies `z ← f(z, x)`, where `x` is the backbone's contextual representation. This refines the embedding until `z` stops changing significantly.
3. **Adaptive stopping**: Iteration halts when the change between steps falls below a threshold, so easy inputs converge quickly and hard ones get more iterations automatically.
4. **Implicit differentiation**: For backpropagation, instead of unrolling through all iterations, the gradient at the fixed point `z*` is computed by solving the linear system `(I - ∂f/∂z*)ᵀ · v = ∂L/∂z*` once. This replaces the backward pass entirely, so memory and gradient stability are independent of iteration count.
5. **Decoding**: The converged equilibrium embedding `z*` is passed to a standard language model head to produce the final token distribution.

**Strengths**

- **Constant training memory**: No need to store intermediate states across iterations, enabling deeper effective computation without GPU memory blowup
- **Stable gradients**: Implicit differentiation avoids vanishing/exploding gradients that plague long unrolled recurrences
- **Parameter efficiency**: Significantly fewer parameters needed to match or exceed larger standard Transformers
- **Compute-adaptive inference**: Hard inputs automatically receive more compute steps, easy ones less
- **Inference portability**: Equilibrium internalization means the attractor module can be removed at inference, running as fast as a normal Transformer
- **Strong structured reasoning**: Tiny models solve combinatorial puzzles where much larger frontier models fail

**Limitations**

- Fixed-point convergence is not always guaranteed; some inputs may cause slow convergence or oscillation
- Implicit differentiation requires solving a linear system at each backward pass, adding computational overhead
- Evaluation is strongest on structured reasoning benchmarks (Sudoku, mazes); broader language tasks and real-world applications need more evidence
- Two-module architecture (backbone + attractor) introduces additional hyperparameters compared to a standard Transformer
- Long-run scaling behavior beyond a few hundred million parameters and trillions of tokens is not yet established

**Terms to know**

- **Fixed point**: A point `z*` where `f(z*) = z*`; the model's iteration converges to this equilibrium embedding.
- **Implicit differentiation**: A technique to compute gradients of functions defined implicitly by equations, without unrolling the iterative computation that produced them.
- **Looped Transformer**: An architecture that applies the same Transformer block K times, gaining computational depth without extra parameters.
- **Equilibrium internalization**: The observed phenomenon where fixed-point training causes the backbone's initial proposal to sit near the fixed point naturally, making the attractor module optional at test time.
- **Effective depth**: The total number of layer applications when accounting for loops or iterations, as distinct from the number of unique learned layers.
- **Attractor**: In dynamical systems, a state or set toward which a system evolves; here, the converged output embedding the attractor module produces.
- **Pareto improvement**: An outcome that is better on one axis (e.g., perplexity) without being worse on others (e.g., training cost), indicating a genuinely superior operating point.

**Why it is worth watching**

The looped-Transformer idea has long promised "think more deeply with the same parameters," but practical obstacles — instability, memory cost, fixed iteration count — have blocked adoption. Attractor Models clear those hurdles with a mathematically principled solution borrowed from fixed-point theory. The result that a 27M-parameter model with a thousand examples can solve logic puzzles that defeat frontier models points to a key insight: for structured reasoning, the architecture of computation may matter more than raw scale. If these gains hold up at scale and across more diverse tasks, Attractor Models could influence how the next generation of reasoning-focused language models are built.

**My take**

이 논문은 언어 모델의 반복 연산을 고정점 문제로 재해석함으로써, 루프 아키텍처의 근본적인 두 가지 장벽(메모리, 불안정성)을 한꺼번에 해결하는 수학적으로 우아한 접근을 보여준다. 소형 모델의 추론 결과가 특히 놀랍지만, 자연어 생성과 대규모 학습에서도 동일한 이점이 유지되는지 더 광범위한 검증이 필요하다.

This paper offers a mathematically elegant solution to two fundamental problems of looped architectures — memory and instability — by reframing them as a fixed-point problem. The reasoning results with tiny models are striking, but broader validation on natural language generation and large-scale training is needed before the approach can be considered production-ready.
