---
title: "Lying Is Just a Phase: The Hidden Alignment Transition in Language Model Scaling"
date: 2026-05-27
topic: AI
tags: [AI, alignment, scaling, LLM, truthfulness, capability, phase-transition, safety]
source: https://arxiv.org/abs/2605.18838
---

# Lying Is Just a Phase: The Hidden Alignment Transition in Language Model Scaling

* Date: 2026-05-27
* Source: https://arxiv.org/abs/2605.18838
* Topic: AI / LLM Alignment & Scaling
* Why it matters: Standard scaling laws describe how loss decreases with compute, but they say nothing about how distinct capabilities interact. This paper shows empirically — across 63 base models from 16 families — that reasoning ability and truthfulness are anticorrelated below a critical scale (~3.5B parameters) and cooperative above it, and that data curation and architecture can shift this transition point dramatically, meaning alignment is not purely a size problem.

## Korean Summary

**한줄 요약**

63개의 기본 언어 모델(base LM)을 16개 패밀리에 걸쳐 분석한 결과, 추론 능력과 진실성(truthfulness)은 약 35억 파라미터 미만의 모델에서 서로 반비례(anticorrelation)하다가 그 이상에서는 협력 관계(cooperation)로 전환되는 '정렬 위상 전이(alignment phase transition)'가 존재함이 밝혀졌다. 놀랍게도 이 임계 규모는 데이터 큐레이션, 아키텍처, 훈련 방식에 따라 크게 달라지며, 잘 선별된 데이터로 훈련된 소형 모델이 훨씬 큰 웹 스케일 훈련 모델과 동등한 정렬 특성을 보일 수 있다.

**핵심 아이디어**

기존 스케일링 법칙(scaling law)은 컴퓨팅 예산과 손실(loss) 감소 사이의 관계를 잘 예측하지만, 서로 다른 능력들이 어떻게 상호작용하는지는 설명하지 못한다. 이 논문은 '추론 능력'과 '진실성'이라는 두 가지 중요한 능력의 결합(coupling)을 직접 측정한다. 핵심 발견은 모델이 특정 임계 규모 Nc를 넘기 전과 후에 이 두 능력의 상관관계 방향이 뒤집힌다는 것이다. 소형 모델은 추론이 좋아지면 진실성이 떨어지고, 일정 규모를 넘으면 두 능력이 함께 향상된다. 더욱 중요한 점은 이 임계 규모가 모델 크기만으로 결정되지 않으며, 훈련 데이터 품질, 아키텍처 설계, 훈련 방식으로도 조절된다는 사실이다.

**무엇이 새로운가?**

- **위상 전이의 발견**: 표준 손실 곡선에는 보이지 않는 능력 간 결합(capability coupling)의 위상 전이를 정량적으로 최초 규명
- **대규모 교차-패밀리 실험**: 16개 모델 패밀리에서 63개 기본 모델을 체계적으로 비교하여 재현 가능한 패턴 확인
- **임계 규모의 공학적 가변성**: 데이터 큐레이션만으로도 임계 규모가 10배 이동 가능함을 실증 (Phi 1B가 웹 스케일 훈련 10B 수준의 결합 지수 달성)
- **출력 투영 병목 가설**: 폭 정규화(width normalization)가 모든 테스트된 패밀리에서 반상관을 제거한다는 발견으로 출력 투영 레이어 병목 메커니즘 제시
- **정렬에 대한 재해석**: "더 큰 모델만이 더 잘 정렬된다"는 기존 관행에 의문을 제기하고, 데이터 품질과 아키텍처가 모델 크기와 독립적으로 정렬에 기여함을 보임

**어떻게 작동하는가?**

1. **모델 선정**: 16개 주요 모델 패밀리(Qwen, Phi, Gemma 등)에서 다양한 규모의 체크포인트 총 63개를 선택
2. **능력 측정**: 각 모델에 대해 추론 능력(reasoning capability)과 진실성(truthfulness)을 표준 벤치마크로 독립적으로 평가
3. **결합 지수 계산**: 두 능력 점수 간의 상관 지수(coupling coefficient)를 모델 규모별로 계산
4. **위상 전이 탐지**: 스케일에 따라 결합 지수가 음수(반상관)에서 양수(협력)로 뒤집히는 임계 규모 Nc를 부트스트랩 통계로 추정 (Nc ≈ 35억 파라미터, 95% CI: [29억, 134억])
5. **조절 인자 분석**: Qwen(데이터 큐레이션), Phi(데이터 큐레이션), Gemma-4(증류+아키텍처 혁신) 등 다양한 사례를 통해 Nc를 이동시키는 인자 분리 분석
6. **메커니즘 탐색**: 폭 정규화 실험을 통해 출력 투영 레이어가 반상관의 병목임을 추정

**강점**

- 단일 모델 또는 소수 가족에 국한하지 않고 63개/16패밀리라는 광범위한 실증적 근거 제공
- 결과가 표준 손실 곡선이나 단순 규모 증가로는 설명되지 않는 새로운 현상을 포착
- 데이터 품질 및 아키텍처 개선만으로도 소형 모델을 대형 모델 수준으로 '정렬 위상'을 앞당길 수 있다는 실용적 함의 제공
- 정렬 연구에 새로운 측정 도구(capability coupling coefficient)를 제시

**한계**

- 단독 저자이며 소속이 알려지지 않은 소규모 연구소(ZEHEN Labs)로, 동료 검토(peer review)를 거치지 않은 프리프린트
- 추론 및 진실성을 측정한 구체적인 벤치마크와 결합 지수 계산 공식이 공개된 요약에서 명확하게 명시되어 있지 않음
- 인과관계(causality) 미립증 — 동일 패밀리 내 모델들의 교차 스냅샷 상관관계이므로 메커니즘적 해석에 주의 필요
- 기본 모델(base LM)만 다루며, RLHF·DPO 등 사후 정렬(post-alignment) 단계 이후의 거동은 분석하지 않음
- 63개 모델이 전체 LLM 지형을 대표한다고 보기 어려울 수 있음

**알아둘 용어**

- **위상 전이 (Phase Transition)**: 물리학에서 차용한 개념으로, 연속적 변화(규모 증가)에도 시스템 거동이 질적으로 달라지는 임계점
- **결합 지수 (Coupling Coefficient)**: 두 능력 점수가 모델 규모에 따라 얼마나 같은 방향으로 움직이는지를 나타내는 상관 척도
- **반상관 (Anticorrelation)**: 한 능력이 향상될 때 다른 능력이 감소하는 관계
- **진실성 (Truthfulness)**: 모델이 사실에 기반한 응답을 생성하고 허위 진술을 피하는 경향; TruthfulQA 등으로 측정
- **임계 규모 (Critical Scale, Nc)**: 위상 전이가 발생하는 모델 파라미터 수 기준점
- **폭 정규화 (Width Normalization)**: 모델 레이어의 출력 투영 가중치 행렬을 정규화하는 기법
- **기본 모델 (Base LM)**: RLHF, DPO 등 사후 정렬 없이 사전 훈련(pretraining)만 완료된 원시 모델

**왜 주목할 만한가?**

LLM 정렬 연구의 지배적인 가정 중 하나는 "더 큰 모델이 더 안전하다"는 것이다. 이 논문은 이 가정이 단순히 규모 문제가 아님을 보여준다. 소형 모델도 데이터 큐레이션과 아키텍처 개선으로 "정렬 위상"에 진입할 수 있다는 발견은, 고비용 대형 모델 없이도 더 정직하고 추론 능력이 좋은 AI를 만들 수 있는 실용적 경로를 시사한다. 또한 스케일링 법칙이 능력 간 상호작용을 설명하지 못한다는 한계를 명확히 제시함으로써, AI 안전성 평가의 새로운 측정 프레임을 제안한다.

---

## English Summary

**One-line summary**

An empirical study of 63 base language models across 16 families reveals a hidden phase transition: below a critical scale of ~3.5B parameters, reasoning and truthfulness anticorrelate, while above it they cooperate — and data curation or architectural choices can shift this transition by up to 10×, making alignment not simply a function of model size.

**Core idea**

Standard scaling laws reliably predict how loss decreases with compute, but they are silent on how distinct capabilities interact with each other. This paper directly measures the *coupling* between two critical capabilities — reasoning and truthfulness — as a function of model scale. The central finding is that this coupling undergoes a phase transition: in smaller models, getting better at reasoning tends to come at the cost of truthfulness, while above a family-dependent critical scale the two capabilities become positively correlated and improve together. Crucially, the critical scale is not fixed by size alone; data quality and architectural choices can dramatically shift when the transition occurs.

**What is new?**

- **Empirical discovery of capability phase transition**: First systematic quantification of a coupling sign-flip between reasoning and truthfulness across a large, multi-family model survey
- **Cross-family scale at 63 models**: Unlike typical studies that examine one model family, the analysis spans 16 families for reproducible, generalizable findings
- **Data curation shifts critical scale by ~10×**: Phi at 1B parameters achieves coupling comparable to a web-trained 10B model through data curation alone; Qwen's coupling jumps from 0.025 to 0.830 between generations at matched scale
- **Architecture can substitute for scale**: Gemma-4 at 4B reaches a coupling score of 0.871 — characteristic of 13B+ standard-trained models — through distillation and design improvements
- **Output-projection bottleneck hypothesis**: Width normalization eliminates anticorrelation across all tested families, providing a mechanistic lead for future work

**How does it work?**

1. **Model selection**: 63 base model checkpoints are drawn from 16 prominent families (including Qwen, Phi, Gemma, and others) spanning a wide range of parameter counts
2. **Capability scoring**: Each model is evaluated independently on reasoning and truthfulness benchmarks to produce two scalar scores per model
3. **Coupling measurement**: A coupling coefficient (the correlation between the two scores as a function of scale within and across families) is computed
4. **Phase detection**: The critical scale Nc is estimated as the point where the coupling crosses zero, with bootstrap confidence intervals: Nc ≈ 3.5B parameters [2.9B, 13.4B] at 95% CI
5. **Factor isolation**: Specific model families are used as natural experiments — curated data (Phi, Qwen), distillation (Gemma-4) — to decompose which factors shift Nc
6. **Mechanism probing**: Width normalization experiments implicate the output-projection layer as the architectural bottleneck driving anticorrelation in small models

**Strengths**

- Large, diverse empirical base (63 models, 16 families) gives the finding broader credibility than single-family studies
- The phase transition is invisible to loss curves, meaning it captures something genuinely new beyond standard scaling metrics
- Practical takeaway is immediately actionable: invest in data quality and architecture to reach the "cooperative phase" without scaling up
- Introduces a new measurement concept (capability coupling coefficient) applicable to other capability pairs beyond reasoning and truthfulness

**Limitations**

- Single-author preprint from a little-known lab (ZEHEN Labs); not yet peer-reviewed
- The specific benchmarks used to measure reasoning and truthfulness are not detailed in available summaries — important for reproducibility
- The coupling metric formula and exact statistical procedure are not fully described in available information
- Observational design: correlations across model families do not establish a causal mechanism
- Covers only base (pretrained) models; behavior may differ substantially after RLHF, DPO, or other alignment fine-tuning
- 63 models may not represent the full diversity of the LLM landscape

**Terms to know**

- **Phase transition**: A qualitative change in system behavior at a critical threshold, borrowed from physics; here, the flip from anticorrelation to cooperation at Nc
- **Coupling coefficient**: A scalar measuring how correlated two capabilities are across a set of models; positive = cooperative, negative = anticorrelated
- **Truthfulness**: A model's tendency to produce factually grounded outputs and avoid confident falsehoods; commonly assessed via benchmarks like TruthfulQA
- **Critical scale (Nc)**: The parameter-count threshold at which the capability coupling changes sign
- **Width normalization**: A technique that normalizes the output-projection weight matrices in transformer layers; here found to eliminate anticorrelation
- **Base model**: A language model after pretraining only, before any alignment fine-tuning (RLHF, DPO, etc.)
- **Anticorrelation**: A negative coupling where improving one capability comes at the cost of another

**Why it is worth watching**

The dominant narrative in AI alignment is that larger models are inherently safer and more aligned. This paper complicates that picture: the capability-alignment phase transition means that small models exist in a regime where getting smarter can make them *less* honest — an important failure mode often attributed simply to "insufficient scale." More importantly, the finding that data curation and architecture can shift the transition point by up to an order of magnitude offers a cost-efficient path: you do not necessarily need a 10× larger model to reach the cooperative phase. As inference costs, energy consumption, and deployment constraints push practitioners toward smaller models, this paper provides a principled empirical framework for evaluating whether a small model is in the "safe zone" of capability-alignment cooperation.

**My take**

이 논문은 LLM 안전성 연구에서 드물게 보이는 흥미로운 측정 결과를 제시한다. "모델 크기만이 정렬을 결정한다"는 단순화된 관점에 도전하는 empirical 증거로, 데이터 큐레이션과 아키텍처 설계의 중요성을 재조명한다는 점에서 가치 있다. 다만 단독 저자의 미검토 프리프린트라는 점과 벤치마크·측정 방법의 투명성이 충분하지 않다는 점은 결과를 해석할 때 주의해야 할 부분이다.

This paper presents a rare and interesting empirical result in LLM safety research. It offers a challenge to the oversimplified narrative that model size alone governs alignment, and highlights the underappreciated role of data curation and architecture. The findings are worth tracking, but as a single-author preprint with incomplete methodological transparency, the results should be treated as a compelling hypothesis awaiting independent replication rather than a settled conclusion.
