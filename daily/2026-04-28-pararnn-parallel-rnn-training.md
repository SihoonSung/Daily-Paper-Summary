---
title: "ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models"
date: 2026-04-28
topic: AI
tags: [AI, RNN, LSTM, GRU, parallel-training, LLM, architecture, inference-efficiency, ICLR2026]
source: https://arxiv.org/abs/2510.21450
---

ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models

* Date: 2026-04-28
* Source: https://arxiv.org/abs/2510.21450
* Topic: AI / Sequence Modeling / Training Efficiency
* Why it matters: RNNs have been sidelined for a decade because their sequential recurrence prevents GPU parallelism; this Apple Research ICLR 2026 Oral paper eliminates that barrier using Newton's method, enabling the first 7B-parameter RNNs competitive with Transformers and Mamba2 in quality.

## Korean Summary

**한줄 요약**

Apple Research가 ICLR 2026에서 발표한 ParaRNN은 뉴턴법(Newton's method)을 이용해 RNN의 순차 재귀 계산을 연립방정식으로 재정식화하여 병렬 학습을 가능하게 하고, 기존 순차 방식 대비 최대 665배 속도 향상을 달성했다. 이 접근법으로 최초의 70억(7B) 파라미터 규모 LSTM·GRU 언어 모델을 훈련했으며, Transformer 및 Mamba2와 경쟁하는 성능을 보였다.

**핵심 아이디어**

전통적인 RNN은 현재 은닉 상태 h_t를 계산하려면 반드시 이전 상태 h_{t-1}이 필요하기 때문에 시퀀스 길이 L만큼의 순차 연산이 불가피했다. ParaRNN은 이 L번의 반복 계산을 "L개의 미지수를 갖는 비선형 연립방정식"으로 변환하고, 이를 뉴턴법으로 반복 풀어낸다. RNN의 마르코프 구조 덕분에 야코비안 행렬(Jacobian)이 블록 이중대각(block bi-diagonal) 형태를 가지므로, 병렬 리덕션 연산으로 뉴턴 반복을 매우 효율적으로 수행할 수 있다.

**무엇이 새로운가?**

- RNN 순차 재귀를 비선형 연립방정식으로 재정식화하여 뉴턴법 기반 병렬 풀이를 최초로 적용
- 야코비안의 블록 이중대각 구조를 활용한 맞춤형 고성능 병렬 리덕션 구현
- 대각 야코비안(ParaGRU)과 블록 대각 야코비안(ParaLSTM)을 갖도록 GRU·LSTM 셀을 재설계하여 뉴턴 반복의 계산 비용을 절감
- 기존 순차 방식 대비 최대 665배 훈련 속도 향상 달성
- 최초의 7B 파라미터 규모 고전 RNN 언어 모델 훈련 및 Transformer·Mamba2와의 성능 비교

**어떻게 작동하는가?**

1. **연립방정식 재정식화**: 길이 L의 시퀀스에 대한 L번의 RNN 적용을 `g(H) = 0` 형태의 비선형 연립방정식으로 변환한다. 여기서 H = [h_1, ..., h_L]이 미지수 벡터이다.
2. **뉴턴 반복**: 연립방정식을 선형화한 뒤 반복적으로 해를 업데이트한다. 수렴까지 여러 번의 반복이 필요하지만, 각 반복은 완전히 병렬로 수행된다.
3. **블록 이중대각 야코비안**: RNN의 마르코프 특성으로 인해 h_t는 오직 h_{t-1}에만 의존한다. 따라서 전체 시스템의 야코비안은 블록 이중대각 구조를 가지며, 이를 병렬 스캔(parallel scan) 알고리즘으로 효율적으로 처리할 수 있다.
4. **ParaGRU와 ParaLSTM**: 기존 GRU와 LSTM의 가중치 행렬을 대각화하여 야코비안이 각각 대각(diagonal)·블록 대각(block-diagonal) 구조를 갖도록 재설계한다. 이를 통해 수렴 속도를 높이고 계산 비용을 줄인다.
5. **GPU 최적화**: 병렬 리덕션 연산에 대한 맞춤형 고성능 CUDA 커널을 구현하여 실제 GPU 훈련 속도를 최대화한다.
6. **대규모 훈련**: 위 방법으로 400M~7B 파라미터 규모의 모델을 훈련하고 언어 모델링 성능을 평가한다.

**강점**

- 순차 재귀라는 RNN의 근본적인 병목을 해결하여 수십 년 만에 RNN의 확장성 장벽을 극복
- 7B 파라미터 RNN이 Transformer 및 Mamba2와 경쟁하는 성능 달성
- RNN은 Transformer의 KV 캐시 없이 O(1) 추론 메모리를 사용하므로, 훈련 가능성이 높아지면 배포 비용 절감 잠재력이 있음
- 오픈소스 코드베이스 공개로 재현 및 확장 가능
- SSM(State Space Model)의 선형성 제약 없이도 병렬 훈련이 가능함을 증명

**한계**

- 뉴턴법은 근사 추론이므로, 반복 횟수가 적을 경우 정확한 RNN 적용에 비해 수치 오차가 발생할 수 있음
- 병렬화를 위해 GRU·LSTM 셀 구조를 변형(대각화)해야 하므로 원래 셀과의 표현 차이가 있을 수 있음
- Mamba2에 비해 여전히 약간의 성능 격차가 있으며, 매우 긴 시퀀스에서 뉴턴 수렴 특성에 대한 추가 연구가 필요함
- 현재는 언어 모델링에 집중되어 있으며, 오디오·시계열 등 다른 모달리티에서의 검증은 아직 부족함

**알아둘 용어**

- **RNN(Recurrent Neural Network, 순환 신경망)**: 이전 단계의 은닉 상태를 다음 단계로 전달하며 시퀀스를 처리하는 신경망
- **GRU(Gated Recurrent Unit)**: 게이팅 메커니즘으로 장기 의존성을 모델링하는 RNN의 한 종류
- **LSTM(Long Short-Term Memory)**: 셀 상태와 게이트를 사용해 장단기 의존성을 처리하는 RNN의 한 종류
- **뉴턴법(Newton's Method)**: 함수의 근을 반복적 선형화(Jacobian 역행렬 적용)로 구하는 수치 최적화 기법
- **야코비안(Jacobian)**: 다변수 벡터 함수의 1차 편미분을 모아놓은 행렬; 뉴턴법의 핵심 연산에 사용됨
- **병렬 스캔(Parallel Scan)**: 이중대각 등 구조화된 행렬 시스템을 O(log L)의 병렬 단계로 푸는 알고리즘
- **SSM(State Space Model, 상태 공간 모델)**: Mamba 등 선형 재귀 구조를 사용해 병렬 훈련을 지원하는 시퀀스 모델; 선형성으로 인해 비선형 RNN보다 표현력이 제한될 수 있음

**왜 주목할 만한가?**

Transformer가 RNN을 대체한 핵심 이유 중 하나는 RNN의 순차성이 GPU 병렬 처리를 가로막아 대규모 훈련을 불가능하게 만들었기 때문이다. 그동안 SSM(Mamba 등)이 "선형 재귀"로 이 문제를 우회했지만, 비선형성을 포기해야 했다. ParaRNN은 비선형 재귀를 포기하지 않고도 병렬 훈련을 달성하며, RNN이 LLM 아키텍처의 진지한 경쟁자로 다시 부상할 수 있음을 보여준다. 추론 시 KV 캐시가 필요 없는 RNN의 메모리 효율성 장점이 이제 대규모 훈련 능력과 결합됨으로써, 향후 배포 비용에 민감한 AI 응용에서 새로운 선택지를 제공할 수 있다.

---

## English Summary

**One-line summary**

Apple Research's ParaRNN (ICLR 2026 Oral) eliminates the fundamental sequential bottleneck in RNN training by recasting the recurrence as a nonlinear system of equations solved via Newton's method, achieving a 665× training speedup and enabling the first 7B-parameter RNNs competitive with Transformers and Mamba2.

**Core idea**

Classical RNNs compute hidden states sequentially: h_t = f(h_{t-1}, x_t), meaning each step must wait for the previous one. This makes GPU parallelism along the sequence dimension impossible and has forced the field toward Transformers (fully parallel but with quadratic attention) and SSMs like Mamba (parallel but restricted to linear recurrences). ParaRNN breaks the sequential barrier by treating the entire sequence of L hidden states as a system of L nonlinear equations, then solving it iteratively using Newton's method. Because the Markovian structure of classical RNNs forces the system's Jacobian to be block bi-diagonal, each Newton iteration can be executed efficiently using parallel reduction operations, achieving asymptotically O(log L) parallel depth instead of O(L) sequential depth.

**What is new?**

- First application of Newton's method to parallelize arbitrary nonlinear RNN recurrences over the sequence dimension
- Exploits the block bi-diagonal Jacobian structure of Markovian RNNs to make Newton iterations efficient via parallel scan
- Introduces ParaGRU and ParaLSTM: redesigned GRU and LSTM cells with diagonal and block-diagonal Jacobians respectively, reducing Newton iteration cost while preserving expressive nonlinearity
- Achieves up to 665× speedup over naive sequential application of RNNs
- First demonstration of 7B-parameter classical RNNs (LSTM, GRU) with language modeling quality competitive with similarly-sized Transformers and Mamba2

**How does it work?**

1. **System reformulation**: The sequential application h_1 = f(h_0, x_1), h_2 = f(h_1, x_2), ..., h_L = f(h_{L-1}, x_L) is recast as a single system g(H) = 0 where H = [h_1, ..., h_L] is the vector of all hidden states to be solved simultaneously.
2. **Newton's iterations**: The system is linearized at the current estimate using the Jacobian, producing a linear system solved in each iteration. Convergence yields the exact (or near-exact) hidden states without requiring sequential computation.
3. **Block bi-diagonal structure**: Because each h_t depends only on h_{t-1} (Markov property), the Jacobian ∂g/∂H has a block bi-diagonal structure. This structured system can be solved in O(log L) parallel depth using a parallel scan algorithm, rather than O(L) sequential depth.
4. **ParaGRU and ParaLSTM design**: The standard GRU and LSTM cells are modified so that their inter-step weight matrices are diagonal (GRU) or block-diagonal (LSTM), ensuring the Newton step Jacobian maintains the needed structure while keeping model expressiveness.
5. **Custom GPU kernels**: High-performance CUDA implementations of the parallel reduction operations are used to convert the theoretical parallelism into practical wall-clock speedup on modern hardware.
6. **Large-scale training**: Models from 400M to 7B parameters are trained on language modeling benchmarks, with perplexity and downstream task scores compared against Transformers and Mamba2 baselines.

**Strengths**

- Solves a fundamental bottleneck that has blocked classical RNNs from scaling for over a decade, without requiring linearity like SSMs
- 7B-parameter RNNs match Transformer quality, with competitive performance against Mamba2 on language modeling and commonsense reasoning
- Deployed RNNs have O(1) inference memory per token (no KV cache), which becomes increasingly attractive as context lengths grow
- Open-source framework released, enabling the community to build on and extend the approach
- Method is architecture-agnostic: any Markovian nonlinear RNN can in principle benefit from the same parallelization framework

**Limitations**

- Newton's method is iterative and approximate; insufficient iterations may introduce numerical error relative to exact sequential application
- ParaGRU and ParaLSTM modify the original cell structure (diagonal weight matrices), which may reduce representational capacity compared to unconstrained GRU/LSTM
- Mamba2 still outperforms ParaRNN models on most benchmarks; the gap at 7B scale remains to be closed
- The method's convergence properties on very long sequences (e.g., >10K tokens) and non-language modalities (audio, time series) are not yet extensively characterized
- Requires writing custom GPU kernels to realize the theoretical speedup in practice, which increases engineering complexity

**Terms to know**

- **Recurrent Neural Network (RNN)**: A neural network that processes sequences by passing a hidden state from each step to the next; inherently sequential in the standard formulation.
- **GRU (Gated Recurrent Unit)**: An RNN variant with gating mechanisms that control information flow, reducing the vanishing-gradient problem.
- **LSTM (Long Short-Term Memory)**: An RNN variant with a separate cell state and three gates (input, forget, output) for modeling long-range dependencies.
- **Newton's method**: An iterative root-finding algorithm that linearizes a function using its Jacobian (first-derivative matrix) and updates the estimate accordingly.
- **Jacobian**: The matrix of all first-order partial derivatives of a vector-valued function; the key per-iteration computation in Newton's method.
- **Block bi-diagonal matrix**: A sparse matrix structure where nonzero blocks appear only on the main block diagonal and one adjacent block diagonal; arises naturally from Markovian dependencies.
- **Parallel scan (prefix scan)**: An algorithm that computes cumulative operations over structured matrices in O(log L) parallel steps instead of O(L) sequential steps; the core primitive enabling ParaRNN's speedup.

**Why it is worth watching**

The dominance of Transformers over RNNs in large-scale language modeling has rested partly on the parallelizability gap during training. SSMs like Mamba narrowed the gap by restricting recurrences to linear operations. ParaRNN is a more fundamental solution: it parallelizes training for general nonlinear RNNs without sacrificing expressiveness. The result is that the oldest family of sequence models — classical RNNs — is now trainable at 7B+ parameter scale. As inference costs and memory constraints become more pressing in deployment, RNNs' O(1) memory-per-step property may make them increasingly attractive alternatives to Transformers, and ParaRNN removes the last major obstacle to exploring them at competitive scale.

**My take**

이 논문의 핵심 가치는 "비선형 RNN은 병렬 훈련이 불가능하다"는 오랜 통념을 깨뜨렸다는 점이다. 수학적으로는 뉴턴법을 이용한 연립방정식 풀이라는 우아한 아이디어이며, 공학적으로는 블록 이중대각 구조를 활용한 병렬 리덕션 구현이 핵심이다. 다만 주의할 점은, 7B 규모에서 Mamba2보다 약간 낮은 성능을 보이며 야코비안 대각화로 인한 표현력 제한이 더 큰 규모에서 어떻게 작용할지 아직 불분명하다는 것이다. 그러나 RNN 기반 LLM이 Transformer 수준의 성능을 내는 최초의 사례라는 점, 그리고 추론 메모리 효율성 잠재력을 고려하면, 이 연구는 향후 시퀀스 모델 아키텍처 선택에 중요한 데이터 포인트를 제공한다.

The paper's core value is breaking the long-held assumption that nonlinear RNNs are incompatible with parallel GPU training. The mathematical insight — recasting recurrence as a Newton-solved equation system — is elegant, and the engineering contribution of exploiting block bi-diagonal structure for efficient parallel reductions is solid. The caveat is that 7B ParaRNN models still trail Mamba2 slightly, and it remains to be seen whether the Jacobian diagonalization trade-off limits scaling further. Nevertheless, as the first demonstration of classical RNNs reaching Transformer-class quality at 7B scale, combined with the O(1) inference memory advantage, this work is a meaningful data point for anyone designing next-generation sequence model architectures.
