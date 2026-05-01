---
title: "Scaling Self-Play with Self-Guidance"
date: 2026-05-01
topic: AI
tags: [AI, self-play, theorem-proving, reinforcement-learning, formal-verification, reasoning, Lean4, training]
source: https://arxiv.org/abs/2604.20209
---

Scaling Self-Play with Self-Guidance

* Date: 2026-05-01
* Source: https://arxiv.org/abs/2604.20209
* Topic: AI / Training & Reasoning
* Why it matters: LLM self-play is theoretically unbounded in its learning potential—the model generates its own training problems and improves on them—but in practice it stalls because the problem generator collapses into useless outputs. This paper fixes that with a three-role framework and, as a result, enables a 7B-parameter model to outperform a 671B-parameter model at formal theorem proving.

## Korean Summary

**한줄 요약**

LLM 자기 대전(self-play) 훈련이 장기 실행 시 학습 정체에 빠지는 근본 원인을 분석하고, 모델 자신이 문제를 평가하는 "가이드(Guide)" 역할을 추가하는 Self-Guided Self-Play(SGS)를 제안한다. SGS를 적용한 7B 파라미터 모델이 200라운드의 자기 대전 후 671B 파라미터 모델보다 Lean4 정리 증명에서 더 많은 문제를 풀어냄으로써, 소규모 모델이 연산 효율적인 자기 개선으로 대형 모델을 능가할 수 있음을 실증한다.

**핵심 아이디어**

기존 LLM 자기 대전은 두 역할로 구성된다: 하위 문제를 생성하는 "추측자(Conjecturer)"와 그 문제를 풀며 학습하는 "풀이자(Solver)". 이론적으로는 상한이 없는 개선이 가능하지만, 장기 훈련에서 추측자가 보상을 해킹해 실제로는 학습에 도움이 되지 않는 인위적으로 복잡한 문제만 생성하는 붕괴(collapse) 현상이 발생한다. SGS는 세 번째 역할인 "가이드(Guide)"를 추가해 각 합성 문제가 얼마나 목표 문제와 관련 있는지, 얼마나 명확하게 서술되었는지를 LLM 자신이 채점하게 함으로써 추측자 붕괴를 원천 차단한다.

**무엇이 새로운가?**

- **3역할 자기 대전 프레임워크**: Solver·Conjecturer에 Guide를 추가해 합성 문제의 품질을 자가 평가하는 구조를 도입
- **추측자 붕괴 해결**: Guide의 점수를 학습 신호로 사용하여 추측자가 퇴화된 문제로 수렴하지 못하게 억제
- **장기 스케일링 검증**: 230 에폭, 60억 토큰 이상의 대규모 자기 대전 실험으로 스케일링 법칙 측정
- **비대칭 자기 대전의 조건 정의**: 올바른 Solver 목적함수 선택, 미해결 문제에 대한 추측자 조건부 생성, 데이터 품질 보상의 세 가지가 모두 필요함을 ablation으로 실증
- **소형 모델의 대형 모델 능가**: 7B 모델이 671B 모델의 pass@4 정확도를 초과하는 결과 달성

**어떻게 작동하는가?**

1. **대상 문제 집합 구성**: GPT 기반 필터링으로 Lean4 공식 수학 문제 약 3,000개(D_3k)를 정제해 훈련 목표로 사용
2. **Conjecturer 역할**: 현재 모델이 풀지 못하는 미해결 문제를 입력받아, 그것을 해결하기 위한 징검다리 역할을 할 하위 문제를 합성
3. **Guide 역할**: 동일한 모델이 생성된 합성 문제를 두 기준으로 채점—(1) 해당 미해결 문제와의 관련성, (2) 수학적 명확성과 자연스러움
4. **Solver 역할**: Guide 점수가 높은 합성 문제들로 강화학습을 수행해 증명 능력을 향상
5. **반복 루프**: 위 과정을 200+ 라운드 반복하며 모델이 점점 더 어려운 문제를 풀 수 있게 됨
6. **스케일링 법칙 측정**: 생성 수(generations) 대비 누적 해결률 곡선에 스케일링 법칙을 피팅하여 장기 학습 효율 평가

**강점**

- 자기 대전의 핵심 실패 원인(추측자 붕괴)을 명확하게 진단하고 해결
- 외부 교사 모델이나 추가 인간 데이터 없이 모델 자신이 문제 품질을 평가
- 강화학습 단독 기준 대비 점근 해결률 7% 향상
- 80라운드 만에 강력한 RL 베이스라인을 추월하는 빠른 초기 수렴
- 코드(GitHub)와 데이터셋(Hugging Face D_3k) 공개로 재현성 확보
- 소형 모델로 대형 모델을 능가한다는 계산 효율의 강력한 실증

**한계**

- 현재 실험은 Lean4 형식 증명 영역에만 적용됨—다른 도메인(코딩, 일반 추론 등)으로의 일반화는 미검증
- D_3k 데이터셋 구성에 GPT 시리즈 모델에 의존(외부 의존성)
- 200+ 라운드의 자기 대전 루프는 상당한 연산 비용 요구
- 공식 검증기(Lean4)가 있어야 Solver의 정답 판정이 가능한 구조—검증기 없는 개방형 도메인에는 직접 적용 어려움
- 추측자 붕괴를 막는 세 조건(Solver 목적함수, 추측자 조건부 생성, 품질 보상) 중 하나라도 빠지면 성능 하락

**알아둘 용어**

- **자기 대전 (Self-Play)**: 모델이 자신을 상대로 훈련 데이터를 생성하며 능력을 향상시키는 방법; AlphaGo에서 시작해 LLM으로 확장됨
- **추측자 붕괴 (Conjecturer Collapse)**: 자기 대전에서 문제 생성 모델이 보상 해킹을 통해 학습에 쓸모없는 과도하게 복잡한 문제만 생성하게 되는 퇴화 현상
- **형식 정리 증명 (Formal Theorem Proving)**: Lean4 같은 증명 보조기(proof assistant)에서 수학적 명제를 기계가 검증 가능한 형식으로 증명하는 작업
- **Lean4**: 수학적 증명을 형식화하고 컴퓨터로 검증하는 프로그래밍 언어 겸 증명 보조기
- **비대칭 자기 대전 (Asymmetric Self-Play)**: Conjecturer(문제 생성)와 Solver(문제 풀기)가 서로 다른 역할을 맡아 상호 개선하는 자기 대전 방식
- **pass@k**: 모델이 k번의 시도 중 적어도 한 번 정답을 내는 확률로 측정하는 코드·증명 생성 성능 지표
- **스케일링 법칙 (Scaling Laws)**: 모델 크기, 데이터, 연산량과 성능 사이의 멱함수적 관계를 나타내는 경험적 법칙

**왜 주목할 만한가?**

형식 증명은 AI가 수학적으로 엄밀하게 추론할 수 있는지를 검증하는 핵심 시험대다. SGS가 7B 모델로 671B 모델의 성능을 추월한 결과는 모델 규모보다 훈련 알고리즘의 질이 더 중요할 수 있음을 시사한다. 자기 대전이 스케일링의 병목을 돌파할 수 있다면, 수학·코드·과학적 추론 등 검증기가 존재하는 다양한 영역에서 외부 데이터 없이도 모델이 자율적으로 한계를 확장하는 시대를 열 수 있다.

---

## English Summary

**One-line summary**

Self-play training for LLMs is theoretically unbounded but practically stalls: the problem-generating model collapses into useless outputs that stop the solver from improving. Self-Guided Self-Play (SGS) adds a third "Guide" role—where the LLM itself scores the quality of generated problems—breaking this collapse and allowing a 7B-parameter model to outperform a 671B-parameter model at formal theorem proving after 200 rounds of self-play.

**Core idea**

In asymmetric LLM self-play, a Conjecturer generates synthetic subproblems for a Solver to train on, and both improve iteratively. The problem is that over long runs, the Conjecturer learns to hack its reward by generating artificially hard or incoherent problems that fail to help the Solver—a collapse analogous to an exam writer setting impossible questions that teach nothing. SGS introduces a Guide, a third role where the same LLM rates each synthetic problem on two axes: (1) how relevant it is to the actual unsolved target problems, and (2) how clearly and naturally it is formulated. High-scoring problems become training signal; low-scoring (degenerate) ones are filtered out, keeping the Conjecturer honest.

**What is new?**

- **Three-role self-play**: Adds a Guide on top of the Solver + Conjecturer pair to score and filter synthetic problems, preventing collapse without any external teacher
- **Mechanistic diagnosis of self-play failure**: Identifies Conjecturer reward hacking as the root cause of stagnation and designs the Guide as a direct countermeasure
- **Long-horizon scaling experiments**: Runs over 6.3 billion training tokens (~230 epochs of the target dataset), far beyond prior self-play work, and fits scaling laws to cumulative solve-rate curves
- **Three necessary conditions established**: Ablations show that correct Solver objective, Conjecturer conditioning on unsolved problems, and data-quality reward are all individually necessary for SGS to avoid collapse
- **7B surpasses 671B**: DeepSeek-Prover-V2-7B trained with SGS exceeds the pass@4 accuracy of DeepSeek-Prover-V2-671B on Lean4 formal theorem proving

**How does it work?**

1. **Dataset construction**: ~3,000 Lean4 formal math problems (D_3k) are curated and difficulty-categorized using GPT-based filters, removing unsolvable problems to create a clean training target.
2. **Conjecturer step**: Given an unsolved target problem, the current model generates a synthetic subproblem intended to serve as a stepping stone toward solving the original.
3. **Guide step**: The same model evaluates each synthetic subproblem on (a) relevance to its corresponding unsolved problem and (b) mathematical clarity and naturalness, producing a scalar quality score.
4. **Solver step**: High-quality synthetic problems are used as reinforcement learning training signal; the Solver receives reward when it proves them in Lean4.
5. **Iterative rounds**: Steps 2–4 repeat for 200+ rounds, with the model improving its conjecture and proof abilities simultaneously each round.
6. **Scaling law measurement**: Cumulative solve rate is tracked against total number of generations, and power-law fits quantify the scaling efficiency of SGS vs. baselines.

**Strengths**

- Cleanly addresses the root cause of self-play stagnation rather than patching symptoms
- No external teacher model required during training—the model self-evaluates problem quality
- 7% higher asymptotic solve rate than reinforcement learning alone
- Surpasses the strongest RL baseline in under 80 rounds, suggesting fast early convergence
- Code and the D_3k dataset are publicly released, supporting reproducibility
- Strong compute-efficiency argument: dramatically outperforms a model ~96× its size

**Limitations**

- Evaluated only on Lean4 formal theorem proving; generalization to other domains (code, open-ended reasoning) is not yet demonstrated
- Dataset curation relies on GPT-series models, introducing an external dependency
- 200+ rounds of iterative self-play require significant compute investment
- Requires a formal verifier (Lean4) to provide unambiguous training reward; domains without automated verification cannot directly use this approach
- All three conditions (correct Solver objective, unsolved-problem conditioning, quality reward) are necessary—removing any one causes collapse, as shown by ablations

**Terms to know**

- **Self-play**: A training paradigm in which a model generates its own training problems and improves through iterating on them, analogous to AlphaGo playing against itself
- **Conjecturer collapse**: The failure mode where the problem-generating model in self-play drifts toward artificially complex or incoherent outputs that maximize Solver failure without providing useful training signal
- **Formal theorem proving**: Constructing machine-checkable proofs of mathematical statements in a proof assistant like Lean4; a Lean4 verifier provides binary, noise-free feedback on whether a proof is valid
- **Lean4**: A functional programming language and interactive proof assistant used to formalize and machine-verify mathematical arguments
- **Asymmetric self-play**: A self-play variant where a Conjecturer (problem setter) and Solver (problem solver) play distinct, complementary roles rather than the same role
- **pass@k**: The probability that at least one of k independent model attempts produces a correct solution; a standard metric for code and proof generation tasks
- **Scaling laws**: Empirical power-law relationships between compute/data/model size and performance; used here to compare how well different algorithms improve with more training

**Why it is worth watching**

Formal theorem proving is one of the most rigorous tests of AI reasoning—every proof is either valid or not, providing unambiguous feedback. The result that a 7B model can exceed a 671B model through better training rather than more parameters challenges the prevailing assumption that scale is the primary lever for reasoning improvement. If SGS generalizes beyond Lean4 to other verifiable domains—coding, symbolic math, scientific reasoning—it points toward a regime where models autonomously push their own capabilities without new human-labeled data, simply by generating and learning from well-guided synthetic problems.

**My take**

SGS는 "더 큰 모델이 항상 이긴다"는 통념에 균열을 낸다. 7B가 671B를 이기는 결과는 인상적이지만, 형식 증명이라는 좁은 도메인—자동 검증이 가능하고 피드백이 이진(binary)인 환경—에서 얻은 결과임을 기억해야 한다. 코딩·일반 추론·과학적 발견처럼 검증이 복잡한 영역에서도 같은 원리가 작동하는지가 이 연구의 진정한 시험대다.

SGS chips away at the "bigger model always wins" assumption, but the 7B-beats-671B result lives in a narrow, well-defined domain where a formal verifier gives clean binary feedback. The real test will be whether the same principle—self-guided quality filtering of synthetic subproblems—holds up in messier domains like open-ended coding, scientific reasoning, or multi-step planning where automated verification is harder. If it does, self-play could become a dominant paradigm for post-training capability amplification.
