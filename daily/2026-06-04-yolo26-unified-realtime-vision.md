---
title: "Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models"
date: 2026-06-04
topic: computer-vision
tags: [computer-vision, object-detection, real-time, YOLO, NMS-free, end-to-end, deep-learning, inference-optimization]
source: https://arxiv.org/abs/2606.03748
---

# Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models

* Date: 2026-06-02 (arXiv preprint)
* Source: https://arxiv.org/abs/2606.03748
* Topic: computer vision / real-time object detection
* Why it matters: YOLO is one of the most widely deployed real-time vision frameworks in industry. YOLO26 eliminates the longstanding NMS post-processing bottleneck with a native end-to-end dual-head design, imports optimizer ideas from LLM training, and improves COCO mAP by 1.6–2.8 points over YOLO11 — a meaningful step forward for the most-used detection pipeline in production.

## Korean Summary

**한줄 요약**

Ultralytics는 YOLO26을 통해 기존 YOLO 계열의 핵심 병목이었던 Non-Maximum Suppression(NMS) 후처리를 네이티브 이중 헤드 아키텍처로 완전히 제거하고, LLM 학습에서 차용한 MuSGD 옵티마이저, 작은 객체 대응 레이블 할당 전략(STAL), 점진적 손실(ProgLoss) 세 가지 학습 혁신을 결합했다. COCO 탐지 기준 40.9–57.5 mAP를 1.7–11.8 ms(T4 TensorRT)로 달성하며 YOLO11 대비 1.6–2.8 AP 향상을 보였다. 탐지·인스턴스 분할·포즈 추정·분류·방향성 탐지를 단일 파이프라인으로 지원한다.

**핵심 아이디어**

전통적인 YOLO 모델은 중복 탐지 박스를 제거하기 위해 NMS라는 후처리 단계가 필수였다. NMS는 레이턴시를 추가하고 엣지·임베디드 배포를 복잡하게 만든다. YOLO26은 학습용 헤드와 추론용 헤드로 구성된 이중 헤드 구조를 도입해 모델이 훈련 중 NMS 없이도 고품질 탐지를 수행하도록 직접 최적화한다. Distribution Focal Loss(DFL)도 완전히 제거해 헤드를 경량화하고 회귀 범위 제한을 해소했다.

**무엇이 새로운가?**

- **NMS-free 이중 헤드 아키텍처**: 학습 헤드와 추론 헤드를 분리해 NMS 후처리 없이 엔드투엔드 추론을 최초로 YOLO 계열에 통합
- **DFL 제거**: Distribution Focal Loss를 제거해 더 가볍고 회귀 범위 제약이 없는 탐지 헤드 구현
- **MuSGD 옵티마이저**: LLM 학습용 Muon 옵티마이저와 SGD를 결합한 하이브리드 옵티마이저로 수렴 품질 향상
- **ProgLoss (Progressive Loss)**: 학습이 진행되면서 감독 신호를 학습 헤드에서 추론 헤드로 점진적으로 이동시키는 손실 전략
- **STAL**: 작은 객체에 양성 샘플을 보장하는 레이블 할당 전략 — 포즈 추정에서 YOLO11 대비 최대 +7.2 AP 향상

**어떻게 작동하는가?**

1. **이중 헤드 추론**: 백본과 넥(Neck)은 그대로 유지하되, 탐지 헤드를 학습 헤드(풍부한 감독 신호 활용)와 추론 헤드(경량, NMS 불필요) 두 개로 분리
2. **ProgLoss 학습**: 초반에는 학습 헤드에 감독 가중치를 높게 두고, 학습이 진행될수록 가중치를 추론 헤드 쪽으로 점진적으로 이동시켜 최종적으로 추론 헤드가 단독으로 정확한 예측을 내도록 훈련
3. **MuSGD 옵티마이저**: Muon이 행렬 가중치의 스케일 불변적 업데이트(뉴턴법 유사)를 담당하고, SGD가 나머지 파라미터를 처리하는 하이브리드 방식
4. **STAL 레이블 할당**: 앵커 프리 방식에서 작은 객체에 양성 샘플이 배정되지 않는 문제를 해결하기 위해 그리드 격자 인근 위치에도 강제로 양성 샘플을 할당
5. **다중 태스크 지원**: 탐지, 인스턴스 분할, 포즈 추정, 분류, 방향성 객체 탐지(OBB) 각각에 최적화된 헤드·손실 설계를 적용, 5가지 스케일(n/s/m/l/x) 제공

**강점**

- NMS 제거로 배포 파이프라인 단순화 및 레이턴시 감소 — 엣지·임베디드 환경에서 특히 유리
- YOLO11 대비 COCO mAP 1.6–2.8 점 향상, 포즈 추정 최대 +7.2 AP
- LLM 학습 기법(MuSGD)을 비전 모델에 성공적으로 이식한 선례
- 단일 파이프라인에서 5가지 시각 태스크를 지원해 인프라 단순화
- Ultralytics 생태계와의 완벽한 호환성으로 기존 YOLO 사용자들이 즉시 적용 가능

**한계**

- 이중 헤드 구조로 파라미터 수가 소폭 증가 — 극단적 메모리 제약 환경에서 불리할 수 있음
- NMS-free 설계는 밀집 객체 시나리오에서 학습이 충분하지 않으면 오탐이 증가할 수 있음
- MuSGD는 LLM에서 검증됐으나 시각 모델에서의 하이퍼파라미터 감도는 추가 연구 필요
- YOLO26 이름이 출시 연도를 반영하나, 버전 계보 혼란(YOLO11 다음이 YOLO26)은 외부 사용자에게 불명확할 수 있음

**알아둘 용어**

- **NMS (Non-Maximum Suppression)**: 객체 탐지 후처리 단계. 동일 객체에 대한 중복 예측 박스 중 가장 신뢰도 높은 것만 남기고 나머지를 제거. 순차적 특성상 병렬화가 어렵고 레이턴시를 유발
- **이중 헤드 (Dual Head)**: 학습 시에만 사용하는 보조 헤드와 실제 추론에 사용하는 주 헤드를 분리한 구조. NMS-free 학습을 가능하게 하는 핵심 설계
- **DFL (Distribution Focal Loss)**: 바운딩 박스 회귀를 확률 분포로 모델링하는 손실 함수. YOLOv8부터 도입됐으나 YOLO26에서 제거됨
- **MuSGD**: Muon 옵티마이저(뉴턴법 유사 스케일-불변 업데이트)와 SGD를 결합한 하이브리드 옵티마이저. 원래 LLM 학습에 개발됨
- **ProgLoss (Progressive Loss)**: 학습 과정에서 감독 신호를 학습 헤드에서 추론 헤드로 점진적으로 이동하는 손실 스케줄링 전략
- **STAL (Small Target Anchor-free Label assignment)**: 작은 객체에도 반드시 양성 앵커를 할당해 탐지 누락을 방지하는 레이블 할당 전략
- **OBB (Oriented Bounding Box)**: 축 정렬이 아닌 임의 각도로 회전된 바운딩 박스. 항공사진, 텍스트 탐지 등에서 유용

**왜 주목할 만한가?**

YOLO 계열은 전 세계 실시간 객체 탐지 파이프라인의 대부분을 차지하는 사실상의 산업 표준이다. YOLO26은 단순한 성능 향상을 넘어 NMS 제거라는 구조적 변화를 통해 배포 복잡도를 줄이고, LLM 학습에서 검증된 옵티마이저 기법을 비전 도메인으로 가져왔다는 점에서 의미가 있다. 엣지 디바이스부터 서버까지 다양한 환경에서 동작하는 단일 파이프라인 솔루션으로서, 이 논문의 영향은 컴퓨터 비전 응용 전 영역에 걸쳐 빠르게 퍼질 것이다.

---

## English Summary

**One-line summary**

Ultralytics YOLO26 eliminates the longstanding NMS post-processing step in the YOLO family by introducing a native dual-head architecture, and pairs it with three training innovations — MuSGD (a hybrid Muon–SGD optimizer borrowed from LLM training), Progressive Loss, and STAL — to achieve 40.9–57.5 mAP on COCO detection at 1.7–11.8 ms T4 TensorRT latency, improving over YOLO11 by 1.6–2.8 AP across scales.

**Core idea**

Every YOLO model before YOLO26 required Non-Maximum Suppression as a mandatory post-processing step to filter duplicate bounding box predictions. NMS adds deployment latency, resists hardware parallelization, and complicates edge deployment. YOLO26 introduces a dual-head design where a training head receives rich supervision and a separate inference head is trained — via Progressive Loss — to produce clean, non-redundant detections directly, eliminating NMS entirely. Distribution Focal Loss (DFL) is also dropped, resulting in a lighter head with unconstrained regression range. Three synchronized training improvements then extract maximum accuracy from this architecture: MuSGD for better convergence, ProgLoss for smooth supervision transfer, and STAL to ensure small objects always receive positive label assignments.

**What is new?**

- **NMS-free dual-head architecture**: The first native end-to-end NMS-free design in the YOLO family, with a dedicated training head and a lighter inference head optimized for deployment
- **DFL removal**: Drops Distribution Focal Loss entirely, yielding a simpler, lighter detection head with no regression range constraints
- **MuSGD optimizer**: A hybrid Muon–SGD optimizer that applies Newton-like scale-invariant updates (from LLM training) to matrix weights while SGD handles the remaining parameters
- **Progressive Loss (ProgLoss)**: A loss scheduling strategy that smoothly shifts supervision signal from the training head to the inference head over the course of training
- **STAL (Small Target Anchor-free Label assignment)**: Forces positive sample assignments for small objects that would otherwise be missed in anchor-free pipelines; delivers up to +7.2 AP on COCO pose estimation over YOLO11

**How does it work?**

1. **Dual head**: The backbone and neck are unchanged; the detection head is split into a training head (receives full supervision) and an inference head (lighter, NMS-free). Only the inference head is used at deployment time
2. **Progressive Loss**: Early in training, supervision loss weight is concentrated on the training head; as training progresses, the weight is gradually shifted toward the inference head, forcing it to produce accurate, non-redundant predictions independently by the end of training
3. **MuSGD optimizer**: Muon handles scale-invariant updates for matrix parameters using a Newton-step-like rule derived from the Muon LLM optimizer; SGD handles biases and normalization parameters. The combination improves convergence quality without requiring different learning rates per layer
4. **STAL label assignment**: In anchor-free detectors, very small objects often fall outside the receptive field radii used for positive assignment. STAL forces assignments in a small neighborhood of the target center, guaranteeing at least one positive sample per small object even under aggressive downsampling
5. **Multi-task pipeline**: Task-specific head and loss designs cover detection, instance segmentation, pose estimation, image classification, and oriented bounding box detection (OBB) in five model scales (n/s/m/l/x)

**Strengths**

- Eliminating NMS simplifies deployment pipelines and reduces latency, with direct benefits for edge and embedded hardware
- 1.6–2.8 mAP improvement over YOLO11 on COCO detection; up to +7.2 AP on COCO pose estimation
- Successful transfer of LLM-derived optimizer techniques (MuSGD / Muon) to vision model training
- Single unified pipeline covers five vision tasks across five model scales — reduces infrastructure overhead for multi-task deployments
- Fully compatible with the existing Ultralytics ecosystem, giving immediate access to all existing YOLO11/v8 tooling

**Limitations**

- Dual-head structure adds a small parameter overhead versus single-head designs — may be limiting in extreme memory-constrained environments
- NMS-free training requires the inference head to learn globally consistent non-redundant predictions, which may be harder to train correctly on highly crowded scenes
- MuSGD hyperparameters (Muon step size, transition schedule) are well understood for LLMs but sensitivity in vision models warrants additional study
- The "YOLO26" naming (skipping from YOLO11 to YOLO26 to reflect the release year) may cause versioning confusion for users tracking the YOLO lineage

**Terms to know**

- **NMS (Non-Maximum Suppression)**: Post-processing step that eliminates duplicate bounding boxes by keeping only the highest-confidence prediction for each detected object. Sequential nature limits parallelization and adds inference latency
- **Dual head**: An architecture with separate training-time and inference-time detection heads; during training both heads are supervised, at inference only the lighter head runs
- **DFL (Distribution Focal Loss)**: A loss that models bounding box regression as a discrete probability distribution, introduced in YOLOv8. Removed in YOLO26 for a simpler regression formulation
- **MuSGD**: Hybrid optimizer combining Muon (Newton-like scale-invariant updates for matrix weights) with SGD (for biases and normalization layers), originally developed for large language model training
- **ProgLoss (Progressive Loss)**: A loss scheduling technique that gradually transfers supervision weight from a rich training head to a leaner inference head over the training run
- **STAL**: Small Target Anchor-free Label assignment — ensures small objects receive at least one positive training sample by enforcing assignments in a neighborhood around the object center
- **OBB (Oriented Bounding Box)**: Bounding boxes with arbitrary rotation angle, as opposed to axis-aligned boxes; useful in aerial imagery, scene text detection, and industrial inspection

**Why it is worth watching**

YOLO is the dominant framework for real-time object detection across industry applications ranging from autonomous vehicles and surveillance to robotics and industrial inspection. YOLO26 matters not just for the accuracy gains — which are real but incremental — but for two structural changes with lasting impact. First, removing NMS simplifies the entire deployment pipeline; NMS-free inference is easier to accelerate on custom hardware, easier to export to ONNX/TensorRT, and removes a source of latency variance in production systems. Second, successfully importing the Muon optimizer from LLM training into vision models is an early signal that optimizer research from language modeling may generalize across modalities. For any team currently running YOLO11 or earlier in production, this paper is a direct upgrade path worth evaluating.

**My take**

(Korean) YOLO26의 가장 주목할 만한 점은 단순 성능 향상이 아니라 NMS 제거라는 구조적 변화다. NMS는 오랫동안 탐지 파이프라인에서 불편하지만 필수적인 요소로 인식됐는데, 이를 학습 과정 자체에서 해결한다는 접근은 명확한 실용적 가치가 있다. MuSGD의 크로스-도메인 적용도 흥미롭지만 하이퍼파라미터 민감도에 대한 추가 연구가 필요하다. 전반적으로 이 논문은 점진적 개선이지만 산업 표준 모델의 점진적 개선은 수백만 개의 배포에 직접 영향을 미친다는 점에서 실질적 중요성이 높다.

(English) YOLO26's most durable contribution is the structural removal of NMS rather than the specific accuracy numbers. NMS has been an awkward but accepted fixture of detection pipelines for years; solving it through architecture and training design rather than a learned filter is a cleaner approach and should translate directly to simpler, faster deployment across hardware. The cross-domain transfer of MuSGD from LLMs is interesting but is the claim that needs the most independent verification — optimizer behavior can be sensitive to domain specifics. Overall this is an incremental but high-impact paper: marginal improvements to the world's most widely deployed vision pipeline have outsized practical reach.
