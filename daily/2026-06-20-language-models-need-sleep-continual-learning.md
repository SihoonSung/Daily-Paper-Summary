---
title: "Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories"
date: 2026-06-20
topic: AI
tags: [AI, LLM, continual-learning, knowledge-distillation, reinforcement-learning, memory-consolidation, self-improvement, catastrophic-forgetting]
source: https://arxiv.org/abs/2606.03979
---

# Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories

* Date: 2026-06-20
* Source: https://arxiv.org/abs/2606.03979
* Topic: AI / Continual Learning / LLM
* Why it matters: 현재 LLM의 근본적 한계—배포 이후 경험에서 지식을 영구적으로 흡수하지 못한다는 것—를 인간의 수면·기억 공고화 메커니즘에서 영감을 얻은 Sleep 패러다임으로 해결한다. 장기 에이전트나 지속적으로 진화하는 AI 시스템에 필수적인 기반 기술이 될 수 있다.

---

## Korean Summary

**한줄 요약**

LLM은 문맥 내(in-context)에서는 잘 학습하지만 그 지식을 파라미터에 영구 저장하지 못한다. 이 논문은 수면의 두 단계—메모리 공고화와 꿈(Dreaming)—를 모방한 Sleep 패러다임을 도입해 모델이 배포 중에 경험한 지식을 장기 파라미터로 지속적으로 통합할 수 있게 한다.

**핵심 아이디어**

현재 LLM은 사전 훈련된 파라미터에 지식을 고정한 채 배포되며, 문맥 내 학습은 일회성이고 세션 종료 시 소멸한다. Sleep 패러다임은 인간이 수면 중 단기 기억을 장기 기억으로 통합하는 과정에서 착안하여, 두 단계를 통해 모델이 점진적으로 지식을 흡수하고 스스로를 개선하도록 한다: (1) Knowledge Seeding이라 불리는 상향 증류(upward distillation)로 소형 모델의 기억을 대형 모델에 통합하고, (2) Dreaming 단계에서 RL을 활용해 합성 데이터 커리큘럼을 자동 생성하여 인간 감독 없이 자기 개선을 수행한다.

**무엇이 새로운가?**

- **상향 증류(Upward distillation)**: 기존 지식 증류는 큰 모델→작은 모델 방향이지만, 여기서는 반대 방향(소형 자신 → 대형 자신)으로 메모리를 이전해 용량을 확장하면서 지식을 보존
- **Sleep 패러다임**: 문맥 내 단기 기억을 장기 파라미터로 공고화하는 최초의 완전한 프레임워크
- **Dreaming 단계**: RL을 활용해 합성 데이터 커리큘럼을 생성하고 자기 개선을 수행 — 인간 라벨링 불필요
- **지속적 학습과 자기 수정의 결합**: 연속 학습(catastrophic forgetting 방지)과 파라미터 자기 수정을 하나의 통합 파이프라인으로 처리
- ICLR 2026에서 peer-review를 통과한 검증된 접근법

**어떻게 작동하는가?**

1. **운영 단계(Awake)**: 모델이 일반적으로 배포되어 사용자와 상호작용하며 새로운 지식을 문맥 내 메모리로 축적한다. 이 기억은 현재 세션에만 존재하는 단기 기억이다.

2. **Memory Consolidation — Knowledge Seeding**: 모델이 "잠드는" 단계. 현재 모델(소형 자신)이 문맥에서 획득한 지식을 더 큰 네트워크(대형 자신)로 상향 증류한다. 소형→대형 방향이기 때문에 용량이 증가하면서 기존 지식의 손실(catastrophic forgetting)이 최소화된다.

3. **Dreaming**: 대형 모델이 RL을 활용해 새로운 지식과 기존 역량을 연습하는 합성 데이터 커리큘럼을 자동 생성한다. 인간 감독 없이 자기 개선 사이클을 완성한다.

4. **다음 Awake 단계**: 이제 더 크고 업데이트된 모델이 이후 상호작용에서 통합된 지식을 바탕으로 더 나은 성능을 보인다.

**강점**

- LLM의 핵심 한계인 "배포 후 학습 불가"를 생물학적으로 동기화된 방식으로 해결
- 상향 증류는 catastrophic forgetting을 방지하면서 모델 용량을 자연스럽게 확장
- Dreaming 단계는 인간 라벨링 없이 자기 개선을 가능하게 함으로써 지속적 학습의 비용 문제 완화
- 장기 에이전트, 개인화 AI, 지식 축적이 중요한 응용 분야에 직접 적용 가능
- ICLR 2026 채택으로 peer-review를 거친 검증된 방법

**한계**

- 상향 증류 후 모델이 커짐에 따라 추론 비용이 증가할 수 있어 실제 배포 시 제약이 될 수 있음
- Dreaming 단계에서 RL 기반 합성 커리큘럼이 잘못된 지식을 강화하거나 편향을 확대할 가능성이 있음
- 특정 벤치마크에서의 정량적 이득이 자세히 공개되지 않아 실제 효과 크기 파악이 어려움
- 매우 긴 배포 기간 동안 수면 사이클을 어떻게 스케줄링하는지, 언제 "잠재울지" 결정하는 정책이 명확히 제시되지 않음
- 현재 평가가 실험 환경에 국한되어 있어 실제 프로덕션 시스템에서의 검증이 필요

**알아둘 용어**

- **지속적 학습 (Continual Learning)**: 새로운 정보를 이전 지식 손실 없이 점진적으로 학습하는 능력. "Catastrophic forgetting" 문제 해결이 핵심
- **파국적 망각 (Catastrophic Forgetting)**: 신경망이 새로운 작업을 학습할 때 이전에 학습한 정보를 급격히 잊어버리는 현상
- **문맥 내 학습 (In-Context Learning, ICL)**: 모델이 파라미터 업데이트 없이 프롬프트 내 예시만으로 새로운 작업을 수행하는 능력. 현재 LLM의 핵심 기능이지만 일회성임
- **상향 증류 (Upward Distillation / Knowledge Seeding)**: 소형 모델의 지식을 대형 모델로 전이하는 비전통적 증류 방향. 기존 증류(큰→작은)와 반대
- **Dreaming**: RL을 사용해 모델이 자체적으로 합성 데이터 커리큘럼을 생성하고 스스로를 개선하는 자기 지도 학습 단계
- **Sleep 패러다임**: 이 논문이 제안하는 전체 프레임워크로, 인간 수면의 메모리 공고화와 렘수면의 기억 정리 기능을 LLM에 맞게 구현한 것
- **파라미터 자기 수정 (Parameter Self-Modification)**: 모델이 외부 훈련 없이 자신의 가중치를 업데이트하는 과정

**왜 주목할 만한가?**

현재 LLM 생태계에서 가장 미해결 상태인 문제 중 하나가 "배포 후 학습"이다. ChatGPT든 Claude든 모델은 고정된 스냅샷을 배포하며, 사용자와의 수백만 번의 상호작용에서 얻는 지식을 다음 버전 훈련에 활용하기까지 오랜 주기가 필요하다. 이 논문은 수면이라는 직관적 은유를 통해 단기 기억→장기 파라미터 통합 사이클을 기술적으로 구현함으로써, 진정한 의미의 "경험에서 배우는 AI"를 향한 중요한 발걸음을 제시한다.

---

## English Summary

**One-line summary**

Current LLMs can learn temporarily from context but cannot absorb that knowledge into their long-term parameters. This paper introduces a biologically-inspired "Sleep" paradigm — drawing on how humans consolidate memories during sleep — that enables LLMs to continually transfer in-context learning into permanent model weights through two stages: Knowledge Seeding (upward distillation) and Dreaming (RL-based self-improvement), without human supervision.

**Core idea**

LLMs today are frozen snapshots: they learn from in-context examples during a session, but that knowledge evaporates when the context ends. The Sleep paradigm proposes that, like humans during sleep, LLMs should periodically consolidate their transient in-context memories into stable long-term parameters. This is done via upward distillation from a smaller "self" to a larger one (Memory Consolidation), followed by a Dreaming stage in which the model uses reinforcement learning to generate a synthetic training curriculum and rehearse new knowledge, self-improving without human-labeled data. The result is a continual learner that grows and refines itself from experience.

**What is new?**

- **Upward distillation (Knowledge Seeding)**: Conventional knowledge distillation compresses large to small; here the direction is reversed — a smaller model's memories are distilled upward into a larger network, expanding capacity while preserving existing knowledge and resisting catastrophic forgetting
- **Sleep paradigm**: The first unified framework for translating temporary in-context learning into permanent parameter updates in LLMs
- **Dreaming stage**: RL-driven synthetic curriculum generation for unsupervised self-improvement, eliminating the need for human annotation during learning cycles
- **Continual learning + self-modification**: Addresses both the forgetting problem (via upward distillation) and the stagnation problem (via Dreaming) in a single integrated pipeline
- Peer-reviewed and accepted at ICLR 2026

**How does it work?**

1. **Awake phase**: The model operates in normal deployment, interacting with users and accumulating new knowledge as transient in-context memories. These memories are short-lived and session-local.

2. **Memory Consolidation — Knowledge Seeding**: During the "sleep" phase, the model's current state (smaller self) undergoes upward distillation: the in-context memories it has accumulated are distilled into a larger network version of itself. Because the target is larger, catastrophic forgetting of previously learned knowledge is substantially reduced while capacity grows.

3. **Dreaming**: The enlarged model uses reinforcement learning to automatically generate a synthetic data curriculum. This curriculum rehearses both the newly acquired knowledge and existing capabilities, enabling self-improvement without human supervision or new labeled data.

4. **Return to Awake**: The updated, larger model resumes interactions with consolidated knowledge, outperforming its pre-sleep self on subsequent tasks.

**Strengths**

- Addresses a fundamental and largely unsolved limitation of current LLMs: the inability to learn persistently from deployment experience
- Upward distillation naturally expands model capacity while guarding against catastrophic forgetting — a common failure mode in continual learning
- The Dreaming stage enables continuous self-improvement without human annotation, reducing the cost bottleneck of supervised continual learning
- Directly applicable to long-horizon agents, personalized AI assistants, and any domain where accumulated knowledge matters
- Peer-reviewed at ICLR 2026, one of the top venues in machine learning

**Limitations**

- Growing model size through upward distillation increases inference cost over time; deployment feasibility at scale is not fully addressed
- RL-based synthetic curriculum in the Dreaming stage may inadvertently reinforce errors or amplify biases rather than correcting them
- The paper does not report detailed quantitative results on specific benchmarks, making it difficult to assess the magnitude of improvement
- The policy for deciding when and how often a model should "sleep" in a production system is not elaborated
- Evaluation remains in controlled experimental settings; real-world production deployment has not been demonstrated

**Terms to know**

- **Continual learning**: The ability to learn new information progressively without losing previously acquired knowledge. The core challenge is "catastrophic forgetting."
- **Catastrophic forgetting**: The tendency of neural networks to abruptly lose previously learned knowledge when trained on new tasks.
- **In-context learning (ICL)**: The ability of LLMs to perform new tasks using only examples in the prompt, without updating model parameters. Powerful but transient.
- **Knowledge Seeding (Upward distillation)**: A distillation process that transfers a smaller model's knowledge upward into a larger network — the reverse of the usual compress-to-small direction.
- **Dreaming**: The self-supervised RL stage in which the model generates a synthetic curriculum to rehearse and refine both new and existing knowledge without human labels.
- **Sleep paradigm**: The overarching framework in this paper, inspired by how biological sleep consolidates short-term episodic memories into long-term semantic memory.
- **Parameter self-modification**: The process by which a model updates its own weights in response to experience, without external training pipelines.

**Why it is worth watching**

One of the most glaring unresolved problems in deploying LLMs at scale is the gap between the enormous implicit knowledge that accumulates across billions of user interactions and the inability of deployed models to absorb any of it until a full new training run is completed. The Sleep paradigm offers a principled, biologically-motivated framework for closing that gap. If the upward distillation and Dreaming mechanisms can be shown to work reliably at production scale, this could shift the standard model for LLM deployment from "frozen snapshot + periodic retrain" to a continuous self-updating architecture — a qualitatively different and more powerful operational paradigm.

**My take**

한국어: 아이디어 자체는 직관적이고 생물학적으로 잘 동기화되어 있다. "상향 증류"라는 접근은 catastrophic forgetting을 우회하는 영리한 방법이지만, 모델이 점점 커진다는 점에서 실제 배포 환경에서의 지속 가능성이 중요한 과제로 남는다. Dreaming 단계의 RL 기반 자기 개선이 실제로 얼마나 신뢰할 수 있는지—특히 오류나 편향 증폭 리스크—에 대해 독립적 검증이 필요하다. ICLR 2026 채택은 기술적 엄밀성을 어느 정도 보장하지만, 실제 장기 배포 시나리오에서의 검증이 이 접근법의 실용성을 판단하는 진짜 시험대가 될 것이다.

English: The core idea is intuitive and well-motivated by biology. Upward distillation is a clever mechanism for avoiding catastrophic forgetting, but the fact that the model grows with each sleep cycle raises real sustainability questions at production scale. The Dreaming stage's RL-based self-improvement sounds promising but needs independent scrutiny for reliability — specifically whether it can inadvertently amplify errors or biases. ICLR 2026 acceptance provides a reasonable floor of rigor, but the true test of this framework's value will come from long-horizon real-world deployment, which is yet to be demonstrated.
