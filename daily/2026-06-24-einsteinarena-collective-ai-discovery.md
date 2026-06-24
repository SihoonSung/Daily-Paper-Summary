---
title: "Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries"
date: 2026-06-24
topic: AI
tags: [AI, scientific-discovery, multi-agent, collective-intelligence, mathematics, optimization, open-science, Together-AI, Stanford]
source: https://arxiv.org/abs/2606.10402
---

# Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries

* Date: 2026-06-24
* Source: https://arxiv.org/abs/2606.10402
* Topic: AI / Scientific Discovery / Multi-Agent Systems
* Why it matters: 대부분의 AI 연구 플랫폼은 에이전트가 고립된 세션 안에서 혼자 작동한다. EinsteinArena는 서로 다른 에이전트들이 동일한 공개 문제에 솔루션을 제출하고 토론하며 이전 결과 위에 쌓아 올리는 오픈 분산 플랫폼을 구축해, 2026년 3월 출범 이후 약 두 달 만에 인간과 AI를 통틀어 기존 최고 기록을 넘는 결과를 수학 최적화 문제 12개에서 달성했다.

---

## Korean Summary

**한줄 요약**

Together AI와 스탠퍼드 대학 연구팀이 EinsteinArena를 발표했다. 이는 자율 AI 에이전트들이 개방형 수학 문제에 솔루션을 제출하고, 서로의 발견 위에 점진적으로 구축하며, 공개 토론장에서 아이디어를 교환하는 오픈 소스 분산 연구 플랫폼이다. 출범 두 달 만에 인간 및 AI 최고 기록을 넘는 12개의 새로운 최고 기록을 달성했으며, 가장 주목할 만한 성과는 1980년 이후 최대 폭으로 11차원 키싱 넘버 하한을 593에서 604로 끌어올린 것이다.

**핵심 아이디어**

기존 AI 과학 연구 시스템은 대부분 하나의 에이전트가 단일 세션 안에서 문제를 풀고 결과는 그 세션이 끝나면 사라진다. EinsteinArena는 이 구조를 근본적으로 바꾼다. 플랫폼은 모든 제출 솔루션, 실패한 시도, 부분적 통찰을 영구적인 공유 메모리로 축적하며, 서로 다른 조직의 에이전트들이 이 기반 위에서 경쟁하면서도 협력하도록 설계되었다. 각 에이전트는 이전 에이전트가 발견한 구성을 읽고 개선해 다시 제출할 수 있으며, 그 결과 집단 지성이 개별 에이전트의 능력을 초과하는 발견으로 이어진다.

**무엇이 새로운가?**

- **분산 오픈 연구 플랫폼**: 단일 에이전트·단일 세션이 아닌, 여러 조직의 에이전트들이 지속적으로 참여하는 공개 공유 연구 환경
- **영구 공유 메모리**: 제출 솔루션, 실패 시도, 토론 내용이 모두 공개되어 모든 에이전트가 기존 최고 성과를 기반으로 개선 가능
- **엄밀한 검증 체계**: 각 문제는 결정론적인 Python 검증기(verifier)와 격리된 샌드박스에서 실행되어 모호성 없는 채점이 가능
- **12개의 실제 신기록 달성**: 시뮬레이션 벤치마크가 아닌, 수십 년간 미해결 상태였던 실제 수학 문제에서 인간·AI 통합 최고 기록 경신
- **창발적 협력 메커니즘 관찰**: 키싱 넘버 문제에서, 경쟁하는 에이전트들이 자발적으로 정보를 공유하여 상호 이익이 되는 결과를 도출한 사례 기록

**어떻게 작동하는가?**

1. **문제 사양**: 각 문제는 자연어 설명, JSON solutionSchema(유효한 제출물의 구조 정의), 최적화 방향(높을수록/낮을수록 좋음), 그리고 제출물을 스칼라 점수로 변환하는 Python 검증기로 구성된다.
2. **에이전트 참여**: 에이전트는 REST API를 통해 구조화된 솔루션을 제출한다. 제출 즉시 샌드박스에서 검증기가 실행되어 점수가 기록된다.
3. **공개 리더보드**: 모든 제출 솔루션과 점수가 공개된다. 에이전트는 현재 최고 솔루션을 읽어 자신의 탐색 전략에 반영할 수 있다.
4. **토론 포럼**: 각 문제마다 토론장이 있어 에이전트(또는 인간)가 부분 결과, 실패 원인, 유망한 방향을 게시할 수 있다.
5. **누적 개선**: 새 에이전트는 이전 에이전트의 최고 구성을 출발점으로 삼아 점진적으로 개선해 나간다. 키싱 넘버 사례에서는 한 에이전트가 미완성이지만 유망한 구성을 제출한 후, 48시간에 걸쳐 여러 에이전트가 이를 정제하며 최종 기록을 달성했다.

**강점**

- 개별 에이전트의 한계를 초과하는 집단적 발견이 가능함을 실증
- 완전 오픈 소스로, 누구든 새 에이전트나 새 문제를 기여할 수 있음
- 검증기가 공개되어 에이전트가 정확한 목표 함수에 대해 최적화 가능
- 실패 시도와 부분 결과도 영구 보존되어 중복 탐색을 방지
- 분산 구조로 특정 에이전트나 조직에 대한 의존성이 없음

**한계**

- 현재 결정론적이고 빠른 검증이 가능한 수학·조합 최적화 문제에 한정됨
- 화학, 생물학, 물리학 실험처럼 검증에 비용이나 물리 장비가 필요한 도메인으로의 확장은 미확인
- 에이전트들의 참여 품질과 전략에 대한 통제 또는 조정 메커니즘이 없음
- 달성된 결과는 하한(lower bound) 개선이며, 실제 최적값(kissing number의 정확한 값)을 증명하지 않음
- 에이전트 행동의 비결정론성으로 인해 재현 가능성이 완전히 보장되지 않음
- 검증기 자체가 공개되어 있어 에이전트가 지나치게 검증기에 최적화(overfitting)할 가능성 존재

**알아둘 용어**

- **키싱 넘버(Kissing Number)**: 차원 d에서 중심 구(sphere)와 동시에 접촉(kiss)할 수 있는 동일 크기의 비겹침 구의 최대 수. 2D에서는 6, 3D에서는 12(뉴턴-그레고리 논쟁으로 유명). 11차원에서 기존 하한 593이 604로 개선됨.
- **하한(Lower Bound)**: 특정 값이 최소 이 값 이상임을 보장하는 구성(construction) 또는 증명. 실제 최적값과 다를 수 있음.
- **검증기(Verifier)**: 제출된 솔루션을 입력받아 스칼라 점수를 반환하는 결정론적 Python 코드. 채점의 신뢰성을 보장.
- **에이전트 네이티브 플랫폼(Agent-Native Platform)**: 인간이 아닌 자율 에이전트를 주요 사용자로 설계한 인터페이스와 시스템.
- **영구 공유 메모리(Persistent Shared Memory)**: 세션이 끝난 후에도 모든 에이전트의 과거 결과가 보존되어 미래 에이전트가 접근할 수 있는 구조.
- **solutionSchema**: 유효한 솔루션 제출의 데이터 구조를 JSON 형식으로 정의한 명세.
- **집단 지성(Collective Intelligence)**: 개별 구성원의 능력 합계를 초과하는, 집단적 상호작용에서 창발하는 문제 해결 능력.

**왜 주목할 만한가?**

AI 에이전트가 수학 문제를 푸는 사례는 이미 존재했지만, 대부분은 단일 에이전트 또는 긴밀히 통합된 시스템이었다. EinsteinArena는 완전히 분산되고 개방된 환경에서 독립 에이전트들이 경쟁하면서도 자발적으로 협력하여 수십 년간 풀리지 않은 수학 문제에서 인간·AI 통합 신기록을 달성했다는 점에서 새롭다. 특히 키싱 넘버 결과는 1980년 이후 가장 큰 폭의 하한 개선으로, AI가 단순히 알려진 결과를 검증하는 단계를 넘어 실제 과학적 발견에 기여하기 시작했음을 보여준다. 이 패러다임은 수학에서 출발하지만, 빠른 검증이 가능한 모든 도메인으로 확장될 잠재력을 지닌다.

---

## English Summary

**One-line summary**

EinsteinArena, from Together AI and Stanford University, is an open agent-native platform where autonomous AI agents collectively solve open mathematical problems by submitting solutions, posting in discussion forums, and building on each other's findings in real time. Since its launch in March 2026, agents on the platform have set 12 new state-of-the-art results on problems that had resisted both human and AI efforts for decades — most notably improving the kissing number lower bound in dimension 11 from 593 to 604, the largest advance since 1980.

**Core idea**

Most AI research systems are isolated: one agent, one session, no persistent record. EinsteinArena inverts this by treating the platform itself as a persistent shared memory. Every submission — successful or not — along with discussion thread posts, remains accessible to all future agents. Independent agents from different organizations can read the current best solution, inspect how it was constructed, and propose improvements. The result is emergent collective intelligence: iterative agent-to-agent knowledge transfer that exceeds what any single agent could achieve alone.

**What is new?**

- **Open distributed research platform**: A publicly accessible, agent-native platform where autonomous agents from any organization can participate in ongoing open scientific problems
- **Persistent shared memory across agents**: All submitted solutions, failed attempts, and discussion posts are preserved and visible to all agents — progress accumulates over time rather than disappearing at session end
- **Rigorous, sandboxed verification**: Every problem ships with a Python verifier that deterministically scores any submission in an isolated sandbox, eliminating ambiguity in evaluation
- **12 genuine state-of-the-art results**: Improvements on real open problems (not synthetic benchmarks), surpassing all prior human and AI records
- **Documented emergent cooperation**: In the kissing number case, competing agents voluntarily shared partial results and built on each other's constructions, demonstrating spontaneous collaboration without any explicit coordination protocol

**How does it work?**

1. **Problem specification**: Each problem is defined by four components — a natural-language description, a `solutionSchema` specifying the expected JSON structure of a valid submission, a scoring direction (maximize or minimize), and a Python `verifier` function that maps a submission to a scalar score.
2. **Agent submission**: Agents submit structured solutions via a REST API. Upon submission, the verifier runs immediately in an isolated sandbox and the score is recorded on the public leaderboard.
3. **Public leaderboard**: All submissions and scores are visible to everyone. Agents can inspect the current best solution and use it as a starting point for their own search.
4. **Per-problem discussion forum**: Agents (and humans) can post messages — partial results, failure analyses, promising directions — in a thread specific to each problem. These posts are visible to all.
5. **Iterative collective improvement**: A new agent reads prior submissions and discussion posts, uses them to inform its strategy, submits an improved solution, and the cycle continues. In the kissing number case, one agent posted a slightly-invalid but structurally promising construction; over 48 hours, successive agents refined it, each trading the top leaderboard spot, until the final record was achieved.

**Strengths**

- Demonstrates collective discovery that exceeds individual agent capability on genuine open problems
- Fully open-source: anyone can contribute new agents, new problems, or new verifiers
- Transparent verifier code allows agents to optimize against a well-defined ground truth
- Failed attempts and partial results persist, reducing redundant exploration by future agents
- Decentralized design avoids dependence on any single agent or organization

**Limitations**

- Currently limited to problems with fast, deterministic verification — primarily mathematical and combinatorial optimization
- Extension to domains requiring physical experiments, wet-lab assays, or slow simulations is not yet demonstrated
- No coordination or quality-control mechanism for participating agents; results depend on the agents that happen to participate
- Reported results are lower-bound improvements, not proofs of optimality (the true kissing number in dimension 11 is still unknown)
- The verifier is public, which could lead agents to overfit to the verifier rather than discovering genuinely robust solutions
- Agent behavior is nondeterministic, limiting full reproducibility of the discovery process

**Terms to know**

- **Kissing number**: In dimension d, the maximum number of non-overlapping unit spheres that can simultaneously touch a central unit sphere. Known exactly in dimensions 1, 2, 3, 4, 8, and 24; only bounds are known for most other dimensions. In dimension 11, the prior lower bound was 593; EinsteinArena agents raised it to 604.
- **Lower bound**: A construction or proof showing that the true optimum is at least some value. A lower bound on the kissing number means "we found an arrangement with this many spheres touching"; the true maximum may be higher.
- **Verifier**: A deterministic Python function that takes a submitted solution and returns a scalar score, run in an isolated sandbox to guarantee fair, unambiguous evaluation.
- **Agent-native platform**: A system designed with autonomous agents, rather than humans, as the primary interaction model — APIs, schemas, and feedback loops are optimized for machine consumers.
- **Persistent shared memory**: A design principle where all agents' past outputs (solutions, discussions, failed attempts) remain accessible to future agents indefinitely, allowing progress to accumulate across sessions and organizations.
- **solutionSchema**: A JSON schema that defines the exact structure a valid submission must follow, enabling automated parsing and evaluation.
- **Collective intelligence**: Problem-solving capability that emerges from the interactions of a group and exceeds what individual members can achieve alone.

**Why it is worth watching**

AI agents making progress on mathematical problems is not new. What is new here is the *open, decentralized, multi-agent* framing: independent agents, competing for leaderboard position, spontaneously cooperate by sharing partial results and building on each other's constructions. The kissing number result — the largest improvement in that problem since 1980 — was not achieved by any single agent or team, but by a 48-hour chain of incremental agent-to-agent refinements. This paradigm is currently limited to problems with fast verifiers, but the design is domain-agnostic: any field where progress can be unambiguously measured could in principle host a similar arena. EinsteinArena suggests that the bottleneck in AI-driven discovery may shift from individual agent capability to the quality of infrastructure for accumulating and sharing agent-generated knowledge.

**My take**

EinsteinArena는 AI 과학 연구 자동화를 기술적 쇼케이스가 아닌 실제 미해결 문제에서 검증했다는 점에서 주목할 만하다. 집단 지성의 핵심 설계(영구 공유 메모리 + 공개 검증기 + 분산 참여)는 단순하면서도 강력하다. 다만 결과가 수학 최적화에 국한된다는 점, 그리고 에이전트들의 내부 동기(예: 의도적 허위 제출, 검증기 오남용)를 제어할 수단이 없다는 점은 앞으로 해결해야 할 중요한 설계 문제다. 확장 가능성은 크지만, 화학이나 생물학 같은 느린 실험이 필요한 도메인에 이 패러다임이 얼마나 잘 작동할지는 아직 알 수 없다.

EinsteinArena is notable for validating AI-driven scientific discovery on real open problems rather than synthetic benchmarks. The core design — persistent shared memory, public verifiers, and decentralized participation — is elegant and powerful. The open questions are whether agents with adversarial incentives could poison the shared environment (e.g., submitting misleading partial results), and whether the paradigm can transfer to domains where verification is expensive, slow, or requires physical equipment. The mathematical results are impressive, but the platform's broader significance will depend on how far the verifier-driven model can extend beyond combinatorial optimization.
