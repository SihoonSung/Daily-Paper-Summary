---
title: "GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors"
date: 2026-06-10
topic: robotics
tags: [robotics, humanoid, embodied-AI, sim-to-real, video-foundation-models, data-generation, reinforcement-learning]
source: https://arxiv.org/abs/2606.05160
---

# GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors

* Date: 2026-06-05 (arXiv)
* Source: https://arxiv.org/abs/2606.05160
* Topic: Robotics / Humanoid Embodied AI
* Why it matters: 휴머노이드 로봇이 물체를 옮기고, 앉고, 계단을 오르는 등 전신 조작(loco-manipulation)을 배우려면 대규모의 로봇 호환 시연 데이터가 필요하지만, 텔레오퍼레이션과 모션캡처는 물리적 설비와 인력 때문에 확장하기 매우 어렵다. NVIDIA 연구팀이 발표한 GRAIL은 3D 자산과 비디오 생성 모델만으로 이런 데이터를 완전히 가상으로 생성하는 파이프라인을 제시하며, 실제로 이 데이터만으로 학습한 정책이 실제 Unitree G1 로봇에서 작동함을 보였다.

---

## Korean Summary

**한줄 요약**

NVIDIA와 UCLA 연구진은 텔레오퍼레이션이나 모션캡처 같은 물리적 데이터 수집 없이, 3D 자산과 비디오 생성 모델(video foundation model)의 사전지식만으로 휴머노이드 로봇의 전신 조작(loco-manipulation) 학습 데이터를 생성하는 파이프라인 GRAIL을 제안했다. 이렇게 생성한 약 2만 개 이상의 시퀀스만으로 학습한 시각 기반 정책이 Unitree G1 로봇에서 실제 물체 집기와 계단 오르기에 성공했다.

**핵심 아이디어**

휴머노이드 로봇이 다양한 물체와 지형에서 전신을 사용해 작업을 수행하도록 학습시키려면 막대한 양의 "로봇이 따라할 수 있는" 시연 데이터가 필요하다. 그러나 사람이 직접 로봇을 원격조작(teleoperation)하거나 모션캡처 장비를 착용해 동작을 녹화하는 방식은 매번 물리적 환경, 장비, 배우(actor), 로봇을 준비해야 하므로 규모를 키우기 어렵다. GRAIL의 핵심 아이디어는 "배포 전까지는 완전히 가상으로 머문다"는 것이다. 즉, 실제 환경을 다시 만들거나 로봇을 조작하지 않고, 3D 자산·시뮬레이터용 장면·비디오 생성 모델의 사전지식을 조합해 인간-물체 상호작용(human-object interaction, HOI) 영상을 만들고, 이를 다시 로봇이 따라할 수 있는 4D(3D+시간) 궤적으로 복원한다. 특히 기존 연구들이 임의의 인터넷 영상을 사후에 3D로 복원하려 했던 것과 달리, GRAIL은 영상을 생성하기 "전"에 물체의 기하학적 형태, 카메라 파라미터, 실제 스케일(metric scale), 환경의 깊이 정보, 로봇 비율에 맞춘 캐릭터를 모두 사전에 정의해 두고, 이 정보를 영상 생성과 복원 과정에서 그대로 재사용함으로써 복원 정확도를 크게 높인다.

**무엇이 새로운가?**

- 텔레오퍼레이션이나 모션캡처 없이, 완전히 디지털 환경에서 휴머노이드 전신 조작 학습 데이터를 생성하는 파이프라인
- 영상을 생성하기 전에 물체 기하·카메라·스케일·깊이·로봇 비율 캐릭터를 모두 고정하고 비디오 생성 모델(VFM)에 조건을 주는 "사전 정의 후 생성(specify-then-generate)" 접근으로 4D 복원의 정확도와 일관성을 향상
- 2만 건 이상의 인간-물체 상호작용(HOI) 시퀀스를 생성하고 Unitree G1 로봇 비율로 리타기팅(retargeting)하여 데이터셋과 코드, 모델을 공개
- 물체 집기(테이블/바닥), 전신 조작, 앉기, 지형 이동(계단·경사·연석)을 아우르는 과제 일반(task-general) 정책 학습을 단일 파이프라인으로 지원
- GRAIL 데이터만으로 학습한 1인칭 시점(egocentric) 시각 정책이 실제 로봇에서 물체 집기와 계단 오르기로 sim-to-real 전이에 성공

**어떻게 작동하는가?**

1. **3D 자산 생성:** 절차적으로 생성한 지형(계단, 경사, 연석 등)과 AI로 생성한 물체 자산을 준비한다.
2. **2D 인간-물체 상호작용(HOI) 영상 생성:** Blender로 사전에 정의된 3D 장면(물체 위치, 카메라, 조명 등)을 렌더링한 뒤, 이를 조건으로 Kling과 같은 비디오 생성 모델을 사용해 사람이 해당 물체와 상호작용하는 영상을 합성한다.
3. **4D HOI 복원:** 생성된 2D 영상에서 사람의 자세 추정(pose estimation), 물체 추적(object tracking), 상호작용을 고려한 최적화(interaction-aware optimization)를 통해 실제 스케일을 가진 3D+시간(4D) 인간-물체 상호작용 궤적을 복원한다. 이때 1단계에서 미리 알고 있던 카메라·스케일·깊이 정보를 그대로 재사용하므로 복원이 더 정확하다.
4. **리타기팅:** 복원된 인간 동작을 Unitree G1 휴머노이드 로봇의 신체 비율에 맞게 변환한다.
5. **정책 학습:** 리타기팅된 데이터를 이용해 물체 집기, 전신 조작, 앉기, 지형 이동 등 다양한 과제를 수행할 수 있는 일반화된(task-general) 제어 정책을 학습한다.
6. **배포 및 검증:** 학습된 1인칭 시각 정책을 실제 Unitree G1 로봇에 배포해 물체 집기와 계단 오르기 등의 실세계 과제에서 성능을 검증한다.

**강점**

- 물리적 텔레오퍼레이션·모션캡처 설비 없이도 대규모(2만 건 이상) 로봇 학습 데이터를 생성할 수 있어 데이터 수집 비용과 시간을 크게 절감
- 영상 생성 전에 장면의 기하·스케일·카메라 정보를 고정함으로써, 임의의 인터넷 영상을 사후 복원하는 기존 방식보다 4D 궤적의 정확도가 향상될 가능성이 큼
- 픽업, 전신 조작, 앉기, 지형 이동 등 여러 과제를 하나의 파이프라인과 일반화된 정책으로 다룸
- GRAIL로만 학습한 정책이 실제 로봇(Unitree G1)에서 동작함을 보여 sim-to-real 격차를 줄이는 실질적 증거를 제시
- 데이터셋(Hugging Face)과 코드(GitHub)를 공개해 다른 연구자들이 재현·확장 가능

**한계**

- 비디오 생성 모델(Kling 등)의 품질과 물리적 사실성에 의존하므로, 생성된 동작이 실제 물리 법칙을 완벽히 따르지 않을 가능성이 있고 이에 대한 보정 과정의 한계는 추가 검증이 필요
- 실세계 검증 과제는 물체 집기와 계단 오르기 등 일부에 한정되어 있어, 더 복잡하거나 정교한 양손 조작·동적 균형 과제로의 일반화는 아직 입증되지 않음
- 4D 복원 과정(자세 추정, 물체 추적, 최적화)의 정확도가 최종 정책 성능에 미치는 영향과 오차 누적 가능성에 대한 정량적 분석은 본 요약 자료만으로는 충분히 확인되지 않음
- Unitree G1이라는 특정 로봇 플랫폼에 맞춰 검증되었으며, 다른 형태(다른 신체 비율·자유도)의 휴머노이드로의 이식성은 추가 확인이 필요
- NVIDIA 라이선스로 공개되어 비상업적 용도로 제한되는 등 활용 범위에 제약이 있을 수 있음

**알아둘 용어**

- **로코-매니퓰레이션 (Loco-Manipulation):** 이동(locomotion)과 조작(manipulation)을 동시에 수행하는 전신 동작. 예: 걸으면서 물건을 집거나, 계단을 오르며 균형을 잡는 동작.
- **비디오 파운데이션 모델 (Video Foundation Model, VFM):** 대규모 영상 데이터로 사전학습되어 사실적인 영상을 생성할 수 있는 모델. 이 논문에서는 Kling 같은 모델을 활용해 인간-물체 상호작용 영상을 합성한다.
- **인간-물체 상호작용 (Human-Object Interaction, HOI):** 사람이 물체를 잡거나 옮기는 등 상호작용하는 동작과 그 데이터를 의미하며, 로봇 학습의 시연 데이터로 활용된다.
- **리타기팅 (Retargeting):** 사람의 동작 데이터를 로봇의 신체 비율과 관절 구조에 맞게 변환하는 과정.
- **4D 복원 (4D Reconstruction):** 2D 영상으로부터 시간에 따라 변화하는 3D 형상과 자세(즉, 3D + 시간)를 복원하는 작업.
- **Sim-to-Real 전이:** 시뮬레이션이나 가상 환경에서 학습한 정책을 실제 로봇 하드웨어에서도 동작하도록 이전하는 것. 둘 사이의 차이(현실 격차, reality gap)를 극복하는 것이 핵심 과제다.
- **과제 일반(Task-General) 정책:** 하나의 모델/정책이 여러 종류의 과제(집기, 앉기, 지형 이동 등)를 수행할 수 있도록 일반화된 형태로 학습된 정책.

**왜 주목할 만한가?**

휴머노이드 로봇 연구에서 가장 큰 병목 중 하나는 "로봇이 학습할 수 있는 양질의 전신 동작 데이터가 절대적으로 부족하다"는 점이다. 텔레오퍼레이션이나 모션캡처는 정밀하지만 사람과 장비, 시간이 많이 들어 확장성이 떨어진다. GRAIL은 이 문제를 비디오 생성 모델의 사전지식과 정밀하게 통제된 3D 장면 설정을 결합해 우회하려는 시도이며, NVIDIA라는 산업계 주요 플레이어가 대규모 데이터셋과 코드를 함께 공개했다는 점에서 다른 연구팀들이 즉시 활용·검증할 수 있는 실용적 자원이 된다. 실제 로봇에서의 sim-to-real 성공 사례까지 보고했다는 점에서, "데이터 생성의 가상화"가 휴머노이드 로봇 학습의 새로운 표준 워크플로로 자리잡을 가능성을 보여준다.

---

## English Summary

**One-line summary**

Researchers from NVIDIA and UCLA introduce GRAIL, a fully digital data-generation pipeline that synthesizes humanoid loco-manipulation training data by combining 3D assets, simulator-ready scenes, and priors from video foundation models — without any teleoperation, motion capture, or physical setup. Using only GRAIL-generated data (20,000+ sequences), the resulting egocentric visual policies were deployed on a real Unitree G1 humanoid and successfully performed object pick-up and stair-climbing.

**Core idea**

Training humanoid robots to perform whole-body loco-manipulation across diverse objects, motions, and terrains requires large amounts of robot-compatible demonstration data. Teleoperation and motion capture, the traditional sources of such data, don't scale well because each session needs physical setups, instrumented actors, and actual robot operation. GRAIL's central idea is to "stay fully virtual until deployment": instead of reconstructing motion from arbitrary in-the-wild videos after the fact, it first fully specifies a 3D configuration — object geometry, camera parameters, metric scale, environment depth, and a robot-proportioned character — and only then generates a video using a video foundation model (VFM) conditioned on that scene. Because all this geometric information was known beforehand, it can be reused during reconstruction, making the resulting 4D (3D + time) human-object interaction trajectories far more accurate and consistent than reconstructions from unconstrained video.

**What is new?**

- A fully digital pipeline for generating humanoid loco-manipulation training data with no teleoperation or motion capture required
- A "specify-then-generate" approach: 3D geometry, camera parameters, metric scale, depth, and a robot-proportioned character are fixed before video generation and reused for reconstruction, improving 4D reconstruction accuracy
- Generation and release of 20,000+ human-object interaction (HOI) sequences, retargeted to the Unitree G1 humanoid, along with public dataset, code, and models
- A single pipeline supporting task-general policy training across pick-up (tabletop and ground), whole-body manipulation, sitting, and terrain traversal (stairs, slopes, curbs)
- Demonstrated sim-to-real transfer: egocentric visual policies trained solely on GRAIL data perform real-world object pick-up and stair-climbing on a physical robot

**How does it work?**

1. **3D asset generation:** Procedurally generated terrains (stairs, slopes, curbs) and AI-generated object assets are prepared.
2. **2D HOI video generation:** A pre-specified 3D scene (object placement, camera, lighting) is rendered in Blender, then used to condition a video foundation model (e.g., Kling) to synthesize a video of a human interacting with the object.
3. **4D HOI reconstruction:** Pose estimation, object tracking, and interaction-aware optimization recover a metric-scale 4D (3D + time) human-object interaction trajectory from the generated 2D video, reusing the camera, scale, and depth information known from step 1.
4. **Retargeting:** The reconstructed human motion is retargeted to the body proportions of the Unitree G1 humanoid robot.
5. **Policy training:** The retargeted data trains task-general control policies covering pick-up, whole-body manipulation, sitting, and terrain traversal.
6. **Deployment and validation:** The trained egocentric visual policy is deployed on a real Unitree G1 robot and evaluated on real-world tasks such as object pick-up and stair-climbing.

**Strengths**

- Eliminates the need for physical teleoperation or motion-capture infrastructure, dramatically reducing the cost and time of generating large-scale humanoid training data
- The "specify-then-generate" strategy likely improves 4D trajectory accuracy compared to reconstructing motion from unconstrained internet videos
- Unifies multiple task categories (pick-up, whole-body manipulation, sitting, terrain traversal) under one pipeline and one task-general policy
- Provides concrete sim-to-real evidence — policies trained purely on synthetic data work on a real humanoid robot
- Public release of dataset (Hugging Face), code, and models (GitHub) enables reproduction and extension by other researchers

**Limitations**

- Quality and physical plausibility of generated motion depend on the underlying video foundation model (e.g., Kling), and how well any physical inaccuracies are corrected requires further validation
- Real-world validation is limited to a subset of tasks (pick-up and stair-climbing); generalization to more complex bimanual manipulation or dynamic balance tasks is not yet demonstrated
- The accuracy of the 4D reconstruction stage (pose estimation, object tracking, optimization) and how errors propagate into final policy performance are not quantitatively detailed in available summaries
- Validated specifically on the Unitree G1 platform; portability to humanoids with different body proportions or degrees of freedom remains to be confirmed
- Released under an NVIDIA license restricted to non-commercial use, which may limit broader adoption

**Terms to know**

- **Loco-Manipulation:** Combined locomotion and manipulation — e.g., walking while carrying an object, or maintaining balance while climbing stairs and reaching for something.
- **Video Foundation Model (VFM):** A large model pretrained on video data that can generate realistic video clips; here used to synthesize human-object interaction footage (e.g., Kling).
- **Human-Object Interaction (HOI):** Data capturing how humans grasp, move, or otherwise interact with objects, used as demonstration data for robot learning.
- **Retargeting:** The process of converting human motion data to fit a robot's body proportions and joint structure.
- **4D Reconstruction:** Recovering 3D shape and pose over time (3D + time) from 2D video.
- **Sim-to-Real Transfer:** Deploying a policy trained in simulation or virtual environments onto real hardware, bridging the "reality gap" between the two.
- **Task-General Policy:** A single trained policy capable of performing multiple distinct task types (e.g., picking up objects, sitting, traversing terrain) rather than one policy per task.

**Why it is worth watching**

One of the biggest bottlenecks in humanoid robotics is the scarcity of high-quality, robot-usable whole-body demonstration data — teleoperation and motion capture are precise but too labor- and equipment-intensive to scale. GRAIL attacks this bottleneck by combining the priors of modern video generation models with tightly controlled 3D scene specification, sidestepping the need for physical data collection altogether. The fact that NVIDIA released a large dataset, code, and models alongside the paper makes this an immediately usable resource for other groups, and the reported real-robot sim-to-real success suggests "virtualized data generation" could become a standard part of the humanoid training workflow.

**My take**

한국어: GRAIL의 가장 흥미로운 점은 "현실의 영상을 복원"하는 대신 "원하는 3D 장면을 먼저 정의하고 그에 맞춰 영상을 생성"한다는 발상의 전환이다. 이는 비디오 생성 모델의 한계(물리적 부정확성, 임의 카메라 등)를 줄이는 합리적인 우회 전략으로 보인다. 다만 비디오 생성 모델 자체의 품질에 여전히 의존하고, 실세계 검증 과제가 아직 제한적이라는 점에서 더 폭넓은 과제(특히 정밀한 양손 조작)로의 일반화는 추가 검증이 필요하다. 그럼에도 대규모 데이터셋과 코드를 공개했다는 점에서 실용적 가치가 크다.

English: The most interesting aspect of GRAIL is the inversion of the usual workflow — instead of reconstructing motion from existing video, it specifies the desired 3D scene first and generates video to match, which is a sensible way to mitigate the physical inaccuracies and uncontrolled camera conditions typical of generative video. That said, the approach still inherits the limitations of the underlying video generation model, and real-world validation so far covers a relatively narrow set of tasks. Still, releasing a large dataset and full pipeline makes this immediately useful to the broader robotics community regardless of how the open questions resolve.
