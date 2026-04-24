# Efficient RL Training for LLMs with Experience Replay

* Date: 2026-04-09
* Source: https://arxiv.org/abs/2604.08706
* Topic: LLM Post-Training / Reinforcement Learning Efficiency
* Why it matters: LLM reinforcement learning training is bottlenecked by expensive generation; this paper shows replay buffers cut that compute cost by up to 40% while preserving or improving accuracy — a simple, practical lever that challenges a widely-held assumption in the field.

---

## Korean Summary

**한줄 요약**

LLM 강화학습 훈련에서 "항상 새 샘플을 써야 한다"는 통념을 깨고, 경험 재사용(Experience Replay) 버퍼를 도입해 생성 연산 비용을 최대 40%까지 절감하면서 정확도를 유지하거나 오히려 개선할 수 있음을 실증적으로 보여준 연구.

게임·로보틱스 강화학습에서는 표준 기법인 경험 재사용이 LLM 사후 훈련에서는 거의 적용되지 않았다. 기존 통념은 '오래된 샘플(off-policy data)이 성능을 저하시킨다'는 것이었으나, 이 논문은 생성 비용이 높은 상황에서는 엄격한 온-폴리시 샘플링이 오히려 비효율적임을 보인다.

**핵심 아이디어**

LLM 강화학습(RLVR/GRPO 등)의 주요 병목은 매 학습 스텝마다 모델로 새 롤아웃(rollout)을 생성하는 데 드는 연산 비용이다. 본 논문은 추론 워커(inference worker)가 롤아웃을 FIFO 버퍼에 계속 쌓고, 학습자(trainer)가 버퍼에서 균일 샘플링해 재사용하는 단순한 구조를 체계적으로 분석한다. 핵심 발견은 "버퍼가 클수록 학습이 느리지만 안정적이며, 더 높은 최종 정확도에 도달할 수 있다"는 것이다.

**무엇이 새로운가?**

- LLM 사후 훈련에 Experience Replay를 체계적으로 적용한 첫 번째 포괄적 연구
- 온-폴리시 데이터가 필수라는 LLM RL 훈련의 통념에 정면으로 반박
- 리플레이 버퍼 설계를 '샘플 오래됨(staleness)에 의한 분산 vs. 샘플 다양성 vs. 생성 비용'의 최적화 문제로 형식화
- Qwen2.5-7B 모델로 MATH 벤치마크에서 동일 정확도를 최대 40% 적은 추론 연산으로 달성
- 정책 엔트로피(policy entropy)가 보존됨을 실험적으로 확인

**어떻게 작동하는가?**

1. **비동기 아키텍처**: 추론 워커는 현재 정책으로 롤아웃(문제-풀이 쌍)을 생성해 FIFO 버퍼에 추가한다.
2. **균일 샘플링**: 학습자는 버퍼에서 균일하게 샘플을 뽑아 학습한다. 항목을 꺼내도 버퍼에서 삭제하지 않는다.
3. **스탈레니스 트레이드오프**: 버퍼가 클수록 샘플이 오래되지만 다양성이 늘어난다. 학습 속도는 느려지지만 안정성이 높아진다.
4. **연산 절감**: 생성이 매우 비싸기 때문에, 기존 샘플을 재사용하는 것이 계산 단위당 효율을 높인다.
5. **평가**: MATH 수학 추론 벤치마크에서 Qwen2.5-7B 모델로 기존 온-폴리시 기법과 비교 평가.

**강점**

- 구현이 단순하다 — 기존 RL 훈련 파이프라인에 최소한의 수정으로 드롭인(drop-in) 적용 가능
- 연산 절감(~40%)이 크고 실용적이며, GPU 비용에 직접적인 영향
- GRPO 등 다양한 RLVR 알고리즘에 호환됨
- 정확도를 유지하거나 개선하면서 비용 절감을 동시에 달성
- Meta FAIR의 신뢰할 수 있는 저자진과 체계적인 실험 설계

**한계**

- 실험이 MATH 수학 벤치마크와 Qwen2.5-7B에 집중되어 있어, 다른 태스크나 모델 스케일에서의 일반화 여부는 추가 검증 필요
- 버퍼 크기, 샘플링 전략 등 하이퍼파라미터 선택이 성능에 영향을 미치며, 최적값은 태스크마다 다를 수 있음
- 오래된 샘플이 쌓이는 큰 버퍼에서 샘플 분포가 정책에서 멀어지는 문제(distribution shift)의 이론적 분석이 제한적
- 모델 훈련 전체 파이프라인(PPO, 보상 모델 갱신 등) 맥락에서의 영향은 완전히 탐구되지 않음

**알아둘 용어**

- **경험 재사용(Experience Replay)**: 이전에 수집한 상호작용 데이터를 버퍼에 저장하고 재사용하는 강화학습 기법. DQN에서 처음 대중화됨.
- **롤아웃(Rollout)**: 현재 정책으로 모델이 문제를 풀어나가는 과정에서 생성된 토큰 시퀀스(추론 궤적).
- **온-폴리시(On-policy)**: 현재 정책이 생성한 최신 데이터만 사용하는 학습 방식. 오프-폴리시(off-policy)는 이전 정책 데이터도 허용.
- **RLVR(Reinforcement Learning with Verifiable Rewards)**: 수학 문제 정답 여부처럼 검증 가능한 보상 신호를 사용하는 LLM 강화학습.
- **GRPO(Group Relative Policy Optimization)**: 여러 롤아웃을 그룹으로 비교해 보상 신호를 정규화하는 LLM RL 알고리즘. DeepSeek-R1에서 알려짐.
- **FIFO 버퍼(First-In First-Out Buffer)**: 먼저 들어온 데이터가 먼저 나가는 큐 구조의 재사용 버퍼.
- **스탈레니스(Staleness)**: 버퍼 내 샘플이 현재 정책과 얼마나 다른지를 나타내는 척도. 오래된 샘플일수록 스탈레니스가 높다.

**왜 주목할 만한가?**

LLM을 강화학습으로 훈련하는 비용(특히 생성 비용)은 매우 크다. 이 연구는 로보틱스/게임 RL에서 수십 년간 쓰인 기법을 LLM에 적용하는 것이 충분히 가능함을 증명하며, 연산 예산이 제한된 연구자와 기업 모두에게 즉시 활용 가능한 접근법을 제공한다. "온-폴리시가 필수"라는 믿음이 재고될 계기를 마련한다는 점에서 패러다임적 의의가 있다.

---

## English Summary

**One-line summary**

This Meta FAIR paper challenges the prevailing assumption that LLM reinforcement learning requires fresh on-policy data at every step, showing that a simple replay buffer can cut inference compute by up to 40% with no loss — and sometimes an improvement — in accuracy.

Experience Replay is a foundational technique in robot and game RL but has been largely ignored in LLM post-training. The authors systematically study why it was avoided, reframe the design as a formal trade-off, and demonstrate that it is both safe and beneficial when generation is the dominant compute cost.

**Core idea**

The key bottleneck in LLM RL training (e.g., GRPO, RLVR) is that generating new rollouts on every training step is expensive. This paper proposes using a FIFO replay buffer: inference workers continuously push rollouts into the buffer, and trainers sample uniformly from it — reusing past trajectories instead of always generating fresh ones. The central insight is that when generation is costly, strict on-policy sampling is computationally suboptimal even if it is statistically ideal.

**What is new?**

- First systematic study of experience replay buffers for LLM post-training at scale
- Formally frames replay buffer design as a three-way trade-off: staleness-induced variance, sample diversity, and generation compute cost
- Empirically refutes the common belief that off-policy data necessarily degrades LLM RL performance
- Demonstrates up to 40% reduction in inference compute on MATH with Qwen2.5-7B while matching or improving accuracy
- Shows that policy entropy is preserved under replay, addressing a common concern about training collapse

**How does it work?**

1. **Async architecture**: Inference workers generate rollouts (problem–solution pairs) using the current policy and push them into a shared FIFO buffer.
2. **Uniform sampling**: The trainer samples batches uniformly from the buffer for gradient updates. Sampled items are not removed, allowing reuse.
3. **Staleness trade-off**: Larger buffers introduce more stale (off-policy) samples but also more diversity and compute savings. Training slows but stabilizes.
4. **Compute savings**: Because generation is far more expensive than a gradient step, reusing existing samples significantly improves performance per unit of compute.
5. **Evaluation**: Systematic ablation over buffer sizes and sampling strategies on MATH with Qwen2.5-7B, compared against standard on-policy GRPO.

**Strengths**

- Minimal engineering lift — the buffer is a simple FIFO queue, easily plugged into existing RL pipelines
- ~40% compute reduction has direct, tangible impact on GPU costs and accessibility
- Compatible with multiple RLVR algorithms (GRPO and beyond)
- Does not hurt accuracy and sometimes improves it, especially with larger buffers
- Rigorous, systematic ablation from a credible team at Meta FAIR

**Limitations**

- Experiments focus on the MATH benchmark and Qwen2.5-7B; generalization to other tasks, domains, or larger model scales needs further study
- Optimal buffer size and sampling hyperparameters are task-dependent and may require tuning
- Theoretical guarantees on the distribution shift introduced by stale samples are limited
- The full interaction with other components (reward model updates, PPO critic, etc.) in a complete pipeline is not fully explored

**Terms to know**

- **Experience Replay**: Storing past agent interactions in a buffer and reusing them for training; a standard technique in game/robot RL first popularized by DQN.
- **Rollout**: A token sequence (reasoning trace) generated by sampling the current policy on a given problem.
- **On-policy**: Using only data generated by the current policy; contrasted with off-policy, which allows older data.
- **RLVR (Reinforcement Learning with Verifiable Rewards)**: RL fine-tuning for LLMs using rewards from verifiable signals (e.g., math answer correctness).
- **GRPO (Group Relative Policy Optimization)**: An LLM RL algorithm that normalizes rewards across a group of rollouts; used in DeepSeek-R1 training.
- **Staleness**: The degree to which a buffered sample was generated by a policy different from the current one; higher staleness means more off-policy.
- **FIFO buffer (First-In First-Out)**: A queue where the oldest entries are evicted first when capacity is reached.

**Why it is worth watching**

LLM RL training costs are growing rapidly as models and tasks scale. Any technique that reduces the most expensive part of that pipeline — generation — without sacrificing quality is immediately useful. This paper shows that experience replay, a decades-old RL tool, transfers cleanly to LLM training and questions an assumption that has held back its adoption. Labs and independent researchers operating under compute constraints can apply this finding today.

---

## My take

**한국어**: 이 연구의 핵심 기여는 기술적 복잡성이 낮으면서도 실용적 영향이 크다는 점이다. FIFO 버퍼 하나로 40% 연산 절감이 가능하다는 결과는 직관적으로 간단해 보이지만, 이를 뒷받침하는 체계적 분석과 "온-폴리시 필수"라는 통념 극복이 가치 있다. 다만 MATH 단일 벤치마크에서 7B 모델만 검증한 점은 한계이며, 다른 도메인과 더 큰 모델 스케일에서의 후속 연구가 필요하다.

**English**: The paper's strength lies in its combination of low implementation complexity and high practical impact — a FIFO buffer delivering ~40% compute savings is a compelling result. The systematic framing of the staleness trade-off elevates it beyond a simple engineering trick. The main caveat is scope: a single math benchmark and one model size are not sufficient to universally recommend this approach, and practitioners should validate on their own tasks before relying on the savings.
