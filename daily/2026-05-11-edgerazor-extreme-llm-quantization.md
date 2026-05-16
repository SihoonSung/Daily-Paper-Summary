---
title: "EdgeRazor: A Lightweight Framework for Large Language Models via Mixed-Precision Quantization-Aware Distillation"
date: 2026-05-11
topic: AI
tags: [AI, LLM, quantization, edge-computing, model-compression, distillation, inference-efficiency, on-device-AI]
source: https://arxiv.org/abs/2605.04062
---

EdgeRazor: A Lightweight Framework for Large Language Models via Mixed-Precision Quantization-Aware Distillation

* Date: 2026-05-11
* Source: https://arxiv.org/abs/2605.04062
* Topic: AI / LLM Compression / Edge Inference
* Why it matters: Deploying LLMs on smartphones, microcontrollers, and IoT devices requires extreme compression, but all existing 2-bit quantization methods completely destroy reasoning ability. EdgeRazor's mixed-precision quantization-aware distillation framework achieves an effective 1.88-bit model that outperforms every 3-bit baseline while preserving non-trivial math and coding performance where all 2-bit baselines score zero—and delivers a 15x decoding speedup over the full-precision model.

## Korean Summary

**한줄 요약**

기존 2비트 양자화 방법들은 LLM의 추론 능력(수학, 코딩)을 완전히 파괴하지만, EdgeRazor는 혼합 정밀도 양자화 인식 증류(MPQAD)·적응형 특징 증류(AFD)·엔트로피 인식 KL 발산(EAKLD)의 3단계 프레임워크로 1.88비트 모델을 학습시켜 모든 3비트 기준선을 뛰어넘는다. Qwen3-0.6B 기준으로 저장 용량이 1.41 GB에서 0.28 GB로 줄고 디코딩 속도는 16비트 대비 15.1배 향상되며, 6개의 2비트 기준선이 GSM8K와 HumanEval에서 모두 0점을 기록할 때 EdgeRazor는 각각 37.53%, 40.85%를 유지한다. 학습 토큰 수는 최신 양자화 인식 학습(QAT) 대비 4~10배 적게 사용해 비용 효율도 우수하다.

**핵심 아이디어**

극단적 저비트 양자화가 추론 능력을 망가뜨리는 근본 원인은 두 가지다. 첫째, 모든 레이어를 동일한 낮은 비트폭으로 균일하게 압축하면 특히 중요한 레이어에서 정보 손실이 집중된다. 둘째, 기존 증류 방법은 어려운 판단이 필요한 경우와 단순한 경우를 동일하게 취급해 추론에 핵심인 토큰 분포를 제대로 복원하지 못한다. EdgeRazor는 이 두 문제를 각각 혼합 정밀도 할당과 엔트로피 인식 증류로 해결한다. 레이어별 정밀도를 달리 부여해 임계 경로에 더 많은 비트를 배정하고, 엔트로피가 높은(결정이 어려운) 토큰에 더 강한 KL 패널티를 주어 불확실한 추론 단계를 집중적으로 복원한다.

**무엇이 새로운가?**

- **1.88비트 달성**: 기존 실용적 양자화의 하한선이던 2비트를 실질적으로 넘어선 최초의 프레임워크—이 범위에서 추론 능력을 보존한 선례 없음
- **엔트로피 인식 KL 발산(EAKLD)**: 토큰 분포의 엔트로피를 가중치로 사용해, 쉬운 토큰보다 어려운 토큰(추론 경계점)의 지식 이전을 강화
- **혼합 정밀도 양자화 인식 증류(MPQAD)**: 레이어별로 다른 비트폭을 부여하면서 16비트 교사 모델이 동시에 지식을 증류—기존 PTQ와 QAT를 단일 파이프라인으로 통합
- **적응형 특징 증류(AFD)**: 레이어 중간 표현을 맞추는 특징 수준 증류를 통해 출력 분포 외에도 내부 표현 구조를 보존
- **2비트 전체 기준선 무력화**: 동일 조건에서 평가한 6개의 2비트 방법이 추론 벤치마크에서 완전히 실패(0점)하는 동안 1.88비트 EdgeRazor는 의미 있는 성능 유지

**어떻게 작동하는가?**

1. **16비트 교사 준비**: 원본 전정밀도(fp16) 모델을 교사로 설정하고 동결; 증류 학습 전반에서 참조 표현과 출력 분포를 제공
2. **혼합 정밀도 할당(MPQAD)**: 각 트랜스포머 레이어와 구성 요소(어텐션 쿼리/키/값/출력, FFN 가중치)의 중요도를 사전 분석해 차등 비트폭 할당 계획을 생성—중요 경로는 2~3비트, 덜 중요한 경로는 1비트까지 내림
3. **적응형 특징 증류(AFD)**: 교사의 중간 레이어 활성값과 학생의 대응 표현 간 MSE 손실을 추가해, 외부 출력뿐 아니라 내부 표현 구조도 이전
4. **엔트로피 인식 KL 발산(EAKLD)**: 교사 출력 분포의 엔트로피를 계산해, 엔트로피가 높은(모델이 불확실한) 토큰 위치에 더 큰 KL 손실 가중치를 부여—추론 경계에서의 분포 재현에 집중
5. **혼합 데이터 학습**: 사람이 주석을 단 데이터셋과 교사 모델이 생성한 증류 데이터셋을 함께 사용해 과적합을 줄이고 일반화 성능을 높임
6. **배포**: 학습 완료된 1.88비트 학생 모델을 엣지 디바이스에 배포; 전용 저비트 커널이 15.1x 디코딩 가속을 제공

**강점**

- 전례 없는 1.88비트 압축에서 추론 능력 보존—기존 모든 2비트 방법이 실패하는 영역
- 모든 3비트 기준선을 뛰어넘고, 선두 2비트 PTQ 기준선 대비 14개 태스크에서 11.3포인트 우세
- 15.1배 디코딩 속도 향상으로 실시간 엣지 추론 가능
- 5배 저장 용량 감소(Qwen3-0.6B: 1.41 GB → 0.28 GB)
- 최신 QAT 대비 4~10배 적은 학습 토큰—학습 비용도 경쟁력 있음
- 기존 PTQ·QAT 파이프라인과 달리 단일 통합 프레임워크로 동시 최적화

**한계**

- 주요 실험이 소형 모델(Qwen3-0.6B)에 집중—7B, 13B+ 규모에서의 검증 부족
- 1.88비트 형식은 표준 하드웨어에서 기본 지원되지 않아 전용 커널 또는 소프트웨어 에뮬레이션이 필요
- 증류를 위한 학습 데이터셋이 필요해 완전 zero-shot 배포 불가
- 혼합 정밀도 할당 계획은 모델 아키텍처마다 재설계가 필요할 수 있음
- 전정밀도 대비 여전히 성능 갭 존재—정밀도가 극도로 중요한 응용에는 부적합
- 다양한 LLM 아키텍처(Llama, Mistral, Gemma 등)에서의 범용성 미검증

**알아둘 용어**

- **양자화 (Quantization)**: 모델 가중치나 활성값을 float16/32에서 더 낮은 비트 정수(4비트, 2비트 등)로 변환해 메모리와 계산량을 줄이는 기법
- **PTQ (Post-Training Quantization, 사후 학습 양자화)**: 이미 학습된 모델을 추가 학습 없이 변환하는 방법—빠르지만 정확도 손실이 큼
- **QAT (Quantization-Aware Training, 양자화 인식 학습)**: 학습 중 양자화 효과를 시뮬레이션해 정확도를 유지하는 방법—높은 품질이나 높은 학습 비용
- **지식 증류 (Knowledge Distillation)**: 큰 교사 모델의 출력 분포와 중간 표현을 작은 학생 모델에 전이하는 학습 방법
- **혼합 정밀도 (Mixed Precision)**: 모델의 서로 다른 레이어나 구성 요소에 다른 비트폭을 적용하는 방식—중요한 부분은 높은 정밀도 유지
- **엣지 AI (Edge AI)**: 클라우드 대신 스마트폰·마이크로컨트롤러·IoT 기기 등 자원이 제한된 기기에서 직접 AI 모델을 실행하는 패러다임
- **GSM8K**: 초등학교 수준의 수학 서술형 문제 8,500개로 구성된 추론 벤치마크—LLM의 수학적 사고력 측정에 널리 사용
- **HumanEval**: OpenAI가 공개한 코드 생성 벤치마크—164개 파이썬 함수 작성 과제로 LLM의 프로그래밍 능력을 평가

**왜 주목할 만한가?**

스마트폰부터 산업용 IoT 센서까지, 엣지 디바이스에서 LLM을 실행하려는 수요는 빠르게 증가하고 있지만 기존 2비트 방법들은 추론 능력 자체를 망가뜨리는 치명적 한계가 있었다. EdgeRazor가 1.88비트에서 추론 능력을 실질적으로 보존하면서 3비트 기준선을 넘어섰다는 결과는, 극단적 압축과 기능 보존이 동시에 가능하다는 새로운 가능성을 열어준다. 특히 6개의 경쟁 2비트 방법이 0점을 기록하는 동안 37~40%의 추론 정확도를 유지했다는 점은 단순한 점진적 개선이 아니라 질적 전환을 의미한다. 15.1배 속도 향상과 5배 용량 감소는 배터리 구동 기기에서의 실시간 LLM 서비스를 현실적으로 만들어준다.

---

## English Summary

**One-line summary**

EdgeRazor combines three novel components—Mixed-Precision Quantization-Aware Distillation (MPQAD), Adaptive Feature Distillation (AFD), and Entropy-Aware KL Divergence (EAKLD)—to compress LLMs to an effective 1.88-bit precision that surpasses all 3-bit baselines while preserving 37.53% on GSM8K and 40.85% on HumanEval at a point where every 2-bit competitor scores zero, delivers a 15.1× decoding speedup, and reduces Qwen3-0.6B storage from 1.41 GB to 0.28 GB—all using 4–10× fewer training tokens than the leading quantization-aware training approach.

**Core idea**

Extreme low-bit quantization destroys LLM reasoning because of two compounding problems. First, uniform low-bit compression across all layers concentrates information loss at the most critical layers. Second, standard distillation treats easy and hard token predictions equally, failing to faithfully recover the nuanced distributions that underpin multi-step reasoning. EdgeRazor addresses both: it assigns different bit widths to different layers and components (mixed precision), while directing distillation effort toward the uncertain, high-entropy token positions where reasoning ability is encoded. The result is a student model that operates at sub-2-bit precision yet retains the reasoning patterns that all uniform 2-bit methods erase completely.

**What is new?**

- **Sub-2-bit with preserved reasoning**: First framework to maintain non-trivial math and coding accuracy at 1.88-bit effective precision—a regime where all prior 2-bit methods return zero on standard benchmarks
- **Entropy-Aware KL Divergence (EAKLD)**: Weights the KL distillation loss by the entropy of the teacher's output distribution per token, so uncertain, decision-critical positions receive proportionally stronger learning signal
- **Mixed-Precision Quantization-Aware Distillation (MPQAD)**: Assigns different bit widths to different transformer components while simultaneously performing knowledge distillation from a 16-bit teacher, unifying PTQ and QAT into a single pipeline
- **Adaptive Feature Distillation (AFD)**: Applies intermediate-layer feature-level distillation beyond output logits, preserving internal representation geometry across bit-width transitions
- **Cross-dataset training**: Trains on both human-annotated and teacher-generated (distilled) data to reduce overfitting and improve generalization

**How does it work?**

1. **Freeze the 16-bit teacher**: The full-precision model is frozen and provides reference distributions and intermediate activations throughout training
2. **Mixed-precision assignment (MPQAD)**: Analyze each transformer layer's sensitivity to quantization; assign higher bit widths (e.g., 2-bit) to attention weights and lower widths (e.g., 1-bit) to less sensitive FFN components, targeting an overall effective 1.88-bit
3. **Adaptive feature distillation (AFD)**: For selected intermediate layers, compute MSE loss between teacher and student activations to preserve the internal representation structure, not just the final output distribution
4. **Entropy-aware KL loss (EAKLD)**: For each token position, compute the entropy of the teacher's softmax distribution; scale the KL divergence loss by this entropy so high-uncertainty positions (reasoning branch points) are weighted more heavily
5. **Joint optimization**: Minimize the combined AFD + EAKLD loss on a mixture of human-labeled data and teacher-generated synthetic sequences, using 4–10× fewer tokens than standard QAT requires
6. **Deployment**: The trained 1.88-bit student is deployed with low-bit inference kernels that deliver 15.1× decoding throughput over the 16-bit baseline on the same hardware

**Strengths**

- Achieves 1.88-bit compression—below all prior practical methods—while preserving reasoning where every 2-bit baseline completely fails
- Surpasses all 3-bit baselines and beats the leading 2-bit PTQ method by 11.3 points across 14 tasks
- 15.1× decoding speedup and 5× storage reduction (1.41 GB → 0.28 GB for Qwen3-0.6B) enable real-time edge deployment
- 4–10× more training-token efficient than state-of-the-art QAT, reducing compression cost substantially
- Unified single framework combining PTQ-style analysis with QAT-style distillation
- Entropy-weighted distillation is a principled approach that can be adapted to other compression settings

**Limitations**

- Primary experiments use Qwen3-0.6B, a small model; scaling to 7B+ models is not yet demonstrated
- The 1.88-bit format is not natively supported on standard GPUs or CPUs and requires specialized low-bit inference kernels
- Distillation requires a labeled training dataset—not fully zero-shot compression
- Mixed-precision assignment strategies may need to be re-designed per model architecture
- Meaningful performance gap versus full-precision remains; not suitable for applications demanding near-lossless accuracy
- Generalization across diverse LLM families (Llama, Mistral, Gemma, etc.) is not validated

**Terms to know**

- **Quantization**: Converting model weights or activations from full-precision floating point (fp16/fp32) to lower-bit integer formats (4-bit, 2-bit, 1-bit) to reduce memory and computation
- **PTQ (Post-Training Quantization)**: Quantizing a trained model without further training; fast and low-cost but incurs larger accuracy loss at extreme bit widths
- **QAT (Quantization-Aware Training)**: Simulating quantization during training so the model learns to tolerate low-bit precision; higher quality but requires full re-training budget
- **Knowledge Distillation**: Transferring learned behavior from a large, high-precision teacher model to a smaller or lower-precision student model through output and/or feature matching
- **Mixed Precision**: Using different bit widths for different layers or components of a model, preserving more bits where accuracy is most sensitive
- **Entropy-Aware Weighting**: Scaling a loss term by the Shannon entropy of a probability distribution—high-entropy (uncertain) positions receive more learning signal
- **Edge AI**: Running AI inference directly on resource-constrained devices (smartphones, microcontrollers, IoT sensors) rather than cloud servers
- **GSM8K / HumanEval**: Standard benchmarks for evaluating LLM reasoning ability—GSM8K tests elementary math word problems; HumanEval tests Python function generation from docstrings

**Why it is worth watching**

The demand for on-device LLMs—from always-on phone assistants to industrial edge inference—is accelerating, but the established 2-bit quantization floor has been a hard barrier: every prior method loses the reasoning capabilities that make LLMs useful. EdgeRazor's result—maintaining 37–40% accuracy on math and coding tasks at 1.88-bit while all six 2-bit competitors score zero—is not an incremental improvement but a qualitative shift. It demonstrates that the 2-bit floor was a methods limitation, not a physical one. The 15× speed gain and 5× storage reduction make battery-powered real-time LLM inference genuinely practical for the first time at this compression level. If the approach scales to larger models (the critical open question), it could substantially change the economics of edge AI deployment.

**My take**

EdgeRazor가 보여주는 결과는 단순한 점진적 개선이 아니다. 모든 2비트 방법이 추론 능력을 잃는 상황에서 1.88비트 모델이 GSM8K 37%, HumanEval 40%를 유지한다는 것은, 혼합 정밀도와 엔트로피 인식 증류의 조합이 양자화의 정보 손실 구조 자체를 다르게 접근하고 있음을 시사한다. 다만 주요 실험이 0.6B 소형 모델에 국한된 점은 중요한 유보 조건이다. 7B 이상 규모에서도 같은 패턴이 나타날지는 추가 검증이 필요하며, 전용 저비트 커널의 하드웨어 지원 확산도 실용화의 관건이다.

EdgeRazor's entropy-weighted distillation and mixed-precision assignment are principled ideas that clearly address the right failure modes of prior 2-bit methods. The numbers are striking—especially the clean zero-vs-nonzero separation between baselines and EdgeRazor on reasoning benchmarks. The main uncertainty is scale: a 0.6B model is a proof of concept, not a deployment target. If the same gains hold at 7B and beyond, and if the 1.88-bit inference kernels become more widely available, this could redefine the practical lower bound for edge LLM compression. For now it is a compelling existence proof that deserves replication on larger models.
