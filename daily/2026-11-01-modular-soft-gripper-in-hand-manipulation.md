---
title: "A Modular Soft Gripper with Enhanced In-Hand Manipulation Capabilities"
date: 2026-11-01
topic: robotics
tags: [robotics, soft-robotics, grippers, in-hand-manipulation, manufacturing, modular-design]
source: https://doi.org/10.1088/1748-3190/ae901e
---

A Modular Soft Gripper with Enhanced In-Hand Manipulation Capabilities

* Date: 2026-11-01
* Source: https://doi.org/10.1088/1748-3190/ae901e
* Topic: Robotics (soft robotic grippers)
* Why it matters: Soft grippers are safe and compliant but usually can't reposition a grasped object without letting go and re-grasping it; this design adds active, modular degrees of freedom that let it rotate and reorient objects in-hand while keeping the original grip, which is useful for assembly and handling fragile or irregularly shaped parts.

## Korean Summary

**한줄 요약**

스페인 마드리드 카를로스 3세 대학교(UC3M)와 나바라 공립대학교(UPNA) 연구진이 물체를 놓지 않고도 손 안에서 회전·재배치할 수 있는 모듈형 소프트 그리퍼를 개발해 2026년 Bioinspiration & Biomimetics에 발표했다. 기존 소프트 그리퍼는 부드럽고 안전하지만 움켜쥔 물체의 자세를 바꾸려면 보통 놓고 다시 잡아야 했는데, 이 그리퍼는 그 한계를 줄였다.

**핵심 아이디어**

손가락 자체에 능동 회전 구동을 추가해, 소프트 핑거의 유연성(안전성·적응성)과 능동 자유도(정밀한 재배치 능력)를 동시에 확보하는 것이 핵심 아이디어다. 즉 "부드럽지만 다룰 수 있는" 그리퍼를 지향한다.

**무엇이 새로운가?**

* 각 손가락이 3자유도(텐던 기반 비대칭 굽힘 + 손가락 밑동의 능동 회전)를 갖는 독립 구동형 소프트 핑거 3개로 구성.
* 비대칭 소프트 관절이 방향에 따라 다른 유연성(compliance)을 제공해, 특정 방향으로는 쉽게 굽혀지고 다른 방향으로는 저항하도록 설계.
* 수동적인 기구적 걸림(geometric blocking) 구조로 과도한 변형을 막아 손가락을 보호.
* 손가락이 모듈식으로 분리·교체 가능해, 한 손가락이 손상돼도 그리퍼 전체를 바꾸지 않고 해당 손가락만 교체 가능.
* 그리퍼로 쥔 물체를 놓지 않은 채 축을 따라 연속적으로 회전시키는 인핸드(in-hand) 조작 시연.

**어떻게 작동하는가?**

세 개의 소프트 손가락이 물체를 감싸 쥐면, 각 손가락의 텐던이 비대칭적으로 당겨지며 굽힘을 만들고, 동시에 손가락 밑동의 액추에이터가 손가락을 회전시킨다. 세 손가락의 굽힘과 회전을 조합하면 물체가 손가락 사이에서 굴러가듯 회전하며 자세가 바뀌지만, 접촉과 파지력은 계속 유지된다. 비대칭 관절 설계는 평소에는 유연하게 변형되다가 일정 범위를 넘으면 기구적으로 걸려(block) 더 이상 변형되지 않도록 해, 과도한 힘에도 손가락이 손상되지 않게 한다.

**강점**

* 소프트 로봇 특유의 안전성·적응성을 유지하면서도 정밀한 인핸드 재배치가 가능.
* 병, 각진 블록, 티슈 상자, 장난감, 3D 프린팅 피규어, 고무 오리, 드라이버, 조화(造花) 등 크기와 강성이 매우 다른 다양한 물체에서 동작을 검증.
* 모듈형 구조로 유지보수(손가락 개별 교체)가 쉬움.
* 조립 전 부품 방향 맞추기, 깨지기 쉽거나 비정형적인 물체 취급 등 산업 현장에 직접 적용 가능한 시나리오가 명확함.

**한계**

* 보도자료와 공개 요약 수준의 정보로 작성되어, 논문 원문의 정량적 수치(회전 속도, 파지력, 반복 정밀도 등)는 구체적으로 확인되지 않았다.
* 손가락 밑동 회전 액추에이터가 추가되어, 완전한 소프트 구조에 비해 기구적 복잡성과 비용이 늘어날 가능성이 있음.
* 아직 실험실 단계의 시연으로, 산업 현장에서의 내구성·반복 작업 신뢰성은 추가 검증이 필요.
* 이 요약은 이 세션의 네트워크 정책상 논문 원문 페이지(DOI 링크)에 직접 접속해 확인하지 못했고, 웹 검색으로 수집한 UC3M/UPNA 보도자료 및 TechXplore, PubMed 등의 교차 확인된 정보를 바탕으로 작성되었다.

**알아둘 용어**

* 소프트 로보틱스(Soft Robotics): 딱딱한 금속·플라스틱 대신 유연한 재료로 만들어 안전하고 적응력 있는 로봇을 다루는 분야.
* 인핸드 매니퓰레이션(In-Hand Manipulation): 물체를 쥔 채로 손(그리퍼) 안에서 자세나 위치를 바꾸는 동작.
* 자유도(Degree of Freedom, DoF): 로봇의 한 부분이 독립적으로 움직일 수 있는 방향의 수.
* 텐던 구동(Tendon-Driven Actuation): 힘줄처럼 당기는 줄(텐던)을 이용해 유연한 구조를 굽히거나 움직이는 구동 방식.
* 비대칭 소프트 관절(Asymmetric Soft Joint): 방향에 따라 유연성이 다르게 설계된 관절로, 특정 방향으로는 쉽게, 다른 방향으로는 저항하며 굽혀짐.
* 기구적 걸림(Geometric Blocking): 특정 변형 범위를 넘으면 구조가 물리적으로 걸려 더 이상 움직이지 못하게 만드는 수동적 보호 메커니즘.

**왜 주목할 만한가?**

제조·물류 현장에서 로봇이 물체를 잡은 뒤 재배치해야 하는 경우가 매우 흔한데, 기존에는 그리퍼가 손을 놓고 다시 잡는 비효율적인 과정을 거쳐야 했다. 이 연구는 소프트 그리퍼의 안전성을 희생하지 않으면서도 그 비효율을 줄일 수 있는 실용적인 경로를 보여주며, 조립 자동화나 다루기 까다로운 물체를 다루는 로봇 응용에 바로 참고할 만하다.

---

## English Summary

**One-line summary**

Researchers at Universidad Carlos III de Madrid (UC3M) and Universidad Pública de Navarra (UPNA) built a modular soft robotic gripper that can rotate and reposition a grasped object without letting go, publishing the work in Bioinspiration & Biomimetics in 2026. It targets a known weak point of soft grippers: they are safe and compliant but usually must release and re-grasp an object to change its orientation.

**Core idea**

The core idea is to combine the compliance and safety of soft fingers with active, controllable degrees of freedom, so the gripper keeps the adaptability of soft robotics while gaining the dexterity needed for precise in-hand repositioning.

**What is new?**

* Three independently actuated soft fingers, each with 3 degrees of freedom from asymmetric tendon-driven bending plus active rotation at the finger's base.
* An asymmetric soft joint that gives direction-dependent compliance — flexible in one direction, stiffer in another.
* Passive geometric blocking that limits over-deformation, mechanically protecting the fingers from excessive loads.
* A modular build in which each finger can be assembled and removed independently, so a damaged finger can be swapped without replacing the whole gripper.
* A demonstrated capability to continuously rotate a grasped object about its axis without releasing the initial grasp.

**How does it work?**

The three soft fingers wrap around an object; tendons pull asymmetrically within each finger to produce bending, while base actuators rotate each finger independently. Coordinating the bending and base rotation across the three fingers rolls the object between them, changing its orientation while contact and grip force are maintained throughout. The asymmetric joint design normally deforms freely but mechanically "locks" past a certain range, protecting the fingers from damage under excessive force.

**Strengths**

* Preserves the safety and adaptability of soft robotics while adding precise in-hand repositioning.
* Validated across a wide range of object sizes and stiffnesses: bottles, cubes, tissue boxes, toys, a 3D-printed figurine, a rubber duck, a screwdriver, and an artificial rose.
* Modular design simplifies maintenance, since individual fingers can be replaced.
* Clear, practical use cases: orienting parts before assembly, and handling fragile or irregularly shaped objects.

**Limitations**

* This summary is based on press releases and secondary coverage; quantitative details from the full paper (rotation speed, grip force, repeatability) were not directly confirmed.
* The added base-rotation actuators increase mechanical complexity and cost relative to a fully passive soft gripper.
* The work is a lab-stage demonstration; industrial durability and repeated-use reliability still need further validation.
* This session's network policy blocked direct access to the paper's DOI landing page, so the summary relies on cross-checked web search results (UC3M/UPNA press releases, TechXplore, and a PubMed listing) rather than a direct read of the full text.

**Terms to know**

* Soft robotics: A field of robotics using flexible materials instead of rigid metal or plastic, for safer and more adaptable robots.
* In-hand manipulation: Changing an object's position or orientation while it remains held by a gripper or hand.
* Degree of freedom (DoF): An independent direction or axis along which a robotic part can move.
* Tendon-driven actuation: A method of bending or moving flexible structures using pulled cables, similar to biological tendons.
* Asymmetric soft joint: A joint engineered to be more flexible in one direction than another.
* Geometric blocking: A passive mechanism where a structure mechanically stops moving past a certain deformation limit, protecting it from damage.

**Why it is worth watching**

Robots in manufacturing and logistics routinely need to reorient a part after grasping it, and today's soft grippers often handle this inefficiently by releasing and re-grasping. This work offers a practical path to reduce that inefficiency without sacrificing the safety benefits of soft robotics, with direct relevance to assembly automation and handling of delicate or irregular objects.

---

## My take

이 논문은 화려한 발표보다는 실용적인 공학적 개선에 가깝다. 소프트 그리퍼의 안전성과 능동 자유도를 결합한 아이디어 자체는 완전히 새롭지는 않지만, 모듈형 설계와 비대칭 관절을 통한 보호 메커니즘을 결합해 실제 산업 적용 가능성을 높인 점이 눈에 띈다. 다만 이 요약은 논문 원문이 아니라 보도자료와 2차 자료를 바탕으로 작성되었으므로, 정량적 성능(회전 속도, 반복 정밀도 등)에 대한 평가는 유보적으로 보는 것이 맞다.

This paper reads as a solid, incremental engineering contribution rather than a flashy breakthrough. Combining soft-gripper compliance with active degrees of freedom isn't entirely new, but pairing it with a modular build and a passive protection mechanism (asymmetric joints with geometric blocking) makes it more plausible for real industrial use. That said, since this summary was built from press releases and secondary sources rather than the full paper text, quantitative performance claims (rotation speed, repeatability) should be treated with some caution until the primary source is reviewed directly.
