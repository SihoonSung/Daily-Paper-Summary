---
title: "LLMs Get Lost In Multi-Turn Conversation"
date: 2026-04-24
topic: AI
tags: [AI, LLM, evaluation, multi-turn, conversation, benchmark, reliability]
source: https://arxiv.org/abs/2505.06120
---

LLMs Get Lost In Multi-Turn Conversation

* Date: 2026-04-24
* Source: https://arxiv.org/abs/2505.06120
* Topic: AI / LLM Evaluation
* Why it matters: Most LLM benchmarks measure single-turn performance, but real users interact through multi-turn conversations. This paper reveals a sharp and universal 39% performance drop across all major LLMs when instructions are spread across multiple turns, exposing a critical blind spot in how the field evaluates AI assistants.

## Korean Summary

**한줄 요약**

15개의 주요 LLM 모델을 대상으로 200,000건 이상의 대화를 시뮬레이션한 결과, 멀티턴 대화 환경에서 평균 성능이 39% 하락하며 모든 모델이 일관되게 길을 잃는다는 사실이 밝혀졌다. 이 연구는 ICLR 2026 Outstanding Paper로 선정되었다.

**핵심 아이디어**

실제 사용자는 한 번에 완전한 지시를 주지 않고 여러 턴에 걸쳐 조금씩 정보를 제공하는 경우가 많다. 이 논문은 기존의 단일턴 벤치마크 과제를 여러 개의 작은 조각(샤드)으로 분해하여 멀티턴 대화를 시뮬레이션하는 "샤드 시뮬레이션(Sharded Simulation)" 방법론을 제안하고, 이 환경에서 GPT-4.1, Claude 3.7 Sonnet, Gemini 2.5 Pro를 포함한 모든 최신 LLM이 심각하게 성능이 저하됨을 보인다.

**무엇이 새로운가?**

- 기존 단일턴 벤치마크를 재활용하여 멀티턴 대화를 자동으로 생성하는 샤드 시뮬레이션 방법론 제안
- GPT-4.1, Claude 3.7 Sonnet, Gemini 2.5 Pro, LLaMA 3.1 등 15개 주요 LLM에 걸쳐 39% 성능 저하를 체계적으로 측정
- 성능 저하를 "적성(aptitude) 감소"와 "신뢰도(unreliability) 증가"로 분리하여 분석: 신뢰도 저하가 압도적 원인(+112% 증가)
- 코드, 수학, 번역, 요약 등 7개 과제에서 일관된 패턴 확인
- 멀티턴 실패의 4가지 구체적 원인 규명

**어떻게 작동하는가?**

1. **샤딩(Sharding)**: 기존 단일턴 벤치마크의 완전한 지시문을 여러 개의 원자적 조각(샤드)으로 분해한다. 예를 들어 "파이썬으로 X를 수행하는 Y 함수를 작성하라"는 지시를 "파이썬 함수를 작성해 줘" → "함수 이름은 Y야" → "X를 수행해야 해"처럼 분할한다.
2. **멀티턴 대화 시뮬레이션**: 각 턴마다 최대 하나의 샤드만 공개하며 LLM과 대화를 시뮬레이션한다.
3. **평가**: 최종 응답의 품질을 단일턴 성능과 비교 측정한다.
4. **분석**: 적성(올바른 답변 생성 능력)과 신뢰도(일관성 유지 능력)를 구분하여 실패 원인을 분해 분석한다.
5. **15개 LLM, 200,000건 이상의 대화**를 통해 통계적으로 유의미한 결과를 도출한다.

**강점**

- 기존 벤치마크를 재활용하므로 별도의 대규모 데이터 수집 없이 새로운 평가 차원 추가 가능
- GPT-4.1부터 LLaMA-8B까지 규모를 막론하고 동일한 현상 관찰, 보편성 입증
- Microsoft Research에서 코드와 데이터셋 공개(github.com/microsoft/lost_in_conversation)
- 실패 원인을 구체적인 4가지 행동 패턴으로 분류하여 개선 방향 제시

**한계**

- 시뮬레이션된 멀티턴 대화이므로 실제 사용자와의 자연스러운 대화와 차이가 있을 수 있음
- 샤딩 과정이 반자동화되어 있어 분해 품질이 원본 과제에 따라 다를 수 있음
- 멀티턴 실패를 줄이는 구체적인 해결책(파인튜닝, 프롬프트 기법 등)은 논문에서 깊이 다루지 않음
- 성능 저하가 모델 크기나 아키텍처와 어떻게 관련되는지 상세 분석 부족

**알아둘 용어**

- **샤딩 (Sharding)**: 완전한 지시문을 여러 개의 작은 조각(샤드, shard)으로 분해하는 과정. 이 논문에서는 단일턴 과제를 멀티턴 대화로 변환하는 핵심 기법
- **멀티턴 대화 (Multi-Turn Conversation)**: 한 번의 메시지 교환이 아닌 여러 차례의 메시지 교환으로 이루어지는 대화 형식
- **신뢰도 (Reliability / Unreliability)**: 동일한 입력에 대해 LLM이 일관된 답변을 생성하는 능력. 이 논문에서는 멀티턴 환경에서 신뢰도가 112% 저하됨
- **적성 (Aptitude)**: 올바른 답변을 생성하는 고유한 능력. 멀티턴 환경에서 약 15~16% 저하
- **중간 턴 망각 현상 (Loss-of-Middle-Turns)**: LLM이 대화의 첫 번째와 마지막 턴에 지나치게 의존하고 중간 턴의 정보를 무시하는 현상
- **조기 답변 시도 (Premature Answer Attempt)**: LLM이 충분한 정보를 받기 전에 최종 답변을 먼저 제시하고 이후 수정하지 못하는 현상
- **샤드 시뮬레이션 (Sharded Simulation)**: 이 논문이 제안한 멀티턴 대화 평가 프레임워크로, 단일턴 벤치마크를 멀티턴 시나리오로 변환하는 방법론

**왜 주목할 만한가?**

ICLR 2026에서 Outstanding Paper로 선정된 이 연구는, 현재 AI 평가 패러다임의 근본적인 맹점을 드러낸다. 실제 사용자의 상당수는 완전한 지시 대신 점진적으로 정보를 제공하는데, 기존 벤치마크는 이를 전혀 고려하지 않는다. GPT-4.1, Claude 3.7 Sonnet, Gemini 2.5 Pro처럼 최신 SOTA 모델들도 예외 없이 같은 문제를 겪는다는 사실은, LLM 기반 제품을 개발하는 엔지니어와 평가 체계를 설계하는 연구자 모두에게 즉각적인 실천적 함의를 가진다.

---

## English Summary

**One-line summary**

A systematic study of 15 major LLMs across 200,000+ simulated multi-turn conversations finds that all models — from LLaMA-8B to Gemini 2.5 Pro — suffer an average 39% performance drop when instructions are delivered incrementally across turns rather than all at once. The paper was awarded Outstanding Paper at ICLR 2026, recognizing it as among the most impactful work at the conference.

**Core idea**

Real users rarely hand LLMs a perfectly specified single prompt. They converse, revealing intent piece by piece. Yet virtually all LLM benchmarks evaluate models in single-turn, fully-specified settings. This paper bridges that gap by introducing *sharded simulation*: a method that decomposes existing single-turn benchmark tasks into ordered atomic sub-instructions (shards) and replays them one turn at a time, creating scalable multi-turn evaluation without new data collection. The results show that every model tested degrades substantially and consistently — not because the model becomes less capable per se, but because it becomes radically less reliable when context arrives across multiple turns.

**What is new?**

- **Sharded simulation**: a scalable, semi-automatic method to repurpose any existing single-turn benchmark as a multi-turn evaluation suite, enabling broad and reproducible comparisons
- **Universal degradation finding**: a 39% average performance drop across 15 LLMs on 7 diverse tasks (code, math, database, actions, data2text, summarization, translation), showing no model is immune
- **Decomposed failure analysis**: separates degradation into aptitude loss (~15–16% drop) and unreliability increase (+112%), revealing that inconsistency — not incapability — is the main culprit
- **Four concrete failure modes** documented through behavioral analysis of 200,000+ conversations
- **Open benchmark and code** released for the community to reproduce and extend results

**How does it work?**

1. **Sharding**: A semi-automatic process breaks a complete, well-specified single-turn instruction into multiple atomic sub-instructions (shards) that together carry the full information. For example, a coding task becomes: turn 1 → "write a Python function", turn 2 → "the function should be named `process_data`", turn 3 → "it should take a list and return the sorted unique values."
2. **Simulation**: A conversation is simulated by feeding one shard per turn to the LLM and prompting it to respond, as a user would.
3. **Evaluation**: The model's final response at the end of the conversation is scored against the ground-truth answer from the original benchmark.
4. **Decomposition**: Performance is split into aptitude (quality when the model does answer correctly) and reliability (fraction of runs where the model produces a consistent correct answer), enabling root-cause analysis.
5. **Scale**: 15 models × multiple tasks × 10 simulation runs each = 200,000+ total conversations, ensuring statistical robustness.

**Strengths**

- The sharded simulation framework is model-agnostic and reuses existing benchmark infrastructure, making it cheap to apply to new models and tasks
- Results span a wide range of model families, sizes, and providers, strongly supporting generalizability
- Behavioral failure modes are actionable — they point directly at concrete engineering fixes (e.g., reducing verbosity, resisting premature commitment)
- Code and datasets are publicly available at [github.com/microsoft/lost_in_conversation](https://github.com/microsoft/lost_in_conversation)

**Limitations**

- Sharded conversations are machine-generated simulations; they may not perfectly capture the full diversity and naturalness of real human multi-turn interaction
- The sharding process is semi-automatic and quality may vary across task domains and instruction types
- The paper does not deeply explore solutions (fine-tuning strategies, prompting interventions) to mitigate the identified failures
- The relationship between model scale, architecture type (MoE vs. dense), and severity of degradation is not fully characterized

**Terms to know**

- **Sharded simulation**: the core method of this paper — breaking a single complete instruction into atomic sub-instructions delivered one turn at a time, to simulate multi-turn underspecified conversations
- **Multi-turn conversation**: a dialogue where context and instructions are spread across several exchanges rather than a single message
- **Aptitude**: a model's inherent ability to produce a correct answer when it engages properly with a task; drops ~15% in multi-turn settings
- **Unreliability**: inconsistency in outputs across repeated runs or turns; increases by ~112% in multi-turn settings — the primary driver of degradation
- **Loss-of-middle-turns**: the tendency of LLMs to overweight the first and last turns of a conversation and discount information revealed in middle turns
- **Premature answer attempt**: when a model commits to a full solution before all necessary constraints are known, then fails to correct itself as more information arrives
- **Sharding**: decomposing a fully-specified instruction into ordered atomic sub-instructions that together convey the same information

**Why it is worth watching**

Nearly every production LLM application — coding assistants, customer service bots, document editors, research tools — relies on multi-turn interaction. Yet the field's evaluation infrastructure is almost entirely single-turn. This paper, selected as an ICLR 2026 Outstanding Paper, provides the first large-scale systematic evidence of how badly all current models degrade in the setting that actually matters for deployment. For engineers building LLM products, the four failure modes offer a concrete diagnostic checklist. For researchers, the sharded simulation framework opens a new evaluation axis that existing benchmarks miss entirely.

**My take**

이 논문은 단순히 흥미로운 관찰을 넘어, LLM 평가 방법론 전체를 재검토하게 만드는 결과를 제시한다. 최고 성능 모델들이 멀티턴 환경에서 이렇게 급격히 저하된다는 사실은 놀랍지만, 동시에 연구 커뮤니티가 이 문제를 그동안 얼마나 체계적으로 측정하지 못했는지를 보여준다. 샤드 시뮬레이션 방법론 자체는 우아하고 실용적이다.

This paper is more than an interesting observation — it forces a rethink of how the field evaluates LLMs. The magnitude of the drop (39%) across all tested models, including the best available at the time, is striking. The sharded simulation methodology is elegant and immediately actionable. Its selection as an ICLR 2026 Outstanding Paper reflects both the quality of the work and the importance of the problem it exposes.
