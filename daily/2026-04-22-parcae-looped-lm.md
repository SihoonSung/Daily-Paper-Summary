---
title: "Parcae: Scaling Laws For Stable Looped Language Models"
date: 2026-04-22
topic: AI
tags: [AI, LLM, architecture, efficiency, scaling-laws, looped-models, dynamical-systems]
source: https://arxiv.org/abs/2604.12946
---

# Parcae: Scaling Laws For Stable Looped Language Models

* Date: 2026-04-14
* Source: https://arxiv.org/abs/2604.12946
* Topic: AI
* Why it matters: Looped language models can multiply effective compute without multiplying parameters, but prior approaches suffered from training instability; Parcae solves this with a principled dynamical-systems fix and establishes the first predictive scaling laws for looped architectures.

## Korean Summary

**한줄 요약**

Parcae는 트랜스포머 레이어를 반복 순환하는 언어 모델의 훈련 불안정성을 제어 이론 기반의 음수 대각 파라미터화(negative diagonal parameterization)로 해결하고, 순환 횟수와 학습 토큰 수의 최적 조합을 예측하는 최초의 루프 스케일링 법칙을 도출한다. 770M 파라미터 Parcae 모델이 1.3B 파라미터 트랜스포머에 필적하는 성능을 달성한다.

**핵심 아이디어**

루프 언어 모델(looped LM)은 동일한 레이어 블록을 여러 번 반복 실행하여 파라미터 수는 유지하면서 연산량을 늘리는 방식이다. 이론적으로는 매력적이나, 기존 구현은 잔차 폭발(residual explosion)과 손실 스파이크(loss spike)로 안정적인 대규모 훈련이 어려웠다. Parcae는 루프 과정을 비선형 시변 동역학 시스템(nonlinear time-variant dynamical system)으로 재해석하고, 불안정성의 원인이 주입 파라미터(injection parameter)의 큰 스펙트럼 노름(spectral norm)에 있음을 밝혀낸다. 이를 해결하기 위해 항상 음수를 유지하는 대각 행렬 파라미터화를 적용해 스펙트럼 노름을 구조적으로 1 미만으로 제한한다.

**무엇이 새로운가?**

- 루프 아키텍처의 불안정성을 동역학 시스템 이론으로 엄밀하게 분석하고, 원인을 스펙트럼 노름으로 특정한 최초 연구
- 스펙트럼 제약을 구조적으로 보장하는 음수 대각 파라미터화(A := Diag(−exp(log A))) 도입
- 루프 아키텍처에 대한 최초의 스케일링 법칙: 최적 평균 순환 횟수는 C^0.40, 최적 토큰 수는 C^0.78로 스케일
- Prelude-Recurrent-Coda(P-R-C)의 3단계 미들-루프(middle-looped) 설계
- 140M~1.3B 파라미터 규모의 모델과 Hugging Face 공개 릴리스

**어떻게 작동하는가?**

1. **아키텍처 구성**: 모델을 세 블록으로 나눈다. Prelude(P)가 입력 시퀀스를 잠재 상태 e로 임베딩하고, Recurrent block(R)이 T번 반복 실행하면서 매 순환마다 e를 주입해 은닉 상태 h_t를 갱신하며, Coda(C)가 최종 h_T를 출력으로 변환한다.
2. **불안정성 분석**: 루프를 선형 동역학 시스템으로 모델링하면, 스펙트럼 노름 ρ(Ā) < 1일 때 안정, ≥ 1일 때 불안정해진다. 기존 루프 모델은 이 조건을 강제하지 않아 훈련 중 폭발이 발생했다.
3. **음수 대각 파라미터화**: 연속 시간 행렬 A를 Diag(−exp(log A))로 정의한다. 지수 함수 앞에 음수 부호가 있으므로 모든 대각 원소는 항상 음수이고, 이로부터 스펙트럼 노름 < 1이 구조적으로 보장된다.
4. **이산화**: 학습 가능한 스텝 크기와 ZOH(zero-order hold) 또는 오일러 이산화 기법을 적용해 연속 파라미터화를 실제 훈련에 활용한다.
5. **스케일링 법칙 도출**: 다양한 FLOP 예산에서 순환 횟수와 토큰 수를 체계적으로 실험하여 멱함수 스케일링 법칙을 도출, 주어진 예산에서 최적 구성을 사전 예측할 수 있게 한다.

**강점**

- 770M 모델이 1.3B 트랜스포머에 필적: 동일 성능을 약 절반의 파라미터로 달성
- RDM(파라미터·데이터 대비 기준 순환 심층 모델) 대비 검증 퍼플렉시티 최대 6.3% 감소
- 스케일링 법칙을 통해 훈련 전 최적 구성 예측 가능 — 탐색 비용 절감
- 140M~1.3B까지 일관된 성능 향상 확인
- 테스트 시 순환 횟수를 늘려 추가 연산 투입 가능(추론 시 스케일링)
- 모델 및 코드 공개(Hugging Face, GitHub)

**한계**

- 테스트 시 추가 순환은 훈련 시 사용한 평균 순환 횟수 부근에서 이득이 포화됨
- 안정적 훈련을 위해 음수 대각 파라미터화 외에도 여러 추가 기법이 필요
- 현재 언어 모델링 태스크 중심으로 평가되어, 코드·수학·멀티모달 등 다른 도메인에서의 성능 검증이 추가로 필요
- 루프 과정의 반복 연산으로 인해 동일 FLOP 대비 메모리 접근 패턴이 표준 트랜스포머와 다를 수 있어 하드웨어 최적화 연구가 필요

**알아둘 용어**

- **루프 언어 모델(Looped LM)**: 동일한 레이어 블록을 여러 번 반복 실행하여 파라미터 수 증가 없이 연산량을 늘리는 모델
- **잔차 폭발(Residual Explosion)**: 반복 순환 시 잔차 스트림 값이 기하급수적으로 커지는 훈련 불안정 현상
- **스펙트럼 노름(Spectral Norm)**: 행렬의 최대 특이값; 동역학 시스템의 안정성을 결정하는 핵심 지표
- **음수 대각 파라미터화(Negative Diagonal Parameterization)**: 모든 대각 원소가 음수임을 보장하는 행렬 파라미터화 기법
- **ZOH(Zero-Order Hold) 이산화**: 연속 시간 동역학 시스템을 이산 시간으로 변환하는 표준 기법
- **스케일링 법칙(Scaling Laws)**: 모델 크기, 데이터, 연산량 간의 성능 관계를 예측하는 멱함수 법칙
- **퍼플렉시티(Perplexity, PPL)**: 언어 모델이 텍스트를 얼마나 잘 예측하는지를 나타내는 지표; 낮을수록 좋음

**왜 주목할 만한가?**

파라미터 효율은 대규모 언어 모델 훈련 및 배포 비용을 결정하는 핵심 요소다. Parcae는 루프 아키텍처의 고질적 훈련 불안정 문제를 이론적으로 해결하고, 최적 훈련 구성을 예측하는 스케일링 법칙을 최초로 제시함으로써 파라미터 효율적인 모델 설계의 현실적 경로를 열었다. 파라미터 절반으로 동급 트랜스포머에 필적하는 성능은 훈련·배포 비용 모두에서 실질적 의미를 가진다.

---

## English Summary

**One-line summary**

Parcae introduces a stable looped language model architecture that uses a negative diagonal parameterization — grounded in dynamical systems theory — to guarantee training stability, and derives the first predictive scaling laws for looped models, enabling a 770M parameter model to match the quality of a 1.3B parameter transformer.

**Core idea**

Looped language models pass activations through the same block of transformer layers repeatedly, multiplying effective compute without multiplying parameters. Prior attempts at this idea suffered from residual explosion and loss spikes because they did not enforce the spectral norm constraint needed for a stable dynamical system. Parcae reframes looping as a nonlinear time-variant dynamical system over the residual stream, identifies large spectral norms in the injection parameters as the root cause of instability, and solves it by construction: a negative diagonal parameterization ensures the spectral norm stays below 1 throughout training. The paper then derives the first scaling laws for looped architectures, enabling principled selection of optimal loop counts and training token budgets for any compute budget.

**What is new?**

- First rigorous dynamical-systems analysis of looped LM instability, tracing the cause to spectral norm violations in injection parameters
- Negative diagonal parameterization (A := Diag(−exp(log A))) that guarantees spectral norm < 1 by construction, eliminating residual explosion
- First scaling laws for looped LMs: optimal mean recurrence scales as C^0.40 and optimal training tokens scale as C^0.78
- Middle-looped Prelude–Recurrent–Coda (P-R-C) architecture with per-iteration input injection
- Public model releases (Parcae-140M, 370M, 770M, 1.3B) trained on FineWeb-Edu, available on Hugging Face

**How does it work?**

1. **Architecture**: The model is split into three blocks. The Prelude (P) embeds the input sequence into a latent state e. The Recurrent block (R) runs T times, injecting e at each iteration to update hidden state h_t. The Coda (C) maps the final h_T to output logits.
2. **Stability analysis**: Modeling the loop as a linear dynamical system shows that stability requires the spectral norm ρ(Ā) < 1. Prior looped models did not enforce this, causing divergence during training.
3. **Negative diagonal parameterization**: The continuous matrix A is defined as Diag(−exp(log A)), where log A is a learnable vector. Because −exp(·) is always negative, all diagonal entries are always negative, which guarantees spectral norm < 1 by construction — no special regularization needed.
4. **Discretization**: A learned step size combined with standard zero-order hold (ZOH) or Euler discretization converts the continuous parameterization into a practical recurrence update rule.
5. **Scaling law derivation**: The authors systematically vary loop counts and token budgets across FLOP budgets, fit power-law curves, and arrive at closed-form predictions for compute-optimal training configurations.

**Strengths**

- 770M Parcae matches a 1.3B transformer — roughly half the parameters for equivalent downstream quality
- Up to 6.3% validation perplexity reduction over parameter- and data-matched recurrent deep models (RDMs)
- First scaling laws for looped architectures allow compute-optimal planning without exhaustive search
- Consistent gains across 140M to 1.3B scale
- Test-time looping provides an additional compute scaling axis at inference
- Code and models are publicly released (Hugging Face, GitHub)

**Limitations**

- Test-time compute scaling saturates near the mean recurrence used during training, limiting how much extra inference compute helps
- Stable training requires several additional techniques beyond the core negative diagonal parameterization
- Evaluations focus on language modeling; generalization to code, math, or multimodal tasks needs further study
- Repeated passes through the same layers may create hardware utilization patterns that differ from standard transformers, potentially requiring custom kernels for peak efficiency

**Terms to know**

- **Looped language model**: A model that passes activations through the same layer block multiple times, increasing effective compute without adding parameters
- **Residual explosion**: A training failure mode where residual stream values grow exponentially across loop iterations
- **Spectral norm**: The largest singular value of a matrix; the key quantity governing stability of linear dynamical systems
- **Negative diagonal parameterization**: A matrix construction where all diagonal entries are forced to be negative, guaranteeing spectral norm below 1
- **Zero-order hold (ZOH)**: A standard method for discretizing continuous-time dynamical systems
- **Scaling laws**: Power-law relationships between compute, data, and model size that predict optimal training configurations
- **Perplexity (PPL)**: A measure of how well a language model predicts text; lower is better

**Why it is worth watching**

Parameter efficiency is one of the most practical levers for reducing the cost of training and deploying large language models. Parcae resolves the long-standing training instability of looped architectures with a theoretically grounded fix, and introduces the first scaling laws that tell practitioners exactly how to trade loop depth against training data for a given compute budget. Achieving transformer-level quality at roughly half the parameter count is a meaningful advance for both research and production deployment.

**My take**

**[Korean]** Parcae는 기존 루프 모델의 불안정성 문제를 추측이나 경험적 트릭이 아닌 동역학 시스템 이론으로 정면 해결한다는 점에서 방법론적으로 탄탄하다. 스케일링 법칙의 도출은 연구 재현성과 실용적 활용 모두에 도움이 된다. 다만 언어 모델링 외 도메인 검증과 하드웨어 수준의 효율성 분석이 추가로 이루어져야 실제 채택 여부를 판단할 수 있다.

**[English]** Parcae addresses looped model instability not with empirical tricks but with a principled fix rooted in control theory — a methodologically strong approach. The derived scaling laws are a genuine contribution that will help both researchers and practitioners plan looped model training more efficiently. The remaining open questions around non-language domains and hardware-level efficiency are reasonable next steps, not fundamental barriers.
