---
title: "Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent"
date: 2026-07-01
topic: AI
tags: [AI, LLM, agents, MoE, distillation, long-horizon, agentic-AI, inference-efficiency, multi-agent]
source: https://arxiv.org/abs/2606.30616
---

# Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent

* Date: 2026-07-01
* Source: https://arxiv.org/abs/2606.30616
* Topic: AI
* Why it matters: Agents-A1 is a 35B Mixture-of-Experts model from Shanghai AI Laboratory that matches or exceeds the performance of trillion-parameter frontier models on long-horizon agentic tasks — not by scaling model size, but by systematically scaling the length and diversity of agent training trajectories and unifying six specialized teachers through multi-teacher distillation.

## Korean Summary

**한줄 요약**

상하이인공지능연구원(Shanghai AI Lab)이 공개한 Agents-A1은 35B 파라미터 MoE(전문가 혼합) 모델이지만, 1조(1T) 파라미터급 최신 모델들과 비슷하거나 이를 능가하는 에이전트 작업 성능을 달성합니다. 핵심 전략은 모델 크기가 아닌 '에이전트 지평선(agent horizon)'을 확장하는 것으로, 평균 45,000 토큰에 달하는 장기 지식-행동 궤적과 6개 이질적 도메인의 전문 교사 모델을 활용합니다.

**핵심 아이디어**

AI 에이전트 연구의 주류는 단순히 더 큰 모델을 학습하는 방향이었습니다. 그러나 모델 크기를 수십 배 늘리는 것은 학습·추론 비용을 기하급수적으로 높여 현실 배포가 어렵습니다. 이 논문은 대안적 스케일링 축, 즉 **에이전트 지평선(agent horizon)** 을 제안합니다. 에이전트 지평선이란 두 가지를 의미합니다: (1) 얼마나 긴 궤적(장기적 추론·행동 연쇄)으로 학습하는가, (2) 얼마나 다양한 이질적 도메인의 능력을 하나의 모델에 통합하는가.

Agents-A1은 외부 지식 검색, 행동 실행, 관측 결과, 검증기 피드백을 연결하는 **장기 지식-행동 인프라**를 구축하고, 이를 통해 평균 45K 토큰 분량의 장기 에이전트 궤적 데이터를 생성합니다. 이 데이터로 기반 모델을 전체 도메인 SFT로 정렬한 뒤, 각 도메인 전문 교사 모델을 별도 학습하고, 마지막으로 **다중 교사 도메인 라우팅 온-폴리시 증류(multi-teacher domain-routed on-policy distillation)** 로 6개 교사 모델의 능력을 35B 단일 학생 모델로 통합합니다. 핵심 기법인 **두드러진 어휘 정렬(Salient Vocabulary Alignment)** 은 서로 다른 도메인 간 지식 전달 효율을 높입니다.

**무엇이 새로운가?**

1. **에이전트 지평선 스케일링** 개념의 체계적 제안: 모델 크기 대신 궤적 길이(평균 45K 토큰)와 도메인 이질성이라는 두 축으로 에이전트 성능을 확장
2. **장기 지식-행동 인프라**: 외부 지식 → 행동 → 관측 → 검증기 출력을 연결하는 데이터 생성 파이프라인 구축
3. **다중 교사 도메인 라우팅 온-폴리시 증류**: 6개 이질적 도메인의 전문 교사를 하나의 배포 가능한 35B 학생 모델로 통합하는 학습 방법
4. **두드러진 어휘 정렬(Salient Vocabulary Alignment)**: 도메인 간 어휘 분포 차이를 극복하여 지식 전달 효율을 높이는 증류 기법
5. **오픈-웨이트 공개**: Apache 2.0 라이선스로 모델 가중치와 코드를 완전 공개하여 재현 및 연구 활용 가능

**어떻게 작동하는가?**

1. **장기 궤적 데이터 수집**: 검색, 과학 연구, 소프트웨어 엔지니어링, 일반 에이전트 작업, 지시 따르기, 도구 호출 등 6개 도메인에서 외부 지식 검색 → 행동 실행 → 환경 관측 → 검증기 피드백의 루프로 평균 45K 토큰 길이의 장기 에이전트 궤적 데이터를 자동 생성합니다.
2. **전체 도메인 SFT (1단계)**: Qwen3.5-35B-A3B 기반 모델을 6개 도메인의 장기 궤적 데이터 전체로 감독 학습 미세조정하여 폭넓은 에이전트 행동 패턴을 정렬합니다.
3. **도메인별 교사 모델 학습 (2단계)**: 각 도메인(예: 검색 전문, 과학 연구 전문, 엔지니어링 전문 등)에 특화된 교사 모델을 별도로 학습시켜 각 도메인의 깊은 전문성을 포착합니다.
4. **다중 교사 온-폴리시 증류 (3단계)**: 학생 모델(35B)이 실시간으로 생성한 궤적에 대해 각 도메인 교사 모델이 지도를 제공하는 온-폴리시 방식으로 6개 교사의 지식을 통합합니다. 도메인 라우터가 적절한 교사를 선택하고, 두드러진 어휘 정렬이 도메인 간 어휘 분포 차이를 보정합니다.
5. **통합 배포 모델**: 3단계를 거쳐 6개 도메인 전문성이 하나의 35B MoE 모델(추론 시 3B 파라미터 활성화)에 통합되어, 단일 모델로 다양한 장기 에이전트 작업을 처리할 수 있습니다.

**강점**

- 추론 시 활성 파라미터 3B로 1T+ 모델에 근접한 성능을 달성해 배포 비용을 대폭 절감
- 6개 이질적 도메인을 단일 모델에 통합하여 실용적인 범용 에이전트 구현
- Apache 2.0 오픈-웨이트 공개로 학계·산업계 즉시 활용 가능
- 온-폴리시 증류로 학생 모델 스스로의 분포에 맞춘 지식 전달 가능
- 장기 궤적 스케일링이라는 새로운 차원의 에이전트 개선 경로를 입증

**한계**

- "1조 파라미터 수준 성능"은 특정 벤치마크 기준이며, 모든 작업 영역에서 실제 1T 모델을 능가한다는 보장은 없음
- 45K 토큰 장기 궤적 데이터의 자동 생성·검증에는 상당한 컴퓨팅 자원이 필요
- MoE 아키텍처 특성상 전체 35B 가중치를 메모리에 적재해야 하므로, 실제 하드웨어 요구사항은 3B 밀집 모델보다 훨씬 높음
- 6개 도메인 이외의 전문 영역(예: 의료 코딩, 법률 추론 등)에서의 성능은 별도 검증이 필요
- 학습에 사용된 도메인별 교사 모델의 품질이 최종 학생 모델 성능의 상한을 결정하는 구조적 제약 존재
- 아카이브 프리프린트 단계이므로 동료 심사를 아직 통과하지 않음

**알아둘 용어**

- **MoE (Mixture of Experts, 전문가 혼합)**: 모델의 각 입력마다 전체 파라미터 중 일부(전문가 집합)만 선택적으로 활성화하는 아키텍처; 전체 파라미터는 많지만 추론 시 활성 파라미터는 적어 효율적
- **에이전트 지평선 (Agent Horizon)**: 에이전트가 하나의 작업을 수행하는 동안 유지하는 추론·행동 연쇄의 길이 및 다양성을 나타내는 개념
- **온-폴리시 증류 (On-policy Distillation)**: 학생 모델이 자신의 현재 정책으로 생성한 샘플에 대해 교사 모델이 지도를 제공하는 지식 증류 방식
- **두드러진 어휘 정렬 (Salient Vocabulary Alignment)**: 서로 다른 도메인(또는 모델) 간 어휘 분포 차이를 식별하고 보정하여 지식 전달 효율을 높이는 기법
- **지식-행동 궤적 (Knowledge-Action Trajectory)**: 에이전트가 외부 지식을 검색하고, 행동을 취하며, 환경으로부터 관측 및 검증 피드백을 받는 전 과정을 타임라인으로 기록한 데이터
- **SEAL-0**: 장기 검색 에이전트 능력을 평가하는 벤치마크 (Search Agent Leaderboard-level 0)
- **FrontierScience**: 최전선 과학 연구 수행 능력을 평가하는 에이전트 벤치마크 시리즈 (올림피아드 및 연구 수준 하위 트랙)

**왜 주목할 만한가?**

AI 에이전트 분야에서 성능 향상의 주된 방법은 모델 크기를 키우는 것이었으나, 이는 배포 비용과 접근성 측면에서 심각한 병목이 됩니다. Agents-A1은 모델 크기를 늘리는 대신 '얼마나 오래, 얼마나 다양하게 행동하는가'라는 에이전트 지평선을 키우는 것이 더 효율적인 스케일링 경로임을 보여줍니다. 또한 오픈-웨이트로 공개된 점에서 소규모 연구그룹이나 기업도 최전선 에이전트 성능을 활용·개선할 수 있는 현실적인 기반이 됩니다.

---

## English Summary

**One-line summary**

Agents-A1, a 35B Mixture-of-Experts agent from Shanghai AI Laboratory's InternScience group, achieves performance competitive with trillion-parameter frontier models on long-horizon agentic benchmarks. Rather than scaling model parameters, it scales the agent horizon — the length and domain diversity of training trajectories — combined with a three-stage pipeline that distills six specialized teacher models into a single deployable student. The model is released as open weights under Apache 2.0.

**Core idea**

The dominant path to better AI agents has been training larger models. But scaling to 1 trillion parameters is enormously expensive and limits who can deploy or improve such systems. Agents-A1 proposes a different axis: scale the **agent horizon** instead of the parameter count. Agent horizon has two dimensions: (1) how long the reasoning-and-action chains used during training are, and (2) how many heterogeneous capability domains are unified in one model.

To operationalize this, the team builds a **long-horizon knowledge-action infrastructure** that chains together external knowledge retrieval, action execution, environmental observations, and verifier feedback into coherent trajectories averaging 45K tokens in length. They then train through three stages: broad alignment via full-domain supervised fine-tuning, specialization into six domain-level teacher models, and finally multi-teacher domain-routed on-policy distillation with salient vocabulary alignment to unify all teachers into a single 35B student model. At inference, only 3B parameters are active (MoE routing), making the model cheap to run despite its 35B total parameter count.

**What is new?**

1. **Agent-horizon scaling** as a principled alternative to parameter scaling: demonstrated that systematically increasing trajectory length (45K tokens on average) and domain breadth produces frontier-level agent capability in a compact model
2. **Long-horizon knowledge-action infrastructure**: an automated data pipeline that connects external knowledge retrieval, executable actions, environment observations, and outcome verification to produce multi-step agentic training data at scale
3. **Multi-teacher domain-routed on-policy distillation**: a three-stage training recipe that first trains six specialized domain teachers and then distills them into one student model using the student's own live rollouts as training signal
4. **Salient vocabulary alignment**: a novel component of the distillation process that identifies and compensates for vocabulary distribution differences across domains, improving cross-domain knowledge transfer fidelity
5. **Fully open-weight release** under Apache 2.0, including model weights and training code, enabling broad community research and deployment

**How does it work?**

1. **Trajectory data collection**: Across six domains (web search, scientific research, software engineering, general agentic tasks, instruction following, tool calling), the infrastructure automatically runs loops of knowledge retrieval → action execution → environment observation → verifier feedback, producing agentic trajectories averaging 45K tokens each.
2. **Stage 1 — Full-domain SFT**: The base model (Qwen3.5-35B-A3B) is supervised fine-tuned on trajectories from all six domains together, giving it broad coverage of agentic behaviors as a starting point.
3. **Stage 2 — Domain-level teacher training**: Six specialized teacher models are fine-tuned independently, each focusing on deep expertise in one domain (e.g., one for long-horizon search, one for scientific reasoning, one for software engineering). This extracts specialized knowledge that the broad SFT step would otherwise dilute.
4. **Stage 3 — Multi-teacher on-policy distillation**: The student model generates its own live trajectories (on-policy), and domain-specific teachers provide corrective supervision on those rollouts. A domain router selects the appropriate teacher for each trajectory, and salient vocabulary alignment compensates for distribution mismatches between domain vocabularies. The combined signal from all six teachers updates a single student model.
5. **Deployment**: The resulting 35B MoE model activates only ~3B parameters per forward pass, making inference substantially cheaper than dense models of comparable benchmark performance while covering all six domains within a single set of weights.

**Strengths**

- Inference cost scales with active parameters (3B), not total parameters (35B), enabling deployment at a fraction of the cost of 1T dense models
- Six heterogeneous domains unified in one model, covering a wide range of real-world agentic use cases
- Fully open-weight with Apache 2.0 license, democratizing access to near-frontier agentic performance
- On-policy distillation ensures knowledge transfer is calibrated to the student model's own behavior distribution, reducing distribution mismatch
- Demonstrates a replicable scaling paradigm (longer and more diverse trajectories) that doesn't require exponentially more compute at inference

**Limitations**

- "Trillion-parameter parity" is benchmark-specific; on tasks outside the six training domains, performance gaps versus actual 1T models may persist
- Collecting high-quality long-horizon trajectory data (45K tokens per trajectory) requires significant compute and well-designed environments for each domain
- MoE models require loading all 35B weights into memory, so the hardware requirements are much higher than a dense 3B model despite matching active parameter counts
- Performance in specialized domains not covered in the six training areas (e.g., medical coding, legal reasoning) has not been characterized
- Quality of the final student is ultimately bounded by the quality of each domain-level teacher; weak teacher models propagate errors
- Preprint only; peer review has not yet occurred

**Terms to know**

- **Mixture of Experts (MoE)**: A neural network architecture that activates only a subset of parameters (experts) for each input token, keeping inference cost proportional to active parameters rather than total parameters
- **Agent horizon**: The length and domain diversity of the reasoning-action sequences an agent executes; the central scaling axis in this paper
- **On-policy distillation**: A form of knowledge distillation where the student model's own live rollouts (rather than fixed static data) are used as training inputs, with teacher models providing corrective signals on those rollouts
- **Salient vocabulary alignment**: A technique to identify and correct for vocabulary distribution differences across domains during distillation, enabling more faithful knowledge transfer between domain-specific teachers and a unified student model
- **Knowledge-action trajectory**: A recorded sequence in which an agent retrieves external knowledge, takes actions, receives environmental observations, and obtains verification feedback — the fundamental unit of agentic training data in this work
- **SEAL-0**: A long-horizon search agent benchmark used to assess multi-step information retrieval and synthesis capabilities
- **FrontierScience**: A family of benchmarks assessing an agent's ability to conduct scientific research at the frontier level, with Olympiad (problem-solving) and Research (open-ended discovery) sub-tracks

**Why it is worth watching**

The trend in AI agent development has been to build ever-larger models, but this creates a steep cost barrier that concentrates frontier capabilities in a small number of well-resourced organizations. Agents-A1 offers evidence that a carefully designed training pipeline — one that scales trajectory length and domain diversity rather than raw parameter count — can reach comparable performance at a fraction of the deployment cost. Combined with full open-weight release, this is a practical foundation for the broader research community to build and improve upon. The paper also highlights that agent performance may be more sensitive to *what the model learns to do across time* than to raw model size, a finding that could reorient near-term research priorities in agentic AI.

**My take**

단순히 모델 크기를 키우는 경쟁에서 벗어나 에이전트 학습 데이터의 질적·시간적 깊이를 늘리는 방향이 효율적임을 보인 점은 주목할 만합니다. 특히 오픈-웨이트 공개가 소규모 연구팀에게 실질적인 기회를 제공합니다. 다만 6개 도메인에 집중된 평가이고 동료 심사를 거치지 않은 프리프린트이므로, 결과의 일반화 가능성과 재현성은 독립적 검증이 필요합니다.

This work makes a compelling case that agent training quality — particularly trajectory length and domain breadth — may matter as much as raw model size. The open-weight release is practically significant. That said, the benchmark suite is specific to the model's training domains, and the paper has not yet been peer-reviewed, so independent reproduction and evaluation outside the reported benchmarks is warranted before drawing strong conclusions.
