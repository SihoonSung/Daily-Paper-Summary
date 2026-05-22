---
title: "STELLAR: Scaling 3D Perception Large Models for Autonomous Driving"
date: 2026-05-22
topic: autonomous-driving
tags: [autonomous-driving, 3D-perception, scaling-laws, LiDAR, sensor-fusion, transformer, Waymo]
source: https://arxiv.org/abs/2605.20390
---

# STELLAR: Scaling 3D Perception Large Models for Autonomous Driving

* Date: 2026-05-19
* Source: https://arxiv.org/abs/2605.20390
* Topic: autonomous-driving
* Why it matters: Scaling laws transformed NLP and vision — but whether the same recipe works for multi-sensor 3D perception remained an open question. STELLAR answers it affirmatively: a 500M-parameter model trained on 50 million real driving examples with LiDAR, radar, camera, and HD-map inputs yields clear empirical scaling curves and a new state-of-the-art on the Waymo Open Dataset, the hardest public AV perception benchmark.

## Korean Summary

**한줄 요약**

자율주행 인식 시스템에도 LLM과 동일한 스케일링 법칙이 적용되는가는 오랫동안 열린 질문이었다. Waymo의 STELLAR는 Sparse Window Transformer 기반으로 LiDAR·레이더·카메라·HD맵을 동시에 융합해 5억 개 파라미터, 5천만 주행 사례 규모로 훈련하면서 모델 크기·데이터·연산량과 성능 간의 명확한 경험적 스케일링 곡선을 도출하고 Waymo Open Dataset에서 새 최고 성능을 기록했다.

**핵심 아이디어**

대형 언어 모델과 이미지 기초 모델에서 검증된 '모델 크기·데이터·연산량이 늘면 성능도 예측 가능하게 향상된다'는 스케일링 패러다임이 자율주행 3D 인식에도 적용되는지를 체계적으로 연구한 논문이다. 자율주행 인식은 LiDAR 포인트 클라우드처럼 희소하고 3차원인 데이터를 다뤄야 하고, 이질적인 여러 센서를 동시에 융합해야 하며, 실세계 주행 시나리오의 다양성이 매우 크기 때문에, 단순한 스케일업이 통할지 자명하지 않았다. STELLAR는 이 질문에 긍정적으로 답한다: 올바른 아키텍처와 데이터 파이프라인 아래서 자율주행 인식도 예측 가능한 스케일링 곡선을 따른다.

**무엇이 새로운가?**

- 자율주행 3D 인식에서 모델 크기·데이터·연산량이 성능에 미치는 영향을 체계적으로 측정한 최초의 대규모 스케일링 연구
- 단일 모델에 LiDAR·레이더·카메라·HD맵 4가지 이질적 입력 모달리티를 통합해 최대 5억 파라미터, 5천만 주행 사례 규모로 훈련
- 자율주행 인식 특유의 도전(이질적 센서 융합, 3D 공간 이해)을 극복하면서도 확장 가능한 아키텍처 설계 제시
- LLM과 유사한 스케일링 곡선이 자율주행 인식에서도 성립함을 실증
- Waymo Open Dataset 챌린지에서 기존 최고 성능을 큰 폭으로 경신

**어떻게 작동하는가?**

1. **Sparse Window Transformer (SWFormer) 기반 아키텍처**: 3D 포인트 클라우드를 희소 복셀(voxel)로 변환한 뒤 공간 윈도우 단위로 나눠 트랜스포머 어텐션을 적용한다. 복셀 집합의 길이가 가변적인 문제는 버킷팅(bucketing) 기법으로 해결한다.
2. **다중 모달리티 입력 통합**: LiDAR(정밀 3D 형상), 레이더(도플러 속도, 악천후 강인성), 카메라(색상·텍스처·의미론적 정보), HD맵(도로 위상·차선 정보)을 단일 모델에서 공동 처리한다.
3. **대규모 데이터셋 구축**: Waymo의 실세계 주행 데이터 5천만 건을 훈련에 활용한다. 다양한 날씨·시간대·지역 시나리오를 포괄한다.
4. **스케일링 실험 설계**: 파라미터 수(~수백만 → 5억)·훈련 데이터 양·연산 예산을 각각 체계적으로 변화시키면서 3D 객체 탐지 성능(mAP, mAPH 등) 변화를 측정한다.
5. **스케일링 법칙 도출**: 실험 결과를 멱함수(power law)로 피팅해 모델 크기·데이터·연산량과 성능 간의 경험적 관계식을 추출한다. 이 관계식은 미래 모델 설계의 가이드가 된다.

**강점**

- 자율주행 인식에 스케일링 법칙이 성립함을 실증적으로 보인 첫 번째 포괄적 연구
- Waymo의 방대한 실제 주행 데이터(5천만 건)를 활용해 실험의 현실성과 규모를 보장
- 단일 아키텍처로 4종 이질적 센서를 통합해 복잡한 앙상블 없이 높은 성능 달성
- 도출된 스케일링 곡선은 업계 전반의 연산 자원 배분과 모델 설계 의사결정에 실용적 가이드 제공
- Waymo Open Dataset이라는 독립 검증 가능한 공개 벤치마크에서 최고 성능 기록

**한계**

- Waymo의 독점 50M 주행 데이터셋을 사용하므로 외부 연구자의 완전한 재현이 어려움
- 도출된 스케일링 곡선이 다른 지리·기후·센서 구성을 가진 환경에도 일반화되는지 불명확
- 훈련 비용(컴퓨팅, 에너지)이 구체적으로 공개되지 않아 비용 대비 이익을 평가하기 어려움
- HD맵에 의존하는 map prior 입력은 맵이 없는 도로나 변경된 도로에서는 활용이 제한됨
- 5억 파라미터 모델이 실시간 온보드 처리에 적합한지 배포 측면의 분석이 불분명

**알아둘 용어**

- **스케일링 법칙 (Scaling Laws)**: 모델 파라미터 수, 훈련 데이터 양, 연산량이 늘어남에 따라 모델 성능이 예측 가능한 멱함수 관계로 향상된다는 경험 법칙. LLM에서 Chinchilla 등이 대표적.
- **Sparse Window Transformer (SWFormer)**: 3D 포인트 클라우드를 희소 복셀로 변환하고 공간 윈도우 단위로 트랜스포머 어텐션을 적용해 효율적인 3D 객체 탐지를 수행하는 아키텍처.
- **LiDAR (Light Detection and Ranging)**: 레이저 펄스를 이용해 주변 환경의 정밀한 3D 포인트 클라우드를 취득하는 센서. 자율주행의 핵심 센서.
- **레이더 (Radar)**: 전파를 이용해 객체의 거리와 속도(도플러)를 측정하는 센서. 빛이나 날씨 조건에 덜 민감해 LiDAR를 보완한다.
- **HD맵 (High-Definition Map)**: 차선 위치, 교통 신호, 도로 경계 등을 센티미터 수준 정밀도로 담은 지도. 인식 모델의 prior 정보로 활용된다.
- **mAP / mAPH (mean Average Precision / Heading)**: 3D 객체 탐지 성능 지표. mAPH는 탐지된 객체의 방향(heading)까지 정확해야 높은 점수를 받는다.
- **Waymo Open Dataset**: Waymo가 공개한 자율주행 인식 벤치마크. 다수의 3D 탐지 과제로 구성되며, 자율주행 연구의 사실상 표준 평가 기준이다.

**왜 주목할 만한가?**

LLM에서 검증된 스케일링 패러다임이 자율주행 인식으로 확장된다는 것은 산업 전체에 중요한 메시지다. 이제 "더 많은 데이터와 더 큰 모델이 AV 인식 성능을 얼마나 높이는가?"를 수치로 예측할 수 있게 됐다는 의미이기 때문이다. 이는 투자 규모 결정, 아키텍처 선택, 데이터 수집 전략 수립에 실용적 기준을 제공한다. 또한 단일 모델이 4가지 이질 센서를 통합하면서도 명확한 스케일링 이득을 보인다는 사실은 다중 모달 기초 모델의 가능성을 AV 도메인으로 넓히는 증거이기도 하다.

---

## English Summary

**One-line summary**

Whether the scaling-laws recipe from LLMs applies to multi-sensor 3D perception for autonomous driving was an open question. STELLAR, a Sparse Window Transformer model trained on 50 million real driving examples with LiDAR, radar, camera, and HD-map inputs at up to 500M parameters, answers yes: clear empirical scaling curves emerge and the model sets a new state-of-the-art on the Waymo Open Dataset by a large margin.

**Core idea**

In NLP and 2D vision, it is well established that model performance improves predictably as model size, training data, and compute grow together. The autonomous driving perception domain poses distinct challenges — fusing heterogeneous sensor modalities (LiDAR point clouds, radar returns, camera images, HD maps), reasoning in 3D space, and handling enormous scene diversity — so it was not obvious that the same scaling paradigm would hold. STELLAR is a systematic study that demonstrates it does: given the right architecture and data pipeline, AV 3D perception follows predictable scaling trends, and a large model trained at scale achieves a decisive new performance record on the hardest public AV benchmark.

**What is new?**

- First comprehensive scaling study for 3D perception in autonomous driving, measuring the joint impact of model size, data volume, and compute on detection performance
- Unifies four heterogeneous sensor modalities (LiDAR, radar, camera, HD-map prior) in a single model scaled to 500M parameters trained on 50M driving examples
- Derives empirical scaling laws specific to multi-sensor 3D perception, analogous to Chinchilla-style laws in NLP
- Shows that AV-specific challenges (sparse 3D inputs, sensor heterogeneity) do not break the scaling paradigm
- Achieves state-of-the-art by a large margin on the Waymo Open Dataset challenge

**How does it work?**

1. **Sparse Window Transformer backbone**: 3D LiDAR point clouds are voxelized and partitioned into spatial windows; Transformer self-attention is applied within each window. A bucketing scheme handles the variable length of sparse window contents efficiently.
2. **Multi-modal input fusion**: LiDAR (precise 3D geometry), radar (Doppler velocity, weather robustness), camera (color, texture, semantic content), and HD-map prior (lane topology, road boundaries) are all fed into a unified model.
3. **Large-scale dataset**: Training uses 50 million real-world driving examples from Waymo's proprietary fleet, spanning diverse weather, time-of-day, and geographic conditions.
4. **Scaling experiment design**: Model size (millions to 500M parameters), training data volume, and compute budget are each varied systematically while measuring 3D object detection metrics (mAP, mAPH).
5. **Scaling law derivation**: Experimental outcomes are fit to power-law relationships between scale axes and performance, producing predictive equations that can guide future architecture and resource decisions.

**Strengths**

- First paper to rigorously establish that scaling works for AV 3D perception, providing a practical roadmap for the industry
- Uses 50M real driving examples at Waymo scale, making the experiments realistic and hard to dismiss as toy results
- Single unified architecture handles four sensor types without complex ensemble pipelines
- Derived scaling curves offer actionable guidance for compute budgeting and data collection prioritization
- Results validated on the Waymo Open Dataset, a publicly verifiable, industry-standard benchmark

**Limitations**

- Training data (50M examples) is from Waymo's proprietary fleet; full independent replication by academic labs is not feasible
- It is unclear how well the derived scaling curves generalize to different geographies, climates, sensor configurations, or vehicle types
- Training cost (GPU-hours, energy consumption) is not publicly detailed, making cost-benefit analysis difficult
- Dependence on HD-map priors limits applicability in unmapped or dynamically changing road environments
- Whether a 500M-parameter model can run in real time on on-board AV compute hardware is not addressed in available summaries

**Terms to know**

- **Scaling laws**: Empirical power-law relationships showing that model performance improves predictably as model size, training data, and compute scale together; best known from NLP research (Kaplan et al. 2020, Chinchilla 2022).
- **Sparse Window Transformer (SWFormer)**: An efficient 3D detection architecture that voxelizes point clouds, partitions them into sparse spatial windows, and applies Transformer attention within each window; developed originally at Waymo/Google in 2022.
- **LiDAR**: A sensor that fires laser pulses and measures return times to build a precise 3D point cloud of the surroundings; the primary geometric sensor in most AV systems.
- **Radar**: A sensor using radio waves to measure distance and radial velocity (Doppler); more robust than LiDAR in fog, rain, or night conditions, but sparser.
- **HD map (High-Definition map)**: A centimeter-precision map encoding lane positions, road boundaries, traffic signs, and topology; used here as a prior input to inform the perception model.
- **mAP / mAPH**: Standard 3D detection metrics. Mean Average Precision (mAP) measures localization and classification accuracy; mAPH additionally penalizes incorrect heading prediction.
- **Waymo Open Dataset**: The leading public benchmark for AV 3D perception, released by Waymo; used as the independent evaluation standard in this paper.

**Why it is worth watching**

The practical stakes are high: once scaling curves for AV perception are known, companies can forecast how much their detection performance will improve per dollar of compute and data investment. This turns what was a guesswork-driven R&D question into a more engineering-like one. STELLAR's result also signals that the foundation-model paradigm — large, general, multi-modal — is not limited to language and 2D vision; it extends to the physically demanding, safety-critical domain of 3D sensor fusion. For anyone building, funding, or regulating autonomous driving systems, this paper sets a new empirical baseline for what scaled perception can achieve.

**My take**

STELLAR은 '스케일링이 자율주행에도 통하는가'라는 현실적이고 중요한 질문에 대한 첫 번째 포괄적인 실증 답변이다. 결과 자체도 인상적이지만, 더 중요한 기여는 도출된 스케일링 곡선이다 — 이는 업계 전반에 걸쳐 데이터·컴퓨팅 투자 의사결정을 수치화할 수 있는 기준을 제공한다. 다만 Waymo의 독점 데이터에 기반한 결과가 다른 환경과 센서 구성으로 얼마나 일반화되는지는 독립적인 검증이 필요하다.

STELLAR gives the first comprehensive empirical answer to "do scaling laws hold for AV perception?" and the answer is yes. Beyond the record-setting numbers, the most durable contribution is the scaling curve itself — a quantitative tool for forecasting returns on data and compute investment across the AV industry. The main caveat is that the findings rest on Waymo's proprietary large-scale fleet data; how well the scaling relationships transfer to other sensor suites, geographies, and data regimes will require independent validation.
