---
title: "Earth System Foundation Model (ESFM): A unified framework for heterogeneous data integration and forecasting"
date: 2026-05-31
topic: climate-AI
tags: [climate-AI, weather-forecasting, Earth-system, foundation-model, heterogeneous-data, axial-attention, Aurora, geoscience]
source: https://arxiv.org/abs/2605.00850
---

# Earth System Foundation Model (ESFM): A unified framework for heterogeneous data integration and forecasting

* Date: 2026-05 (arXiv preprint submitted May 2026; presented at EGU General Assembly 2026, Vienna, 3–8 May 2026)
* Source: https://arxiv.org/abs/2605.00850
* Topic: climate-AI / Earth system forecasting
* Why it matters: All major AI weather models to date are trained on dense, uniform atmospheric reanalysis grids alone. ESFM is the first fully open Earth system foundation model that integrates heterogeneous observational data — dense reanalysis, climate simulations, sparse satellite imagery with as little as 3% pixel coverage, and scattered ground-station records — under a single backbone, and can accurately forecast weather variables even when most input data is missing at initialization time.

## Korean Summary

**한줄 요약**

ETH 취리히·EPFL 공동 연구팀이 개발한 ESFM은 ERA5 격자 데이터·CMIP6 기후 시뮬레이션·MODIS 위성 영상·지상 관측소 데이터를 단일 모델로 통합하는 완전 공개형 지구 시스템 기반 모델로, 유효 픽셀이 3%에 불과한 희소 위성 데이터만으로도 기상 예측을 수행하며 훈련 데이터 외 극단적 기상 사례(태풍 독수리, 성층권 급가열)에도 강건한 일반화 성능을 보인다. 기존 AI 기상 모델들이 대기 격자 데이터에만 집중한 한계를 넘어, 대기·수문·육지 과정을 하나로 연결한다.

**핵심 아이디어**

지구 관측 데이터는 ERA5(0.25° 균등 격자 재분석), CMIP6(거친 기후 시뮬레이션), MODIS(희소 위성 영상, ~3% 유효 픽셀), 기상 관측소(비격자 점 데이터) 등 해상도·밀도·변수 구성이 크게 다른 이질적 형태로 존재한다. ESFM은 각 물리 변수를 독립적으로 토크나이즈하고, 결측 관측을 위한 학습 가능한 '결측 토큰'을 도입하며, 변수 차원에 대한 Axial Attention으로 온도·기압·습도 등 변수 간 물리적 상관관계를 포착함으로써, 초기 시점에 데이터가 없는 지역이나 기압면도 예측할 수 있다.

**무엇이 새로운가?**

- **개별 변수 토크나이저**: 각 물리 변수에 독립적인 tokenizer를 부여하고, 학습 가능한 결측 관측 토큰을 사용해 훈련 중 변수 집합을 무작위로 섞어도 처리 가능하며 어떤 변수 조합이 누락돼도 자연스럽게 대응
- **다중 해상도 tokenizer 그룹**: ERA5(0.25°), CMIP6(더 거친 격자), MODIS 위성 영상, 관측소 점 데이터를 해상도 범주별로 별도 tokenizer 집합으로 인코딩하여 동일한 Swin UNet backbone에서 처리
- **탐욕적(Greedy) 관측소 격자 매핑**: 비격자형 지상 관측소를 불규칙 위도-경도 격자에 순차적으로 배치하여 윈도우 어텐션 내에서 공간적 인접성 유지
- **변수 차원 Axial Attention**: 변수 토큰 축에 대해서만 자기-어텐션을 수행하여 변수 간 상호 의존성을 효율적으로 포착하고, 특정 지역·기압면에 관측이 없어도 물리적으로 연관된 변수를 통해 예측 가능
- **적응형 Layer Norm 앙상블**: 노이즈 조건부 토큰으로 결정론적 모델을 확률적 기반 모델로 확장하여 예측 불확실성 정량화 가능

**어떻게 작동하는가?**

1. 입력 데이터(ERA5 격자, CMIP6, MODIS 위성, 관측소)를 해상도 범주에 따라 분류하고 해당 tokenizer로 패치 임베딩 생성; 결측 픽셀·변수는 학습된 결측 토큰으로 대체
2. 비격자 관측소 데이터는 탐욕적 알고리즘으로 불규칙 위도-경도 격자에 매핑 — 열 내 위도와 행 내 경도가 단조 증가하도록 배치하여 윈도우 어텐션 내 공간 인접성 보장
3. Aurora로부터 계승한 3D Swin UNet backbone이 시공간 특징을 계층적으로 추출
4. Axial Attention이 변수 차원의 상호작용을 처리 — 온도·기압·습도가 동시에 존재하지 않아도 물리적 상관관계 기반 예측 가능
5. 적응형 Layer Norm 앙상블 헤드가 노이즈 토큰 조건에 따라 확률적(앙상블) 또는 결정론적 예측 생성
6. 원하는 하위 작업(수문 예측, 계절 예측, 가뭄 지수 등)에 파인튜닝하여 특화 모델로 활용

**강점**

- ERA5·CMIP6·MODIS·관측소 데이터 등 4종 이질적 데이터를 단일 기반 모델에서 처리
- 픽셀의 3%만 유효한 위성 데이터로도 기상 예측 가능
- 훈련 데이터 외 사례(태풍 독수리 2023, 성층권 급가열 2024)에도 강건한 일반화 성능 — 바람 강도·이동 경로·팽창 규모를 며칠 동안 정확히 예측
- GraphCast, SFNO, Aurora 대비 경쟁적 또는 우수한 성능
- 완전 공개(fully open source, github.com/swiss-ai/ESFM) — 재현성·협업 연구 보장
- 농업·수문·생물 다양성·가뭄 위험 지도·재난 대응 등 다양한 다운스트림 과제로 파인튜닝 가능

**한계**

- 공개 요약에서 구체적인 정량 벤치마크 수치(RMSE 개선 폭 등)가 충분히 제공되지 않음
- Aurora의 3D Swin UNet backbone을 상속하므로 backbone 자체의 고정 패치 크기·메모리 비용 등 제약이 그대로 적용
- 탐욕적 관측소 매핑은 관측소 밀도가 매우 높거나 불규칙한 지역에서는 최적 해법이 아닐 수 있음
- ECMWF 운영 예측 시스템과의 체계적 직접 비교는 향후 과제
- 확률적 앙상블의 보정(calibration) 성능 상세 평가 미공개

**알아둘 용어**

- **지구 시스템 기반 모델 (Earth System Foundation Model)**: 대기·수문·육지 과정을 통합적으로 모델링하는 기상·기후 AI 기반 모델; 특정 예측 작업에 파인튜닝 가능한 범용 사전학습 모델
- **ERA5**: ECMWF(유럽중기예보센터)의 지구 대기 재분석 데이터셋, 0.25° 해상도 격자, 1940년~현재
- **CMIP6**: 제6차 기후 모형 상호 비교 프로젝트 — 다수의 기후 시뮬레이션 표준 데이터
- **MODIS**: NASA의 중해상도 영상 분광계(Moderate Resolution Imaging Spectroradiometer), 구름 등으로 인해 픽셀 대부분이 결측인 희소 위성 관측 데이터 제공
- **Axial Attention**: 고차원 데이터의 특정 축(여기서는 변수 축)에 대해서만 자기-어텐션을 수행하는 효율적 어텐션 기법; 전체 크로스-변수 어텐션 대비 계산 비용 대폭 감소
- **결측 토큰 (Learnable Missing Token)**: 관측이 없는 시공간 위치를 대체하는 학습 가능한 임베딩 벡터; 마스크 훈련 시 자연스럽게 결측 처리 가능
- **3D Swin UNet**: Aurora에서 사용된 3차원 슬라이딩 윈도우 기반 Vision Transformer + U-Net 인코더-디코더 구조

**왜 주목할 만한가?**

기후 변화로 극단적 기상 현상이 빈번해지는 시대에, 기상 AI 모델은 격자형 대기 데이터만으로는 불충분하다. ESFM은 위성·관측소·기후 시뮬레이션까지 통합함으로써 데이터 인프라가 부족한 개발도상국이나 관측 공백 지역에서도 고품질 예측을 제공할 수 있는 가능성을 열었다. 완전 공개 모델로 재현성과 과학적 협업을 보장한다는 점, 그리고 EGU 2026에서 발표돼 국제 지구과학 커뮤니티의 주목을 받고 있다는 점에서 앞으로의 후속 연구가 기대된다.

---

## English Summary

**One-line summary**

ESFM is a fully open Earth system foundation model from ETH Zurich and EPFL that integrates heterogeneous observational data — dense reanalysis grids (ERA5), climate simulations (CMIP6), sparse satellite imagery (MODIS, as little as 3% valid pixels), and ground-station records — under a single 3D Swin UNet backbone, enabling accurate forecasting even when most input observations are absent at initialization.

**Core idea**

Existing AI weather models, including GraphCast and Aurora, are trained almost exclusively on dense, uniformly gridded atmospheric reanalysis data. Real Earth observations are far more heterogeneous: MODIS satellite images often have fewer than 3% valid pixels due to cloud cover; ground stations are spatially scattered and report only a local subset of variables; climate simulation data arrives on coarser, irregular grids. ESFM solves this by extending the Aurora foundation model with three architectural innovations — individual variable tokenization with learnable missing tokens, axial attention over the variable dimension, and greedy station-to-grid mapping — enabling a single model to digest all four data types simultaneously without requiring complete observations.

**What is new?**

- **Individual variable tokenization**: Each physical variable (temperature, pressure, humidity, etc.) has its own learned tokenizer and a dedicated learnable "missing observation token," so any subset of variables can be absent at any spatial location; the model is trained with randomly shuffled variable sets to develop robustness to missing inputs
- **Multi-resolution tokenizer groups**: Different resolution bins (ERA5 at 0.25°, coarser CMIP6, satellite images, station point data) are encoded by separate tokenizer sets that map into the same backbone, avoiding the need to resample heterogeneous inputs to a common grid
- **Greedy station-to-grid mapping**: Irregular in-situ station coordinates are greedily assigned to a pseudo-regular latitude-longitude grid such that latitudes are monotonically increasing within each column and longitudes within each row, preserving spatial adjacency for windowed self-attention
- **Axial attention across the variable dimension**: Self-attention computed along the variable-token axis captures physical correlations (e.g., temperature–pressure–humidity co-variation) and allows the model to infer variables in unobserved regions or pressure levels from co-varying observed quantities
- **Adaptive layer-norm ensembles**: A noise-conditioning token transforms the deterministic backbone into a probabilistic forecaster without any architectural change, enabling uncertainty quantification over ensemble members

**How does it work?**

1. Incoming data is grouped by resolution: ERA5/CMIP6 gridded fields, MODIS satellite imagery, and station point observations each pass through their respective tokenizer; missing pixels or absent variables are replaced by learned missing tokens
2. Non-gridded station records are placed on a pseudo-regular grid via greedy longitude-latitude assignment that maintains spatial proximity to support windowed self-attention
3. All tokens enter the 3D Swin UNet backbone (inherited from Aurora) for hierarchical spatiotemporal feature extraction
4. Axial attention over the variable dimension then processes inter-variable interactions, learning that temperature, pressure, and humidity co-vary even when some are unobserved in certain locations
5. The adaptive layer-norm ensemble head generates probabilistic forecasts when a noise token is provided, or deterministic forecasts otherwise — the same backbone serves both modes
6. For downstream applications (flood forecasting, drought indices, seasonal outlooks, etc.), users fine-tune the pretrained backbone on task-specific data

**Strengths**

- Handles four heterogeneous data modalities (ERA5, CMIP6, MODIS, stations) in one unified foundation model
- Produces skillful forecasts from MODIS satellite images with as little as 3% pixel coverage
- Accurately forecasts out-of-distribution extreme events: Super Typhoon Doksuri (2023) wind strength, track, movement speed, and spatial extent over multiple days; 2024 sudden stratospheric warming events
- Competitive or superior to GraphCast, SFNO, and Aurora across multiple evaluation sets
- Fully open source (github.com/swiss-ai/ESFM), promoting reproducibility and community development
- Versatile foundation for fine-tuning to agriculture, hydrology, biodiversity, disaster risk, and regional climate applications

**Limitations**

- Specific quantitative benchmark numbers (e.g., RMSE improvements vs. baselines) are not fully detailed in available public summaries
- Inherits the constraints of the Aurora 3D Swin UNet backbone, including fixed patch sizes and memory requirements
- Greedy station mapping may not be optimal for very dense or highly irregular observing networks
- Systematic head-to-head comparison against ECMWF operational forecasts is left for future work
- Calibration quality (reliability diagrams) of the probabilistic ensemble has not yet been fully evaluated

**Terms to know**

- **Earth system foundation model**: An AI model trained jointly on atmosphere, hydrosphere, and land-surface data to serve as a versatile pre-trained base for downstream climate and weather tasks, rather than a task-specific forecast model
- **ERA5**: ECMWF's global atmospheric reanalysis dataset on a 0.25° grid, covering 1940 to the present; the de facto standard training dataset for AI weather models
- **CMIP6**: The sixth phase of the Coupled Model Intercomparison Project — a standard library of coupled climate model simulation outputs at coarser resolutions
- **MODIS**: NASA's Moderate Resolution Imaging Spectroradiometer, a satellite instrument that provides global surface observations but with highly variable coverage due to cloud cover and orbital geometry
- **Axial attention**: Self-attention restricted to a single data axis (here the variable axis), dramatically reducing the quadratic cost of full cross-variable attention while still capturing inter-variable dependencies
- **Learnable missing token**: A trainable embedding vector that replaces absent observations at any spatiotemporal location, allowing masked training that naturally handles incomplete multimodal input
- **3D Swin UNet**: The hierarchical sliding-window Transformer combined with a U-Net encoder-decoder architecture used in the Aurora foundation model and inherited by ESFM

**Why it is worth watching**

As climate change drives more frequent and severe extreme weather events, forecasting systems must go beyond uniform atmospheric grids and integrate the full diversity of available Earth observations. ESFM demonstrates that a single open foundation model can unify satellite imagery, in-situ station records, and gridded climate data — remaining accurate even when data coverage is sparse — and produces physically coherent forecasts for novel extreme events it was never trained on. This opens a path to high-quality, globally accessible forecasting in data-scarce regions, and provides the community with a freely reusable base for downstream climate applications from drought early warning to agricultural planning. The presentation at EGU 2026 and accompanying press coverage signal broad interest from the geoscience community.

**My take**

(Korean) ESFM은 이질적 지구 관측 데이터를 단일 기반 모델로 통합한다는 구체적인 아키텍처 혁신을 통해 AI 기상 예측의 중요한 공백을 메운다. 완전 공개 모델이라는 점과 훈련 외 극단 사례에서의 강건한 성능은 고무적이다. 다만 운영 예측 시스템과의 체계적 비교 및 보정 평가가 아직 부족하여, 실제 기상 서비스 도입을 위해서는 추가 검증이 필요하다.

(English) ESFM fills a genuine gap in AI weather modeling by tackling the heterogeneous-data integration problem with concrete, well-motivated architectural choices rather than workarounds. The fully open release and strong generalization to unseen typhoon and stratospheric events are encouraging signals. However, the paper would benefit from systematic head-to-head comparisons with operational forecast centers and full calibration evaluations before it can be confidently positioned as a practical upgrade to existing weather services.
