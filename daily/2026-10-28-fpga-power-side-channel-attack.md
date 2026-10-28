---
title: "ML-Assisted Power Side-Channel Attacks on ML Accelerators in Shared FPGAs"
date: 2026-10-28
topic: security
tags: [security, side-channel-attack, fpga, hardware-security, cloud-computing, machine-learning]
source: https://arxiv.org/abs/2610.16164
---

ML-Assisted Power Side-Channel Attacks on ML Accelerators in Shared FPGAs

* Date: 2026-10-28
* Source: https://arxiv.org/abs/2610.16164
* Topic: Security / hardware side-channel attacks
* Why it matters: Cloud providers increasingly let multiple customers share the same physical FPGA chip to run machine-learning accelerators cheaply; this paper shows that a co-located tenant can use only an on-chip sensor (no external equipment) to leak and reconstruct realistic, full-color images that a neighboring tenant's ML accelerator is processing.

## Korean Summary

**한줄 요약**

이 논문(arXiv:2610.16164, 2026년 10월 12일 공개, 동료 검토 전 프리프린트)은 클라우드에서 여러 사용자가 하나의 FPGA 칩을 공유할 때, 같은 칩에 입주한 공격자가 외부 장비 없이 칩 내부 센서만으로 피해자의 ML 가속기가 처리 중인 이미지를 복원할 수 있음을 보여준다. Yale 대학의 Anthony Etim, Kenan Erol, Jakub Szefer가 저자이다.

**핵심 아이디어**

FPGA는 전력 소비 패턴이 그 안에서 실행되는 연산 내용과 상관관계를 가진다. 기존 연구들은 외부 오실로스코프 없이 FPGA 내부에 구현한 TDC(Time-to-Digital Converter) 센서로도 이런 전력 신호를 측정할 수 있음을 보였지만, 흑백의 MNIST 숫자 이미지 같은 아주 작고 단순한 입력만 복원할 수 있었다. 이 논문은 머신러닝 기반 업스케일링·컬러 복원 기법을 결합해, 실제 클라우드 서비스에서 쓰이는 224×224 크기의 ImageNet급 컬러 이미지까지 복원 범위를 확장했다.

**무엇이 새로운가?**

* 외부 프로브나 오실로스코프 없이, 칩 내부에 구현한 TDC 센서만으로 수행하는 최초의 ImageNet급 완전 컬러 이미지 복원 공격.
* 피해자의 CNN 중 첫 번째 합성곱(convolution) 레이어가 224×224 입력을 처리하는 동안의 전력 흔적만으로 공격이 이루어짐.
* 누출된 저해상도·저품질 신호를 ML 모델로 업스케일링·컬러 복원하여, "실제로 누출된 정보"와 "ML이 그럴듯하게 생성(hallucination)한 부분"을 구분해서 평가.
* 픽셀 치환(pixel-substitution) 방어 기법을 시험적으로 평가: 정해진 밝기 예산 내에서 각 픽셀 값을 다른 해밍 거리(Hamming weight)를 갖는 값으로 바꿔 전력 신호 패턴을 바꾸는 방식.
* 기존 동일 연구팀의 MNIST/이진 신경망(BNN) 대상 원격 전력 공격 연구를 실제 규모의 딥러닝 서비스 환경으로 확장.

**어떻게 작동하는가?**

1. 피해자(victim)는 AWS F1류의 멀티테넌트(multi-tenant) 클라우드 FPGA 인스턴스에서 CNN 기반 ML 가속기를 돌리며, 224×224 크기의 ImageNet 이미지를 입력으로 처리한다.
2. 공격자는 특별한 권한 없이 같은 물리적 FPGA 칩에 테넌트로 입주한 상태에서, 자신의 영역에 TDC 센서를 구현해 둔다. 이 센서는 전압 변화에 따른 신호 전파 지연을 디지털 값으로 측정해 전력 소비 변화를 간접적으로 감지한다.
3. 피해자의 첫 합성곱 레이어가 입력 이미지를 처리하는 동안, 공격자는 TDC 센서로 전력 흔적(trace)을 수집한다.
4. 수집된 흔적은 해상도가 낮고 잡음이 많으므로, 별도로 학습한 ML 업스케일링·컬러 복원 모델에 입력해 완전한 컬러 이미지로 복원한다.
5. 저자들은 복원된 이미지 중 실제로 신호에서 온 정보와 모델이 임의로 채워 넣은 부분을 구분해, 공격의 실제 정보 누출량을 더 정확히 평가한다.
6. 방어 실험에서는 각 픽셀 값을 정해진 밝기 범위 내에서 다른 해밍 거리 값으로 치환해 TDC 신호 패턴 자체를 바꾸는 방법을 시험한다. 그 결과 이 방어는 피해자 모델의 정확도를 공격자의 복원 성능보다 더 많이 떨어뜨리고, 공격자가 변환된 데이터로 재학습하면 방어 효과가 크게 줄어드는 것으로 나타났다.

**강점**

* 외부 계측 장비가 필요 없는 순수 온칩(on-chip) 공격이어서, 실제 클라우드 환경에서도 현실적으로 수행 가능성이 높다.
* 작은 장난감 데이터셋이 아니라 실제 서비스 규모와 유사한 ImageNet급 컬러 이미지까지 공격 범위를 넓혀 위협의 현실성을 높였다.
* 복원된 이미지에서 "진짜 누출 정보"와 "ML이 만들어낸 부분"을 구분하려 시도해, 공격 효과를 과장하지 않고 투명하게 평가하려 한 점이 신뢰성을 높인다.
* 방어 기법까지 함께 실험해, 단순한 방어로는 충분하지 않다는 점과 앞으로 무작위화·입력 의존적 방어가 필요하다는 구체적 방향을 제시한다.

**한계**

* 아직 동료 검토를 거치지 않은 프리프린트(2026년 10월 12일 공개)로, 결과가 추가 검증을 거치지 않았다.
* 복원 이미지의 상당 부분이 ML 모델의 생성(보완) 결과일 수 있어, 시각적으로 그럴듯해 보여도 실제 누출된 정보량은 논문이 주장하는 것보다 적을 수 있다.
* 평가한 방어 기법은 저자들도 "예비적(preliminary)"이라고 명시한 단순한 방식이며, 공격자가 재학습하면 쉽게 무력화된다.
* 공격이 성립하려면 공격자가 피해자와 동일한 물리적 FPGA 칩에 테넌트로 배치되어야 하는데, 클라우드 제공업체들은 이미 테넌트 배치 정책으로 이런 공존을 줄이려 하고 있어 실제 성공률은 배치 정책에 크게 좌우될 수 있다.
* 특정 FPGA·가속기 아키텍처와 CNN의 첫 레이어만을 대상으로 했기 때문에, 다른 하드웨어·모델 구조에 얼마나 일반화되는지는 추가 검증이 필요하다.

**알아둘 용어**

* 사이드채널 공격 (Side-channel attack): 암호나 연산 결과 자체가 아니라, 전력 소비·시간·전자기 방출 등 부수적인 물리적 신호를 통해 비밀 정보를 추론하는 공격 기법.
* FPGA (Field-Programmable Gate Array): 사용자가 회로 구조를 재구성할 수 있는 반도체 칩으로, 클라우드 업체들이 가속기 용도로 여러 고객에게 부분을 나누어 임대(멀티테넌트)하기도 한다.
* TDC (Time-to-Digital Converter): 신호의 전파 지연 시간을 디지털 값으로 변환하는 회로로, 전압 변화를 간접적으로 측정하는 온칩 센서로 활용될 수 있다.
* 멀티테넌트(Multi-tenant) 클라우드: 여러 고객이 같은 물리적 하드웨어 자원을 나누어 쓰는 클라우드 운영 방식.
* 해밍 거리/가중치 (Hamming weight): 이진수 표현에서 1의 개수(또는 두 값 간 차이)를 나타내는 척도로, 전력 소비 패턴과 상관관계가 있을 수 있다.
* 합성곱 신경망(CNN) / 합성곱 레이어: 이미지 처리에 널리 쓰이는 딥러닝 구조와 그 핵심 연산 단위.

**왜 주목할 만한가?**

AWS, Azure 등 주요 클라우드가 FPGA 기반 가속기 인스턴스를 멀티테넌트 방식으로 제공하는 상황에서, 이 연구는 "하드웨어를 나눠 쓰는 것 자체가 보안 위험이 될 수 있다"는 구체적이고 현실적인 증거를 제시한다. 공격에 특별한 장비가 필요 없다는 점, 그리고 복원 가능한 이미지의 품질과 규모가 실제 서비스 수준에 가까워졌다는 점에서, 클라우드 ML 서비스의 테넌트 격리 정책과 하드웨어 수준 방어 설계에 영향을 줄 수 있는 연구다.

---

## English Summary

**One-line summary**

This preprint (arXiv:2610.16164, posted October 12, 2026, not yet peer-reviewed) by Anthony Etim, Kenan Erol, and Jakub Szefer (Yale) shows that a tenant co-located with a victim on the same shared cloud FPGA can use only an on-chip sensor — no external oscilloscope — to reconstruct realistic, full-color images that the victim's ML accelerator is processing.

**Core idea**

An FPGA's power consumption correlates with the computation running on it. Prior work showed this leakage can be measured purely on-chip using a Time-to-Digital Converter (TDC) sensor instead of external probing equipment, but only recovered small, grayscale inputs like MNIST digits. This paper combines that same on-chip measurement approach with ML-based upscaling and recolorization to extend the attack to full-color, ImageNet-scale (224×224) images — much closer to what real cloud ML services actually process.

**What is new?**

* The first on-chip, TDC-based power side-channel attack that reconstructs full-color, ImageNet-scale images, with no external measurement equipment required.
* The attack works purely from power traces captured while the victim's CNN runs its first convolution layer on a 224×224 input.
* Low-fidelity, noisy leaked signals are upscaled and recolored with an ML model, and the authors try to separate genuinely leaked information from ML-"hallucinated" detail when assessing the attack's real impact.
* A preliminary pixel-substitution defense is evaluated: remapping each pixel, within a fixed intensity budget, to a value with a different Hamming weight so as to change the TDC signature.
* The work extends the same research group's earlier remote power attacks on MNIST-scale binarized neural networks to a realistic deep-learning deployment scale.

**How does it work?**

1. The victim runs a CNN-based ML accelerator on a multi-tenant cloud FPGA instance (similar to AWS F1-style offerings), processing 224×224 ImageNet images.
2. The attacker, holding no special privileges, is simply co-located as a separate tenant on the same physical FPGA chip and implements a TDC sensor in their own allotted region. The TDC indirectly senses voltage fluctuations by measuring signal propagation delay.
3. While the victim's first convolution layer processes an input image, the attacker collects power traces via the TDC.
4. Because the captured traces are low-resolution and noisy, they are fed into a separately trained ML upscaling/recoloring model to produce a full-color image reconstruction.
5. The authors try to disentangle how much of the reconstructed image reflects information truly present in the leaked signal versus content the generative model filled in on its own, to avoid overstating the attack's real leakage.
6. For defense, they test remapping each pixel's value, within a bounded intensity budget, to one with a different Hamming weight, altering the TDC signature. This costs the victim model's own accuracy more than it costs the attacker, and an attacker who retrains on the transformed data largely defeats it — suggesting robust defenses will need randomized or input-dependent transformations instead.

**Strengths**

* A purely on-chip attack with no external instrumentation makes the threat realistically deployable in actual cloud settings.
* Extends prior toy-scale (MNIST/binarized network) attacks to ImageNet-scale color images, closer to real-world ML service workloads.
* Explicitly tries to separate genuine signal leakage from ML-generated embellishment, which is a more rigorous and transparent way to report reconstruction-attack results.
* Also evaluates a candidate defense, giving concrete, actionable guidance (randomized/input-dependent countermeasures) rather than just demonstrating the attack.

**Limitations**

* This is an unreviewed preprint (posted October 12, 2026); the results have not yet gone through peer review.
* A meaningful share of the reconstructed image detail may come from the ML upscaler's own generative "filling in" rather than genuinely leaked signal, so the real information leakage could be smaller than the reconstructions visually suggest.
* The evaluated pixel-substitution defense is explicitly called "preliminary" by the authors and is largely defeated once the attacker retrains on transformed data.
* The attack requires the adversary to be physically co-located with the victim on the same FPGA chip — a precondition cloud providers already try to reduce through tenant placement policies, so real-world success depends heavily on those policies.
* Evaluation focuses on one FPGA/accelerator setup and only the first convolution layer of a CNN, so generalization to other hardware and model architectures remains to be shown.

**Terms to know**

* Side-channel attack: Inferring secret information from incidental physical signals (power, timing, electromagnetic emissions) rather than from the computation's output itself.
* FPGA (Field-Programmable Gate Array): A reconfigurable chip; cloud providers sometimes partition and rent out regions of a single FPGA to multiple customers (multi-tenancy).
* TDC (Time-to-Digital Converter): A circuit that converts signal propagation delay into a digital value, usable as an on-chip proxy sensor for voltage/power fluctuations.
* Multi-tenant cloud: A deployment model where multiple customers share the same underlying physical hardware.
* Hamming weight: The number of 1-bits in a binary representation (or a distance metric between values), which can correlate with power draw.
* CNN / convolution layer: A deep learning architecture widely used for image processing, and its core computational building block.

**Why it is worth watching**

As major cloud providers (AWS, Azure, and others) offer multi-tenant FPGA-based accelerator instances, this work provides concrete, realistic evidence that sharing hardware itself can be a security liability. Because the attack needs no special equipment and scales to image sizes resembling real production workloads, it is the kind of finding that could influence tenant-isolation policy and hardware-level defense design for cloud ML infrastructure.

---

## My take

이 논문은 멀티테넌트 FPGA 환경에서의 전력 사이드채널 공격을 실험실 수준의 작은 데이터셋에서 실제 서비스 규모로 확장했다는 점에서 의미가 있다. 다만 아직 동료 검토 전 프리프린트이고, 복원 이미지에 ML이 생성한 부분이 섞여 있을 가능성을 저자들 스스로 인정하고 있어, 실제 정보 누출량에 대한 해석은 신중할 필요가 있다. 방어 기법 평가도 예비 단계에 머물러 있어, 이 연구의 가장 큰 가치는 "공격이 완성됐다"는 것이 아니라 "클라우드 FPGA 공유 모델에 구조적 위험이 있고, 더 견고한 방어 연구가 필요하다"는 경고 신호를 명확히 제시했다는 점에 있다.

This paper is notable for scaling multi-tenant FPGA power side-channel attacks from toy datasets to realistic image sizes, but it remains an unreviewed preprint, and the authors themselves flag that reconstructed images mix genuine leakage with ML-generated detail, so claims about actual information leakage should be read cautiously. The defense evaluation is also only preliminary. The paper's main value is less "the attack is complete" and more a clear warning signal that shared-FPGA cloud deployments carry structural risk and need more robust defenses.
