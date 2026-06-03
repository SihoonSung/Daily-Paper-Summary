---
title: "Sandboxed Coding Agents are Competitive Omni-modal Task Solvers"
date: 2026-06-03
topic: AI
tags: [AI, agents, multimodal, coding-agent, audio-video-understanding, tool-use, omni-modal, LLM]
source: https://arxiv.org/abs/2606.00579
---

# Sandboxed Coding Agents are Competitive Omni-modal Task Solvers

* Date: 2026-06-02 (arXiv preprint)
* Source: https://arxiv.org/abs/2606.00579
* Topic: AI / multimodal agents
* Why it matters: Building a specialized omnimodal model that natively understands video and audio is expensive and slow. This paper shows that a standard text+image coding agent, given a sandboxed code execution environment, can match or outperform purpose-built native omnimodal models on audio-video benchmarks by writing code to extract and process the relevant signals — fundamentally reframing multimodal perception as a code-based retrieval problem.

## Korean Summary

**한줄 요약**

메릴랜드 대학교와 MBZUAI 연구팀은 텍스트·이미지만 처리하는 코딩 에이전트가 샌드박스 코드 실행 환경을 활용해 오디오·비디오 벤치마크에서 최신 네이티브 옴니모달 모델과 동등하거나 이를 능가함을 보였다. 핵심은 멀티모달 미디어를 모델이 직접 스트림으로 소화하지 않고 코드를 작성해 프레임·트랜스크립트·오디오 특징을 선택적으로 추출하는 방식이다. 이 접근법은 필요한 컨텍스트 토큰 수를 크게 줄이면서도 더 높은 정확도를 달성한다.

**핵심 아이디어**

기존에는 비디오·오디오 이해 태스크에 네이티브 옴니모달 모델(영상·음성을 직접 입력으로 받는 모델)이 필수적이라고 가정했다. 그러나 코딩 에이전트는 `ffmpeg`, `whisper`, `librosa`, `opencv` 같은 도구를 코드로 호출해 영상을 프레임 이미지로, 음성을 텍스트 트랜스크립트로 변환하고, 필요한 정보만 선택적으로 추출할 수 있다. 이 방식은 멀티모달 태스크를 '검색 및 정보 처리 문제'로 전환하므로 원본 미디어 스트림을 모델 컨텍스트에 직접 넣을 필요가 없다.

**무엇이 새로운가?**

- 텍스트+이미지 전용 코딩 에이전트가 OmniGAIA, SocialOmni, LVOmniBench, VideoZeroBench 등 4개 오디오-비디오 벤치마크에서 네이티브 옴니모달 모델을 처음으로 체계적으로 능가함을 입증
- **Code-X** 레시피 및 6,035개 궤적 데이터셋(비디오·오디오·이미지·크로스모달 태스크 포함) 구축 — 오픈소스로 공개하여 옴니모달 터미널 에이전트 훈련 지원
- **스킬 주입(skill injection)**: 사람이 작성하거나 자가 증류된 스킬을 주입하면 성능이 추가로 크게 향상됨을 실험적으로 증명
- 에이전트의 실패 패턴을 체계적으로 분류하는 **실패 분류법(failure taxonomy)** 및 프로세스 수준 추적 분석 제공
- 코딩 에이전트가 프로액티브 도구 사용으로 필요한 정보만 선택 취득하므로 네이티브 옴니모달 모델 대비 **토큰 소비가 현저히 적음**을 정량적으로 확인

**어떻게 작동하는가?**

1. **태스크 수신**: 에이전트는 텍스트 질문과 (선택적) 이미지만 입력으로 받고, 원본 비디오·오디오 파일 경로는 샌드박스 내 도구를 통해 접근
2. **도구 선택 및 코드 작성**: 에이전트는 무엇이 필요한지 추론한 뒤 `ffmpeg`로 특정 시간대 프레임 추출, `whisper`로 음성→텍스트 변환, `librosa`로 오디오 특징 추출 등 적합한 도구를 코드로 호출
3. **선택적 증거 수집**: 전체 미디어 스트림 대신 질문과 관련 있는 부분만 추출 — 관련 프레임 몇 장, 관련 구간의 트랜스크립트 등
4. **다단계 추론**: 추출한 증거를 기반으로 추가 코드 실행이나 이미지 분석을 반복하며 최종 답 도출
5. **스킬 주입(선택)**: 사전에 정의된 스킬(예: "비디오에서 화자를 식별하는 방법")을 컨텍스트로 주입하면 에이전트가 더 효율적인 도구 사용 패턴을 빠르게 학습
6. **평가**: OmniGAIA(오픈엔드 팩추얼·멀티홉 추론), SocialOmni(오디오-비주얼 소셜 인식), LVOmniBench(장편 오디오-비디오 이해), VideoZeroBench(고난도 비디오 추론) 등 4개 벤치마크에서 성능 측정

**강점**

- 네이티브 옴니모달 모델 없이도 동등 이상의 성능 달성 — 모달리티별 전용 대형 모델 구축 필요성 감소
- 프로액티브 선택적 검색으로 컨텍스트 토큰 사용량 대폭 절감 — 비용·지연시간 이점
- Code-X 오픈소스 데이터셋으로 27B 오픈 모델도 상당한 성능(OmniGAIA 43.3%, LVOmniBench 60.0%) 달성 — 소규모 팀도 강력한 에이전트 훈련 가능
- 도구 오케스트레이션 방식은 새로운 모달리티·도구 추가에 유연하게 확장 가능
- 실패 분류법 제공으로 후속 연구 방향 명확화

**한계**

- 코드 실행 환경(샌드박스)이 필수 — 런타임 오버헤드 및 환경 설정 복잡도 증가
- 도구 호출 전략(어떤 프레임을, 어떤 구간을 추출할지)이 잘못되면 오류 전파 — 에이전트가 잘못된 증거를 기반으로 추론할 위험
- SocialOmni처럼 화자 정체성 인식이 필요한 복잡한 소셜 인지 태스크에서는 네이티브 모델 대비 여전히 취약할 수 있음
- 스킬 주입 효과는 스킬의 품질에 크게 의존 — 잘못된 스킬은 성능 저하 유발 가능
- 비교 대상이 특정 시점의 네이티브 모델이므로 향후 더 강력한 네이티브 모델 출시 시 우위가 유지될지 불확실

**알아둘 용어**

- **옴니모달 모델 (Omni-modal model)**: 텍스트, 이미지, 오디오, 비디오 등 여러 모달리티를 네이티브 입력으로 직접 처리하는 AI 모델 (예: Gemini, GPT-4o 등)
- **샌드박스 코드 실행 (Sandboxed code execution)**: 격리된 환경에서 에이전트가 작성한 코드를 안전하게 실행할 수 있는 인프라; 파일 시스템 접근, 외부 도구 호출 등이 허용
- **도구 오케스트레이션 (Tool orchestration)**: 에이전트가 여러 전문 도구(FFmpeg, Whisper 등)를 코드로 호출하고 그 결과를 조합해 복잡한 태스크를 수행하는 방식
- **스킬 주입 (Skill injection)**: 특정 태스크 유형을 처리하는 방법을 기술한 사전 작성 지침이나 예시를 에이전트 컨텍스트에 주입하여 성능을 향상시키는 기법
- **Code-X**: 이 논문에서 공개한 오픈소스 다중 모달 에이전트 훈련용 궤적 데이터셋 및 레시피 (6,035개 예제 수록)
- **프로액티브 검색 (Proactive retrieval)**: 에이전트가 태스크 요구사항을 분석한 뒤 필요한 정보만 선별적으로 추출하는 전략; 미디어 전체를 컨텍스트에 넣는 방식과 대비됨
- **실패 분류법 (Failure taxonomy)**: 에이전트가 실패하는 유형을 체계적으로 분류한 프레임워크; 도구 선택 오류, 증거 추출 실패, 추론 오류 등을 구분

**왜 주목할 만한가?**

멀티모달 AI 인프라를 구축하려는 팀에게 이 논문은 "반드시 네이티브 옴니모달 모델이 필요하다"는 통념에 실증적으로 도전한다. 텍스트+이미지 코딩 에이전트가 코드 실행만으로 오디오·비디오 태스크를 풀 수 있다면, 고비용의 특수 모달리티 모델 대신 범용 코딩 에이전트를 최적화하는 전략이 실용적 선택지가 된다. Code-X 오픈소스 데이터셋과 스킬 주입 기법은 외부 팀이 직접 검증하고 확장할 수 있는 구체적 출발점을 제공한다.

---

## English Summary

**One-line summary**

Researchers from University of Maryland and MBZUAI show that a text+image coding agent, equipped only with a sandboxed code-execution interface, can match and in several settings surpass state-of-the-art native omnimodal models on audio-video benchmarks by converting multimodal perception into code-based retrieval and processing rather than ingesting raw media streams. The finding challenges the assumption that natively omnimodal models are necessary for audio-video reasoning tasks, and is backed by an open-source training recipe (Code-X) and a detailed failure analysis.

**Core idea**

Native omnimodal models process video, audio, and text as raw input streams, which requires expensive model architectures trained on diverse multimodal data. This paper shows an alternative: a coding agent that perceives only text and images can write code to call specialized tools (FFmpeg, Whisper, librosa, OpenCV) and selectively extract the exact frames, transcripts, or audio features needed to answer a given question. By reframing multimodal tasks as retrieval and information-processing problems solved via code, the agent avoids loading entire media streams into context, stays token-efficient, and generalizes to new modalities simply by adding new tools.

**What is new?**

- First systematic demonstration that text+image coding agents match or outperform state-of-the-art native omnimodal models across four audio-video benchmarks (OmniGAIA, SocialOmni, LVOmniBench, VideoZeroBench)
- **Code-X**: an open-source recipe and a 6,035-trajectory training dataset spanning video, audio, image, and cross-modal tasks, enabling open 27B models to achieve 43.3% on OmniGAIA and 60.0% on LVOmniBench
- **Skill injection**: empirically demonstrates that injecting human-written or self-distilled skills substantially improves agent performance, with both skill sources being effective
- **Failure taxonomy**: a structured classification of agent failure modes, supported by process-level trace analysis, that guides future improvement
- Quantitative evidence that proactive tool use significantly reduces token consumption compared to native omnimodal models ingesting full media streams

**How does it work?**

1. **Input**: The agent receives only a text question and optional images; raw video or audio files are accessible only via sandboxed tool calls
2. **Plan and code**: The agent reasons about what evidence is needed, then writes code to call appropriate tools — extracting specific video frames with FFmpeg, transcribing speech with Whisper, computing audio features with librosa
3. **Selective evidence gathering**: Only the relevant portions of the media are extracted (e.g., the 3-second clip where a speaker appears, or the specific frame showing an object) rather than the entire stream
4. **Multi-step reasoning**: The agent iterates — extracting additional evidence, running further code, or analyzing extracted images — until it has enough to answer the question
5. **Skill injection (optional)**: Domain-specific skills (e.g., how to identify speakers in a video, how to handle long-form audio) can be prepended to the agent's context to improve efficiency and reduce tool-use errors
6. **Evaluation**: Performance is measured on four complementary benchmarks covering open-ended factual reasoning, social audio-visual perception, long-form understanding, and challenging video-centric reasoning

**Strengths**

- Competitive or superior accuracy versus native omnimodal models on four benchmarks — without any native video/audio model components
- Substantially lower token consumption through proactive selective retrieval, translating directly to lower latency and cost
- Code-X open-source dataset and recipe allows teams to train capable omnimodal agents from a 27B open-weight base model
- Architecture is modality-agnostic: adding support for a new modality requires only integrating a new tool, not retraining the underlying model
- Structured failure taxonomy and trace analysis make weaknesses concrete and actionable for follow-up research

**Limitations**

- Requires a functioning sandboxed code execution environment, adding infrastructure complexity and runtime overhead from external tool calls
- Tool-selection errors propagate: if the agent extracts the wrong frames or transcribes the wrong audio segment, subsequent reasoning is built on faulty evidence
- Certain tasks requiring fine-grained native perception (e.g., detecting subtle speaker emotion from audio prosody) may still favor native omnimodal architectures
- Skill injection benefit depends heavily on skill quality — poorly written skills can degrade performance
- Benchmarks reflect a specific point in time; the performance gap over native models may close as those models improve

**Terms to know**

- **Omnimodal model**: A model that natively ingests multiple modalities — text, image, audio, video — as raw input without an intermediate transcription or conversion step
- **Sandboxed code execution**: An isolated runtime environment that safely executes agent-generated code, allowing access to tools (FFmpeg, Whisper, etc.) and file systems without affecting the host system
- **Tool orchestration**: The strategy of calling multiple specialized tools in sequence or in parallel via code to decompose a complex perceptual task into discrete, solvable sub-problems
- **Skill injection**: Prepending task-specific procedural instructions or worked examples to the agent's context to guide tool-use strategy without fine-tuning the underlying model
- **Code-X**: The open-source many-modality agent training recipe and 6,035-example trajectory dataset released alongside this paper
- **Proactive retrieval**: An agent strategy of reasoning about what evidence is needed before issuing tool calls, then fetching only that evidence, as opposed to loading all available content into context
- **OmniGAIA / LVOmniBench**: Evaluation benchmarks for omnimodal agents; OmniGAIA tests open-ended factual and multi-hop reasoning over mixed media, LVOmniBench focuses on long-form audio-video understanding

**Why it is worth watching**

The result directly challenges a widely held design assumption in multimodal AI: that strong audio-video performance requires models trained natively on those modalities. If text-image coding agents can routinely match or beat purpose-built omnimodal models, it changes the cost-benefit calculus for teams building multimodal AI systems — investing in better coding agents and richer tool libraries may deliver better returns than training specialized multimodal architectures. The open-source Code-X release makes the claim immediately reproducible. The failure taxonomy is also practically useful for anyone debugging audio-video agents today. This paper is worth tracking both for its benchmark result and for the broader architectural question it raises.

**My take**

(Korean) 이 논문의 핵심 기여는 실험적 발견 자체보다 그것이 제시하는 설계 원칙에 있다. "모달리티별 전용 모델" 대신 "범용 코딩 에이전트 + 도구"라는 패러다임이 실용적으로 경쟁력 있음을 보인 것이다. 다만 특정 모델(GPT-5.4, Gemini 3.1 Pro 등)에 대한 결과가 그 모델들의 버전에 강하게 의존하고, 더 강력한 네이티브 옴니모달 모델이 등장하면 우위가 역전될 수 있다는 점은 열린 문제다. Code-X 오픈소스 공개는 연구 커뮤니티가 독립적으로 검증할 수 있다는 점에서 높이 평가된다.

(English) The paper's most durable contribution may be less about the specific numbers and more about the architectural principle it establishes: that tool-mediated code execution is a legitimate alternative to native multimodal ingestion for a wide class of audio-video tasks. The benchmark results depend on the specific model versions tested, and as native omnimodal models continue to improve, the advantage may shrink or flip. Still, the open-source Code-X release and the failure taxonomy provide concrete tools for the research community to build on and challenge the claims directly.
