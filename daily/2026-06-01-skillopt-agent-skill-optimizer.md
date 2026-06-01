---
title: "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"
date: 2026-06-01
topic: AI
tags: [AI, agents, prompt-optimization, text-space-optimization, LLM, agentic-AI, skill-learning, reinforcement-learning]
source: https://arxiv.org/abs/2605.23904
---

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

* Date: 2026-05-22 (arXiv preprint; revised 2026-05-25)
* Source: https://arxiv.org/abs/2605.23904
* Topic: AI / agentic systems
* Why it matters: Most deployed LLM agents rely on manually authored skill documents (system prompts, instruction files, context Markdown) that are never systematically improved. SkillOpt introduces the first disciplined, controllable text-space optimizer for those documents — borrowing the entire conceptual machinery of gradient descent (epochs, learning rate, momentum, validation gating) and mapping it onto bounded natural-language edits — achieving a 19–25 percentage-point accuracy gain on seven frozen language models with zero inference-time overhead.

## Korean Summary

**한줄 요약**

마이크로소프트 리서치가 개발한 SkillOpt는 LLM 에이전트의 행동을 규정하는 자연어 '스킬 문서'(Markdown 파일)를 딥러닝 역전파처럼 체계적으로 최적화하는 텍스트 공간 옵티마이저로, 모델 가중치를 전혀 수정하지 않고도 6개 벤치마크·7개 모델·3개 실행 환경에서 52전 전승(52-out-of-52)을 기록하며 GPT-5.5 기준 +19–25 퍼센트포인트의 정확도 향상을 달성한다. 배포 산출물은 300~2,000 토큰 분량의 Markdown 파일 하나에 불과하며, 최적화된 스킬은 다른 모델·환경으로도 재사용 가능하다.

**핵심 아이디어**

현재 LLM 에이전트의 스킬(시스템 프롬프트, 지침 파일, CLAUDE.md 등)은 사람이 직접 작성하거나, 한 번의 LLM 호출로 생성하거나, 검증 없이 자유롭게 자가 수정하는 세 가지 방식에 의존한다. 어느 방식도 딥러닝 옵티마이저처럼 반복적이고 검증 게이팅된 개선을 보장하지 않는다. SkillOpt는 스킬 문서를 '훈련 가능한 파라미터'로 취급하고, 별도의 옵티마이저 LLM이 에이전트의 실행 궤적(rollout)에서 얻은 점수를 기반으로 add/delete/replace 편집을 제안한다. 제안된 편집은 홀드아웃 검증 세트에서 성능이 실제로 향상될 때만 반영되며, 학습률 예산·거절 편집 버퍼·에폭 단위 슬로우/메타 업데이트로 학습이 안정화된다.

**무엇이 새로운가?**

- **텍스트 공간 딥러닝 유사 훈련**: 학습률(textual learning-rate budget), 미니배치, 모멘텀, 검증 게이팅을 자연어 편집 공간에 완전히 대응시킨 최초의 체계적 스킬 옵티마이저
- **검증 게이팅**: 편집 후보가 홀드아웃 세트에서 성능을 순증가시킬 때만 반영 — 자가 수정에서 흔한 성능 퇴행 방지
- **거절 편집 버퍼**: 실패한 편집을 캐싱하여 동일한 잘못된 편집의 반복을 차단
- **배포 시 추가 추론 비용 0**: 최적화된 best_skill.md를 그대로 사용하므로 배포 단계에서 추가 모델 호출 불필요
- **범용 전이성**: 한 모델·환경에서 최적화된 스킬이 다른 모델 크기, 다른 실행 환경(Codex → Claude Code), 유사 벤치마크에서도 재최적화 없이 성능 유지

**어떻게 작동하는가?**

1. **초기화**: 에이전트의 현재 스킬 문서(혹은 빈 문서)를 시작점으로 설정
2. **롤아웃 수집**: 여러 태스크 인스턴스를 실행하여 에이전트 궤적과 결과 점수를 수집 (미니배치)
3. **편집 제안**: 별도의 옵티마이저 LLM이 롤아웃 점수와 현재 스킬 문서를 보고 add/delete/replace 편집 후보를 생성; 학습률 예산이 편집 크기를 제한
4. **검증 게이팅**: 편집 후보를 홀드아웃 검증 세트에 적용하여 성능이 순증가하면 채택, 그렇지 않으면 거절 편집 버퍼에 추가
5. **버퍼 활용**: 거절 버퍼에 쌓인 편집 기록을 차후 제안 생성 시 컨텍스트로 제공 (모멘텀 유사 기능)
6. **에폭 슬로우/메타 업데이트**: 에폭이 끝날 때마다 전체 스킬 문서를 전반적으로 정제 (느린 업데이트) 및 옵티마이저 자체의 메타 업데이트 수행
7. **배포**: 학습 완료 후 가장 높은 검증 점수를 기록한 best_skill.md를 에이전트의 스킬로 사용; 모델 가중치 변경 없이 에이전트에 주입

**강점**

- 모델 가중치 수정 없이 19–25 퍼센트포인트 정확도 향상 — 재훈련·파인튜닝 대비 비용 절감
- 52개 (모델, 벤치마크, 실행 환경) 조합 전체에서 최고 성능 달성: 인간 작성 스킬, TextGrad, GEPA, EvoSkill, Trace2Skill 등 기존 모든 방법 상회
- 배포 산출물이 300~2,000 토큰 분량 Markdown 파일 1개 — 모든 기존 에이전트 인프라에 즉시 적용 가능
- 최적화된 스킬이 모델 크기 및 실행 환경 간 전이 — 재최적화 없이 재사용 가능
- MIT 라이선스 공개 (github.com/microsoft/SkillOpt) — 연구 및 실무 재현성 보장

**한계**

- 최적화 단계에서 옵티마이저 LLM의 추가 추론 비용이 필요 (배포 후는 없음)
- 스킬 문서 크기가 300~2,000 토큰으로 제한 — 매우 복잡한 멀티스텝 태스크에서 표현력 한계 가능
- 성능 전이는 경험적으로 보고되나 이론적 보장은 없음
- 옵티마이저 LLM 자체의 품질에 의존: 옵티마이저가 낮은 품질이면 개선 폭 감소 예상
- 검증 세트 분포가 실제 배포 분포와 다를 경우 과적합 위험 (텍스트 공간에서의 오버피팅)

**알아둘 용어**

- **스킬 문서 (Skill Document)**: 에이전트의 행동 방식을 자연어로 기술하는 지침 파일; 시스템 프롬프트, CLAUDE.md, SKILL.md 등이 해당하며 모델 가중치와 독립적으로 존재
- **텍스트 공간 최적화 (Text-Space Optimization)**: 모델 파라미터 대신 자연어 텍스트를 최적화 대상으로 삼는 접근법; 그라디언트를 사용할 수 없으므로 LLM 기반 편집 제안으로 대체
- **롤아웃 (Rollout)**: 에이전트가 태스크를 수행하는 전체 실행 궤적; 액션, 관찰, 최종 점수를 포함
- **검증 게이팅 (Validation Gating)**: 제안된 변경을 홀드아웃 세트에서 검증하고, 성능이 향상될 때만 채택하는 메커니즘
- **학습률 예산 (Textual Learning-Rate Budget)**: 한 편집 단계에서 허용되는 최대 변경량(토큰 수 등)으로, 딥러닝의 학습률에 대응
- **거절 편집 버퍼 (Rejected-Edit Buffer)**: 검증에 실패한 편집 후보를 저장하여 후속 편집 생성 시 참조 — 모멘텀·경사 기록에 해당
- **에폭 슬로우/메타 업데이트 (Epoch-wise Slow/Meta Update)**: 에폭 종료 시 전체 스킬을 전반적으로 정제(느린 업데이트)하고 옵티마이저 자체도 개선하는 이중 업데이트 메커니즘

**왜 주목할 만한가?**

LLM 에이전트 배포가 확산되면서 "스킬(지침) 파일"의 품질이 에이전트 성능을 결정하는 핵심 변수가 되고 있다. 그러나 지금까지 이 파일을 체계적으로 개선하는 방법론은 없었다. SkillOpt는 딥러닝 훈련 루프의 개념을 텍스트 공간으로 온전히 이식함으로써 에이전트 스킬을 '훈련 가능한 파라미터'로 다룰 수 있는 방법론을 제시했다. Claude Code, Codex 등 실제 코딩 에이전트 환경에서의 성능 향상이 검증되었고, 오픈소스로 공개되어 실무 적용도 즉시 가능하다. 에이전트 시대에 '스킬 최적화'가 파인튜닝이나 RAG처럼 표준 기법으로 자리잡을 가능성이 있다.

---

## English Summary

**One-line summary**

SkillOpt, from Microsoft Research, is the first systematic text-space optimizer for agent skill documents: a separate optimizer LLM converts scored agent rollouts into bounded add/delete/replace edits on a natural-language skill Markdown file, accepting each edit only when it strictly improves a held-out validation score, and achieves best or tied-best results on all 52 evaluated (model, benchmark, execution-harness) combinations — lifting GPT-5.5 accuracy by +23.5 pp in direct chat, +24.8 in Codex, and +19.1 in Claude Code, with zero inference-time overhead at deployment.

**Core idea**

LLM agents today are governed by hand-crafted or one-shot-generated skill documents (system prompts, CLAUDE.md-style instruction files) that are never systematically improved after initial authoring. SkillOpt reframes skill authoring as a training problem: the skill document is the trainable artifact (not the model weights), and a separate optimizer LLM acts as the "gradient descent" engine — proposing text edits, validating them on held-out rollouts, and keeping only edits that help. By mapping the full conceptual machinery of deep learning (epochs, learning rate, momentum, validation gating) onto text-space edits, SkillOpt makes skill training as reliable as neural-network training while requiring no changes to the underlying frozen model.

**What is new?**

- **First controllable text-space optimizer for agent skills**: Prior methods (TextGrad, GEPA, EvoSkill, Trace2Skill) lack validation gating or stable learning-rate control; SkillOpt is the first to map the complete DL optimization loop onto natural-language edits
- **Validation-gated updates**: Every proposed edit is applied to a held-out validation set before acceptance; only strict improvements are committed, preventing the regression common in unconstrained self-revision
- **Rejected-edit buffer**: Failed edits are cached and fed back as context to the optimizer, functioning as a textual momentum signal to avoid revisiting dead-ends
- **Textual learning-rate budget**: Explicitly caps the volume of edits per step, analogous to the learning rate in gradient descent, enabling fine-grained control over convergence speed vs. stability
- **Zero deployment overhead**: The final artifact is a single compact Markdown file (300–2,000 tokens); no extra model calls are needed at inference time, and the skill transfers across model families and execution environments without re-optimization

**How does it work?**

1. **Initialize**: Start with an existing skill document or an empty one
2. **Collect rollouts**: Run the agent on a mini-batch of task instances, recording action sequences and outcome scores
3. **Generate edits**: The optimizer LLM receives the current skill document, rollout transcripts, and score feedback, then proposes add/delete/replace edits bounded by a textual learning-rate budget
4. **Validation gate**: Each candidate edit is applied to a held-out validation set; if the score strictly improves, the edit is committed; otherwise it enters the rejected-edit buffer
5. **Buffer feedback**: Rejected edits are included in the optimizer's context during subsequent rounds, preventing repeated failures (analogous to gradient momentum)
6. **Epoch-level slow/meta update**: At the end of each epoch, the optimizer performs a broader "slow" pass that refines the whole skill document, and a "meta" update that sharpens the optimizer's own behavior
7. **Deployment**: The best_skill.md (highest validation score across all epochs) is dropped into the agent's context at inference time — no model weight changes required

**Strengths**

- 52-out-of-52 wins across all evaluated (model, benchmark, harness) combinations against all prior methods: human-written skills, one-shot LLM generation, Trace2Skill, TextGrad, GEPA, and EvoSkill
- 19–25 percentage-point gains on GPT-5.5 across three real-world execution harnesses (direct chat, Codex CLI, Claude Code CLI)
- Deployment artifact is a compact plain-text Markdown file — no framework changes, no weight updates, works with any frozen model
- Optimized skills transfer across model scales, between Codex and Claude Code, and to a related benchmark without further optimization
- Open-source MIT license at github.com/microsoft/SkillOpt — immediately usable by practitioners

**Limitations**

- Training-time cost: running the optimizer LLM over many rollouts and edit rounds requires significant compute at optimization time (though zero at deployment)
- Skill document size is bounded (300–2,000 tokens); very complex task domains with intricate multi-step dependencies may exceed this expressive capacity
- Transfer is empirically demonstrated but lacks theoretical guarantees — distribution shift between validation and deployment environments may reduce gains
- Performance depends on the quality of the optimizer LLM; a weak optimizer yields smaller or no improvements
- Risk of overfitting to validation distribution if validation set is small or unrepresentative

**Terms to know**

- **Skill document**: A natural-language instruction or context file (e.g., SKILL.md, CLAUDE.md, system prompt) that governs how a frozen LLM behaves as an agent, stored externally from model weights
- **Text-space optimization**: A class of methods that optimize natural language artifacts (prompts, instructions, context documents) rather than model parameters, since gradients through text are unavailable
- **Rollout**: A complete execution trace of an agent on a task instance, recording the sequence of actions, observations, tool calls, and a final outcome score
- **Validation gating**: The mechanism of applying a proposed change to a held-out evaluation set and accepting it only when the change strictly improves the metric — prevents performance regressions common in self-revision pipelines
- **Textual learning-rate budget**: An explicit per-step limit on the size or number of edits the optimizer may make, analogous to the learning rate hyperparameter in gradient descent
- **Rejected-edit buffer**: A cache of previously failed edit candidates fed back to the optimizer as context, serving the role of gradient momentum or adaptive step-size history
- **Epoch-wise slow/meta update**: A two-level update at the end of each training epoch: a "slow" global refinement of the skill document and a "meta" update that improves the optimizer's own proposal strategy

**Why it is worth watching**

As LLM agents become the primary deployment mode for frontier models, the quality of the skill documents that govern them becomes a performance bottleneck that neither prompt engineering nor model fine-tuning addresses cleanly. SkillOpt demonstrates that skill documents can be trained with the same rigor as model weights, and that the resulting improvements are large, stable, and transferable — without touching the underlying model. The clean 52/52 benchmark result, the immediate open-source release, and direct applicability to widely-used agent frameworks (Claude Code, Codex) make this a high-priority paper for any team building or deploying LLM agents. If the approach proves robust across wider evaluations, "skill optimization" could become as standard a step in agent deployment as prompt engineering or retrieval augmentation is today.

**My take**

(Korean) SkillOpt는 에이전트 스킬 최적화라는 실용적으로 중요하지만 그동안 방치된 문제를 딥러닝 훈련 루프의 언어로 정확하게 재구성했다는 점에서 방법론적 기여가 크다. 52/52 전승 결과와 오픈소스 공개는 즉각적인 실무 적용 가능성을 높인다. 다만 옵티마이저 자체의 추론 비용, 스킬 문서 크기 제한, 이론적 수렴 보장 부재 등은 열린 문제로 남아 있으며, 소규모 벤치마크 외의 더 복잡한 장기 에이전트 태스크에서의 검증이 필요하다.

(English) SkillOpt cleanly recasts a practically important but previously under-addressed problem — how to reliably improve agent skill documents — using the familiar vocabulary of neural-network training. The 52/52 benchmark result and open-source release are strong signals of both technical soundness and real-world applicability. The main open questions are optimizer compute costs at scale, the expressive ceiling of short Markdown skills, and whether gains hold on longer-horizon agentic tasks beyond the benchmarks tested.
