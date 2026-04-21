# The Curious Case of In-Training Compression of State Space Models

* Date: 2026-04-20
* Source: https://arxiv.org/abs/2510.02823
* Topic: Efficient ML / Model Compression / State Space Models
* Why it matters: State space models are fast sequence models increasingly used as Transformer alternatives, but their inference cost scales with state dimension. This paper shows how to compress that dimension *during* training using a control-theoretic technique, yielding smaller, faster models without sacrificing accuracy.

---

## Korean Summary

### 한줄 요약

훈련 중에 상태 공간 모델(SSM)의 내부 상태 차원을 점진적으로 줄여, 작게 처음부터 학습하는 것보다 더 높은 정확도와 빠른 추론 속도를 동시에 달성하는 방법을 제안한다.

상태 공간 모델은 긴 시퀀스를 처리하는 데 효율적인 구조지만, 내부 숨겨진 상태(hidden state)의 차원이 클수록 계산 비용이 늘어난다. 기존에는 큰 모델을 훈련한 후 사후 압축하거나, 처음부터 작은 모델을 훈련하는 방식을 택했다. 본 논문은 제어 이론(control theory)에서 온 균형 절단(balanced truncation) 기법을 훈련 도중 적용하여, 중요도가 낮은 상태 차원을 점차 제거하는 **CompreSSM**을 제안한다.

### 핵심 아이디어

제어 이론의 **핸켈 특이값(Hankel singular value)**은 동역학 시스템에서 각 상태가 입출력 동작에 기여하는 에너지를 측정하는 지표다. CompreSSM은 훈련 초반(전체 훈련의 약 10% 시점)부터 핸켈 특이값을 계산하여, 값이 작은—즉 기여도가 낮은—상태 차원을 점진적으로 제거한다. 큰 모델로 시작해 훈련하면서 줄여나가는 이 방식은, 처음부터 작은 모델로 훈련하는 것보다 우수한 성능을 유지한다.

### 무엇이 새로운가?

- **훈련 중 압축(in-training compression)**: 사후 가지치기(post-training pruning)가 아닌, 훈련 과정 자체에서 상태 차원을 줄인다.
- **핸켈 특이값 기반 중요도 평가**: 제어 이론의 균형 절단을 SSM 훈련에 최초로 적용한다.
- **"크게 시작, 줄이며 학습" 패러다임**: 큰 차원으로 시작해 압축해 나가는 방식이 처음부터 작은 차원으로 훈련하는 것보다 성능이 높음을 증명한다.
- **LRU 및 선택적 SSM(Mamba)으로의 확장 가능성**: 선형 시간 불변 SSM(LRU)뿐 아니라 선택적 SSM에도 적용 가능하다.
- **이론적 보장**: 균형 절단은 근사 오차에 대한 제어 이론적 품질 보장을 제공한다.

### 어떻게 작동하는가?

1. **큰 상태 차원으로 훈련 시작**: 표준 SSM보다 큰 은닉 상태로 훈련을 시작한다.
2. **핸켈 특이값 계산**: 훈련 초반(약 10% 시점)에 현재 모델의 핸켈 특이값을 산출한다. 이 값은 각 상태 차원이 시스템의 입출력에 얼마나 영향을 주는지를 나타낸다.
3. **낮은 기여 차원 제거**: 사전 설정한 상대 임계값(tolerance)보다 작은 핸켈 특이값을 가진 상태 차원을 제거한다.
4. **줄어든 모델로 훈련 계속**: 압축된 더 작은 SSM으로 훈련을 이어간다.
5. **반복 적용 가능**: 필요에 따라 훈련 중 여러 번 반복적으로 압축을 적용할 수 있다.

### 강점

- 별도의 사후 압축 단계 없이 훈련과 압축을 동시에 수행한다.
- 처음부터 작은 모델로 훈련하는 것보다 정확도가 높다.
- 제어 이론 기반의 이론적 근거가 있다.
- 여러 SSM 변형(LRU, Mamba)에 적용 가능하다.
- 추론 시 상태 차원이 줄어 메모리와 연산 비용이 감소한다.

### 한계

- 주요 실험은 LRU에 집중되어 있으며, Mamba 실험은 별도 저장소로 분리되어 있다.
- 일부 데이터셋(IMDB, AAN)에서는 기준 모델 대비 혼재된 결과를 보인다.
- 임계값(tolerance)이 하이퍼파라미터로, 데이터셋마다 조정이 필요하다.
- 비선형 또는 완전한 선택적 SSM에 대한 이론적 보장의 확장은 아직 불완전하다.

### 알아둘 용어

- **상태 공간 모델(State Space Model, SSM)**: 선형 동역학 시스템 기반의 시퀀스 모델. 병렬 훈련과 빠른 추론을 동시에 지원한다.
- **핸켈 특이값(Hankel Singular Value, HSV)**: 동역학 시스템에서 각 상태가 입력에서 출력으로 에너지를 전달하는 크기를 측정하는 값.
- **균형 절단(Balanced Truncation)**: 핸켈 특이값이 작은 상태 차원을 제거하여 시스템의 차수를 줄이는 제어 이론 기법.
- **선형 반복 단위(Linear Recurrent Unit, LRU)**: 안정적인 반복 동역학을 가진 선형 SSM의 한 종류.
- **Mamba**: 입력에 따라 상태를 선택적으로 활용하는 선택적 SSM 아키텍처.
- **모델 차수 축소(Model Order Reduction)**: 동역학 시스템의 복잡도를 줄이면서 원래 동작을 보존하는 기법.
- **훈련 중 압축(In-Training Compression)**: 훈련이 완료된 후가 아닌, 훈련 과정 도중에 모델을 압축하는 방식.

### 왜 주목할 만한가?

트랜스포머의 대안으로 주목받는 SSM(Mamba, LRU 등)은 긴 시퀀스 처리에서 효율적이지만, 상태 차원이 클수록 추론 비용이 증가한다. CompreSSM은 제어 이론의 고전 기법을 딥러닝 훈련에 접목해 이 딜레마를 해소한다. ICLR 2026에 채택된 이 연구는 MIT에서 발표되었으며, 자원 효율적인 SSM 배포에 실질적인 경로를 제시한다.

---

## English Summary

### One-line summary

CompreSSM applies balanced truncation from control theory during training to progressively remove low-importance state dimensions in state space models, achieving 2–8× state compression while matching or exceeding the accuracy of the original full-size model.

State space models (SSMs) like LRU and Mamba offer parallelizable training and fast inference, but their recurrent update cost scales directly with state dimension — creating a fundamental tension between model capacity and efficiency. Prior approaches either train small from the start (losing expressivity) or prune after training (an expensive two-step process). CompreSSM eliminates this tradeoff by compressing during training itself, guided by Hankel singular values that quantify each state dimension's contribution to system behavior.

### Core idea

Hankel singular values — a concept from linear systems theory — measure how much each state in a dynamical system contributes to input-output energy transfer. CompreSSM computes these values early in training (around 10% through) and progressively removes state dimensions whose Hankel singular values fall below a relative threshold. Starting large and shrinking preserves the high-value structure learned early, unlike training a small model from scratch which never develops that structure at all.

### What is new?

- **In-training compression**: compression happens during the training run, not as a separate post-training step.
- **Hankel singular value-based state ranking**: first application of balanced truncation from control theory to SSM training-time compression.
- **"Start large, shrink" paradigm**: empirically shows this outperforms training directly at smaller state dimension.
- **Broad SSM applicability**: method is demonstrated on Linear Recurrent Units (LRU) and is extendable to selective models such as Mamba.
- **Theoretical grounding**: balanced truncation has classical guarantees on approximation error in terms of discarded Hankel singular values.

### How does it work?

1. **Start training with a large state dimension**: begin with a full-size SSM, larger than the target final model.
2. **Compute Hankel singular values**: after roughly 10% of training, compute HSVs for the current model's recurrent kernel. Each HSV quantifies how much that state dimension contributes to the system's input-output map.
3. **Truncate low-importance states**: remove all state dimensions whose HSV falls below a preset relative threshold (tolerance parameter).
4. **Continue training with the compressed model**: resume training on the now-smaller SSM, which retains the high-value structure discovered during the initial large-model phase.
5. **Repeat if needed**: the process can be applied iteratively throughout training.

### Strengths

- No separate post-training compression step needed; compression is folded into the training run.
- Compressed models outperform models trained directly at smaller dimension — the large initial phase captures useful structure.
- Grounded in classical control theory with provable approximation guarantees.
- Applicable to multiple SSM architectures (LRU, extendable to Mamba).
- Smaller final state dimension reduces memory and compute cost at inference time.

### Limitations

- Main experiments focus on LRU; Mamba experiments are provided in a separate repository, making end-to-end reproduction less straightforward.
- Mixed results on some benchmark datasets (IMDB, AAN), where baselines remain competitive.
- The tolerance threshold is a hyperparameter requiring per-dataset tuning.
- Full theoretical guarantees for nonlinear or fully selective SSMs have not yet been established.
- Code underwent heavy refactoring for public release, with potential reproducibility rough edges.

### Terms to know

- **State Space Model (SSM)**: A sequence model based on linear dynamical systems, enabling both parallel training and fast recurrent inference. Examples include S4, LRU, and Mamba.
- **Hankel Singular Value (HSV)**: A scalar measure of how much a given state dimension contributes to energy transfer from input to output in a linear dynamical system; large HSV = important state.
- **Balanced Truncation**: A classical control theory technique for model order reduction that removes states with small Hankel singular values, with provable error bounds.
- **Linear Recurrent Unit (LRU)**: A linear SSM variant with guaranteed stable recurrent dynamics, designed for practical sequence modeling.
- **Mamba**: A selective SSM architecture that uses input-dependent state selection, making it a strong Transformer alternative for long sequences.
- **Model Order Reduction**: The field of reducing the complexity of a dynamical system while preserving its essential input-output behavior.
- **In-Training Compression**: Compressing a neural network's parameters or structure during the training process, as opposed to post-hoc pruning after training is complete.

### Why it is worth watching

SSMs are emerging as serious Transformer alternatives for long-context tasks, and their inference efficiency depends critically on state dimension. CompreSSM offers a principled, control-theory-backed method to shrink that dimension without the usual accuracy penalty of training small, and without a costly two-phase train-then-prune pipeline. Accepted at ICLR 2026 and featured in MIT News in April 2026, this work provides a practical route to deploying capable SSMs under tight resource budgets — relevant for edge inference, real-time systems, and large-scale deployment.

---

## My take

이 논문은 제어 이론의 고전 기법을 현대 딥러닝 훈련 루프에 우아하게 통합한 사례다. "크게 시작해 줄인다"는 직관은 간단하지만, 핸켈 특이값이라는 이론적 도구로 정당화된다는 점이 강점이다. 다만 혼재된 벤치마크 결과와 Mamba 실험의 분리는 아직 범용적 검증이 남아 있음을 시사한다. SSM 연구자와 효율적 추론을 고민하는 엔지니어 모두에게 읽을 가치가 있다.

This paper is a clean example of importing a classical engineering tool — balanced truncation — into a modern deep learning context. The "start big, shrink" intuition is simple, but the Hankel singular value lens gives it rigorous backing. Mixed results on some benchmarks and the separation of Mamba experiments suggest the method isn't universally dominant yet. Still, it is a worthwhile read for SSM researchers and engineers who care about inference efficiency.
