---
title: "Remarks on the disproof of the unit distance conjecture"
date: 2026-05-23
topic: mathematics
tags: [mathematics, discrete-geometry, AI-for-math, OpenAI, combinatorics, algebraic-number-theory, reasoning-models]
source: https://arxiv.org/abs/2605.20695
---

# Remarks on the disproof of the unit distance conjecture

* Date: 2026-05-20
* Source: https://arxiv.org/abs/2605.20695
* Topic: mathematics
* Why it matters: An internal OpenAI reasoning model autonomously disproved the unit distance conjecture — an 80-year-old open problem in discrete geometry posed by Paul Erdős in 1946 — by discovering a surprising algebraic construction that a team of nine leading mathematicians independently verified and published in this companion paper.

## Korean Summary

**한줄 요약**

1946년 폴 에르되시(Paul Erdős)가 제기한 '단위거리 추측'이 OpenAI의 내부 추론 모델에 의해 반증되었다. 이 모델은 n개의 점 집합에서 거리가 정확히 1인 쌍의 수가 n^(1+δ) (δ > 0인 고정 지수)에 달할 수 있다는 대수적 구성을 독자적으로 발견했으며, 이는 수십 년간의 인간 연구를 뛰어넘는 결과이다. 노가 알론, 팀 가워스(Fields Medal 수상자) 등 9명의 수학자로 구성된 팀이 이 AI가 생성한 증명을 검증하고 단순화한 동반 논문을 arXiv에 공개했다.

**핵심 아이디어**

평면 위 n개의 점이 주어졌을 때, 두 점 사이의 거리가 정확히 1인 쌍(단위거리 쌍)의 수는 최대 얼마나 될 수 있는가? 에르되시는 1946년 이 질문을 제기하면서 제곱 격자(square grid) 배치가 본질적으로 최선일 것이라고 추측했다. 제곱 격자는 n^(1+c/log log n) 정도의 단위거리 쌍을 가지며, 이는 n에 비해 거의 선형적이다. OpenAI 모델은 이 추측을 반증했다: 대수적 수 이론을 활용한 새로운 점 배치를 발견함으로써, 어떤 고정된 지수 δ > 0에 대해 n^(1+δ)개의 단위거리 쌍을 만들 수 있음을 증명했다. Princeton의 Will Sawin은 이를 이어받아 δ ≥ 0.014가 명시적으로 가능함을 보였다.

**무엇이 새로운가?**

- AI가 수학의 핵심 분야에서 중요한 미해결 추측을 자율적으로 반증한 최초의 사례
- 제곱 격자 배치가 점근적으로 최적이라는 80년 된 믿음을 번복하는 구성 발견
- n^(1+c/log log n)에서 n^(1+δ) (고정 δ > 0)으로의 수열적(polynomial) 개선
- Will Sawin의 후속 작업(arXiv 2605.20579)에서 δ ≥ 0.014임을 명시적으로 확인
- 일반 목적 추론 모델이 수학 전용 시스템 없이 심층 수학적 논증을 스스로 생성할 수 있음을 시연

**어떻게 작동하는가?**

1. **문제 설정**: 평면 위 n개의 점 집합에서 단위거리 쌍의 수를 최대화하는 배치를 찾는다.
2. **AI의 탐색**: OpenAI 내부 추론 모델이 대수적 수 이론의 다양한 아이디어를 탐색하며 새로운 구성을 발견했다. 구체적으로, Golod-Shafarevich 기준(criterion)을 활용해 degree가 크고 판별식(discriminant)이 작으며 작은 노름(norm)의 소수(prime)가 많은 대수적 수체(algebraic number field)를 구성하는 방법을 발견했다.
3. **핵심 대수적 도구**: Ellenberg-Venkatesh, Golod-Shafarevich, Hajir-Maire-Ramakrishna의 아이디어를 결합하여, 특수한 대수적 구조 위에 점들을 배치함으로써 단위거리 쌍이 다항식적(polynomial)으로 많아지게 만든다.
4. **인간 검증**: 9명의 저명한 수학자(Alon, Bloom, Gowers, Litt, Sawin, Shankar, Tsimerman, Wang, Wood)가 AI가 생성한 증명을 검토하고, 더 짧고 이해하기 쉬운 버전으로 재구성하여 arXiv 2605.20695로 공개했다.
5. **명시적 하한 도출**: Will Sawin이 별도 논문(arXiv 2605.20579)에서 이 구성의 지수를 정확히 계산해 δ ≥ 0.014임을 증명했다.

**강점**

- 80년 동안 인간이 해결하지 못한 주요 미해결 문제를 AI가 독자적으로 해결
- 수학 전용 모델이 아닌 일반 목적 추론 모델이 달성한 결과로, AI 추론 능력의 범용성을 시사
- Fields Medal 수상자 팀 가워스를 포함한 최고 수학자들에 의해 독립적으로 검증됨
- AI가 기존에 알려진 패턴을 재활용한 것이 아니라, 기존 수학적 도구의 새로운 조합을 발견

**한계**

- 이 결과를 달성한 OpenAI 내부 모델은 공개되지 않아 독립적 재현이 어려움
- 단위거리 쌍의 상한(O(n^{4/3}), Szemerédi-Trotter 정리)과 새 하한(n^{1.014}) 사이의 간극은 여전히 매우 큼
- 아직 수학 저널의 정식 동료심사(peer review)를 거치지 않음
- AI가 발견한 접근법이 다른 유형의 미해결 문제에도 일반화되는지는 불명확
- AI의 '발견' 과정이 창의적 통찰인지 체계적 탐색인지 구분하기 어려움

**알아둘 용어**

- **단위거리 문제 (unit distance problem)**: n개의 점 집합에서 거리가 정확히 1인 쌍의 최대 수를 묻는 조합기하 문제
- **단위거리 추측 (unit distance conjecture)**: 최대 단위거리 쌍 수가 n^(1+o(1))이라는 믿음 (AI에 의해 반증됨)
- **Golod-Shafarevich 기준**: 무한 class field tower가 존재하기 위한 군론적·대수적 조건을 제공하는 이론
- **대수적 수체 (algebraic number field)**: 유리수 위의 유한 차수 확장체로, 정수론의 핵심 대상
- **판별식 (discriminant)**: 대수적 수체의 복잡도를 나타내는 정수 불변량; 작을수록 소수 분포가 유리
- **Class field tower**: 체를 반복적으로 확장하여 얻는 무한 탑 구조
- **Szemerédi-Trotter 정리**: n개의 점 집합에서 단위거리 쌍의 수는 O(n^{4/3})임을 보장하는 상한

**왜 주목할 만한가?**

AI가 수학을 '도구로 활용'하는 것을 넘어, 수십 년간 해결되지 못한 미해결 추측을 자율적으로 반증했다는 점에서 이 결과는 AI 과학의 새 이정표다. 특히 수학 전용 시스템이 아닌 일반 목적 추론 모델이 이를 달성했다는 점은, 현세대 AI 추론 능력이 임의적 지식 재활용을 넘어 진정한 수학적 발견에 도달했을 가능성을 시사한다. 에르되시 문제처럼 명확하게 정의되고 검증 가능한 문제에서 AI의 역량이 확인된 만큼, 앞으로 더 많은 미해결 문제에서 AI의 역할이 주목받을 전망이다.

---

## English Summary

**One-line summary**

An internal OpenAI general-purpose reasoning model autonomously disproved the Erdős unit distance conjecture — an 80-year-old open problem in discrete geometry — by discovering a novel algebraic number-theoretic construction, which nine leading mathematicians independently verified and published as a companion paper on May 20, 2026.

**Core idea**

The planar unit distance problem, posed by Paul Erdős in 1946, asks: among n points placed in the plane, what is the maximum number of pairs that lie exactly distance 1 apart? For decades, the best known constructions (such as square grids) produced only about n^(1+c/log log n) unit-distance pairs — essentially linear in n. Many believed this was essentially optimal (a belief sometimes called the "unit distance conjecture" in the lower-bound sense). An OpenAI reasoning model disproved this by discovering configurations that yield n^(1+δ) unit-distance pairs for a fixed exponent δ > 0, representing a polynomial improvement over all prior constructions. Princeton mathematician Will Sawin then made this explicit, showing δ ≥ 0.014 (i.e., at least n^1.014 pairs).

**What is new?**

- First known instance of an AI autonomously disproving a prominent open conjecture central to a field of mathematics
- Breaks the 80-year belief that square grids are essentially optimal for unit-distance constructions
- Achieves a polynomial improvement (n^(1+δ), fixed δ > 0) over all prior lower bounds
- Will Sawin's follow-up (arXiv:2605.20579) makes the exponent explicit: δ ≥ 0.014
- Demonstrates that a general-purpose reasoning model can independently discover genuinely new mathematical ideas without being specialized or scaffolded for mathematics

**How does it work?**

1. **The problem**: Find configurations of n points in the plane that maximize the count of unit-distance pairs (pairs at exactly distance 1).
2. **AI discovery**: An internal OpenAI reasoning model explored algebraic number theory and discovered a new type of point configuration. The key insight is number-theoretic: construct algebraic number fields of large degree and small discriminant, such that many small-norm primes exist, using the Golod-Shafarevich criterion.
3. **Core algebraic tools**: The construction draws on ideas from Ellenberg-Venkatesh (arithmetic geometry), Golod-Shafarevich (group theory / class field towers), and Hajir-Maire-Ramakrishna (algebraic number theory) — combining them in a new way to engineer point sets with many unit-distance pairs.
4. **Human verification**: Nine prominent mathematicians — Noga Alon, Thomas Bloom, W. T. Gowers (Fields Medalist), Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, and Melanie Matchett Wood — reviewed the AI-generated proof, produced a shorter human-readable version, and submitted it as arXiv:2605.20695.
5. **Explicit bound**: Will Sawin's separate paper (arXiv:2605.20579) worked out the exponent explicitly, establishing that configurations with at least n^1.014 unit-distance pairs exist for arbitrarily large n.

**Strengths**

- Solves a major 80-year-old problem that human mathematicians had not resolved despite sustained effort
- Achieved by a general-purpose model, not a system specifically trained for mathematics, suggesting broad transfer of reasoning
- Independently verified by multiple Fields Medalists and leading specialists in combinatorics and number theory
- The AI discovery appears to be a genuinely new combination of known mathematical ideas rather than simple pattern matching

**Limitations**

- The specific OpenAI model used is not publicly disclosed, making independent replication of the discovery process difficult
- The gap between the new lower bound (n^1.014+) and the known upper bound (O(n^{4/3}) ≈ n^{1.333}) remains very large — the true answer is still unknown
- Not yet published in a peer-reviewed mathematics journal (companion paper and Sawin's paper are arXiv preprints as of May 2026)
- It is unclear how well this approach generalizes to other types of open mathematical problems
- The degree to which the AI's process reflects "creative insight" versus broad systematic search is not yet well understood

**Terms to know**

- **Unit distance problem**: The combinatorics question of how many pairs among n plane points can be exactly distance 1 apart
- **Unit distance conjecture**: The informal belief that the maximum number of unit-distance pairs is n^(1+o(1)), disproved here
- **Golod-Shafarevich criterion**: A group-theoretic condition that guarantees the existence of infinite class field towers; a key tool in this proof
- **Algebraic number field**: A finite extension of the rationals; the construction lives in these algebraic structures
- **Discriminant**: An integer invariant of a number field measuring its "complexity"; small discriminant is favorable for this construction
- **Class field tower**: An infinite sequence of extensions of a number field, used here to build a rich structure of prime factorizations
- **Szemerédi-Trotter theorem**: The classical result giving the O(n^{4/3}) upper bound on unit-distance pairs

**Why it is worth watching**

This result is a landmark: AI has now moved from assisting mathematicians to autonomously disproving a central conjecture in discrete geometry. It is particularly significant that the model was not tuned for mathematics — it is a general-purpose reasoner that arrived at a solution experts had sought for 80 years. For the AI research community, this raises the question of how far general reasoning can go in pure science. For mathematics, the gap between n^1.014 and O(n^{4/3}) remains wide open, and the new constructions may catalyze further progress on one of Erdős's most famous unsolved problems.

**My take**

이 결과는 과장 없이 이정표적이다. AI가 특정 수학 문제에 맞춤화되지 않은 상태에서 80년 된 추측을 반증했다는 사실은 AI 추론의 실질적인 진보를 보여준다. 다만 공개되지 않은 내부 모델이 달성한 결과라는 점, 그리고 문제의 상한과 하한 사이 간극이 여전히 크다는 점은 유의해야 한다. 앞으로 이 방법이 수학의 다른 분야로 확장될 수 있는지가 핵심 질문이다.

This result is a genuine milestone without exaggeration. An unspecialized AI disproving an 80-year-old conjecture represents a real leap in machine reasoning. Two important caveats: the model remains undisclosed and unreproducible externally, and the gap between the new lower bound and the theoretical upper bound is still enormous — the true answer remains unknown. The key question going forward is whether this kind of discovery transfers to other areas of mathematics.
