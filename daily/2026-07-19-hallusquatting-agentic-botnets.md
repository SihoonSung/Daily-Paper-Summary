---
title: "Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting"
date: 2026-07-19
topic: security
tags: [security, ai-agents, llm-security, supply-chain-attack, prompt-injection, hallucination]
source: https://arxiv.org/abs/2607.07433
---

Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting

* Date: 2026-07-19
* Source: https://arxiv.org/abs/2607.07433
* Topic: security
* Why it matters: It shows that LLM-based coding agents can be hijacked at scale without ever directly targeting a victim — attackers just have to pre-register the fake resource names that models predictably hallucinate, turning a routine "hallucination bug" into a botnet-style propagation vector.

## Korean Summary

**한줄 요약**

이 논문은 Cursor, Windsurf, GitHub Copilot, Cline, Gemini CLI 등 코딩 에이전트들이 특정 프롬프트에 대해 실제로 존재하지 않는 저장소나 "스킬" 이름을 예측 가능한 패턴으로 환각(hallucinate)한다는 사실을 이용해, 공격자가 그 가짜 이름을 미리 선점·오염시켜 두면 아무 직접 접촉 없이도 다수의 사용자를 동시에 감염시킬 수 있음을 보였습니다. 저자들은 이를 "HalluSquatting"이라 부르며, 실제 상용 에이전트 도구들에서 원격 코드 실행까지 성공시켰습니다.

**핵심 아이디어**

기존 프롬프트 인젝션 공격은 공격자가 피해자의 프롬프트나 컨텍스트에 직접 접근할 수 있어야 했습니다. 이 논문은 그런 직접 채널이 전혀 없어도 공격이 가능하다는 것을 보여줍니다. LLM이 "이 저장소를 clone해줘", "이 스킬을 설치해줘" 같은 요청을 받으면 서로 다른 모델들도 놀랄 만큼 일관되게 같은 가짜 이름을 지어내는데, 공격자는 이를 사전에 프로파일링해 그 이름으로 악성 저장소나 패키지를 미리 등록해 두기만 하면 됩니다. 이후 아무 사용자나 비슷한 요청을 하면 에이전트가 알아서 공격자의 함정으로 걸어 들어갑니다.

**무엇이 새로운가?**

* 직접적인 프롬프트 인젝션 채널 없이도 성립하는 "비표적형(untargeted)" 대규모 공격 모델을 제시.
* 서로 다른 벤더의 여러 LLM에서 환각되는 가짜 리소스 이름이 놀랄 만큼 겹친다는(전이 가능한, transferable) 사실을 실증.
* 저장소 clone 요청에서 최대 85%, 스킬 설치 요청에서 최대 100%에 달하는 높은 환각 발생률을 보고.
* Cursor, Cursor CLI, Windsurf, GitHub Copilot, Cline, Gemini CLI 등 실제 상용 에이전트 도구를 대상으로 한 종단 간(end-to-end) 실증 공격에서 도구 호출 및 원격 코드 실행 성공.
* 감염된 에이전트가 다시 다른 사용자에게 전파될 수 있는 "봇넷형" 확산 가능성을 제기.

**어떻게 작동하는가?**

1. 공격자는 다양한 프롬프트(예: "인기 있는 X 관련 저장소를 clone해줘")를 여러 LLM에 반복 질의해, 모델들이 공통적으로 환각하는 존재하지 않는 저장소·패키지·스킬 이름의 확률 분포를 프로파일링합니다.
2. 확률이 높은 가짜 이름들을 실제로 등록하고, 그 안에 악성 코드나 숨겨진 프롬프트 인젝션 페이로드를 심어 둡니다.
3. 이후 어떤 사용자가 코딩 에이전트에게 비슷한 자연스러운 요청을 하면, 에이전트는 자체적으로 그 가짜 이름을 지어내고 그대로 접근을 시도합니다.
4. 에이전트가 공격자의 리소스를 가져오는 순간, 그 안에 숨겨진 프롬프트나 코드가 에이전트의 컨텍스트를 장악해 도구 호출이나 명령 실행으로 이어집니다.
5. 실험에서는 이 과정이 여러 상용 에이전트 도구에서 실제 원격 코드 실행까지 이어졌음을 확인했습니다.

**강점**

* 기존에 알려진 slopsquatting(패키지 환각 악용)보다 한 단계 더 나아가, 공격자가 프로파일링을 통해 특정 가짜 이름을 "유도"할 수 있음을 보여줌.
* 여러 벤더의 실제 상용 도구를 대상으로 한 종단 간 실증(end-to-end demonstration)으로 이론에 그치지 않음.
* 서로 다른 LLM 간 환각 패턴이 전이된다는 점을 정량적으로 제시해, 특정 모델에 국한되지 않는 구조적 문제임을 명확히 함.
* 책임 있는 공개(responsible disclosure) 절차를 거쳐 관련 벤더들에게 사전 통보한 것으로 알려짐.

**한계**

* 이 세션은 네트워크 접근이 제한되어 있어 arXiv 원문 페이지를 직접 재조회(fetch)하지 못했습니다. 본 요약은 검색 엔진을 통해 확인된 arXiv 메타데이터(제목, 저자, 제출일)와 SecurityWeek, Tom's Hardware, Decrypt, DevOps.com, GBHackers 등 다수의 독립적인 2차 보도를 교차 검증하여 작성되었습니다.
* 동료 심사를 거친 학술지 논문이 아니라 arXiv 프리프린트이며, 보안 연구 성격의 공개 자료입니다.
* 공격 성공률(20~65% 수준의 도구 호출/RCE 성공률 등)은 테스트한 특정 프롬프트·모델 조합에 의존하며, 벤더들이 방어책을 마련하면 빠르게 변할 수 있는 수치입니다.
* 상용 벤더들이 이미 패치나 완화 조치를 배포했을 가능성이 있으나, 이 요약 시점에서 각 벤더별 대응 현황은 확인하지 못했습니다.

**알아둘 용어**

* **프롬프트웨어(Promptware)**: 프롬프트나 콘텐츠에 악성 지시를 숨겨 LLM 기반 시스템을 조작하는 공격 범주.
* **간접 프롬프트 인젝션(Indirect prompt injection)**: 사용자가 아닌 외부 콘텐츠(웹페이지, 저장소 등)에 숨겨진 지시를 LLM이 신뢰하고 실행하게 만드는 공격.
* **슬롭스쿼팅(Slopsquatting)**: LLM이 존재하지 않는 패키지 이름을 지어낼 때, 공격자가 그 이름으로 악성 패키지를 미리 등록해두는 공급망 공격.
* **할루스쿼팅(HalluSquatting)**: 이 논문이 제안한 용어로, 환각되는 리소스 이름을 사전에 프로파일링해 선점하는 확장된 형태의 슬롭스쿼팅.
* **전이 가능성(Transferability)**: 하나의 공격 기법이나 패턴이 서로 다른 모델·시스템에도 동일하게 통하는 성질.
* **에이전틱 봇넷(Agentic botnet)**: 감염된 AI 에이전트들이 서로 연쇄적으로 다른 시스템을 감염시키는 방식으로 확산되는 네트워크.

**왜 주목할 만한가?**

코딩 에이전트가 개발 워크플로우에 빠르게 통합되고 있는 지금, 이 논문은 "모델이 가끔 틀린 이름을 지어낸다"는 익숙한 문제가 실제로는 조직적이고 예측 가능한 대규모 공급망 공격 표면이 될 수 있음을 구체적으로 보여줍니다. 특정 벤더 하나의 결함이 아니라 여러 LLM에 공통된 구조적 취약점이라는 점에서, AI 에이전트 보안 분야가 앞으로 반드시 다뤄야 할 문제로 보입니다.

---

## English Summary

**One-line summary**

This paper shows that AI coding agents such as Cursor, Windsurf, GitHub Copilot, Cline, and Gemini CLI predictably hallucinate the same non-existent repository or "skill" names for certain prompts, and that an attacker who pre-registers those fake names with malicious payloads can compromise many users' agents without ever directly targeting any of them — a technique the authors call "HalluSquatting."

**Core idea**

Traditional prompt-injection attacks require a direct channel into a victim's prompt or context. This work demonstrates an untargeted variant that needs no such channel at all. When asked to do routine tasks like "clone the trending repo for X" or "install this skill," different LLMs tend to hallucinate strikingly similar fake resource names. An attacker can profile this behavior in advance, register those exact fake names with malicious content, and then simply wait — any user whose agent independently hallucinates its way to that name walks straight into the trap.

**What is new?**

* Introduces an untargeted, large-scale attack model that requires no direct prompt-injection channel to the victim.
* Empirically shows that hallucinated resource names are strikingly consistent and transferable across LLMs from different vendors.
* Reports hallucination rates as high as 85% for repository-cloning prompts and up to 100% for skill-installation prompts.
* Demonstrates end-to-end attacks against real commercial agentic tools — Cursor, Cursor CLI, Windsurf, GitHub Copilot, Cline, and Gemini CLI — achieving tool invocation and remote code execution.
* Frames the threat as potentially self-propagating ("agentic botnets"), since compromised agents could go on to affect further users.

**How does it work?**

1. The attacker repeatedly queries multiple LLMs with realistic prompts (e.g., "clone the popular repo for X") to profile which fake resource names — repos, packages, skills — the models consistently hallucinate.
2. The attacker registers the highest-probability fake names as real resources, embedding malicious code or a hidden prompt-injection payload inside them.
3. Any user who later gives their coding agent a similar natural request causes the agent to independently hallucinate the same fake name and fetch it.
4. Once fetched, the hidden payload hijacks the agent's context, triggering unintended tool calls or code execution.
5. The authors validated this end-to-end against several production agentic coding tools, achieving remote code execution in a meaningful fraction of trials.

**Strengths**

* Extends known "slopsquatting" package-hallucination abuse into a more deliberate, profiling-driven attack that an adversary can actively steer.
* Backed by end-to-end demonstrations against real, widely used commercial tools rather than a purely theoretical argument.
* Quantifies cross-model transferability, showing this is a structural issue across vendors rather than a single model's quirk.
* Reportedly followed responsible disclosure, notifying affected vendors ahead of publication.

**Limitations**

* This session's network access is restricted, so the arXiv page itself could not be fetched directly. This summary was compiled by cross-referencing arXiv's indexed metadata (title, authors, submission date) with multiple independent secondary reports (SecurityWeek, Tom's Hardware, Decrypt, DevOps.com, GBHackers).
* It is an arXiv preprint / security research disclosure, not a peer-reviewed journal publication.
* Reported success rates (e.g., 20-65% tool-invocation/RCE success in end-to-end tests) depend on the specific prompts and models tested and may shift quickly as vendors deploy mitigations.
* Vendor-side fixes or mitigations may already be underway, but their current status was not independently confirmed for this summary.

**Terms to know**

* **Promptware**: A category of attacks that hide malicious instructions in prompts or content to manipulate LLM-based systems.
* **Indirect prompt injection**: An attack where instructions hidden in external content (a webpage, a repository) rather than the user's own input get executed by a trusting LLM.
* **Slopsquatting**: A supply-chain attack where an attacker registers a malicious package under a name that LLMs are known to hallucinate.
* **HalluSquatting**: This paper's term for a more deliberate, profiling-driven extension of slopsquatting that targets predictable, high-probability hallucinated names.
* **Transferability**: The property that an attack technique or pattern works consistently across different models or systems.
* **Agentic botnet**: A network formed when compromised AI agents go on to compromise further systems in a chain-reaction manner.

**Why it is worth watching**

As coding agents become deeply embedded in everyday developer workflows, this paper turns a familiar annoyance — "the model sometimes makes up a name" — into a concrete, systematic, and scalable supply-chain attack surface. Because the underlying hallucination patterns are shared across vendors rather than being one company's bug, this looks like a problem the whole AI-agent ecosystem will need to address.

---

## My take

이 논문은 개념적으로 명확하고 실용적인 위험을 잘 짚어낸 보안 연구입니다. 다만 동료 심사를 거치지 않은 프리프린트이며, 이번 세션에서는 네트워크 제약으로 원문을 직접 확인하지 못하고 검색 결과와 여러 2차 보도로 교차 검증했다는 한계가 있습니다. 그럼에도 다수의 독립적인 보안 매체가 동일한 수치와 공격 대상 도구 목록을 일관되게 보도하고 있어 핵심 주장의 신뢰도는 상당히 높다고 판단됩니다. AI 코딩 에이전트를 도입하는 조직이라면 이런 유형의 공급망 위험을 진지하게 검토할 필요가 있습니다.

This is a conceptually clear piece of security research that identifies a genuinely practical risk. It is a non-peer-reviewed preprint, and this session's network restrictions meant the primary source could not be fetched directly — verification here relies on search-indexed metadata and cross-referencing multiple independent secondary reports rather than a first-person read of the paper. That said, several independent security outlets consistently report the same figures and list of affected tools, which lends real credibility to the core claims. Organizations adopting AI coding agents should take this class of supply-chain risk seriously.
