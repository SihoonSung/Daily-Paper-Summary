---
title: "AI systems out-persuade expert humans"
date: 2026-06-21
topic: AI safety
tags: [AI, persuasion, AI-safety, HCI, social-impact, LLM, policy, democracy, misinformation]
source: https://arxiv.org/abs/2606.16475
---

# AI systems out-persuade expert humans

* Date: 2026-06-21
* Source: https://arxiv.org/abs/2606.16475
* Topic: AI Safety / HCI / Social Impact
* Why it matters: 상업용 AI가 전문 토론자, 직업적 모금 캠페이너를 포함한 모든 인간 설득 전문가를 4개의 사전 등록 실험에서 일관되게 능가했음을 보여준다. AI가 인간 수준의 설득력을 갖게 됐다는 가설이 아니라 실증적으로 입증된 첫 대규모 연구이며, 정치 광고·선거·자선 모금 등 사회 전반에 광범위한 함의를 가진다.

---

## Korean Summary

**한줄 요약**

Oxford 대학 연구팀이 18,978건의 대화를 통해 상업용 AI 시스템이 일반인, 설득 토너먼트 우승자, 세계 챔피언 급 토론자, 직업적 모금 캠페이너 모두를 실제 설득력 지표에서 일관되게 능가함을 입증했다. 특히 Save the Children을 위한 실제 기부 실험에서 AI는 전문 캠페이너 대비 약 2.7배의 기부율을 이끌어냈다.

**핵심 아이디어**

현재의 대형 언어 모델(LLM)은 단순히 정보 검색 도구를 넘어 매우 효과적인 설득 엔진으로 기능할 수 있다. 이 연구는 AI의 설득 우위가 단순한 인상이 아니라 실제 실험에서 측정 가능한 형태로 존재하며, 그 핵심 메커니즘이 정보량의 빠른 처리와 전달(throughput)임을 밝혀냈다. 인간이 연습하고 코칭을 받아도 이 격차를 좁히기 어렵다는 점에서 AI 안전성과 민주주의에 대한 심각한 함의를 가진다.

**무엇이 새로운가?**

- **대규모 사전 등록 실험**: 4개의 사전 등록(preregistered) 실험, 18,978건 대화, 6,923명 설득 대상자, 295명 인간 설득자라는 역대 최대 규모의 AI vs. 인간 설득 비교 연구
- **전문가 전 계층 비교**: 일반인부터 토너먼트 우승자, 세계 챔피언 급 토론자, 직업적 캠페이너까지 설득 전문가 모든 계층에서 AI가 우위를 보임
- **실제 행동 결과 측정**: 의견 변화가 아닌 실제 기부 여부·금액이라는 실제 경제적 행동으로 설득 효과를 측정
- **설득 메커니즘 규명**: AI의 우위가 주로 처리 속도와 정보량(throughput)에서 온다는 것을 속도·길이 제약 실험으로 실증
- **코칭 효과 한계 확인**: AI와의 연습, 성과 검토, AI의 답변 비교 코칭 도구를 제공해도 전문가의 격차가 좁혀지지 않음을 확인

**어떻게 작동하는가?**

1. **실험 1–설득 토너먼트**: 일반인 설득자 집단과 사전 등록된 4라운드 온라인 토너먼트를 통해 선발된 최우수 설득자를 AI와 비교. 참가자들은 대화 후 의견 변화를 측정

2. **실험 2–세계 토론 챔피언**: 세계 챔피언십 급 토론자들이 자신의 토픽을 선택하고 사전 조사하며 몇 시간의 구조화된 연습을 거친 후, £1,000 보너스 인센티브 조건에서 AI와 경쟁. AI가 여전히 우위

3. **실험 3–코칭 후 재도전**: 패배한 토론자들에게 AI와 연습하고 자신의 성과 이력과 AI의 답변을 볼 수 있는 코칭 도구를 제공하여 재도전. AI의 우위가 지속됨

4. **실험 4–실제 모금 (현장 비교)**: 실제 UK 모금 회사의 직업적 캠페이너 vs. AI(Claude Opus 4.6)를 실제 기부 실험으로 비교. 참가자들은 자신의 연구 참가비 일부를 Save the Children에 기부할 의향이 있는지 대화를 통해 설득. AI는 17.2% 기부율, 전문 캠페이너는 6.4%를 기록하여 AI가 약 2.7배 더 효과적이었으며, 기부액도 평균 13% 높았음

5. **메커니즘 실험**: AI를 인간 수준의 응답 속도와 메시지 길이로 제한했을 때, 코칭된 토론자 대비 AI의 우위는 통계적 유의성을 잃음 → 처리량이 핵심 메커니즘임을 확인

**강점**

- 4개의 사전 등록 실험으로 방법론적 엄밀성 확보 (사후 가설화 방지)
- 6,923명이라는 대규모 표본, 의견 변화뿐만 아니라 실제 금전적 행동 결과 측정
- 설득 전문가의 모든 계층을 망라하는 포괄적 비교
- 코칭·연습 조건 포함으로 인간 학습 효과도 검증
- 설득 메커니즘(throughput)을 규명하는 통제된 실험 포함

**한계**

- 사전 심사(peer review)를 거치지 않은 프리프린트
- 텍스트 기반 온라인 채팅만 테스트—음성, 영상, 대면 설득은 미포함
- Prolific 플랫폼 기반 크라우드소싱 참가자가 다수—실제 세계를 완전히 대표하지 않을 수 있음
- 참가자들이 15~20분 대화에 자발적으로 참여한 조건—현실의 짧은 상호작용과 다를 수 있음
- AI가 설득적이지만 사실이 아닌(fabricated) 정보를 생성한 사례 보고—설득력과 정확성이 반드시 일치하지 않음
- UK 자선 모금 맥락에서의 결과가 정치·상업 등 다른 설득 맥락에 그대로 적용되는지 불확실

**알아둘 용어**

- **설득(Persuasion)**: 대화나 논증을 통해 상대방의 의견, 태도, 행동을 변화시키는 과정
- **사전 등록(Preregistration)**: 연구 시작 전에 가설과 분석 계획을 공개 등록하는 연구 윤리 관행. 사후 가설화(HARKing)를 방지해 결과의 신뢰성을 높임
- **처리량(Throughput)**: 이 논문에서 AI의 핵심 설득 우위 메커니즘으로, 단위 시간당 더 많은 정보와 논증을 전달하는 능력
- **프리프린트(Preprint)**: 정식 동료 심사 전에 공개된 연구 논문. arXiv와 같은 플랫폼에 게재
- **동료 심사(Peer Review)**: 동일 분야 전문가들이 연구의 방법론과 결론을 검증하는 학술 출판 과정
- **대형 언어 모델(Large Language Model, LLM)**: GPT, Claude 등 대규모 텍스트 데이터로 훈련된 언어 생성 AI 시스템
- **사전 등록된 실험(Preregistered Experiment)**: 방법론, 가설, 통계 분석 계획을 미리 공개 등록하고 진행한 실험. 결과 편향을 방지하기 위한 표준적 관행

**왜 주목할 만한가?**

AI가 인간보다 설득력이 높다는 우려는 이전에도 있었지만, 이를 대규모 통제 실험으로 실증한 것은 이 논문이 처음이다. 결과는 단순히 인상적인 수준이 아니라—2.7배의 기부율, £1,000 인센티브를 가진 세계 챔피언 토론자도 패배—정치 광고, 선거 캠페인, 자선 모금, 여론 조작 등 사회 전반에서 AI가 인간 설득자를 대체하거나 압도할 수 있음을 시사한다. 설득이 처리량의 문제라면, AI의 자연적인 비교 우위(속도, 병렬성)가 이미 결정적으로 작용하고 있다는 의미이다.

---

## English Summary

**One-line summary**

A large-scale preregistered study by Oxford University researchers found that commercial AI systems reliably out-persuade every class of human expert they were tested against — including tournament-winning persuaders, world championship debaters with financial incentives, and professional fundraising canvassers — across 18,978 conversations with 6,923 participants. In a real-money charity donation experiment, AI was approximately 2.7 times more effective than professional human canvassers.

**Core idea**

Modern large language models are not just information retrieval tools — they are already effective persuasion engines that surpass even the most skilled human persuaders in measurable conversational settings. This study is the first large-scale, preregistered empirical demonstration of AI persuasion superiority, and it identifies the underlying mechanism: AI's advantage comes primarily from its ability to deliver more information faster (throughput), not from qualitatively different rhetorical strategies. This has significant implications for AI safety, political influence, and democratic discourse.

**What is new?**

- **Largest preregistered AI-vs-human persuasion study to date**: 4 preregistered experiments, 18,978 conversations, 6,923 persuadees, 295 human persuaders — far exceeding prior work in scale and rigor
- **All expert classes beaten**: AI out-persuaded random laypeople, selected laypeople, tournament persuasion winners, world champion debaters, and professional fundraising canvassers — covering the full spectrum of human persuasion expertise
- **Real behavioral outcomes**: Persuasion was measured not just by opinion change but by actual monetary donation behavior, lending ecological validity to the findings
- **Mechanism identified**: A controlled speed/length constraint experiment pinpointed throughput as the primary driver of AI's advantage
- **Coaching resistance**: Even after giving experts a coaching tool (AI practice, performance history, AI response comparison), AI's advantage persisted

**How does it work?**

1. **Experiments 1–2 (Persuasion tournament and world debaters)**: AI systems were pitted against laypeople in a preregistered multi-round persuasion tournament, then against world-class debaters who chose their own issues, researched them, practiced for hours, and were offered £1,000 cash bonuses to beat the AI. AI won in both conditions.

2. **Experiment 3 (Coaching intervention)**: Losing expert debaters were given a coaching tool allowing them to practice against the AI, review their own performance history, and see what the AI would have said at key moments. Despite coaching, AI's persuasive advantage over humans remained.

3. **Experiment 4 (Real-money fundraising field comparison)**: Professional canvassers from a UK fundraising firm and an AI system (Claude Opus 4.6) were compared head-to-head in live charity conversations for Save the Children. Participants chose whether to donate part of their study bonus. AI achieved a 17.2% donation rate vs 6.4% for human professionals — approximately 2.7x more effective — and average donations were 13% larger under AI.

4. **Mechanism experiment (Throughput test)**: When the AI was artificially constrained to respond at human writing speeds and with human-length messages, its persuasive advantage over coached debaters was no longer statistically significant — confirming that the volume and speed of information delivery, not rhetorical quality per se, is the main source of AI's edge.

**Strengths**

- Four preregistered experiments provide methodological rigor and protect against post-hoc hypothesis generation
- Large sample size with actual behavioral outcome (money donated) rather than self-reported opinion shift
- Comprehensive comparison across the full range of human persuasion expertise
- Coaching intervention tests whether humans can close the gap with structured practice (they largely cannot)
- Mechanism isolation through controlled throughput experiment

**Limitations**

- Preprint: has not yet undergone peer review
- Text-only chat format — does not cover voice, video, or in-person persuasion, which may yield different results
- Prolific platform crowdsourced participants may not represent the general population or high-stakes real-world audiences
- Participants self-selected into long 15–20 minute conversations, which is not representative of most real-world persuasion interactions
- AI sometimes generated convincing but factually unsupported or fabricated information — persuasiveness and accuracy are not the same thing
- Results from a UK charity fundraising context may not generalize to political, commercial, or adversarial persuasion settings
- Experiments were conducted online and in English; cross-cultural and cross-linguistic generalization is unknown

**Terms to know**

- **Persuasion**: The process of changing someone's beliefs, attitudes, or behaviors through conversation or argument
- **Preregistration**: The practice of publicly registering hypotheses and analysis plans before data collection, preventing post-hoc hypothesis fitting and increasing result credibility
- **Throughput**: In this paper's context, the ability to deliver more information, arguments, and references per unit of conversational time — identified as AI's primary persuasive mechanism
- **Preprint**: A research paper made publicly available (e.g., on arXiv) before formal peer review
- **Peer review**: The process by which domain experts evaluate a study's methodology and conclusions before formal publication
- **LLM (Large Language Model)**: AI systems like Claude or GPT trained on large text datasets, capable of generating fluent, contextually appropriate text
- **Effect size**: A quantitative measure of the magnitude of an experimental effect, independent of sample size. The 2.7x donation rate difference in this study represents a very large effect.

**Why it is worth watching**

Concerns about AI's persuasive capabilities have been raised for years, but this is the first large-scale, preregistered empirical demonstration that commercial AI systems already reliably out-persuade the most skilled human experts across diverse conditions. The magnitude of the effect — 2.7x fundraising effectiveness, world-champion debaters losing despite financial incentives and coaching — suggests this is not a marginal edge but a qualitative shift. If AI's persuasive advantage is fundamentally rooted in throughput rather than rhetorical sophistication, then the structural features of AI (speed, parallelism, tirelessness) make this advantage essentially permanent. The implications span political advertising, election campaigns, misinformation campaigns, and large-scale opinion manipulation — making this one of the most socially urgent AI capability results published in 2026.

**My take**

한국어: 연구의 규모와 방법론적 엄밀성은 인상적이다—사전 등록, 대규모 표본, 실제 금전적 행동 측정은 이 결과를 단순한 인상론에서 경험적 사실로 격상시킨다. 그러나 몇 가지 중요한 유보가 있다: 텍스트 기반 채팅이라는 제약, 크라우드소싱 참가자, 15~20분이라는 비전형적으로 긴 상호작용. 가장 걱정스러운 발견은 AI가 설득력이 높지만 반드시 정확하지는 않다는 점이다—설득적 허구(fabrication)의 위험이 크다. 동료 심사 통과 후 독립 복제 연구가 나온다면 이 결과는 AI 규제 논의의 핵심 증거가 될 것이다.

English: The study's scale and methodological rigor are impressive — preregistration, large samples, and real monetary behavioral outcomes elevate this from anecdote to empirical evidence. Important caveats remain, however: the text-chat-only format, crowdsourced participants, and the unusually long 15–20 minute conversations are not typical of real-world persuasion contexts. The most concerning finding is that AI persuasiveness does not correlate with accuracy — the chatbots sometimes deployed convincing fabrications. If replicated by independent groups and the findings survive peer review, this result will become a cornerstone of AI governance and regulation debates. It is already worth taking seriously.
