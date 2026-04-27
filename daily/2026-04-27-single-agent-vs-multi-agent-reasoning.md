---
title: "Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets"
date: 2026-04-27
topic: AI
tags: [AI, multi-agent, single-agent, reasoning, information-theory, LLM, compute-efficiency, agentic-systems]
source: https://arxiv.org/abs/2604.02460
---

Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

* Date: 2026-04-27
* Source: https://arxiv.org/abs/2604.02460
* Topic: AI / Agentic Systems / Reasoning
* Why it matters: Multi-agent LLM systems are widely assumed to be stronger than single agents, but this Stanford paper shows that the performance advantage disappears — and often reverses — once total thinking-token usage is held equal, with a clean information-theoretic explanation for why.

## Korean Summary

**한줄 요약**

멀티 에이전트 LLM 시스템의 성능 우위는 대부분 추론 토큰 예산이 더 많기 때문이며, 동일한 연산 예산 하에서는 단일 에이전트 LLM이 멀티 에이전트 시스템보다 멀티홉 추론 태스크에서 일관되게 같거나 더 나은 성능을 보인다는 스탠퍼드 연구 결과다. 이 결과는 데이터 처리 부등식(Data Processing Inequality)이라는 정보이론적 원리로 설명된다.

**핵심 아이디어**

멀티 에이전트 시스템(MAS)이 단일 에이전트 시스템(SAS)보다 뛰어나다는 기존 보고들은 MAS가 단순히 더 많은 추론 토큰을 사용한다는 사실을 통제하지 않았다. 정보이론에서 데이터 처리 부등식(DPI)은, 에이전트가 메시지를 다른 에이전트에게 전달할 때마다 정보량이 감소하거나 같아질 수밖에 없음을 보장한다. 따라서 고정된 총 토큰 예산 내에서 단일 에이전트가 전체 맥락을 유지하면서 추론하는 것이 이론적으로 더 효율적이다.

**무엇이 새로운가?**

- 멀티 에이전트 시스템의 성능 우위가 추가 연산(더 많은 추론 토큰)에서 비롯된다는 사실을 통제된 실험으로 처음 체계적으로 입증
- 데이터 처리 부등식(DPI)을 활용해 멀티 에이전트 구조의 정보 손실 메커니즘을 형식적으로 설명
- 에이전트 간 통신이 정보 병목(information bottleneck)을 유발한다는 이론 예측을 세 가지 모델 패밀리로 검증
- 맥락 활용 저하(context utilization degradation) 또는 추가 연산 제공 시에만 MAS가 경쟁력을 회복한다는 구체적 조건 제시
- FRAMES, MuSiQue(4-홉) 등 멀티홉 지식 추론 벤치마크에서 체계적 평가 수행

**어떻게 작동하는가?**

1. **사고 토큰(thinking token) 예산 정규화**: 단일 에이전트와 멀티 에이전트 시스템이 총 생성하는 사고 토큰 수를 동일하게 맞춰 공정한 비교를 구성한다.
2. **정보이론적 분석**: 데이터 처리 부등식에 따르면 I(X;Z) ≤ I(X;Y)가 항상 성립한다. 즉, 에이전트 A가 맥락 X에서 메시지 Y를 생성하고 에이전트 B가 Y만 보고 Z를 생성하면, Z는 X에 대해 Y보다 많은 정보를 담을 수 없다. 에이전트를 추가할수록 이 손실이 누적된다.
3. **예측 도출**: 단일 에이전트가 전체 맥락을 완전히 활용할 수 있으면 MAS를 능가해야 하며, 단일 에이전트의 맥락 활용 능력이 저하되거나 MAS에 추가 예산이 주어지면 MAS가 회복할 수 있다.
4. **실험 검증**: Qwen3, DeepSeek-R1-Distill-Llama, Gemini 2.5 세 모델 패밀리에서 여러 MAS 아키텍처(병렬 에이전트, 순차 에이전트, 분해(decomposition) 기반)를 단일 에이전트와 비교한다.
5. **결과 확인**: 동일 예산 조건에서 단일 에이전트가 모든 모델 패밀리에서 MAS와 동등하거나 우수한 성능을 보임을 확인한다.

**강점**

- 이론(DPI)과 실험이 일치하는 명확한 과학적 설명 제공
- 세 가지 모델 패밀리에서 결과가 재현되어 특정 모델에 국한되지 않는 일반적 발견
- 실무자들이 즉시 활용 가능한 지침 제공: 동일 예산이면 단일 에이전트가 더 효율적
- 멀티 에이전트가 언제 유용한지(맥락 활용이 저하될 때)에 대한 조건도 명시
- 기존 MAS 연구의 방법론적 약점(연산 예산 불일치)을 체계적으로 드러냄

**한계**

- 멀티홉 지식 추론(FRAMES, MuSiQue)에 초점을 맞추며, 코드 실행, 도구 사용, 병렬 처리가 필요한 태스크에서는 다른 결론이 나올 수 있음
- 단일 에이전트의 컨텍스트 윈도우 한계를 초과하는 매우 긴 맥락 태스크는 연구 범위에서 제외됨
- 에이전트 간 메시지 압축, 선택적 요약 등의 고급 MAS 아키텍처는 아직 충분히 탐색되지 않음
- 정보 병목 이론은 에이전트 수가 늘어날 때의 비대칭적 확장(asymmetric scaling)을 완전히 설명하지 못할 수 있음

**알아둘 용어**

- **사고 토큰(Thinking Token)**: 모델이 최종 답변을 생성하기 전 내부적으로 추론하는 데 사용하는 중간 토큰; test-time compute의 핵심 단위
- **데이터 처리 부등식(Data Processing Inequality, DPI)**: 정보이론의 기본 원리로, 데이터를 추가 처리하면 정보량이 증가하지 않음을 보장
- **멀티홉 추론(Multi-Hop Reasoning)**: 답을 얻기 위해 여러 중간 단계의 추론을 연결해야 하는 추론 방식
- **단일 에이전트 시스템(Single-Agent System, SAS)**: 하나의 LLM이 전체 태스크를 처음부터 끝까지 처리하는 방식
- **멀티 에이전트 시스템(Multi-Agent System, MAS)**: 여러 LLM 인스턴스가 역할을 분담하고 서로 메시지를 주고받으며 태스크를 처리하는 방식
- **맥락 활용(Context Utilization)**: 모델이 주어진 컨텍스트 윈도우의 정보를 얼마나 효과적으로 이용하는지의 정도
- **정보 병목(Information Bottleneck)**: 에이전트 간 통신에서 원래 맥락의 정보 일부가 손실되는 현상

**왜 주목할 만한가?**

현재 AI 업계에서는 더 복잡한 태스크를 위해 멀티 에이전트 아키텍처를 구축하는 것이 당연한 선택처럼 여겨진다. 그러나 이 논문은 멀티 에이전트의 성능 우위가 추가 연산에서 비롯되는 것이지 아키텍처 자체의 장점이 아님을 보여준다. 동일한 연산 비용으로 더 나은 성능을 원한다면, 에이전트를 추가하기보다 단일 에이전트에 더 많은 추론 예산을 주는 편이 낫다는 실용적 결론은 LLM 시스템을 설계하는 모든 실무자에게 중요한 시사점을 준다.

---

## English Summary

**One-line summary**

This Stanford paper shows that single-agent LLMs consistently match or outperform multi-agent systems on multi-hop reasoning when total thinking-token budgets are held equal, explaining the result through the Data Processing Inequality from information theory.

**Core idea**

Reports of multi-agent LLM systems (MAS) outperforming single-agent systems (SAS) have typically not controlled for the total amount of reasoning computation used. When the total thinking-token budget is equalized, the advantage disappears or reverses. The Data Processing Inequality (DPI) provides a formal explanation: each agent-to-agent message passing step can only reduce or preserve information content, never increase it. Therefore, splitting a fixed reasoning budget across multiple agents introduces cumulative information bottlenecks that a single agent reasoning over the full context avoids.

**What is new?**

- First systematic controlled study showing MAS performance gains vanish when total reasoning-token budgets are matched to SAS
- Applies the Data Processing Inequality to formally explain why multi-agent message passing causes information loss under fixed budgets
- Derives concrete predictions about when MAS can recover competitiveness: when single-agent context utilization degrades, or when MAS is given additional compute
- Validates predictions across three model families (Qwen3, DeepSeek-R1-Distill-Llama, Gemini 2.5) and multiple MAS architectures
- Identifies a systematic methodological flaw in prior MAS research: uncontrolled compute budgets inflate MAS performance metrics

**How does it work?**

1. **Normalize thinking-token budgets**: The experimental setup ensures SAS and MAS produce the same total number of thinking tokens, eliminating compute as a confound.
2. **Information-theoretic argument**: By the DPI, if agent A observes context X and produces message Y, and agent B observes only Y and produces output Z, then I(X;Z) ≤ I(X;Y) ≤ H(X). Every agent communication step can only lose information relative to the original context.
3. **Derive predictions**: A SAS with full context access should outperform MAS under equal budgets. MAS becomes competitive when: (a) the single agent fails to utilize its context well (e.g., lost-in-the-middle effect), or (b) the MAS is given a larger compute budget.
4. **Empirical validation**: Compare SAS against multiple MAS architectures (parallel agents, sequential agents, decomposition-based) on multi-hop reasoning benchmarks FRAMES and MuSiQue (4-hop questions only), across three LLM families under matched budgets.
5. **Confirm predictions**: SAS matches or outperforms all MAS variants under equal budget conditions across all tested model families.

**Strengths**

- Elegant theoretical grounding in well-established information theory (DPI), making the argument universally applicable rather than model-specific
- Replicated across three distinct model families, ruling out artifact explanations
- Directly actionable for practitioners: under equal compute, prefer a single agent with a larger budget over splitting across multiple agents
- Clarifies exactly when MAS does add value (tasks where context utilization is inherently limited, or when parallel execution speed matters)
- Exposes a systematic flaw in how prior MAS research is evaluated

**Limitations**

- Focused on multi-hop knowledge reasoning (FRAMES, MuSiQue); results may differ on tasks requiring tool use, code execution, or inherently parallelizable work
- Does not cover tasks that genuinely exceed a single agent's context window capacity
- Advanced MAS architectures with selective summarization or compressed inter-agent communication are not fully explored
- The information-bottleneck framing assumes sequential agent pipelines; fully parallel independent agents may behave differently
- Thinking-token normalization may not perfectly capture all forms of test-time compute (e.g., tool calls, retrieval steps)

**Terms to know**

- **Thinking token**: A token generated internally by the model during chain-of-thought or extended reasoning before producing the final answer; the unit of test-time compute used for budget normalization.
- **Data Processing Inequality (DPI)**: A fundamental theorem in information theory stating that processing (transforming) data cannot increase the amount of information about the original source.
- **Multi-hop reasoning**: A reasoning task that requires connecting multiple intermediate steps or facts to reach an answer, such as 4-hop knowledge graph traversal.
- **Single-Agent System (SAS)**: A setup where one LLM handles the entire task end-to-end with the full context available.
- **Multi-Agent System (MAS)**: A setup where multiple LLM instances divide the task, each receiving a subset of context and passing messages to one another.
- **Context utilization**: How effectively a model exploits all the information in its context window; degraded when key facts are buried far from the query (the "lost in the middle" effect).
- **Information bottleneck**: The phenomenon where inter-agent message passing compresses and discards information from the original context.

**Why it is worth watching**

Multi-agent architectures have become a dominant pattern in production AI systems, with the assumption that more agents means better performance. This paper punctures that assumption with both theory and evidence: MAS gains are primarily a compute artifact, not an architectural advantage. The practical implication is significant — if you have a fixed inference budget, you should spend it on a single agent with more thinking tokens rather than dividing it across multiple agents coordinating via message passing. This finding should inform how teams design, evaluate, and compare agentic AI systems going forward.

**My take**

이 논문의 핵심 가치는 "더 많은 에이전트 = 더 나은 성능"이라는 통념에 이론과 실험 모두로 도전한다는 점이다. 그러나 주의할 점이 있다: 결과가 멀티홉 지식 추론에 집중되어 있으며, 병렬 처리가 본질적으로 필요한 태스크(예: 대규모 코드베이스 탐색, 다중 도구 사용)에서는 MAS의 가치가 다를 수 있다. 그럼에도 불구하고 "에이전트 수를 늘리기 전에 연산 예산을 통제했는가?"라는 질문을 표준 평가 항목으로 만든 것은 이 분야에 중요한 기여다.

The paper's core value is challenging the "more agents = better performance" assumption with both theory and data. The important caveat is that results focus on multi-hop knowledge reasoning; tasks requiring genuine parallelism (e.g., large codebase exploration, multi-tool orchestration) may legitimately benefit from MAS even under equal per-agent budgets. Nevertheless, making "did you control for total compute?" a standard evaluation checkpoint for agentic AI claims is a meaningful methodological contribution to the field.
