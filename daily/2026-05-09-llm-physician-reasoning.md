---
title: "Performance of a large language model on the reasoning tasks of a physician"
date: 2026-05-09
topic: medical-AI
tags: [medical-AI, healthcare, clinical-reasoning, LLM, diagnosis, emergency-medicine, AI-evaluation]
source: https://www.science.org/doi/10.1126/science.adz4433
---

Performance of a large language model on the reasoning tasks of a physician

* Date: 2026-04-30
* Source: https://www.science.org/doi/10.1126/science.adz4433
* Topic: Medical AI / Healthcare
* Why it matters: This is the first rigorously controlled study to test an AI reasoning model against physicians using real, unprocessed emergency department records. Published in *Science*, it found that OpenAI's o1 model matched or outperformed physicians across all six clinical reasoning experiments, including a prospective real-world arm—marking a qualitative threshold in medical AI evaluation.

## Korean Summary

**한줄 요약**

하버드 의대·베스 이스라엘 디코니스 메디컬센터 연구팀이 OpenAI의 추론 모델(o1-preview)을 의사들과 비교하는 대규모 임상 추론 평가를 실시했다. 6가지 실험(진단 차별화, 확률적 추론, 처치 관리 추론, 실제 응급실 환자 사례 등) 전반에서 LLM이 의사 기준치를 일관되게 초과했다. 이 결과는 *Science* 저널에 2026년 4월 30일 게재되었으며, AI가 실제 임상 환경에서 의사 수준의 추론에 도달했음을 보여준 가장 엄밀한 증거로 주목받고 있다.

**핵심 아이디어**

기존 의료 AI 평가는 주로 표준화된 의료 시험(USMLE 등)이나 전처리된 사례 데이터를 사용했다. 이 연구는 실제 응급실 전자 건강기록(EHR)을 전혀 가공하지 않은 상태로 모델에 입력하고, 숙련 의사들과 동일한 정보로 동일한 진단·처치 과제를 수행하게 했다. OpenAI의 o1-preview는 답변 전에 여러 전략을 탐색하고 자기 검토를 수행하는 "추론 모델"로, 이 능력이 단순 언어 모델 대비 임상 추론에서 뚜렷한 강점으로 나타났다.

**무엇이 새로운가?**

- **실제 ER 데이터 사용**: 전처리 없이 76명의 실제 응급실 환자 EHR을 입력해 전향적(real-world) 비교 실시
- **6개 실험의 포괄적 평가**: 감별진단 생성·진단 추론·응급실 트리아지 감별·확률적 추론·처치 관리 추론 등 5개 실험 + 실세계 실험
- **수백 명의 의사 대비**: 다양한 수련 단계의 의사 수백 명을 기준선으로 삼아 체계적인 비교
- **정보 불확실 상황에서 강점 입증**: 초기 트리아지처럼 제한된 정보만 있는 상황에서 AI의 우위가 가장 두드러짐
- **추론 모델(reasoning model)의 임상적 가치 실증**: 단순 LLM 대비 o1의 자기 수정·다단계 사고 능력이 임상 추론에서 유의미한 차이를 만들어냄

**어떻게 작동하는가?**

1. 연구팀은 5가지 임상 추론 과제(진단 차별화, 진단 추론 표시, 응급 트리아지 차별 진단, 확률적 추론, 처치 관리 추론)를 설계하고, 검증된 10점 척도와 전문의 심사로 결과를 평가했다.
2. 각 과제에서 o1-preview 모델과 다양한 수련 단계의 의사 수백 명을 직접 비교했다.
3. 여섯 번째 실험(실세계 팔)에서는 보스턴 소재 대형 학술 메디컬센터 응급실에서 무작위 선택된 76명의 환자 차트를 실제 임상 당시와 동일한 형태로 모델과 주치의에게 각각 제시했다.
4. 의사가 EHR에서 특정 정보를 추가로 요청하는 과정과 달리, 모델에는 기록된 정보 전체가 한꺼번에 제공되었고 별도 정제 없이 진단 및 처치 계획을 생성하도록 했다.
5. 결과는 전문의 심사위원단이 검토하여 진단 정확도와 추론 품질을 채점했다.

**강점**

- 실제 EHR 기반 전향적 비교로 생태학적 타당성(ecological validity)이 높음
- 6가지 과제에 걸쳐 일관된 우위—단일 실험의 요행이 아님
- 희귀 질환 및 복잡 케이스(NEJM 사례 포함)에서 특히 강한 성능
- 추론 모델의 단계별 자기 검토 능력이 임상 추론에 실질적으로 기여함을 보여줌
- 정보가 불완전한 초기 단계에서 AI 우위가 가장 뚜렷—의료 현장에서 가장 가치 있는 구간

**한계**

- 실세계 팔은 76명 환자로 표본이 작아 일반화에 한계
- 텍스트 기반 추론만 평가—신체검사, 영상 판독, 직접 환자 소통 등 임상 행위의 상당 부분을 포함하지 못함
- 특정 모델(o1-preview)에 한정된 결과—다른 모델로의 일반화 불확실
- AI가 정보를 능동적으로 요청·선별하는 과정(임상적으로 중요한 기술)은 평가되지 않음
- 저자들 스스로 "AI가 자율 진료에 나설 준비가 되지 않았다"고 명시
- 더 엄밀한 무작위 대조 임상 시험(RCT)이 필요함

**알아둘 용어**

- **임상 추론(Clinical Reasoning)**: 의사가 환자 정보를 바탕으로 진단 가설을 세우고 검사·처치를 결정하는 사고 과정
- **감별진단(Differential Diagnosis)**: 동일 증상을 설명할 수 있는 여러 가능한 질환 목록을 생성하는 과정
- **추론 모델(Reasoning Model)**: 최종 답변 전에 다단계 내부 '사고(chain-of-thought)'를 수행하는 LLM (예: OpenAI o1)
- **트리아지(Triage)**: 응급실 도착 시 환자 상태를 신속히 분류해 우선순위를 결정하는 과정
- **전자 건강기록(EHR, Electronic Health Record)**: 환자의 진단·처방·검사 이력을 전자적으로 기록한 데이터
- **생태학적 타당성(Ecological Validity)**: 실험 결과가 실제 현실 환경에도 적용될 수 있는 정도
- **선택적 분류(Selective Classification)**: 불확실한 입력에 대해 답변 거부 옵션을 포함한 분류 방식

**왜 주목할 만한가?**

지금까지 의료 AI 평가 대부분은 의료 시험 문제 풀기나 정제된 사례 데이터를 사용했다. 이 연구는 처음으로 실제 응급실 환경의 원시 EHR을 그대로 사용해, 의사 수백 명과 동일한 조건에서 AI 추론 능력을 비교했다. *Science* 게재라는 점과 6개 실험 전반의 일관된 결과는 의료 AI가 실제 임상 의사결정 지원 도구로 진지하게 고려되어야 할 임계점에 도달했음을 시사한다.

---

## English Summary

**One-line summary**

A Harvard/Beth Israel team published in *Science* the most rigorous real-world test yet of an AI reasoning model against physicians: OpenAI's o1-preview matched or outperformed doctors across six clinical reasoning experiments, including a prospective arm using raw, unprocessed emergency department records from 76 actual patients. The advantage was largest in early triage—the condition of greatest clinical need with the least available information.

**Core idea**

Previous medical AI benchmarks used standardized exam questions or carefully cleaned vignette data. This study fed raw, unstructured electronic health records directly into OpenAI's o1-preview—a "reasoning model" that explores multiple strategies and self-corrects before answering—and compared it against hundreds of physicians across a structured battery of clinical tasks. The results show that chain-of-thought reasoning confers a genuine advantage in clinical inference, especially when information is incomplete.

**What is new?**

- **Real-world prospective arm**: 76 randomly selected actual ER patients, EHR data used without preprocessing, evaluated against attending physicians under identical information constraints
- **Six-experiment battery**: Covers differential diagnosis generation, diagnostic reasoning display, triage differential diagnosis, probabilistic reasoning, management reasoning, and the real-world ER comparison
- **Hundreds of physician comparators**: Physicians at every level of training served as the baseline—not just novices
- **Uncertainty advantage demonstrated**: AI's edge was most pronounced at initial triage, where information is minimal and decisions are most consequential
- **Reasoning model vs. base LLM distinction**: o1's multi-step self-verification yielded measurable clinical improvement over prior-generation models

**How does it work?**

1. Five structured experiments were designed around validated clinical reasoning tasks: generating a differential diagnosis, displaying diagnostic logic, triage differential diagnosis, probabilistic reasoning, and management planning.
2. o1-preview was scored against physician baselines using expert-adjudicated 10-point rubrics with validated psychometrics.
3. A sixth, prospective experiment compared the model to attending physicians on 76 randomly selected ER cases, using the exact EHR data that clinicians had available at each clinical decision point.
4. The model was given the full record at once; physicians could request additional information incrementally. Scoring was done by blinded expert physician panels.
5. Quantitative results: at triage, o1 reached an exact or close diagnosis 67% of the time versus roughly 57% for physicians (>10% gap). In one experiment, o1 achieved a perfect clinical reasoning score in 98% of cases versus 35% for attending physicians.

**Strengths**

- High ecological validity from real, unprocessed ER data
- Consistent advantage across six heterogeneous task types, not a single benchmark result
- Particularly strong on rare diseases and complex NEJM case studies
- Demonstrates that reasoning models represent a qualitative step change over base LLMs in clinical settings
- Most pronounced advantage at the clinically highest-stakes point: early triage with minimal data

**Limitations**

- Real-world arm is only 76 patients—small for generalization
- Text-only evaluation: physical examination, imaging interpretation, and direct patient interaction were excluded
- Results tied to one specific model (o1-preview); generalization across other models is unclear
- The model received data passively; clinical skill also includes knowing what questions to ask and what tests to order
- Authors explicitly state AI is not ready for autonomous clinical practice
- More rigorous randomized controlled trials in actual clinical workflows are needed
- Performance on non-English or non-US patient populations untested

**Terms to know**

- **Clinical reasoning**: The cognitive process by which a physician generates diagnostic hypotheses and decides on tests and treatments based on patient data
- **Differential diagnosis**: A ranked list of possible diagnoses that could explain a patient's symptoms
- **Reasoning model**: An LLM that performs multi-step internal "thinking" before producing an answer, enabling self-correction (e.g., OpenAI o1)
- **Triage**: The ER process of rapidly assessing patients on arrival to prioritize urgency of care
- **EHR (Electronic Health Record)**: A digital record of a patient's medical history, diagnoses, medications, and test results
- **Ecological validity**: The degree to which experimental findings transfer to real-world conditions
- **Prospective study**: A study that follows participants forward in time, as opposed to analyzing historical data retrospectively

**Why it is worth watching**

Medical AI has crossed a benchmark threshold: a reasoning model now demonstrably outperforms physicians on real emergency department cases evaluated under real-world conditions, published in one of the highest-impact journals in science. This is not a narrow exam-passing result. It changes the conversation from "can AI pass a medical licensing exam?" to "when and how should AI be integrated into clinical workflows?" The study is also a methodological blueprint for how serious clinical AI evaluation should be done going forward.

**My take**

이 연구는 의료 AI 평가의 기준을 한 단계 높였다. 시험 문제 풀기가 아닌 실제 응급실 데이터를 사용했고, 소수가 아닌 수백 명의 의사와 비교했으며, *Science*라는 최고 권위의 저널에 게재되었다. 그러나 76명이라는 작은 실세계 표본, 텍스트 전용 평가, 단일 모델 의존 등 한계는 분명하다. 당장의 자율 진료보다는 '의사의 두 번째 의견 도구'로서의 가치가 현실적이며, 본격적인 임상 도입 전 엄밀한 무작위 대조시험이 필수다.

This study meaningfully raises the bar for medical AI evaluation. It used actual ER data rather than exam questions, compared against hundreds of physicians rather than a handful, and appeared in *Science*. The limitations are real—76 real-world cases is a small sample, the evaluation is text-only, and results are tied to one specific model—but the consistent advantage across six task types is hard to dismiss. The near-term value is likely as a clinical decision-support tool for second opinions rather than autonomous diagnosis, and rigorous RCTs in live workflows remain necessary before any deployment decision.
