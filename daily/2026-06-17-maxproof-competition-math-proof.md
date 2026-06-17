---
title: "MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling"
date: 2026-06-17
topic: AI
tags: [AI, reasoning, math, reinforcement-learning, test-time-scaling, olympiad, generative-verifier, proof-generation, LLM]
source: https://arxiv.org/abs/2606.13473
---

# MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

* Date: 2026-06-17
* Source: https://arxiv.org/abs/2606.13473
* Topic: AI / Reasoning / Mathematical Proof
* Why it matters: AI가 IMO 2025에서 35/42, USAMO 2026에서 36/42를 달성하며 두 대회 모두에서 인간 금메달 기준점을 넘어섰다. 이는 형식 증명 도구 없이, 인간이 쓰는 방식의 자연어 수학 증명으로 올림피아드 금메달 수준에 도달한 첫 사례로, AI 수리 추론의 실질적 한계가 어디인지를 다시 그리는 이정표다.

---

## Korean Summary

**한줄 요약**

MiniMax M3 모델을 증명 생성·검증·수정 세 가지 역할로 특화 훈련시키고, 테스트 시점에 후보 증명의 집단(population)을 생성·정제·순위화하여 최종 증명을 고르는 MaxProof 프레임워크를 통해 IMO 2025에서 35/42점, USAMO 2026에서 36/42점을 달성했으며, 두 대회 모두 인간 금메달 기준점을 초과한다. 원샷 대비 각각 8점, 10점 향상으로 테스트 시점 스케일링의 실질적 기여가 크다.

**핵심 아이디어**

올림피아드 수학 문제는 증명이 길고 오류 발생 지점이 다양하여, 단순 확률 샘플링(best-of-N)만으로는 품질 향상에 한계가 있다. MaxProof는 두 가지를 결합한다. 먼저 훈련 단계에서 모델이 생성·검증·수정 역할 모두를 수행할 수 있도록 강화학습 기반으로 특화 훈련하되, 오탐(false positive)을 낮게 억제하도록 설계된 방어 심층 생성적 검증기(defense-in-depth generative verifier)를 활용한다. 그런 다음 테스트 시점에서는 동일 모델을 네 가지 역할(생성기·검증기·정제기·순위 결정기)로 동시에 활용하여 후보 증명 집단에 대해 반복 탐색과 토너먼트 선발을 수행함으로써, 추론 시간 투자(compute budget)에 비례해 성능이 확장되도록 설계한다.

**무엇이 새로운가?**

- **생성적 검증기(Generative Verifier) RL 훈련**: 전통적 분류기 보상 모델 대신, 모델 자신이 자연어로 오류를 지적하고 점수를 매기는 생성적 검증기를 강화학습으로 훈련하여 낮은 오탐율을 달성
- **비평 조건부 수정(Critique-Conditioned Repair)**: 검증기가 생성한 오류 지적을 조건 입력으로 받아 증명을 부분 수정하는 정제기를 단일 모델 안에 통합
- **집단 수준 테스트 시점 스케일링(Population-Level Test-Time Scaling)**: 단순 병렬 샘플링이 아닌, 후보 증명들이 서로 토너먼트 방식으로 경쟁하고 탈락한 후보를 정제기가 수정하는 반복 진화 탐색
- **토너먼트 선발(Tournament Selection)**: 순위 결정기가 두 증명을 직접 비교하는 쌍 비교 방식으로 최종 증명을 선택하여 점수 모델의 절댓값 보정 문제를 우회
- **모델 무관 인터페이스 설계**: MaxProof 프레임워크 자체는 생성기·검증기·정제기·순위 결정기 네 인터페이스를 가정하며, M3 외 다른 모델로도 원칙적으로 적용 가능

**어떻게 작동하는가?**

1. **M3 특화 훈련:** MiniMax M3 베이스 모델에 경쟁 수학 문제-증명 데이터와 RL을 사용하여 (a) 증명 생성, (b) 생성적 증명 검증 및 오류 지적, (c) 비평 텍스트를 조건으로 한 증명 수정이라는 세 능력을 통합 훈련한다. 검증기 훈련 시 오탐을 억제하는 방어 심층 설계를 적용한다.
2. **후보 집단 초기화:** 테스트 시점에 동일 모델의 생성기 역할로 여러 후보 증명을 병렬 샘플링하여 초기 집단을 구성한다.
3. **검증 및 비평 생성:** 검증기 역할로 각 후보 증명의 타당성을 판단하고, 오류가 있다면 구체적인 오류 위치와 내용을 자연어로 생성한다.
4. **정제:** 오류 비평을 입력으로 받아 정제기 역할이 해당 후보를 수정한다. 정제된 증명이 다음 집단에 추가된다.
5. **토너먼트 선발:** 순위 결정기 역할이 후보 쌍을 직접 비교하여 더 나은 증명을 선택하는 방식으로, 집단을 점진적으로 좁혀 최종 증명 하나를 반환한다.

**강점**

- 형식 증명 도구(Lean4, Isabelle 등) 없이 인간 수학자가 쓰는 자연어 증명 형식으로 금메달 수준 달성
- 원샷 대비 IMO +8점, USAMO +10점으로 테스트 시점 스케일링의 실질적 효과를 수치로 입증
- 생성기·검증기·정제기·순위 결정기를 단일 M3 모델로 통합하여 별도 모델 서빙 오버헤드 없음
- 집단 기반 탐색으로 단순 best-of-N 대비 질적으로 다른 오류 수정이 가능
- MiniMax M3의 100만 토큰 컨텍스트 창으로 장문 증명 처리에 유리

**한계**

- IMO·USAMO 문제 채점이 완전히 자동화되어 있는지, 인간 심사가 포함되었는지 논문 공개 정보만으로 명확하지 않음
- 검증기의 오탐율이 낮다고 주장하지만 구체적 측정치와 실패 사례 분석이 공개 초록에는 없음
- 집단 탐색 시 필요한 추론 연산량(inference compute)이 원샷 대비 얼마나 증가하는지 구체적 비용이 공개되지 않음
- 형식적으로 검증된 증명이 아니기 때문에 생성된 증명에 미묘한 논리 오류가 포함될 수 있음
- 경쟁 수학 외 일반 수학 연구(새로운 정리 발견)에 직접 적용 가능한지는 추가 검증이 필요

**알아둘 용어**

- **생성적 검증기 (Generative Verifier):** 증명의 정오를 이진 레이블로 분류하는 대신, 오류 위치와 내용을 자연어로 설명하는 방식으로 동작하는 보상 모델. 오류 비평을 정제 단계에 바로 활용할 수 있는 장점이 있다.
- **방어 심층 (Defense-in-Depth):** 오탐(정답이 아닌 증명을 옳다고 판정)을 막기 위해 여러 검증 단계를 겹쳐 적용하는 설계 원칙.
- **집단 수준 테스트 시점 스케일링 (Population-Level Test-Time Scaling):** 추론 시 여러 후보를 동시에 유지하고, 이들이 서로 경쟁·정제되는 과정을 반복하여 단일 출력 품질을 높이는 방식. 단순 병렬 샘플링(best-of-N)을 넘어 후보 간 상호작용이 핵심이다.
- **토너먼트 선발 (Tournament Selection):** 두 후보를 직접 비교하는 쌍 비교 방식으로 우승자를 결정하는 선발 방법. 절댓값 점수 보정 없이 상대적 우열만 판단하면 되어 순위 결정기 훈련이 안정적이다.
- **비평 조건부 수정 (Critique-Conditioned Repair):** 검증기가 생성한 오류 비평 텍스트를 조건 입력으로 받아 기존 증명에서 오류 부분만 선택적으로 수정하는 능력.
- **IMO (International Mathematical Olympiad, 국제수학올림피아드):** 고등학생 대상의 국제 수학 경시대회. 6문제, 각 7점, 총 42점. 금메달 기준점은 매년 달라지며 통상 28~31점 수준이다.
- **MiniMax M3:** MaxProof의 기반 모델. MiniMax Sparse Attention(MSA) 아키텍처, 최대 100만 토큰 컨텍스트, 네이티브 멀티모달 지원, SWE-Bench Pro 59.0%를 기록한 오픈 웨이트 프론티어 모델로, 2026년 6월 1일 출시.

**왜 주목할 만한가?**

경쟁 수학 올림피아드는 AI가 도달하기 가장 어려운 추론 벤치마크 중 하나였다. 형식 증명 도구를 쓰지 않고 인간과 동일한 자연어 증명 형식으로 IMO·USAMO 양 대회에서 금메달 수준을 넘은 것은 처음 있는 일이다. MaxProof의 핵심 기여는 특정 모델 능력 자체보다 오히려 방법론에 있다: 생성·검증·수정·순위 결정을 단일 모델 안에 통합하고 집단 수준 탐색으로 테스트 시점 스케일링을 실현한 설계는 수학 이외의 장문 추론 태스크(코딩, 과학 논문 검토 등)에도 그대로 이전될 수 있다.

---

## English Summary

**One-line summary**

MaxProof is a population-level test-time scaling framework that, combined with the MiniMax M3 model trained for proof generation, verification, and critique-conditioned repair, achieves 35/42 on IMO 2025 and 36/42 on USAMO 2026 — exceeding the human gold-medal threshold on both competitions without using any formal proof assistants. The gains over M3's one-shot baseline are 8 and 10 points respectively, demonstrating that inference-time search over a population of candidate proofs is a powerful lever for competition-level mathematics.

**Core idea**

Olympiad problems require long, multi-step proofs where errors can occur at any step and are hard to detect without careful reading. Simple sampling strategies (best-of-N) have diminishing returns because a higher-scored candidate is not systematically better — just a different sample. MaxProof breaks the problem into two coordinated parts: during training, M3 learns to generate proofs, verify them with a generative verifier that produces natural-language critiques, and repair proofs conditioned on those critiques — all within a single model. At inference time, MaxProof runs a population-based search: it maintains a pool of candidate proofs, cycles through generate → verify/critique → refine → rank steps, and selects the winner through tournament comparison. This lets inference compute translate directly into higher proof quality.

**What is new?**

- **Generative Verifier RL training:** Instead of a binary classifier reward model, M3 is trained to produce natural-language critiques of candidate proofs, enabling direct conditioning of the repair step. A defense-in-depth design suppresses false positives (accepting wrong proofs as correct).
- **Critique-conditioned proof repair:** A refiner role takes the verifier's critique as context and selectively edits flawed sections of a candidate proof, enabling targeted correction rather than wholesale regeneration.
- **Population-level test-time scaling:** Rather than independent parallel sampling, candidates compete with each other: lower-ranked proofs are refined using critiques, and the population evolves over multiple rounds, mimicking iterative revision.
- **Tournament selection:** A ranker role compares two proofs head-to-head and picks the better one, sidestepping calibration issues with absolute score models.
- **Model-agnostic interface:** MaxProof is defined around four interfaces (generator, verifier, refiner, ranker) and is designed to work with any model that implements them, not just M3.

**How does it work?**

1. **Specialized M3 training:** Starting from the MiniMax M3 base model, RL fine-tuning teaches three capabilities: (a) proof generation for competition problems, (b) generative verification with explicit natural-language error critiques and a defense-in-depth design to minimize false positive verification, and (c) critique-conditioned proof repair that targets the specific error identified by the verifier.
2. **Initial population sampling:** At test time, the generator role produces multiple candidate proofs in parallel, forming the initial population.
3. **Verification and critique:** The verifier role assesses each candidate, assigns a quality judgment, and writes a natural-language critique of any identified errors.
4. **Refinement:** The refiner role receives a flawed candidate along with its critique and produces an improved version. This refined proof enters the next round of the population.
5. **Tournament selection:** The ranker role performs pairwise comparisons between candidates, progressively eliminating weaker proofs in a tournament bracket until a single final proof is selected and returned.

**Strengths**

- Achieves gold-medal-level scores on two major olympiad competitions (IMO and USAMO) using natural-language proofs, matching how human mathematicians write
- Large test-time scaling gain: +8 points on IMO, +10 points on USAMO versus one-shot M3 baseline
- Single model serves all four roles (generator, verifier, refiner, ranker), eliminating multi-model serving complexity
- Population-based search produces qualitatively better corrections than best-of-N sampling, since the verifier critique guides targeted repair
- Built on MiniMax M3's 1M-token context window, which supports the long reasoning chains required by olympiad problems

**Limitations**

- The public abstract does not clarify whether problem grading was fully automated or involved human judges, which affects reproducibility claims
- The false-positive rate of the defense-in-depth generative verifier is claimed to be low but no specific measurement is provided in available summaries
- The inference compute cost of population-level search versus one-shot generation is not quantified in publicly available information
- Natural-language proofs are not formally verified — subtle logical errors that slip past the generative verifier could still appear in the final output
- Applicability beyond competition math (e.g., open-ended mathematical research or theorem discovery) is not demonstrated

**Terms to know**

- **Generative Verifier:** A reward model that produces natural-language critiques of candidate outputs instead of binary labels, making its feedback directly usable for repair/refinement.
- **Defense-in-Depth Verifier Design:** Layering multiple verification sub-checks to suppress false positives — accepting an incorrect proof as valid — which would otherwise mislead the refinement and ranking steps.
- **Population-Level Test-Time Scaling:** Maintaining a set of candidate solutions at inference time and iteratively improving the set through generate-verify-refine-rank cycles, rather than returning the best single sample.
- **Tournament Selection:** A pairwise ranking procedure where a ranker model compares two candidates head-to-head and advances the winner, avoiding the need for calibrated absolute scores.
- **Critique-Conditioned Repair:** Proof editing where the refiner receives both the flawed proof and a natural-language description of the error, allowing targeted correction of specific steps.
- **IMO (International Mathematical Olympiad):** The premier international competition for high-school students, comprising 6 problems worth 7 points each (42 total). Gold-medal thresholds typically fall around 28–31 depending on the year.
- **MiniMax M3:** The base frontier model used in MaxProof. An open-weight model with MiniMax Sparse Attention (MSA) architecture, up to 1M-token context, native multimodality, and a 59.0% score on SWE-Bench Pro. Released June 1, 2026.

**Why it is worth watching**

Competition mathematics has been one of the hardest persistent challenges for AI reasoning — problems require creative multi-step insight, not just pattern matching. Reaching gold-medal level on both IMO and USAMO in natural-language proof format, without formal verification tools, is a meaningful new bar. Beyond the headline numbers, the methodological contribution is the most transferable part: combining generative verifier RL training with population-level test-time search is a general recipe that applies to any domain where (a) outputs are long and multi-step, (b) errors can be located and described, and (c) partial repair is cheaper than full regeneration. Software engineering, scientific hypothesis generation, and legal reasoning are all candidate applications.

**My take**

한국어: MaxProof의 결과가 인상적인 것은 사실이나, 가장 중요한 질문은 검증기 품질이다. 생성적 검증기가 미묘한 논리 오류를 실제로 얼마나 잘 잡아내는지에 따라 집단 탐색의 효과가 좌우되고, 이 부분의 세부 데이터가 공개되지 않은 점이 아쉽다. 그럼에도 단일 모델 안에 생성·검증·수정·순위 결정을 통합하는 프레임워크 설계는 경쟁 수학을 넘어 장문 추론 전반에 적용될 수 있는 실용적 청사진이다.

English: The results are striking, but the most important open question is verifier quality. How reliably the generative verifier catches subtle mathematical errors determines how much value population-level search actually adds — and that detail is not yet publicly quantified. Still, the architectural insight of folding generation, verification, repair, and ranking into a single model with a structured inference-time loop is a practically useful template that should generalize well beyond olympiad math to any domain where long-form outputs can be iteratively critiqued and revised.
