---
title: "The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm"
date: 2026-05-04
topic: AI
tags: [AI, optimization, training, Muon, polar-decomposition, matrix-sign, numerical-methods, LLM-training]
source: https://arxiv.org/abs/2505.16932
---

The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm

* Date: 2026-05-04
* Source: https://arxiv.org/abs/2505.16932
* Topic: AI / Training & Optimization
* Why it matters: The Muon optimizer is emerging as a leading alternative to Adam for large-scale LLM training, cutting training costs roughly in half. Its performance depends entirely on efficiently computing the polar decomposition of gradient matrices. This paper derives theoretically optimal iterations for that computation and shows a clear reduction in training loss for GPT-scale models—earning an ICLR 2026 Honorable Mention.

## Korean Summary

**한줄 요약**

LLM 학습에서 Adam의 유력한 대안으로 부상한 Muon 옵티마이저의 핵심 연산인 극분해(polar decomposition)를 최적화하는 새로운 알고리즘 "Polar Express"를 제안한다. 각 반복에서 미니맥스(minimax) 최적화 문제를 풀어 업데이트 규칙을 적응적으로 결정함으로써, Newton–Schulz 대비 약 2.5배 빠른 수렴과 bfloat16 안정성을 달성한다. GPT-Large 기준 검증 손실이 AdamW(4.172) 및 기존 Newton–Schulz(3.398)보다 낮은 3.340을 기록한다.

**핵심 아이디어**

Muon 옵티마이저는 파라미터 행렬을 그레이디언트가 아닌 "그레이디언트 모멘텀에 가장 가까운 반직교 행렬 방향"으로 업데이트한다. 이 반직교 행렬을 구하려면 극분해(G = U · P, U는 직교 인수)의 직교 인수 U가 필요한데, 기존 Newton–Schulz 방법은 계수가 고정된 다항식 반복을 사용해 수렴에 최대 20번의 반복(행렬-행렬 곱 40회)이 필요하다. Polar Express는 각 반복마다 계수를 미니맥스 최적화로 결정해 초기 수렴과 점근적 수렴 모두 최적임을 이론적으로 보장하며, 8번의 반복(행렬-행렬 곱 24회)으로 기계 정밀도에 도달한다.

**무엇이 새로운가?**

- **반복 적응형 다항식 계수**: Newton–Schulz의 고정 계수 대신, 각 반복 단계에서 미니맥스 문제를 풀어 그 단계에서 가장 오류를 최소화하는 계수를 선택
- **이론적 최적성 증명**: Chen & Chow, Nakatsukasa & Freund의 근사 이론을 토대로 Polar Express가 조기 수렴과 점근적 수렴 모두에서 가능한 최속임을 증명
- **수렴 속도 향상**: Newton–Schulz 대비 약 2.5배 빠른 수렴(8 vs 20 반복, 24 vs 40 행렬 곱)
- **bfloat16 안정성**: 현대 GPU 학습 환경의 혼합 정밀도(bfloat16)에서도 수치적으로 안정하게 작동
- **순수 행렬-행렬 곱 구현**: 별도의 CUDA 커널 없이 GEMM만으로 구현 가능해 어떤 하드웨어에서도 효율적

**어떻게 작동하는가?**

1. **Muon 학습 루프**: 각 스텝에서 가중치 행렬의 그레이디언트 모멘텀 G가 주어지면 직교 인수 U를 구해야 함
2. **행렬 부호 함수 연결**: 극분해의 직교 인수를 구하는 것은 행렬 부호 함수(sign function) 계산과 수학적으로 동치
3. **Polar Express 반복**: 초기 추정값 X₀에서 시작해, 각 반복에서 미니맥스 문제 argmin_{a,b} max_{σ∈[σ_min, 1]} |error(a, b, σ)|를 풀어 최적 계수 (a, b)를 결정
4. **σ_min 활용**: 최소 특이값 σ_min의 추정값으로 ℓ을 설정하면, 해당 반복에서 다른 어떤 다항식 방법보다 오류가 작음이 보장됨
5. **조기 종료**: 5~11번의 반복으로 충분한 정밀도에 도달하므로, 실제 학습에서는 5회 반복을 사용
6. **Muon 업데이트**: 구한 U를 사용해 θ ← θ − η · U (학습률 × 직교 인수) 형태로 가중치 갱신

**강점**

- 이론적으로 최적임이 증명된 알고리즘—임의의 다항식 방법 중 최선
- Newton–Schulz 대비 약 2.5배 빠른 수렴으로 Muon의 연산 비용 추가 절감
- GPT-Large 기준 기존 Newton–Schulz보다 낮은 검증 손실(3.340 vs 3.398) 달성
- AdamW 대비 큰 폭의 성능 개선(3.340 vs 4.172)
- 행렬-행렬 곱만 사용해 H100 등 현대 GPU에 즉시 최적화됨
- bfloat16 혼합 정밀도에서 수치 안정성 확보
- ICLR 2026 Honorable Mention으로 동료 검토를 통한 신뢰성 확인

**한계**

- 실제 학습 손실 개선 폭이 "경우에 따라 미미했다"는 ICLR 리뷰어 지적—이론적 우수성이 항상 대폭적인 실증 개선으로 이어지지는 않음
- σ_min 추정의 정확도에 따라 수렴 품질이 달라질 수 있으며, σ_min 추정 자체에 별도 비용 발생 가능
- 실험이 GPT-2 아키텍처와 FineWeb 데이터셋에 한정—다른 아키텍처(Mamba, Transformer-MoE 등)에서의 효과는 미검증
- Muon 자체가 아직 Adam만큼 생태계 지원이 갖춰지지 않아, Polar Express의 이점을 누리려면 Muon 채택이 전제
- 최소 특이값 ℓ 파라미터를 직접 설정하거나 추정해야 하는 실용적 복잡성 존재

**알아둘 용어**

- **Muon (MomentUm Orthogonalized by Newton-Schulz)**: 가중치 행렬을 그레이디언트 모멘텀의 극분해를 이용해 업데이트하는 옵티마이저; 2024년 말 Keller Jordan이 제안하며 Adam 이후 가장 주목받는 최적화 알고리즘으로 부상
- **극분해 (Polar Decomposition)**: 행렬 G = U · P 로 분해하는 과정(U: 직교 행렬, P: 양의 반정치 행렬); 기하학적으로 U는 G에 가장 가까운 직교 행렬
- **행렬 부호 함수 (Matrix Sign Function)**: 행렬의 고유값을 부호(±1)로 대체하는 함수; 극분해의 직교 인수와 수학적으로 동치
- **Newton–Schulz 반복 (Newton–Schulz Iteration)**: 극분해를 계산하는 고전적 다항식 반복법; 각 반복이 행렬-행렬 곱으로만 구성되어 GPU에 적합하지만 계수가 고정
- **미니맥스 최적화 (Minimax Optimization)**: 최악의 경우 오류를 최소화하는 계수를 찾는 최적화 문제; 각 반복 단계에서 최적 다항식 계수를 유도하는 데 사용
- **특이값 (Singular Value)**: 행렬이 입력 벡터를 얼마나 늘리는지 나타내는 값; 최소 특이값 σ_min이 Polar Express의 수렴 속도에 중요
- **bfloat16**: 16비트 부동소수점 형식으로 현대 GPU 학습에 표준적으로 사용; 정밀도가 낮아 수치 불안정 문제가 생기기 쉬움

**왜 주목할 만한가?**

Muon은 GPT-5, Deepseek 등 최근 대형 언어 모델 학습에 실제로 채택될 만큼 실용성이 검증된 옵티마이저다. 그런데 Muon의 핵심 연산인 극분해가 뉴턴–슐츠 반복에 의존하고 있었고, 그 반복의 계수가 이론적으로 최적인지 여부는 미지수였다. Polar Express는 이 질문에 "아니오"라고 답하며, 적응형 미니맥스 계수를 통해 이론적으로 최적의 수렴을 달성한다. ICLR 2026 Honorable Mention은 이 연구의 수학적 엄밀성과 실용적 의의를 동시에 인정한 결과다.

---

## English Summary

**One-line summary**

The Muon optimizer for LLM training depends on computing the polar decomposition of gradient matrices at every step—Polar Express derives theoretically optimal polynomial iterations for this computation, converging ~2.5× faster than the standard Newton–Schulz method and improving GPT-Large validation loss from 3.398 to 3.340, earning an ICLR 2026 Honorable Mention.

**Core idea**

Muon (MomentUm Orthogonalized by Newton-Schulz) updates weight matrices in the direction of the orthogonal polar factor of the gradient momentum—the closest semi-orthogonal matrix to the current gradient—rather than the gradient itself. Computing this polar factor iteratively via matrix-matrix products (Newton–Schulz) is GPU-friendly, but the standard approach uses fixed polynomial coefficients that are not provably optimal. Polar Express solves a minimax optimization problem at each iteration to find the polynomial coefficients that minimize worst-case error at that step, yielding a method that is provably optimal in both early and asymptotic convergence. The result is machine-accuracy convergence in ~8 iterations (24 matrix products) versus ~20 iterations (40 matrix products) for Newton–Schulz, while remaining numerically stable in bfloat16.

**What is new?**

- **Adaptive polynomial coefficients**: Rather than fixed coefficients, each iteration solves a minimax problem to select the coefficient pair that minimizes worst-case approximation error at that step
- **Provable optimality**: Drawing on approximation theory from Chen & Chow and Nakatsukasa & Freund, the paper proves Polar Express is the fastest possible polynomial method from any starting point, both early on and asymptotically
- **~2.5× convergence speedup**: Reaches machine accuracy in ~8 iterations (24 matrix multiplications) vs Newton–Schulz's ~20 iterations (40 matrix multiplications)
- **bfloat16 stability**: Explicitly addresses and verifies numerical stability in the 16-bit mixed precision format standard in modern GPU training
- **Pure GEMM implementation**: Requires only matrix-matrix multiplications with no custom CUDA kernels, making it immediately portable to any hardware

**How does it work?**

1. **Muon training step**: At each optimizer step, the weight matrix's gradient momentum G must be orthogonalized—the orthogonal polar factor U of G is needed.
2. **Polar decomposition link**: Computing U is mathematically equivalent to computing the matrix sign function of a related augmented matrix; both reduce to an iterative polynomial problem.
3. **Minimax coefficient selection**: Starting from an initial approximation X₀, each Polar Express iteration solves argmin_{a,b} max_{σ∈[ℓ,1]} |error(a, b, σ)| to find the optimal degree-3 polynomial coefficients (a, b) for that iteration.
4. **σ_min conditioning**: Setting the lower spectral bound ℓ ≈ σ_min (smallest singular value) ensures the iteration dominates all other degree-3 polynomial methods at every step.
5. **Early stopping**: 5–11 iterations suffice for high-quality approximation in practice; experiments use 5 iterations per optimizer step.
6. **Weight update**: The resulting U replaces Newton–Schulz's output as the update direction: θ ← θ − η · U.

**Strengths**

- Theoretically optimal: proven best possible convergence among all polynomial methods using only matrix products
- ~2.5× convergence speedup over Newton–Schulz cuts Muon's computational overhead further
- Better validation loss on GPT-Large: 3.340 vs 3.398 (Jordan NS), 3.400 (You), 4.172 (AdamW)
- Consistent gains across varied learning rates on FineWeb with 1–10B tokens
- Pure GEMM implementation: works natively on H100s and any GPU with optimized matrix multiplication
- Numerically stable in bfloat16 mixed precision
- ICLR 2026 Honorable Mention provides peer-reviewed validation of both theory and practice

**Limitations**

- Empirical improvements were sometimes modest, as noted by ICLR reviewers—theory does not always translate to large practical gains
- Optimal performance requires a good estimate of σ_min (the smallest singular value), which may itself require overhead in some settings
- Experiments limited to GPT-2 architecture and FineWeb; generalization to other architectures (Mamba, MoE, state-space models) untested
- Polar Express's benefits are downstream of Muon adoption, which has less ecosystem support than Adam
- The per-iteration minimax coefficient computation adds minor overhead over fixed-coefficient methods, though it is theoretically bounded and fast in practice

**Terms to know**

- **Muon (MomentUm Orthogonalized by Newton-Schulz)**: An optimizer for matrix-weight layers introduced by Keller Jordan in late 2024; steps in the direction of the closest semi-orthogonal matrix to the gradient momentum rather than the gradient itself, proven competitive with or superior to AdamW at LLM training scale
- **Polar decomposition**: The factorization G = U · P where U is orthogonal (unitary) and P is positive semidefinite; U is the closest orthogonal matrix to G and is the quantity Muon needs
- **Matrix sign function**: A function that maps each eigenvalue of a matrix to its sign (±1); mathematically equivalent to the polar factor for Muon's purposes
- **Newton–Schulz iteration**: The classical polynomial method for polar decomposition using only matrix-matrix products; GPU-friendly but uses fixed coefficients
- **Minimax optimization**: Finding coefficients that minimize the maximum possible error over a range of inputs; guarantees worst-case optimality at each iteration step
- **Singular value / σ_min**: Scalar values measuring how much a matrix stretches input vectors; the smallest singular value σ_min controls the hardest case for the polar decomposition approximation
- **bfloat16**: A 16-bit floating point format (Brain Float 16) used in modern GPU training for memory and compute efficiency; lower precision makes numerical stability of iterative algorithms non-trivial

**Why it is worth watching**

The Muon optimizer is no longer a research novelty—it has been used to train production-scale LLMs including the Moonlight model (3B/16B MoE on 5.7T tokens), and is increasingly positioned as a drop-in replacement for AdamW. The polar decomposition is Muon's computational bottleneck, yet the choice of how to compute it had been driven by heuristics rather than theory. Polar Express closes that gap: by proving optimality from first principles and delivering it in a practical, bfloat16-stable, GEMM-only implementation, it gives Muon practitioners a clear upgrade path. The ICLR 2026 Honorable Mention is a signal that the research community considers both the mathematical contribution and its engineering relevance significant.

**My take**

이론적 최적성과 실용적 적용을 깔끔하게 연결한 논문이다. Newton–Schulz가 "작동하기는 하지만 최적이 아니다"라는 문제를 수학적으로 해결한 것은 명확한 기여지만, ICLR 리뷰어들도 지적했듯 실제 학습에서 개선 폭이 항상 극적이지는 않다. 다만 이 연구의 진정한 가치는 성능 숫자보다 방법론에 있다—극분해를 미니맥스 최적화 문제로 바라보는 관점은, 향후 더 복잡한 행렬 연산이 옵티마이저의 핵심 서브루틴이 될 때 동일한 원리가 반복 적용될 수 있는 프레임워크를 제공한다.

Polar Express is a clean example of applying rigorous numerical analysis to an emerging engineering problem. The theoretical optimality result is genuine, the implementation is practical, and the ICLR Honorable Mention reflects that the community recognized the importance of the contribution beyond just its empirical numbers. The caveat is that "sometimes modest" improvements in training loss may not move the needle for every practitioner. The broader relevance depends on how central Muon becomes: if Muon displaces Adam as the default LLM optimizer, then having a provably optimal polar decomposition routine becomes a meaningful piece of the training stack.
