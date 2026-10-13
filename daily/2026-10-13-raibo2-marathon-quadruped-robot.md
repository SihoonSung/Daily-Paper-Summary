---
title: "A quadrupedal robot designed to complete a marathon on a single battery charge"
date: 2026-10-13
topic: robotics
tags: [robotics, quadruped, energy-efficiency, reinforcement-learning, legged-locomotion, battery]
source: https://www.nature.com/articles/s41586-026-11102-5
---

A quadrupedal robot designed to complete a marathon on a single battery charge

* Date: 2026-10-13
* Source: https://www.nature.com/articles/s41586-026-11102-5
* Topic: Legged robotics / energy-efficient locomotion
* Why it matters: Battery life, not motors or control software, is the main thing keeping legged robots tethered to short missions; this paper shows that a whole-system redesign — mechanics, electronics, and a reinforcement-learned gait together — can push a quadruped's energy efficiency past that of a human runner, which matters for any battery-powered field robot that needs long range.

## Korean Summary

**한줄 요약**

KAIST 연구팀이 개발한 4족 보행 로봇 "RAIBO2"가 배터리를 한 번도 교체하거나 충전하지 않고 풀코스 마라톤(42.195km)을 4시간 19분 52초에 완주했습니다. 이 성과는 2026년 9월 23일 네이처(Nature)에 게재되었으며, 로봇의 단위 체중당 이동 에너지 소비량(이동 비용, cost of transport)이 처음으로 인간보다 낮은 값을 기록했다는 점이 핵심입니다.

**핵심 아이디어**

기존에는 로봇의 운행 거리를 늘리려면 단순히 배터리를 더 크고 무겁게 만드는 방식이 흔했습니다. 이 연구팀은 그 대신 장거리 보행을 "로봇 전체 시스템의 문제"로 보고, 기계 구조·전기 회로·보행 제어를 하나로 묶어 에너지 손실 자체를 줄이는 방향으로 접근했습니다. 그 결과 같은 배터리 용량으로도 기존 4족 로봇보다 훨씬 멀리, 그리고 사람보다 효율적으로 달릴 수 있는 로봇을 만들었습니다.

**무엇이 새로운가?**

* 세계 최초로 4족 보행 로봇이 공인 마라톤 풀코스(42.195km)를 완주 — 2024년 11월 상주 곶감마라톤에 정식 참가자로 출전
* 로봇의 총 이동 비용(total cost of transport, TCOT)이 0.25로, 인간의 기준값인 약 0.37보다 낮아 "사람보다 에너지 효율적으로 달리는" 최초의 4족 로봇으로 보고됨
* 기계적 손실, 전기적 손실, 보행 손실을 하나로 통합한 손실 모델(loss model)을 세워 어디서 에너지가 새는지 정량적으로 분석
* 모터 구동 회로를 로봇 관절에 직접 통합해 구동계 손실을 줄이고 제어 대역폭을 높이는 설계 적용
* 내리막에서 기계적 에너지를 회수하는 재생 제동(regenerative braking)을 포함한 통합 하드웨어-제어 설계

**어떻게 작동하는가?**

1. 힘 투과성이 높고 가벼운 기계 구조를 설계해, 로봇이 움직일 때 불필요하게 소모되는 기계적 마찰·관성 손실을 최소화합니다.
2. 저저항 모터 구동 회로를 관절 액추에이터에 직접 통합하여 전기적 손실을 줄이고, 관절 강성(stiffness) 제어를 액추에이터 수준에서 수행해 응답성과 효율을 동시에 확보합니다.
3. 연구팀이 자체 개발한 물리 시뮬레이터(RaiSim)에서 경사면·계단·빙판 등 다양한 지면 조건을 모사하며, 관절 움직임과 발-지면 충돌로 인한 에너지 손실을 최소화하도록 강화학습으로 보행 정책을 훈련합니다.
4. 내리막 구간에서는 재생 제동으로 일부 기계적 에너지를 회수해 배터리 소모를 줄입니다.
5. 이렇게 완성된 로봇(RAIBO2)을 실제 마라톤 대회에 투입해, 배터리 교체나 충전 없이 완주가 가능한지, 그리고 이동 비용이 얼마나 낮아지는지를 실측으로 검증합니다.

**강점**

* 실험실 벤치마크가 아니라 실제 공인 마라톤 대회라는 통제되지 않은 실외 환경에서 성능을 입증
* 배터리 용량을 키우는 대신 시스템 전반의 손실을 줄이는 방식이어서, 로봇을 더 무겁고 둔하게 만들지 않고도 운행 거리를 늘릴 수 있음을 보여줌
* 기계·전기·제어를 아우르는 통합 손실 모델을 제시해, 후속 연구자들이 어느 구성 요소를 개선해야 할지 가늠할 수 있는 정량적 틀을 제공
* 보고된 바에 따르면 마라톤 완주 후에도 약 25km를 더 달릴 수 있는 배터리 여유가 남아 있어, 실용적인 안전 마진을 확보

**한계**

* 보도에 따르면 이 로봇은 완전 자율 주행이 아니라 머리에 장착된 카메라 영상을 보고 사람이 조종하는 방식으로 달렸으며, 자율 항법 성능에 대한 평가는 아님
* 배터리 용량·경사도 등 세부 수치가 네이처 발표 자료와 일부 보도 자료 사이에서 다르게 인용되고 있어, 정확한 값은 원 논문의 수치를 기준으로 삼아야 함
* 42kg급의 특정 로봇 플랫폼과 평탄한 도로 위주의 마라톤 코스에서 얻은 결과로, 험지·계단 등 더 가혹한 환경에서의 장거리 효율은 별도 검증이 필요
* "사람보다 낮은 이동 비용"이라는 비교는 특정 이동 비용 정의와 기준치에 의존하므로, 비교 대상(달리기 방식, 속도, 신체 조건)에 따라 해석이 달라질 수 있음

**알아둘 용어**

* 이동 비용(Cost of Transport, COT): 단위 체중과 단위 거리당 소비하는 에너지로, 걷거나 달리는 동물·로봇의 에너지 효율을 비교하는 표준 지표
* 4족 보행 로봇(Quadrupedal robot): 네 개의 다리로 걷거나 뛰는 로봇으로, 험지 이동에 강점이 있지만 전통적으로 배터리 소모가 큼
* 강화학습 보행 정책(RL locomotion policy): 로봇이 시뮬레이션 환경에서 보상을 최대화하도록 반복 학습해 얻은 다리 움직임 제어 규칙
* 재생 제동(Regenerative braking): 감속하거나 내려갈 때 발생하는 운동 에너지의 일부를 전기 에너지로 회수해 배터리에 되돌리는 기술
* 손실 모델(Loss model): 에너지가 어느 구성 요소(기계·전기·제어)에서 얼마나 소모되는지를 수치적으로 분해한 분석 모델
* 힘 투과성 설계(Force-transparent design): 액추에이터와 다리 사이의 기계적 손실(마찰, 백래시 등)을 최소화해 제어 명령이 손실 없이 힘으로 전달되도록 하는 설계 철학

**왜 주목할 만한가?**

4족 로봇은 재난 현장 탐사, 배송, 순찰 등 장시간·장거리 임무에 활용될 잠재력이 크지만, 지금까지는 배터리 수명이 가장 큰 제약이었습니다. 이 연구는 단순히 더 큰 배터리를 다는 대신 기계·전기·제어를 함께 최적화해 에너지 효율 자체를 끌어올리는 방법론을 실제 마라톤이라는 극한 조건에서 입증했다는 점에서, 앞으로 산업·구조·물류 현장에 투입될 장거리 로봇 설계에 실질적인 참고 사례가 될 것으로 보입니다.

---

## English Summary

**One-line summary**

A quadrupedal robot called RAIBO2, developed by a KAIST team, completed a full 42.195 km marathon in 4 hours, 19 minutes and 52 seconds without ever swapping or recharging its battery. The work, published in Nature on 23 September 2026, reports that the robot's energy cost of transport is, for the first time, lower than a human runner's.

**Core idea**

The conventional way to extend a legged robot's range has been to simply fit a bigger, heavier battery. Instead, this team treated long-distance locomotion as a whole-robot system problem, jointly redesigning the mechanical structure, the electrical drive system, and the gait-control policy to cut energy losses at every stage rather than just supplying more energy. The result is a robot that goes much farther per battery charge than prior quadrupeds, and does so more efficiently than a human runner by a standard efficiency metric.

**What is new?**

* First quadrupedal robot reported to complete a full, officially registered marathon (42.195 km) — RAIBO2 ran as a participant in the Sangju Dried Persimmon Marathon in November 2024
* A total cost of transport (TCOT) of 0.25, compared with a human benchmark of about 0.37 — reportedly the first quadruped robot with a lower cost of transport than a human
* A unified loss model combining mechanical, electrical, and locomotion-related energy losses, used to quantify where energy is actually being spent
* Motor driving circuitry integrated directly at the joint actuators to cut drivetrain losses and increase control bandwidth, with joint stiffness control implemented at the actuator level
* Regenerative braking that recovers part of the mechanical energy generated on downhill sections, feeding it back into the battery

**How does it work?**

1. A force-transparent, lightweight mechanical design minimizes friction and inertial losses so that control commands translate into motion with less wasted energy.
2. Low-resistance motor driver circuitry is built directly into the joint actuators, reducing electrical losses, while joint stiffness control is handled at the actuator level for both responsiveness and efficiency.
3. A walking policy is trained with reinforcement learning inside the team's own physics simulator (RaiSim), which models varied terrain such as slopes, stairs, and icy surfaces, with the training objective penalizing joint motion and foot-ground impact losses.
4. On downhill stretches, regenerative braking recovers some of the robot's mechanical energy and returns it to the battery, further reducing net consumption.
5. The finished robot, RAIBO2, was then entered into an actual marathon race to validate, under real and uncontrolled outdoor conditions, both whether it could finish without a battery swap and how low its cost of transport actually was.

**Strengths**

* Validated in an uncontrolled, real-world marathon race rather than only in lab benchmarks
* Improves range by reducing system-wide energy losses rather than by adding battery mass, avoiding the weight and bulk penalty of simply scaling up the battery
* Provides a combined mechanical/electrical/control loss model that gives future researchers a quantitative framework for identifying which subsystem to improve next
* Reportedly finished the marathon with battery capacity left for roughly another 25 km, giving a practical safety margin rather than running on the edge

**Limitations**

* According to reporting, the robot was steered by a human operator using a head-mounted camera rather than navigating autonomously, so this is an efficiency and endurance result, not an autonomy result
* Specific figures such as battery capacity and maximum slope handled are cited inconsistently across the Nature-affiliated press release and various news reports, so the paper's own reported numbers should be treated as authoritative
* Results come from one specific ~42 kg robot platform on a largely paved marathon course; efficiency over rougher terrain, stairs, or more extreme conditions over similarly long distances is not directly demonstrated here
* The "lower cost of transport than a human" comparison depends on a specific definition of cost of transport and a specific human baseline, so its generality across running styles, speeds, and body types is limited

**Terms to know**

* Cost of transport (COT): energy consumed per unit body weight per unit distance traveled, a standard metric for comparing the locomotion efficiency of animals and robots
* Quadrupedal robot: a four-legged robot well suited to rough terrain, but historically limited by high energy consumption relative to wheeled platforms
* Reinforcement-learning (RL) locomotion policy: a leg-control strategy learned by repeatedly optimizing a reward signal in simulation, rather than hand-programmed
* Regenerative braking: technology that recovers part of the kinetic energy produced during deceleration or descent and converts it back into stored electrical energy
* Loss model: a quantitative breakdown of how much energy is consumed by each subsystem (mechanical, electrical, control) of a system
* Force-transparent design: a mechanical design philosophy that minimizes losses (friction, backlash) between actuator and limb so that commanded forces are delivered with minimal loss

**Why it is worth watching**

Legged robots have long been proposed for disaster response, delivery, and long patrols, but battery endurance has been the key bottleneck rather than motors or control algorithms. This paper demonstrates, under the genuinely unforgiving conditions of an actual marathon, that jointly optimizing mechanics, electronics, and a learned gait can raise energy efficiency past a human benchmark — a result likely to inform how future long-range field robots are engineered.

---

## My take

이 연구는 화려한 새 알고리즘보다는 기계·전기·제어를 아우르는 "시스템 엔지니어링"의 힘을 보여주는 사례로 보입니다. 마라톤이라는 상징적이고 검증 가능한 실외 테스트를 통해 주장을 뒷받침한 점은 설득력이 있지만, 자율 주행이 아니라 사람이 조종했다는 점과 세부 수치가 보도마다 다르다는 점은 감안하고 읽어야 합니다. 그래도 "배터리를 키우지 않고 효율을 높인다"는 접근은 장거리 임무가 필요한 실용 로봇 설계에 실질적으로 참고할 만한 방향입니다.

This reads less as a flashy new algorithm and more as a demonstration of what disciplined systems engineering — mechanics, electronics, and control optimized together — can achieve. Using an actual, verifiable outdoor marathon as the test is a convincing choice, though readers should note the robot was human-steered rather than autonomous, and that specific figures vary across secondary reporting. Even so, the core strategy of raising efficiency instead of simply enlarging the battery is a genuinely useful direction for practical, long-range field robots.
