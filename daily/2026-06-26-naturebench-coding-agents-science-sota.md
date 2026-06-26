---
title: "NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?"
date: 2026-06-26
topic: AI
tags: [AI, benchmark, coding-agents, AI-for-science, evaluation, scientific-discovery]
source: https://arxiv.org/abs/2606.24530
---

# NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?

* Date: 2026-06-24
* Source: https://arxiv.org/abs/2606.24530
* Topic: AI / AI-for-Science Benchmarking
* Why it matters: As AI coding agents are increasingly applied to scientific research, this paper provides the first rigorous, containerized benchmark measuring whether they can actually surpass published state-of-the-art results from Nature-family journals — and finds that even the strongest models do so less than 18% of the time.

## Korean Summary

**한줄 요약**

NatureBench는 Nature 계열 저널에 게재된 논문 90개를 기반으로, AI 코딩 에이전트가 실제 과학 연구에서 발표된 최신 성과(SOTA)를 능가할 수 있는지 측정하는 최초의 엄밀한 크로스-도메인 벤치마크다. 최고 성능 모델조차 18%가 채 안 되는 비율로만 SOTA를 초과했으며, 성공 사례 대부분은 진정한 과학적 발명이 아닌 방법론적 번역에 의존했다.

**핵심 아이디어**

AI 코딩 에이전트가 "과학의 최전선을 밀어낼 수 있는가"라는 질문에 체계적으로 답하기 위해, 저자들은 NatureGym이라는 자동화 파이프라인을 구축했다. 이 시스템은 실제 게재된 논문에서 표준화된 컨테이너 환경으로 구성된 작업 패키지를 생성하고, 에이전트가 원 논문의 방법론을 단순히 재현하지 못하도록 '정보 방화벽'을 적용한다. 에이전트는 논문의 SOTA 결과를 초과해야 과제를 성공으로 평가받는다.

**무엇이 새로운가?**

- **NatureGym 파이프라인**: 논문을 표준화된 컨테이너 환경 과제로 자동 변환하는 최초의 자동화 파이프라인. 데이터 획득, 검증, 정보 방화벽까지 포함.
- **엄밀한 SOTA 기준**: 단순 재현이 아닌 발표된 최고 성과를 능가해야 한다는 새로운 평가 기준 도입.
- **크로스-도메인 구성**: 세포 오믹스, 단백질 생물학, 의생명 모델링, 물리 모델링, 분자 설계, 관계 추론 등 6개 도메인 × 90개 과제.
- **프런티어 모델 대규모 평가**: Claude Code, Codex CLI, Gemini CLI 등 10개 프런티어 에이전트 구성을 엄격한 웹 검색 금지 프로토콜 하에 평가.
- **공개 리더보드**: 논문, NatureGym, 공개 리더보드 및 재현 가능한 평가 환경을 함께 배포.

**어떻게 작동하는가?**

1. **논문 수집**: Nature Machine Intelligence, Nature Methods, Nature Computational Science 등 Nature 계열 저널에서 머신러닝 접근이 가능한 논문을 선별. 2022~2025년 사이 발행된 논문 중심.
2. **NatureGym 처리**: 각 논문에서 데이터셋을 획득·검증하고, 숨겨진 테스트셋과 자동 평가기를 포함한 컨테이너 환경(과제 패키지)을 구성. 에이전트가 원 방법론을 그대로 따라하지 못하도록 정보 방화벽 적용.
3. **에이전트 실행**: 각 에이전트는 과제 설명과 훈련 데이터를 받아 독립적으로 솔루션을 개발. 웹 검색 불가 프로토콜 하에 진행.
4. **SOTA 비교 평가**: 에이전트의 결과를 원 논문에 보고된 SOTA와 비교. g>0.1 기준(SOTA 대비 10%p 이상 초과)으로 성공 판정.
5. **실패 분석**: 실패 원인이 과제 이해 부족이 아닌 잘못된 방법 선택과 불충분한 연산 예산임을 확인.

**강점**

- 실제 게재 논문 기반의 높은 현실성 — 합성 문제가 아닌 진짜 과학적 과제
- 환경 표준화로 평가 신뢰성 향상 — 기존 벤치마크의 환경 파편화 문제 해결
- 도메인 편향 없는 크로스-도메인 구성
- 정보 방화벽으로 단순 재현을 방지해 진정한 문제 해결 능력 측정
- 오픈소스 공개 및 공개 리더보드 제공

**한계**

- 6개 도메인 모두 머신러닝 기법이 적용 가능한 과제에 편향 — 실험·관측 중심 과학은 포함되지 않음
- 90개 과제는 대규모 통계 분석에는 상대적으로 적은 수
- 컨테이너 환경이 실제 연구 환경을 완전히 재현하지는 못할 수 있음
- g>0.1 기준의 임의성 — 기준치 선택이 결과 해석에 영향
- 에이전트가 컴퓨팅 예산 부족으로 실패하는 경우, 더 많은 자원을 주면 결과가 달라질 수 있음

**알아둘 용어**

- **NatureGym**: 출판된 논문을 컨테이너 기반 AI 과제 환경으로 자동 변환하는 파이프라인
- **SOTA (State-of-the-Art)**: 특정 과제에서 현재 알려진 최고 성능 결과
- **방법론적 번역 (Methodological Translation)**: 과학적 과제를 에이전트가 익숙한 지도학습 예측 문제로 변환하여 해결하는 방식
- **정보 방화벽 (Information Firewall)**: 에이전트가 원 논문의 방법론을 직접 확인하거나 재현하지 못하도록 차단하는 장치
- **컨테이너 환경 (Containerized Environment)**: Docker 등의 기술로 격리된 소프트웨어 실행 환경
- **g>0.1 기준**: SOTA 점수 대비 0.1(10%p) 이상의 개선을 달성할 때 성공으로 간주하는 평가 기준
- **세포 오믹스 (Cellular Omics)**: 유전체, 전사체, 단백질체 등 세포 수준의 대규모 분자 데이터를 다루는 연구 분야

**왜 주목할 만한가?**

AI 에이전트가 과학 연구를 자동화할 것이라는 기대가 급증하는 상황에서, NatureBench는 현실을 냉정하게 측정한다. 최고 모델조차 17.8%에 그친 SOTA 초과율은 현재 에이전트가 '발견'보다는 '번역'에 가깝다는 것을 보여준다. 동시에 NatureGym이라는 자동화 파이프라인은 향후 AI-for-Science 에이전트 개발을 위한 재현 가능하고 신뢰할 수 있는 평가 인프라를 제공한다.

---

## English Summary

**One-line summary**

NatureBench is a cross-discipline benchmark of 90 tasks drawn from peer-reviewed Nature-family journals, revealing that even the strongest AI coding agents surpass published state-of-the-art results less than 18% of the time — and succeed mostly by translating tasks into familiar supervised learning problems rather than genuine scientific invention.

**Core idea**

The paper asks a deceptively simple question: can AI coding agents actually advance the scientific frontier, not just reproduce it? To answer this rigorously, the authors built NatureGym, an automated pipeline that converts published scientific papers into standardized containerized task environments. Each task package includes the paper's dataset, a held-out test set with hidden ground truth, an automated evaluator, and an information firewall that prevents agents from simply reusing the source paper's methods. Agents must independently develop a solution and beat the paper's reported SOTA to be counted as successful.

**What is new?**

- **NatureGym pipeline**: First automated system to convert published papers into standardized, containerized benchmark tasks — handling data acquisition, verification, test-set construction, and information firewalling.
- **Strict SOTA-surpassing criterion**: Unlike prior benchmarks that measure reproduction, NatureBench requires agents to genuinely exceed published results (g>0.1 threshold).
- **Cross-discipline breadth**: 90 tasks across six scientific domains — cellular omics, protein biology, biomedical modeling, physical modeling, molecular design, and relational reasoning.
- **Frontier-model evaluation**: Ten frontier agent configurations (including Claude Code, Codex CLI, Gemini CLI) evaluated under a strict web-search-disabled protocol.
- **Open infrastructure**: Benchmark, pipeline, public leaderboard, and maintainer-side reproduction released together.

**How does it work?**

1. **Paper selection**: Nature-family journals (Nature Machine Intelligence, Nature Methods, Nature Computational Science, etc.) are filtered for papers with machine-learning-tractable tasks. Corpus skews 2022–2025.
2. **NatureGym processing**: For each paper, data is acquired and verified; a containerized task package is assembled with a task brief, training data, a hidden test set, and an automated evaluator. An information firewall prevents agents from copying source methods.
3. **Agent execution**: Each agent receives only the task brief and training data, then independently develops a solution under a no-web-search constraint.
4. **SOTA comparison**: Agent results are compared to the source paper's reported state of the art. Success is defined as surpassing SOTA by more than g>0.1 (a 10-percentage-point improvement margin).
5. **Failure analysis**: Post-hoc analysis identifies that failures are driven primarily by wrong method choice and insufficient compute budget — not by failing to understand the task.

**Strengths**

- Grounded in real published science, not synthetic or toy problems
- Containerized environments eliminate the environment-fragmentation problem that has plagued prior benchmarks
- Information firewall ensures genuine problem-solving, not retrieval or reproduction
- Cross-domain coverage reveals variation in agent performance across scientific disciplines
- Fully open-sourced with a live leaderboard enabling longitudinal tracking

**Limitations**

- All 90 tasks are ML-tractable — purely experimental or observational science is excluded by design
- Ninety tasks is a moderate corpus; domain-level statistics may be noisy
- Containerized environments may not capture the full complexity of real research workflows
- The g>0.1 success threshold is somewhat arbitrary; results shift with different margins
- Compute budget constraints may unfairly penalize agents; more resources might change outcomes

**Terms to know**

- **NatureGym**: The automated pipeline that converts published papers into containerized AI benchmark tasks
- **SOTA (State-of-the-Art)**: The best-known result on a given task as reported in a peer-reviewed paper
- **Methodological translation**: The pattern by which agents succeed — converting a novel scientific task into a standard supervised learning problem they already know how to solve
- **Information firewall**: A barrier preventing agents from accessing source paper methods, forcing independent problem solving
- **g>0.1 criterion**: The success threshold requiring an agent to exceed published SOTA by more than 0.1 on the task's primary metric
- **Cellular omics**: High-dimensional molecular biology data (genomics, transcriptomics, proteomics) analyzed at the cellular level
- **Containerized environment**: An isolated, reproducible software execution environment (e.g., Docker) used to standardize task setup

**Why it is worth watching**

The promise of AI agents autonomously accelerating science is one of the most discussed claims in AI right now. NatureBench provides a rigorous reality check: on tasks drawn from elite journals, the best available agents succeed barely one in six times, and when they do succeed, it is mostly by applying familiar ML templates rather than inventing new methods. The NatureGym pipeline simultaneously lowers the cost of creating new science benchmarks, making it possible to track progress as models improve.

**My take**

(Korean) 현재 AI 코딩 에이전트의 과학적 능력은 과대평가되어 있다. 17.8%의 SOTA 초과율은 인상적으로 보일 수 있지만, 이는 과제가 이미 표준 머신러닝 형태로 구성되어 있음에도 불구한 수치다. 방법론적 번역이 주된 성공 경로라는 발견은, 에이전트가 아직 진정한 과학적 추론보다는 패턴 매핑에 의존하고 있음을 시사한다. NatureGym 파이프라인은 향후 진보를 추적하는 데 귀중한 인프라가 될 것이다.

(English) Current AI coding agents are often overhyped for scientific research. A 17.8% SOTA surpass rate sounds modest but is arguably impressive given the task difficulty — yet the finding that success relies on methodological translation rather than invention suggests agents are doing sophisticated pattern matching, not reasoning from scientific first principles. The NatureGym infrastructure is arguably the paper's most durable contribution: it makes it cheap to extend this benchmark and track progress as models improve.
