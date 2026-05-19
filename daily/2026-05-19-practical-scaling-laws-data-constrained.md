---
title: "Practical Scaling Laws: Converting Compute into Performance in a Data-Constrained World"
date: 2026-05-19
topic: AI
tags: [AI, scaling-laws, training, data-constrained, multi-epoch, overfitting, compute-efficiency]
source: https://arxiv.org/abs/2605.09189
---

# Practical Scaling Laws: Converting Compute into Performance in a Data-Constrained World

* Date: 2026-05-09
* Source: https://arxiv.org/abs/2605.09189
* Topic: AI
* Why it matters: Chinchilla's scaling law — the formula that guides how to split compute between model size and training data — breaks down whenever data is limited or training runs for multiple epochs. This paper derives a corrected formula that works in those regimes and directly tells practitioners how to allocate compute when they cannot just collect more data.

## Korean Summary

**한줄 요약**

친칠라(Chinchilla) 스케일링 법칙은 데이터가 충분한 단일 에포크 사전학습에만 유효하며, 데이터가 제한되거나 여러 에포크를 반복하는 상황에서는 발산하거나 과적합을 표현하지 못하는 세 가지 구조적 결함이 있다. 이 논문은 L(N, D, T) = E + (L₀ - E) · h/(1+h) 형태의 새로운 폐쇄형(closed-form) 스케일링 법칙을 제안해, 모델 과소용량·학습 부족·과적합 세 항으로 손실을 분해한다. MLP, ResNet, 푸리에 신경 연산자, 트랜스포머 등 네 가지 아키텍처 군에 걸쳐 멀티-에포크 실험으로 검증되었다.

**핵심 아이디어**

친칠라 스케일링 법칙(L = E + A/N^α + B/D^β)은 현대 모델 학습의 핵심 가이드라인이지만, 원래 설계된 가정—데이터가 풍부하고 한 번만 학습하는 단일 에포크 체제—을 벗어나면 세 가지 방식으로 실패한다: (1) 유일한 데이터 D가 줄어들 때 발산하는 대신 기저 기준선(uninformed baseline)에서 포화돼야 하는데 그렇지 않음, (2) 모델 용량이 데이터를 초과할 때 발생하는 과적합을 표현하지 못함, (3) 고유 데이터 수 D와 전체 학습 샘플 수 T(반복 포함)를 동일시함. 새 공식은 이 세 가지를 모두 수정한 단일 식으로, 친칠라는 이 식의 데이터-풍부·단일 에포크 극한값에 해당한다.

**무엇이 새로운가?**

- 친칠라의 알려진 세 가지 구조적 한계를 하나의 공식으로 동시에 해결
- D(고유 데이터 수)와 T(전체 학습 스텝 수)를 명시적으로 분리해 멀티-에포크 체제를 정확히 모델링
- 손실을 과소용량(a/N^α), 학습 부족(b/T^β), 과적합(c·N^γ/D^δ) 세 항으로 분해
- 손실이 비정보 기준선 L₀와 비가역 손실 E 사이에서 포화하도록 설계
- 비전·과학적 ML·언어 등 다중 도메인과 아키텍처에서 검증

**어떻게 작동하는가?**

1. **세 항 분해**: 새 공식의 핵심 함수 h = a/N^α + b/T^β + c·N^γ/D^δ 는 세 기여분을 합산한다. a/N^α는 모델이 너무 작을 때의 손실, b/T^β는 학습이 부족할 때의 손실, c·N^γ/D^δ는 고유 데이터보다 너무 많이 반복할 때의 과적합 손실이다.
2. **포화 구조**: h → 0이면 L → E(비가역 손실, 이상적 한계), h → ∞이면 L → L₀(데이터 없이 맞출 수 있는 기준선)가 되어 물리적으로 말이 되는 경계를 갖는다.
3. **친칠라로의 환원**: 데이터가 충분하고(D >> 필요량) 단일 에포크(T ≈ D)이면 c·N^γ/D^δ ≈ 0이 되고, 공식은 표준 친칠라 식으로 환원된다.
4. **최적 배분 계산**: 공식이 확립되면, 고정된 학습 예산(FLOPs)과 제한된 데이터 D 조건에서 최적 N과 T의 조합을 수치 최적화로 찾을 수 있다.
5. **검증**: MLP, ResNet, 푸리에 신경 연산자, 트랜스포머를 포함한 네 아키텍처 군에서 멀티-에포크 실험으로 공식의 정확도를 실증했다.

**강점**

- 데이터 제한 환경(파인튜닝, 도메인 특화 모델, 과학적 ML)에서 직접 사용 가능한 실용적 공식
- 아키텍처 독립적: 언어 모델뿐 아니라 ResNet, 과학 시뮬레이션 신경 연산자 등 광범위하게 검증
- 기존 친칠라의 특수 케이스로 환원되므로 호환성 유지
- 멀티-에포크 학습을 언제 중단해야 하는지 예측 가능

**한계**

- 공식의 하이퍼파라미터(a, b, c, α, β, γ, δ)를 추정하려면 여전히 소규모 기준 실험이 필요
- 검증된 아키텍처 외의 도메인(예: 강화학습, 생성 모델)에 대한 일반화는 추가 확인이 필요
- 데이터 품질의 이질성(다양한 품질의 데이터가 섞인 경우)은 다루지 않음
- 두 명의 저자, 단일 기관(Arena Physica)에서 나온 결과로 독립 재현이 필요

**알아둘 용어**

- **친칠라 스케일링 법칙 (Chinchilla scaling law)**: Hoffmann et al.(2022)이 제안한, 고정 컴퓨팅 예산 하에서 모델 크기 N과 학습 데이터 D의 최적 비율을 예측하는 경험적 공식. 약 20 토큰/파라미터를 권장.
- **비가역 손실 (irreducible loss, E)**: 데이터 자체의 불규칙성(노이즈)에 의해 어떤 모델로도 줄일 수 없는 최소 손실.
- **비정보 기준선 (uninformed baseline, L₀)**: 학습 없이 데이터 분포의 기초 통계만으로 달성할 수 있는 손실. 예측 능력의 상한선.
- **과소용량 (undercapacity)**: 모델 크기가 태스크에 비해 너무 작아 패턴을 충분히 포착하지 못하는 상태.
- **멀티-에포크 (multi-epoch)**: 동일한 데이터셋을 여러 번 반복 학습하는 방식. 데이터가 부족할 때 자연스럽게 발생.
- **과적합 항 (overfitting term)**: 고유 데이터 D 대비 총 학습 스텝 T가 너무 많을 때 발생하는 손실 증가 항.
- **푸리에 신경 연산자 (Fourier Neural Operator, FNO)**: 주파수 도메인에서 함수 간 매핑을 학습하는 신경망. 편미분방정식 시뮬레이션 등 과학적 ML에서 사용.

**왜 주목할 만한가?**

인터넷 규모의 원시 텍스트가 빠르게 소진되고, 더 많은 학습이 합성 데이터·도메인 전문 데이터·멀티-에포크 파인튜닝에 의존하게 되는 시점에 등장한 논문이다. 친칠라 법칙을 교과서처럼 쓰던 실무자들이 그 한계를 직접 경험하기 시작하는 지금, 이를 교정하는 실용적 공식이 나왔다는 점에서 시의적절하다.

---

## English Summary

**One-line summary**

Chinchilla's scaling law — the standard formula for choosing model size versus training data — was designed for data-rich, single-epoch pretraining and fails silently in data-constrained regimes. This paper derives a corrected closed-form extension that decomposes training loss into undercapacity, undertraining, and overfitting terms, validated across four architecture families and multiple domains.

**Core idea**

Chinchilla's law (L = E + A/N^α + B/D^β) has three structural failures outside its calibration regime: (1) it diverges as available data D shrinks rather than saturating at an uninformed baseline; (2) it cannot express overfitting when model capacity exceeds data; (3) it conflates unique data D with total training steps T, making multi-epoch training invisible. The new formula L(N, D, T) = E + (L₀ − E) · h/(1 + h), with h = a/N^α + b/T^β + c·N^γ/D^δ, fixes all three issues in a single equation that reduces exactly to Chinchilla in the original data-rich, single-epoch limit.

**What is new?**

- Separates unique data count D from total training examples T, enabling correct multi-epoch modeling for the first time in a Chinchilla-style law
- Decomposes loss into three interpretable terms: undercapacity (model too small), undertraining (too few steps), and overfitting (too many repetitions of data)
- Saturating sigmoid-like structure ensures loss remains physically meaningful, bounded between irreducible loss E and uninformed baseline L₀
- Validated across four architecture families (MLPs, ResNets, Fourier Neural Operators, Transformers) covering vision, scientific ML, and language
- Reduces to the original Chinchilla formula as a special case when data is abundant and training is single-epoch

**How does it work?**

1. **Three-term decomposition**: The auxiliary function h sums three contributions — a/N^α (undercapacity), b/T^β (undertraining), and c·N^γ/D^δ (overfitting from data repetition).
2. **Saturating structure**: When h → 0, L → E (perfect model limit); when h → ∞, L → L₀ (no learning limit). This keeps predictions bounded and physically interpretable.
3. **Chinchilla as a limit**: When D is large and T ≈ D (single epoch), the overfitting term vanishes and the formula collapses to the standard Chinchilla form.
4. **Optimal allocation**: Given a fixed FLOPs budget and a known data limit D, one can numerically optimize over N and T to find the best training configuration.
5. **Fitting**: The seven parameters (a, b, c, α, β, γ, δ) are estimated by fitting the formula to a small grid of training runs at varying N, D, and T — a standard practice inherited from Chinchilla.

**Strengths**

- Directly applicable to data-limited settings: fine-tuning, domain-specific models, scientific machine learning, synthetic data regimes
- Architecture-agnostic validation across vision, language, and scientific ML domains
- Backward compatible with Chinchilla: practitioners need not abandon prior intuitions
- Provides a principled stopping criterion for multi-epoch training
- Clean, closed-form equation that is easy to implement

**Limitations**

- The seven hyperparameters still require a small calibration experiment for each new domain or architecture family
- Generalization to reinforcement learning, generative models, or other non-standard training objectives is not demonstrated
- Data quality heterogeneity (mixing high- and low-quality sources) is not modeled
- Results come from two authors at a single institution (Arena Physica); independent replication is needed
- The formula assumes i.i.d. repeated epochs; curriculum learning or importance-weighted sampling may require further extensions

**Terms to know**

- **Chinchilla scaling law**: The empirical rule (Hoffmann et al., 2022) recommending roughly 20 training tokens per model parameter for optimal compute allocation under a fixed FLOPs budget.
- **Irreducible loss (E)**: The minimum achievable loss, set by noise in the data itself that no model can remove.
- **Uninformed baseline (L₀)**: The loss achievable with no learning at all, e.g., using only the prior over labels. Acts as the ceiling of the new formula.
- **Undercapacity**: When the model is too small to capture data patterns, contributing systematically to high loss.
- **Multi-epoch training**: Repeatedly iterating over the same dataset, making T (total training examples) a multiple of D (unique examples).
- **Overfitting term**: The c·N^γ/D^δ component representing loss increase when a model is trained on data repeated more than it can absorb.
- **Fourier Neural Operator (FNO)**: A neural network architecture operating in frequency space, widely used in scientific ML for solving partial differential equations.

**Why it is worth watching**

Internet-scale pretraining data is increasingly exhausted, and future model improvements are expected to rely more on synthetic data, domain-specific corpora, and multi-epoch fine-tuning. The Chinchilla law — treated as the gospel of efficient training — was not designed for any of these scenarios. This paper provides a drop-in corrected formula that practitioners can use immediately to make better compute allocation decisions in the regimes that are rapidly becoming the norm.

**My take**

이 논문은 새로운 모델이나 알고리즘이 아니라 학습 이론의 핵심 도구를 수정한다는 점에서 소박하지만 중요하다. 실용적으로 보면, 특히 데이터가 제한된 과학·의료·산업 도메인에서 모델을 학습하는 연구자들에게 즉시 유용하다. 다만 Arena Physica라는 상대적으로 알려지지 않은 기관에서 나온 소규모 연구로, 대형 기관의 독립 검증이 이루어진다면 신뢰도가 크게 높아질 것이다.

This paper is modest in scope — it corrects a theoretical tool rather than introducing a new model or algorithm — but that modesty is its strength. The fix addresses a gap that many practitioners encounter in practice but rarely formalize. It is immediately useful for anyone training models with limited or domain-specific data. The main caveat is that it comes from a small, less-established group, so broader replication and adoption will determine its lasting impact.
