---
title: "Thinking in Text and Images: Interleaved Vision-Language Reasoning Traces for Long-Horizon Robot Manipulation"
date: 2026-05-05
topic: robotics
tags: [robotics, VLA, vision-language, reasoning, manipulation, embodied-AI]
source: https://arxiv.org/abs/2605.00438
---

Thinking in Text and Images: Interleaved Vision--Language Reasoning Traces for Long-Horizon Robot Manipulation

* Date: 2026-05-01
* Source: https://arxiv.org/abs/2605.00438
* Topic: robotics
* Why it matters: Long-horizon robotic manipulation demands plans that are both logically ordered and spatially grounded — a combination that existing text-only or vision-only approaches each fail to fully provide. This paper introduces a new intermediate representation that interleaves textual subgoals with visual keyframes, achieving 92.4% success on the demanding LIBERO-Long benchmark.

## Korean Summary

**한줄 요약**

로봇이 긴 작업 순서를 수행하려면 논리적 계획과 공간적 파악이 동시에 필요하다. IVLR은 텍스트 목표와 시각적 키프레임을 교대로 배치한 새로운 중간 표현을 도입하여, 로봇 정책이 이 두 가지를 함께 활용하게 한다. 기존의 텍스트 전용 또는 시각 전용 방식보다 훨씬 높은 성공률을 달성했다.

**핵심 아이디어**

로봇이 작업을 수행하기 전에, 하나의 멀티모달 트랜스포머가 초기 관찰과 지시만을 보고 작업 전체를 아우르는 "IVLR-Trace"를 자동 생성한다. 이 트레이스는 텍스트 서브목표("집게를 컵 위로 이동")와 시각적 키프레임(해당 단계 완료 후 장면 예측)이 번갈아 나타나는 구조다. 생성된 트레이스는 캐시되어, 매 시점마다 실제 관찰과 함께 액션 디코더에 입력된다.

**무엇이 새로운가?**

- IVLR-Trace: 텍스트 서브목표와 시각 키프레임을 교대로 배치한 새로운 중간 표현
- 단일 네이티브 멀티모달 트랜스포머가 초기 관찰만으로 전체 트레이스를 자기회귀적으로 생성
- 생성된 트레이스를 캐시한 뒤, 폐루프(closed-loop) 액션 디코더가 이를 조건으로 동작
- 텍스트 전용(62.0%)과 시각 전용(68.4%) 대비 완전 교차 모달(92.4%) 방식의 우위를 절제 실험으로 증명
- LIBERO-Long에서 트레이스 없이 37.7%에 불과했던 성공률을 92.4%로 크게 향상

**어떻게 작동하는가?**

1. 입력: 초기 관찰 이미지 + 자연어 작업 지시
2. 트레이스 생성: 멀티모달 트랜스포머가 IVLR-Trace를 자기회귀적으로 생성 — 텍스트 서브목표와 시각 키프레임이 교대로 등장
3. 캐시: 생성된 트레이스 전체를 저장
4. 실행: 폐루프 액션 디코더가 캐시된 트레이스, 원래 지시, 현재 관찰을 함께 참조하여 매 스텝 행동 출력
5. 결과: 텍스트와 이미지 두 모달리티의 계획 정보가 결합되어 공간적·의미적으로 일관된 정책 실현

**강점**

- 두 모달리티의 강점 결합: 텍스트는 인과적 순서를, 시각은 공간적 제약을 담당
- 수동 레이블 불필요: 트랜스포머가 트레이스를 스스로 생성
- LIBERO 시리즈에서 95.5% 평균 성공률, LIBERO-Long에서 92.4% 달성
- SimplerEnv-WidowX(실제 로봇 설정 반영)에서 59.4% 전체 성공률
- 절제 실험을 통해 두 모달리티 모두 필수임을 정량적으로 입증

**한계**

- 트레이스는 초기 관찰만으로 생성 — 예상치 못한 환경 변화에 대한 트레이스 재생성 메커니즘 미검토
- LIBERO는 시뮬레이션 환경 기반이며, 실제 로봇 대규모 실험은 제한적
- 트레이스 생성에 추가 추론 비용 발생 (지연 증가 가능)
- 다양한 실제 환경 및 작업 카테고리로의 일반화 능력 미검증
- 긴 시퀀스에서 시각 키프레임의 누적 오류가 미치는 영향 불명확

**알아둘 용어**

- **VLA (Vision-Language-Action)**: 시각·언어 입력을 받아 로봇 행동을 출력하는 정책 모델
- **IVLR-Trace**: Interleaved Vision-Language Reasoning Trace — 텍스트 서브목표와 시각 키프레임이 교대로 나타나는 중간 표현
- **키프레임 (Keyframe)**: 특정 서브목표 완료 후 장면이 어떤 모습일지를 예측한 시각 이미지
- **폐루프 제어 (Closed-loop control)**: 매 스텝 현재 관찰을 반영하여 행동을 결정하는 방식 (사전 계획만 따르는 개루프와 대비)
- **LIBERO**: 장기 로봇 조작 작업을 위한 벤치마크 (LIBERO-Long은 더 어려운 장기 과제 세트)
- **SimplerEnv-WidowX**: 실제 WidowX 로봇 환경을 반영한 평가 벤치마크
- **멀티모달 트랜스포머**: 텍스트와 이미지를 동시에 처리·생성할 수 있는 트랜스포머 모델

**왜 주목할 만한가?**

로봇이 복잡한 작업을 수행하려면 인간처럼 언어로 계획을 세우면서 동시에 공간적으로 상황을 상상해야 한다. 기존 VLA 정책들은 이 둘 중 하나만 잘 하는 경향이 있었다. IVLR은 텍스트와 이미지를 교대로 배치한 명시적 중간 표현을 도입함으로써, 단일 멀티모달 모델이 두 능력을 자연스럽게 결합하도록 만들었다. 이 접근법은 강화학습 기반 훈련 없이도 작동하며, 로봇 정책 설계의 새로운 방향을 제시한다.

---

## English Summary

**One-line summary**

Long-horizon robotic manipulation requires plans that are both causally ordered and spatially grounded; IVLR achieves this by having a single multimodal transformer generate interleaved text subgoals and visual keyframes before execution, which a closed-loop action decoder then uses to produce robot actions. On the demanding LIBERO-Long benchmark, this approach reaches 92.4% success — versus 62% for text-only and 68.4% for vision-only traces.

**Core idea**

Before the robot takes any action, a native multimodal transformer reads the initial observation and task instruction, then autoregressively generates an IVLR-Trace: a sequence that alternates textual subgoals (e.g., "move gripper above the cup") with visual keyframes (predicted images of what the scene should look like after each subgoal is achieved). This trace is cached once and then provided as a fixed conditioning context to a closed-loop action decoder, which also sees the original instruction and the current live observation at each timestep.

**What is new?**

- IVLR-Trace: a new intermediate representation that interleaves text subgoals and predicted visual keyframes over the full task horizon
- A single native multimodal transformer self-generates the trace autoregressively from the initial observation alone — no manual annotation or retrieval needed
- The cached trace conditions a closed-loop action decoder, combining global semantic-geometric planning with reactive execution
- Ablations formally quantify the necessity of both modalities: text-only reaches 62.0%, vision-only 68.4%, full interleaved 92.4% on LIBERO-Long
- The approach lifts LIBERO-Long success from 37.7% (no trace) to 92.4%

**How does it work?**

1. **Input**: initial scene image + natural language task instruction
2. **Trace generation**: a multimodal transformer autoregressively produces the IVLR-Trace — alternating between a textual subgoal and a visual keyframe prediction at each step of the task
3. **Caching**: the full trace is stored before execution begins
4. **Execution**: at every robot timestep, a closed-loop action decoder takes the cached trace, the original instruction, and the current observation as input to output the next action
5. **Result**: text captures causal ordering and semantics; visual keyframes supply geometric and spatial grounding; together they yield coherent, spatially precise long-horizon policies

**Strengths**

- Combines the complementary strengths of text (causal structure) and vision (spatial grounding) in a single unified representation
- No manual trace annotation: the model generates traces from the initial observation alone
- Strong results: 95.5% average success on LIBERO suite, 92.4% on LIBERO-Long, 59.4% on SimplerEnv-WidowX
- Ablations provide clean evidence that both modalities are necessary
- Works within a standard autoregressive multimodal transformer framework without reinforcement learning fine-tuning

**Limitations**

- Trace is generated from the initial observation only; there is no mechanism evaluated for re-planning when unexpected changes occur mid-task
- Evaluations are primarily simulation-based (LIBERO); large-scale real-robot experiments are limited
- Trace generation adds inference overhead before execution begins, increasing latency
- Generalization to diverse real-world settings and task categories is not yet thoroughly established
- Potential for compounding errors from inaccurate visual keyframe predictions in very long sequences is not fully analyzed

**Terms to know**

- **VLA (Vision-Language-Action model)**: a policy that takes visual and language inputs and outputs robot actions
- **IVLR-Trace**: Interleaved Vision-Language Reasoning Trace — the core intermediate representation alternating text subgoals and predicted visual keyframes
- **Keyframe**: a predicted image of what the scene should look like after a particular subgoal is completed
- **Closed-loop control**: an execution strategy where the robot re-reads its current observation at every timestep (as opposed to open-loop plans that are executed blindly)
- **LIBERO / LIBERO-Long**: a benchmark suite for evaluating long-horizon robotic manipulation; LIBERO-Long contains the most challenging multi-step tasks
- **SimplerEnv-WidowX**: an evaluation environment mirroring a real WidowX robot setup, used to measure sim-to-real transfer
- **Multimodal transformer**: a transformer model capable of understanding and generating both text and image tokens

**Why it is worth watching**

Generating a plan that is simultaneously logically coherent and spatially precise has been a persistent bottleneck for robot manipulation policies. Most existing VLA approaches either rely on latent planning (opaque, hard to inspect) or expose only one modality of reasoning. IVLR makes the intermediate plan explicit and bimodal — readable text for causal steps, visual predictions for spatial alignment — which also makes the policy more interpretable. The result is a step toward robot policies that plan more like humans: first picturing the goal, then acting toward it.

**My take**

IVLR의 핵심 통찰은 단순하지만 강력하다: 텍스트와 이미지 중 하나만 골라야 한다는 가정을 버리고, 둘을 번갈아 사용하는 명시적 표현을 정책의 중심에 두라는 것이다. 절제 실험 결과가 이를 명확히 뒷받침한다. 다만, 트레이스가 초기 관찰에서만 생성된다는 점 — 실행 도중 환경이 예상과 달라질 때 어떻게 대응할지 — 은 앞으로 해결해야 할 중요한 과제다.

In English: IVLR's core insight is simple but powerful — drop the assumption that you must choose between text or vision, and make a bimodal explicit trace the center of the policy. The ablations make a clean case for this. The main open question is robustness: what happens when the scene diverges from the predicted keyframes mid-task, and whether on-the-fly re-planning is feasible at robot speeds.
