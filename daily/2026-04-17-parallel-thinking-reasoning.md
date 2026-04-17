# Scaling Reasoning Tokens via RL and Parallel Thinking: Evidence From Competitive Programming

- Date: 2026-04-01
- Source: https://arxiv.org/abs/2604.01302
- Topic: LLM reasoning / inference-time scaling
- Why it matters: Single long chain-of-thought generations hit quadratic attention complexity limits; this paper introduces a parallel thinking pipeline that distributes reasoning across multiple independent threads, scaling total token budgets far beyond what single generations allow.

## Korean Summary

### 한줄 요약
대형 언어 모델(LLM)의 추론 능력을 강화하기 위해 단일 긴 사고 체인(chain-of-thought)을 계속 늘리면 attention 연산의 2차 복잡도 때문에 한계에 부딪힌다. 이 논문은 강화학습(RL) 훈련 개선과 병렬 추론(parallel thinking) 파이프라인을 결합하여 추론 토큰 예산을 여러 쓰레드와 라운드에 분산시키는 방법을 제안한다. 경쟁 프로그래밍 벤치마크에서 GPT-5-high를 능가하는 성과를 달성했다.

### 핵심 아이디어
추론 모델의 성능을 높이려면 더 많은 추론 토큰이 필요하지만, 하나의 긴 생성으로 토큰을 무한정 늘리는 것은 attention의 2차 연산 비용과 실제 학습 데이터 분포 때문에 한계가 있다. 이 연구는 훈련 단계에서 검증 RL 워밍업(verification RL warmup)과 랜덤 클리핑(randomized clipping)으로 정확도-토큰 확장 곡선을 개선하고, 테스트 시에는 여러 쓰레드가 짧은 생성을 독립적으로 수행하고 자기 검증·정제를 반복하는 병렬 파이프라인으로 총 토큰 예산을 수백만 단위로 확장한다.

### 무엇이 새로운가?
- RL 훈련 과정에서 추론 토큰 수와 정확도 사이의 로그-선형 관계를 실증적으로 확인
- 검증 RL 워밍업: 모델이 먼저 솔루션을 검증하는 법을 학습하도록 워밍업하여 훈련 시작점(기저 정확도)을 높이는 기법
- 랜덤 클리핑: RL 훈련 중 토큰 예산을 무작위로 변동시켜 정확도-토큰 확장 곡선의 기울기를 가파르게 만드는 기법
- 다중 쓰레드 생성 → 자기 검증 → 순차적 자기 정제 → 검증 기반 랭킹으로 구성된 멀티턴 병렬 추론 파이프라인
- 전체 멀티턴 파이프라인을 RL로 엔드투엔드 학습하여 훈련-테스트 구조를 일치시킴

### 어떻게 작동하는가?
1. **RL 훈련**: 기본 모델에서 시작하여 경쟁 프로그래밍 문제를 RL로 훈련한다. 검증 RL 워밍업으로 모델이 솔루션 검증 방법을 먼저 학습하고, 랜덤 클리핑으로 다양한 토큰 예산에서 훈련해 확장 효율을 높인다.
2. **병렬 추론(Parallel Thinking)**: 테스트 시 하나의 긴 생성 대신 16개의 독립적인 쓰레드가 짧은 솔루션을 각각 생성한다.
3. **자기 검증(Self-Verification)**: 각 쓰레드의 솔루션을 모델 자신이 검증한다.
4. **자기 정제(Self-Refinement)**: 검증 결과를 바탕으로 솔루션을 순차적으로 개선하며, 이 과정을 최대 16라운드까지 반복한다.
5. **최종 선택**: 검증 점수 기반으로 최종 솔루션을 선택한다.
6. **엔드투엔드 RL 학습**: 전체 멀티턴 파이프라인을 RL로 학습해 훈련과 테스트 구조를 일치시킨다.

### 강점
- 단일 긴 생성의 2차 복잡도 병목을 우회하면서 총 토큰 예산을 훨씬 더 크게 확장 가능
- Pass@1 정확도가 기저 RL 모델의 oracle pass@16과 동등하여 병렬화 효과 입증
- AetherCode의 어려운 문제 456개에서 GPT-5-high를 능가하는 강력한 실험 결과
- 훈련-테스트 구조 정렬로 파이프라인 효율 극대화
- 검증 RL 워밍업과 랜덤 클리핑은 독립적으로도 유용한 기여

### 한계
- 문제당 평균 760만 토큰이라는 높은 추론 비용: 실용적인 대규모 배포에 큰 부담
- 경쟁 프로그래밍에서 검증된 결과이며, 일반 추론이나 자연어 태스크로의 일반화는 추가 연구 필요
- 16 쓰레드 × 16 라운드의 최적 하이퍼파라미터가 다른 도메인에도 동일하게 적용될지 불확실
- 자기 검증의 정확도가 솔루션 품질에 직접 영향하므로 검증 신뢰성이 성능의 병목이 될 수 있음

### 알아둘 용어
- **Chain-of-Thought (연쇄 추론)**: 모델이 최종 답 전에 중간 추론 단계를 생성하는 기법
- **강화학습 (RL, Reinforcement Learning)**: 보상 신호로 모델 정책을 최적화하는 학습 방법
- **추론 토큰 (Reasoning Tokens)**: 최종 답변 전 모델이 생성하는 중간 사고 과정 토큰
- **병렬 추론 (Parallel Thinking)**: 하나의 긴 사고 체인 대신 여러 독립적인 짧은 생성을 병렬로 실행하는 방식
- **자기 검증 (Self-Verification)**: 모델이 자신의 출력을 스스로 검증하는 과정
- **Pass@k**: 코드 생성 태스크에서 k번의 생성 중 적어도 하나가 정답일 확률
- **테스트 시 컴퓨트 스케일링 (Test-Time Compute Scaling)**: 추론 시 더 많은 컴퓨팅을 투입해 성능을 높이는 전략

### 왜 주목할 만한가?
단일 chain-of-thought의 확장 한계를 우회하는 새로운 추론 패러다임을 제시하며, 경쟁 프로그래밍이라는 어려운 태스크에서 GPT-5-high를 능가했다는 점에서 LLM 추론의 새로운 가능성을 보여준다. 병렬 추론과 RL을 결합한 이 접근법은 코딩뿐 아니라 다양한 추론 집약적 태스크에 적용될 수 있는 범용적 원리를 담고 있다.

---

## English Summary

### One-line summary
This paper studies how to scale reasoning token budgets for LLMs through two complementary directions: RL training techniques that improve the accuracy-vs-tokens relationship, and a parallel thinking pipeline at test time that distributes the token budget across multiple independent threads to bypass the quadratic attention bottleneck of single long generations. The resulting system, built on Seed-OSS-36B, surpasses GPT-5-high on a benchmark of 456 hard competitive programming problems.

### Core idea
Long chain-of-thought reasoning scales model performance with more tokens, but a single generation faces quadratic attention costs and training-distribution mismatch when pushed to extreme lengths. The paper shows that (1) training models with verification RL warmup and randomized clipping improves how accuracy scales with token budget, and (2) at test time, a parallel thinking pipeline runs 16 independent threads of short generations, each followed by self-verification and up to 16 rounds of self-refinement, allowing the total token budget to exceed what any single generation can accommodate.

### What is new?
- Empirical demonstration of a log-linear relationship between reasoning token count and accuracy during RL training
- Verification RL warmup: pre-training the model to verify solutions before solving problems, raising the accuracy baseline
- Randomized clipping: varying the token budget during RL training to steepen the accuracy-vs-tokens scaling curve
- Multi-turn parallel thinking pipeline combining multi-thread generation, self-verification, sequential self-refinement, and verification-based ranking
- End-to-end RL training on the full multi-turn pipeline to align training objective with test-time structure

### How does it work?
1. **RL Training**: Starting from a base model, train on competitive programming problems with RL. Verification RL warmup first teaches the model to verify solutions, improving the baseline. Randomized clipping varies token budgets during training to produce steeper accuracy scaling.
2. **Parallel Thinking at Test Time**: Instead of one long generation, 16 independent threads each produce a short solution attempt in parallel.
3. **Self-Verification**: The model evaluates each thread's solution for correctness.
4. **Self-Refinement**: Based on verification feedback, each thread's solution is iteratively improved across up to 16 rounds.
5. **Verification-Based Ranking**: The final answer is selected from all candidate solutions based on verification scores.
6. **End-to-End RL on the Pipeline**: The entire multi-turn pipeline is trained end-to-end via RL, matching the training objective with the test-time structure.

### Strengths
- Bypasses the quadratic attention bottleneck of single long generations while scaling total reasoning tokens far higher
- Pass@1 accuracy matches oracle pass@16 of the base RL model — strong evidence of parallelization benefit
- Surpasses GPT-5-high on 456 hard AetherCode competitive programming problems
- Training-inference structural alignment maximizes pipeline efficiency
- Both RL improvements (verification warmup and randomized clipping) are independently useful contributions

### Limitations
- Very high inference cost: approximately 7.6 million tokens per problem on average, which is expensive for practical deployment
- Results are validated on competitive programming; generalization to broader reasoning or natural language tasks requires further work
- Optimal hyperparameters (16 threads × 16 rounds) may not transfer uniformly to other domains
- Self-verification quality is a bottleneck — if the verifier is unreliable, refinement quality degrades accordingly

### Terms to know
- **Chain-of-Thought (CoT)**: A technique where a model generates intermediate reasoning steps before producing a final answer
- **Reinforcement Learning (RL)**: Learning by optimizing a policy via reward signals
- **Reasoning tokens**: Intermediate thinking tokens generated by the model before the final answer
- **Parallel thinking**: Running multiple independent short generations simultaneously rather than one long sequential generation
- **Self-verification**: The model checking its own output for correctness
- **Pass@k**: In code generation benchmarks, the probability that at least one of k generated solutions is correct
- **Test-time compute scaling**: Improving model outputs at inference time by spending more computation, without retraining

### Why it is worth watching
Parallel thinking offers a principled way to overcome single-generation token limits by distributing reasoning across multiple shorter threads. The approach pairs naturally with RL training, scales strongly on hard problems, and outperforms proprietary frontier models on a rigorous benchmark — making it a credible template for test-time compute scaling that goes beyond simple majority voting or best-of-N sampling.

---

## My take

이 논문은 단순히 성능 수치가 좋다는 것을 넘어, 추론 모델이 어떻게 더 효율적으로 스케일되어야 하는지에 대한 구조적 해답을 제시한다. 병렬화와 자기 검증의 조합은 경쟁 프로그래밍에서 검증되었지만, 비용 문제가 해결되면 코딩 이외의 분야에서도 유망한 방향이 될 것이다.

Beyond the impressive benchmark numbers, this paper offers a structural blueprint for scaling reasoning models: train with RL to better utilize extended token budgets, then deploy with parallel threads and self-verification instead of one monolithic long generation. Both ideas are simple enough to generalize, though the per-problem token cost will need to drop significantly before this approach is practical at scale.
