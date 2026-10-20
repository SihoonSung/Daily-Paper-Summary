---
title: "SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning"
date: 2026-10-20
topic: robotics
tags: [robotics, humanoid-robots, reinforcement-learning, manipulation, sim-to-real, legged-locomotion]
source: https://arxiv.org/abs/2603.10306
---

SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning

- Date: 2026-10-20
- Source: https://arxiv.org/abs/2603.10306
- Topic: Robotics (humanoid loco-manipulation)
- Why it matters: It gives bipedal humanoid robots a practical, modular way to carry unsecured objects (trays, cups, open containers) while walking, without retraining or degrading their existing walking skill — a capability needed for real-world service and logistics tasks. The work was recognized with the Best Mobile Manipulation Paper Award (sponsored by OMRON Sinic X) at IROS 2026, held in Pittsburgh in late September/early October 2026.

## Korean Summary

**한줄 요약**

이 논문은 두 발로 걷는 휴머노이드 로봇이 쟁반처럼 고정되지 않은 물체를 들고 걸을 때 흔들림을 억제하는 방법을 제안한다. 기존에 학습된 보행 정책은 그대로 두고, 그 위에 "잔차(residual)" 제어기를 추가로 학습시켜 걸음걸이에서 발생하는 흔들림만 상쇄하도록 설계했다.

**핵심 아이디어**

휴머노이드가 걸으면서 동시에 쟁반의 균형을 유지하도록 하나의 정책을 처음부터 다시 학습시키면, 걷는 능력 자체가 저하되거나 학습이 불안정해지기 쉽다. 저자들은 이 문제를 "계층적으로 분리"해서 풀었다. 즉, 이미 잘 작동하는 베이스 보행 정책은 고정해 두고, 그 보행으로 인해 상체·손끝에 전달되는 흔들림만을 보정하는 작은 보정 정책(잔차 정책)을 강화학습으로 따로 학습시킨다.

**무엇이 새로운가?**

- ReST-RL이라는 계층적 강화학습 구조를 제안해, 보행(locomotion)과 화물 안정화(payload stabilization)를 서로 다른 모듈로 분리했다.
- 기존에 학습된 보행 정책의 성능을 떨어뜨리지 않으면서 새로운 균형 유지 능력을 "추가"할 수 있다.
- SteadyTray라는 전용 벤치마크(시뮬레이션 환경과 평가 과제 모음)를 공개해 쟁반 균형 유지 과제를 표준화했다.
- 관측 지연(observation delay), 제어 지연(control latency) 등 현실적인 요인을 도메인 랜덤화에 포함해 실물 로봇 전이 성능을 높였다.
- 시뮬레이션에서 학습한 정책을 별도의 미세조정 없이 실제 Unitree G1 휴머노이드에 그대로(zero-shot) 적용해 성공적으로 작동시켰다.

**어떻게 작동하는가?**

1. 먼저 휴머노이드의 보행을 담당하는 베이스 정책을 일반적인 방식으로 학습(또는 기존 정책 재사용)한다.
2. 이 베이스 정책은 고정한 채, 걷는 동안 몸통과 팔·손끝에 가해지는 흔들림(가속, 기울어짐 등)을 관측값으로 받아 이를 상쇄하는 잔차 행동을 출력하는 별도의 작은 신경망을 강화학습으로 훈련한다.
3. 학습 중에는 속도를 변화시키거나 외부에서 힘을 가하는 등 다양한 교란을 주어 로봇이 여러 상황에서도 쟁반을 안정적으로 유지하도록 만든다.
4. 센서 지연, 제어 명령 지연 등 실제 하드웨어에서 발생하는 현실적 조건을 시뮬레이션에 반영(도메인 랜덤화)해, 시뮬레이션에서 학습한 정책이 실제 로봇에서도 거의 그대로 작동하도록 한다.
5. 최종적으로 Unitree G1 로봇에 정책을 옮겨 실제 쟁반 운반 과제를 수행하며 성능을 검증한다.

**강점**

- 기존 보행 정책을 재학습하지 않아도 되므로, 이미 검증된 로봇 시스템에 모듈을 추가하는 방식으로 실용적으로 적용할 수 있다.
- 시뮬레이션 평가에서 속도가 변하는 상황에서도 96.9%의 성공률, 외부 힘 교란 상황에서도 74.5%의 견고성을 보였다.
- 시뮬레이션에서 실제 로봇으로의 전이(sim-to-real)가 추가 미세조정 없이 가능하다는 점을 실제 하드웨어로 입증했다.
- 공개된 벤치마크와 코드(GitHub)를 통해 다른 연구자들이 결과를 재현하고 확장할 수 있다.
- IROS 2026에서 모바일 매니퓰레이션 분야 최우수 논문상을 수상해 학계에서도 그 기술적 완성도를 인정받았다.

**한계**

- 아직 시뮬레이션 중심의 평가이며, 실제 로봇 실험의 범위(다양한 쟁반 형태, 액체가 담긴 용기, 장시간 주행 등)가 논문에서 충분히 넓게 다뤄졌는지는 추가 확인이 필요하다.
- 베이스 보행 정책 자체의 품질에 성능이 크게 의존하므로, 보행이 불안정한 로봇에는 효과가 제한적일 수 있다.
- 쟁반 위 물체의 종류, 무게, 배치가 크게 달라지는 경우에 대한 일반화 성능은 추가 검증이 필요하다.
- 아직 초기 연구 단계로, 상용 서비스 로봇에 바로 적용하기 위해서는 안전성, 내구성 등에 대한 추가 공학적 검증이 필요하다.

**알아둘 용어**

- 잔차 강화학습(Residual Reinforcement Learning): 이미 있는 정책 위에 작은 보정 정책을 추가로 학습해 기존 성능을 유지하면서 새로운 기능을 더하는 방법.
- 휴머노이드 로봇(Humanoid Robot): 사람과 비슷한 형태(두 발, 두 팔)를 가진 로봇.
- 로코매니퓰레이션(Loco-manipulation): 이동(보행)과 물체 조작을 동시에 수행하는 로봇 작업.
- 도메인 랜덤화(Domain Randomization): 시뮬레이션 학습 시 다양한 조건(지연, 마찰 등)을 무작위로 바꿔 실제 환경 전이 성능을 높이는 기법.
- 시뮬레이션-실물 전이(Sim-to-Real Transfer): 시뮬레이션에서 학습한 정책을 실제 로봇에 적용하는 과정.

**왜 주목할 만한가?**

서비스 로봇이나 물류 로봇이 실제 환경에서 쓰이려면 걷는 능력뿐 아니라, 고정되지 않은 물체(음식, 음료, 부품 등)를 안전하게 운반하는 능력이 필요하다. 이 논문은 기존 보행 능력을 해치지 않으면서 이런 기능을 모듈식으로 추가하는 실용적인 방법을 제시했고, 실제 하드웨어 전이까지 성공적으로 보여주었다는 점에서 휴머노이드 로봇의 실용화에 기여할 수 있는 연구다.

---

## English Summary

**One-line summary**

This paper presents a method for bipedal humanoid robots to carry unsecured objects, like a tray, while walking without spilling it. Instead of retraining the whole walking policy, the authors add a separately learned "residual" controller that only cancels out the wobble caused by gait.

**Core idea**

Training a single policy from scratch to both walk and balance a tray tends to degrade walking performance or make learning unstable. The authors instead decouple the problem hierarchically: they keep an already-working base locomotion policy fixed, and train a small residual policy on top of it via reinforcement learning whose only job is to counteract the disturbances that walking induces at the upper body and end-effector.

**What is new?**

- A hierarchical RL framework, ReST-RL, that separates locomotion from payload stabilization into distinct modules.
- The ability to add new balancing capability without degrading the performance of an already-trained walking policy.
- A dedicated benchmark, SteadyTray, released to standardize evaluation of tray-balancing tasks for humanoids.
- Inclusion of realistic factors such as observation delay and control latency in domain randomization to improve real-world transfer.
- Zero-shot sim-to-real deployment on a real Unitree G1 humanoid, without additional fine-tuning on hardware.

**How does it work?**

1. A base locomotion policy for the humanoid is trained (or reused) in the standard way.
2. With that base policy frozen, a separate, small residual network is trained with reinforcement learning to take in observations of the disturbance (accelerations, tilt, etc.) felt at the torso and end-effector while walking, and to output corrective residual actions that cancel it out.
3. During training, the robot is subjected to varying walking speeds and external force perturbations so the residual policy learns to keep the tray steady under diverse conditions.
4. Realistic hardware effects such as sensing delay and control latency are modeled in simulation via domain randomization, so the policy learned in simulation transfers closely to real hardware.
5. The resulting policy is deployed on a Unitree G1 humanoid and tested on real tray-carrying tasks.

**Strengths**

- Practical to deploy because it adds a module on top of an existing, validated walking policy rather than requiring retraining of the whole system.
- Reports a 96.9% success rate under variable-velocity tracking and 74.5% robustness to external force disturbances in simulation.
- Demonstrates zero-shot sim-to-real transfer on real hardware, not just in simulation.
- Releases a public benchmark and code (GitHub), enabling reproducibility and follow-up work.
- Recognized with the Best Mobile Manipulation Paper Award (OMRON Sinic X) at IROS 2026, indicating peer validation of its technical quality.

**Limitations**

- Evaluation is primarily simulation-based; the breadth of real-hardware testing (different tray shapes, liquid-filled containers, long-duration operation) is not fully clear from available descriptions and would need closer reading of the full paper.
- Performance depends heavily on the quality of the underlying base locomotion policy, so the benefit may be limited for robots with less stable gaits.
- Generalization across widely varying object types, weights, and placements on the tray needs further validation.
- This is early-stage research; deploying it in commercial service robots would require additional engineering work on safety and robustness.

**Terms to know**

- Residual Reinforcement Learning: Training a small corrective policy on top of an existing policy to add new capability while preserving the original behavior.
- Humanoid Robot: A robot with a human-like form (two legs, two arms).
- Loco-manipulation: Robot tasks that combine locomotion (walking/moving) with manipulation of objects.
- Domain Randomization: Randomizing simulation conditions (e.g., latency, friction) during training to improve transfer to the real world.
- Sim-to-Real Transfer: Applying a policy trained in simulation directly to a physical robot.

**Why it is worth watching**

For service and logistics robots to be useful in real environments, they need more than stable walking — they need to safely carry unsecured items like food, drinks, or parts. This paper offers a practical, modular way to add that capability without compromising existing walking skills, and backs it up with successful real-hardware deployment, making it a relevant step toward practical humanoid deployment.

---

## My take

이 논문은 화려한 신기술을 제시하기보다, 실용적인 문제(휴머노이드가 물체를 들고 걸을 때의 안정성)를 깔끔한 모듈식 해법으로 푼 사례다. 베이스 정책을 보존하면서 기능을 추가하는 잔차 학습 접근은 재현성과 실제 적용 가능성이 높아 보이고, 실제 하드웨어 전이까지 보였다는 점이 신뢰도를 높인다. 다만 평가가 주로 시뮬레이션에 치중되어 있고, 다양한 실제 환경에서의 장기적 신뢰성은 아직 더 검증이 필요하다.

This is a fairly modest but practically useful contribution: a clean, modular solution to a real deployment problem (keeping unsecured payloads steady on a walking humanoid) rather than a flashy new capability. The residual-learning approach, which preserves the base walking policy while adding new skill, looks reproducible and practically deployable, and the demonstrated real-hardware transfer adds credibility. That said, the evaluation leans heavily on simulation, and long-term reliability across varied real-world conditions still needs further validation.
