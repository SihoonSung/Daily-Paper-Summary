---
title: "Test-Time Scaling Makes Overtraining Compute-Optimal"
date: 2026-04-23
topic: AI
tags: [AI, LLM, scaling-laws, inference, test-time-compute, pretraining, efficiency]
source: https://arxiv.org/abs/2604.01411
---

# Test-Time Scaling Makes Overtraining Compute-Optimal

* Date: 2026-04-01
* Source: https://arxiv.org/abs/2604.01411
* Topic: AI
* Why it matters: Chinchilla scaling laws tell practitioners how to split compute between model size and training tokens — but they assume a single inference sample per query; this paper extends those laws to jointly optimize pretraining and test-time sampling, showing the optimal strategy shifts dramatically toward smaller, more-overtrained models.

## Korean Summary

**한줄 요약**

기존 친칠라(Chinchilla) 스케일링 법칙은 모델 크기와 학습 토큰 수를 최적화하지만, 추론 시 여러 번 샘플링하는 테스트-타임 스케일링을 고려하지 않는다. 이 논문은 훈련과 추론 비용을 하나의 예산으로 통합해 최적 모델 크기·학습 토큰·추론 샘플 수를 함께 결정하는 T² 스케일링 법칙을 제안하며, 테스트-타임 샘플링을 전제하면 훨씬 작은 모델을 대폭 과학습(overtraining)시키는 전략이 최적임을 입증한다.

**핵심 아이디어**

친칠라 스케일링 법칙은 고정 학습 예산에서 모델 파라미터 수 N과 학습 토큰 수 D의 최적 비율(약 20 토큰/파라미터)을 제시한다. 그러나 현대 LLM은 추론 시 동일 쿼리에 여러 출력을 생성하고 가장 좋은 것을 선택하는 best-of-k(pass@k) 방식을 사용하며, 이 추론 비용은 N에 비례한다. Train-to-Test(T²) 프레임워크는 총 예산을 학습 비용 + 추론 비용으로 재정의하고 (N, D, k)를 동시에 최적화한다. 결론: 추론 샘플 수까지 고려하면 더 작은 모델을 훨씬 많은 토큰으로 학습하는 과학습 전략이 최적이며, 아낀 학습 비용을 추론 샘플에 투입하는 것이 유리하다.

**무엇이 새로운가?**

- 학습 컴퓨팅과 추론 컴퓨팅을 단일 예산으로 통합한 최초의 스케일링 법칙(T²)
- pass@k를 명시적으로 모델링해 모델 크기·토큰·샘플 수 세 변수를 동시 최적화
- 두 가지 독립 모델링 방식(손실 기반 멱함수 확장 / Beta 회귀)이 동일한 결론에 수렴
- 5M~901M 파라미터, 12개 컴퓨팅 수준, 100개 이상의 모델로 구성된 대규모 실험 검증
- 최적 과학습 구성으로 사전 훈련한 모델이 8개 다양한 벤치마크와 포스트 트레이닝 이후에도 친칠라 최적 모델을 지속적으로 능가함을 입증

**어떻게 작동하는가?**

1. **예산 재정의**: 총 예산 C = C_train + C_test = 6ND + 2Nk (6ND는 학습 FLOP, 2Nk는 k번 샘플링 시 추론 FLOP)로 정의한다.
2. **pass@k 모델링**: pass@k는 k번의 독립 샘플 중 적어도 하나가 정답일 확률이다. 샘플당 정확도 p와 샘플 수 k의 비선형 관계를 모델링해야 한다.
3. **두 가지 접근 방식**: (a) 손실 스케일링 방식 — 친칠라 손실 함수에 반복 샘플링 효과를 멱함수 항으로 추가해 확장; (b) Beta 회귀 방식 — 질문별 정확도 분포를 직접 Beta 분포로 모델링해 pass@k를 예측. 두 방식이 모두 무거운 과학습을 권장하는 방향으로 수렴한다.
4. **최적화**: C = C_train + C_test 예산 제약하에 (N*, D*, k*)를 탐색한다. 작은 N은 샘플당 추론 비용을 낮추므로 k를 늘릴 수 있고, 남는 학습 예산은 D를 늘리는 데 쓴다.
5. **실험 검증**: 예측된 최적 구성에서 실제로 사전 훈련된 과학습 모델들이 동일한 총 예산의 친칠라 최적 모델보다 SciQ, OpenBookQA 등 8개 태스크에서 더 나은 성능을 보임을 확인한다.

**강점**

- 기존 친칠라 프레임워크를 추론 비용까지 확장해 더 현실적인 최적화 지형 제공
- 두 독립 방법론이 동일한 결론으로 수렴 — 결과의 견고성 확보
- 5M~901M 파라미터, 3 오더 스케일에 걸친 100개 이상 모델로 광범위한 실험 검증
- 8개 다양한 태스크(실제 과학 문답, 수치 추론, 공간 추론, 지식 회상) 모두에서 일관된 개선
- 포스트 트레이닝(RLHF 등) 이후에도 결과가 유지됨

**한계**

- 검증 규모가 최대 901M 파라미터 — 수십~수백 B 파라미터 영역에서의 유효성은 미확인
- pass@k(best-of-N) 전략에 집중; 연쇄적 사고(CoT), 검색 기반 추론, 검증기 안내 추론 등 다른 테스트-타임 전략에 대한 일반화는 추가 연구 필요
- 사전 훈련 단계에서 추론 예산을 미리 알아야 한다는 가정 — 실제 배포 환경에서는 추론 수요가 동적으로 변함
- 과학습 모델은 파인 튜닝이 다소 어려울 수 있다는 점이 실험에서도 확인됨(다만 포스트 트레이닝 후에도 여전히 우위)
- 데이터 품질, 모델 아키텍처 차이 등의 변수는 현재 분석에서 통제되지 않음

**알아둘 용어**

- **친칠라 스케일링 법칙(Chinchilla Scaling Laws)**: DeepMind가 2022년 발표한 법칙으로, 고정 학습 예산에서 최적 모델 크기와 학습 토큰 수의 비율(약 20 토큰/파라미터)을 제시
- **과학습(Overtraining)**: 친칠라 권장치보다 훨씬 많은 토큰으로 모델을 학습시키는 것; 모델 크기 대비 훈련 토큰이 과도하게 많은 상태
- **pass@k**: 모델이 k번 독립 샘플링했을 때 적어도 한 번 정답을 생성할 확률; 테스트-타임 스케일링의 핵심 지표
- **테스트-타임 스케일링(Test-Time Scaling)**: 추론 시 여러 출력을 생성하고 가장 좋은 것을 선택하는 방식으로 성능을 향상시키는 전략
- **T²(Train-to-Test) 스케일링**: 이 논문이 제안하는 프레임워크; 학습과 추론 비용을 통합해 세 변수(모델 크기, 학습 토큰, 추론 샘플 수)를 동시 최적화
- **Beta 회귀(Beta Regression)**: 0과 1 사이 연속 값의 분포를 모델링하는 회귀 기법; 여기서는 질문별 정확도 분포를 모델링하는 데 사용
- **컴퓨팅 최적(Compute-Optimal)**: 주어진 총 컴퓨팅 예산 내에서 최대 성능을 달성하는 구성

**왜 주목할 만한가?**

테스트-타임 스케일링(best-of-N 샘플링, 다수결, 추론 시 반복 시도)은 현대 LLM 배포의 표준이 되어가고 있다. 그럼에도 사전 훈련 전략은 여전히 순수한 학습 예산만 고려하는 친칠라 법칙에 의존한다. T²는 이 간극을 메우는 최초의 원칙적 프레임워크로, AI 연구소와 실무자가 앞으로 모델을 훈련할 방식에 실질적인 변화를 가져올 수 있다. 특히 추론 비용이 지속적으로 하락하는 현재 환경에서, 학습 시 더 과학습하고 추론 시 더 많이 샘플링하는 전략의 최적성을 이론적·실험적으로 뒷받침한다.

---

## English Summary

**One-line summary**

Chinchilla scaling laws optimize the ratio of model parameters to training tokens but assume a single inference call per query; this paper introduces Train-to-Test (T²) scaling laws that jointly optimize model size, training tokens, and the number of inference samples under a unified compute budget, showing that when test-time sampling is planned, heavily overtraining a smaller model is compute-optimal.

**Core idea**

Chinchilla tells you how to divide a fixed training compute budget between model parameters N and training tokens D, recommending roughly 20 tokens per parameter. Modern LLMs routinely spend additional compute at inference by sampling multiple outputs and selecting the best (pass@k). But Chinchilla ignores inference costs entirely. The T² framework redefines the total budget as training compute plus inference compute and jointly optimizes (N, D, k) where k is the number of inference samples. Because inference cost scales with N, smaller models are cheaper to sample from — freeing budget to train on more tokens. The surprising finding is that this trade-off shifts optimal pretraining radically toward overtraining: far smaller models trained on far more data than Chinchilla recommends, combined with generous test-time sampling.

**What is new?**

- First scaling laws that unify training compute and inference compute into a single budget, jointly optimizing model size, training tokens, and inference sample count
- Explicit pass@k modeling within the scaling law framework, capturing the nonlinear benefit of repeated sampling
- Two independent modeling approaches (loss-based power-law extension and Beta regression on per-question accuracy) that converge to the same conclusion
- Extensive empirical testbed: 100+ pretrained models spanning 5M to 901M parameters across 12 compute levels and 8 diverse downstream tasks
- Validation that heavily overtrained T²-optimal models outperform Chinchilla-optimal models both before and after post-training

**How does it work?**

1. **Budget definition**: Total compute budget C = C_train + C_test = 6ND + 2Nk, where 6ND is the standard pretraining FLOP count and 2Nk is the cost of k inference samples from a model of size N.
2. **Modeling pass@k**: pass@k is the probability that at least one of k independent samples is correct. It is a nonlinear, concave function of per-sample accuracy p and sample count k.
3. **Two modeling approaches**: (a) Extend Chinchilla's loss scaling with an additional power-law term for repeated sampling; (b) Fit a Beta distribution to per-question accuracy across models and use it to predict pass@k directly. Both approaches agree closely.
4. **Optimization**: Under the budget constraint, solve for the optimal (N*, D*, k*). Smaller N lowers per-sample inference cost, enabling more samples k; the saved training budget is redirected into more training tokens D.
5. **Empirical validation**: The authors pretrain new models at T²-predicted optimal configurations (heavily overtrained) and confirm they outperform Chinchilla-optimal baselines across all eight tasks, and that this advantage persists after post-training.

**Strengths**

- Closes the gap between pretraining scaling law theory and real-world deployment, where test-time sampling is standard
- Two independent methods reaching the same conclusion provides strong evidence for robustness
- Validated across three orders of magnitude of compute with 100+ models
- Consistent improvements across eight diverse task types, including real-world question answering and synthetic reasoning tasks
- Results survive post-training (fine-tuning, RLHF), making the framework relevant to modern LLM pipelines

**Limitations**

- Empirically validated only up to 901M parameters; generalization to frontier-scale models (tens to hundreds of billions of parameters) is not yet confirmed
- Focused on pass@k (best-of-N) as the test-time strategy; other inference-time methods (chain-of-thought, verifier-guided search, beam search) are not directly addressed
- Assumes the test-time compute budget is known before pretraining — a constraint that may not hold when deployment demand varies
- Overtrained models are somewhat harder to fine-tune, though they still outperform Chinchilla-optimal checkpoints after post-training
- Data quality and model architecture differences are not controlled for in the current analysis

**Terms to know**

- **Chinchilla scaling laws**: DeepMind's 2022 scaling laws recommending roughly 20 training tokens per model parameter for compute-optimal pretraining under a fixed training budget
- **Overtraining**: Training a model with significantly more tokens than Chinchilla recommends for its parameter count
- **pass@k**: The probability that at least one of k independently sampled model outputs is correct; the key metric for test-time compute scaling
- **Test-time scaling**: The practice of generating multiple outputs at inference and selecting the best, trading inference compute for higher accuracy
- **Train-to-Test (T²) scaling**: The framework proposed in this paper, jointly optimizing pretraining and inference compute allocations under a single budget
- **Beta regression**: A regression technique for modeling continuous outcomes bounded between 0 and 1; used here to model per-question accuracy distributions
- **Compute-optimal**: Achieving the highest task performance for a given total compute budget

**Why it is worth watching**

Test-time sampling — generating multiple candidate outputs and picking the best — has become standard practice for improving LLM accuracy in production, yet pretraining decisions are still governed by Chinchilla laws that ignore inference cost entirely. T² is the first principled framework to bridge this gap, and its empirical validation across a broad range of scales and tasks makes it practically relevant. As inference compute continues to fall in cost and test-time scaling becomes even more routine, the insight that pretraining should shift toward smaller, heavily overtrained models may meaningfully reshape how AI labs allocate compute budgets.

**My take**

**[Korean]** T²는 현실에서 이미 널리 쓰이는 테스트-타임 샘플링을 스케일링 법칙에 처음으로 통합했다는 점에서 시의적절하고 실용적인 연구다. 두 독립 방법론이 같은 결론에 도달한다는 점과 포스트 트레이닝 이후에도 결과가 유지된다는 점이 신뢰도를 높인다. 다만 검증 규모가 소형 모델에 한정되고, pass@k 외 다른 추론 전략에 대한 일반화가 미검증이라는 점에서 대규모 실제 적용까지는 추가 연구가 필요하다.

**[English]** T² is a timely and practically motivated contribution — it formalizes what practitioners already implicitly face when deciding how to train models that will be used with test-time sampling. The convergence of two independent modeling approaches and the post-training robustness of results are both credibility-boosting. The main open questions are whether the findings hold at frontier scale and whether they generalize to inference strategies beyond best-of-N sampling, making this a strong but not yet complete picture.
