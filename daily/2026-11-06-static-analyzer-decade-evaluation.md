---
title: "Fixed Detectors, Moving Code: How Well Do Static Security Analyzers Hold Up over a Decade of C/C++ Evolution?"
date: 2026-11-06
topic: security
tags: [security, static-analysis, sast, software-engineering, vulnerability-detection, c-cpp]
source: https://arxiv.org/abs/2611.03742
---

Fixed Detectors, Moving Code: How Well Do Static Security Analyzers Hold Up over a Decade of C/C++ Evolution?

- Date: 2026-11-06
- Source: https://arxiv.org/abs/2611.03742
- Topic: Security (static application security testing)
- Why it matters: Organizations rely on static analysis tools (SAST) to catch vulnerabilities before release, but this study is one of the first to systematically test whether a fixed detector keeps working as effectively as the codebase it scans keeps changing over many years — with results suggesting the answer is often no.

## Korean Summary

**한줄 요약**

이 논문은 CodeQL, Infer, Semgrep 같은 정적 보안 분석(SAST) 도구들이 2016년부터 2025년까지 10년간 변화한 C/C++ 코드에 대해 얼마나 안정적으로 취약점을 탐지하는지 대규모로 검증합니다. 1,116개 오픈소스 프로젝트에서 수집한 2만 개의 취약/수정 코드 사례를 사용해 분석했습니다.

**핵심 아이디어**

보안팀은 보통 분석 도구를 한 번 설정하면 오랫동안 그대로 사용합니다. 이 논문은 "탐지기(detector)는 고정되어 있는데 코드(code)는 계속 변한다"는 현실적인 조건에서, 그 고정된 도구가 시간이 지나도 여전히 효과적이고, 실행 가능하고, 비용이 합리적인지를 체계적으로 검증합니다.

**무엇이 새로운가?**

- 10년(2016~2025)에 걸친 1,116개 프로젝트, 2만 건의 취약/수정 코드 쌍이라는 대규모 종단 데이터셋 구축
- CodeQL 3개 버전, Infer 3개 버전, Semgrep 1개 설정을 동일 조건에서 비교
- 단순 적중률(F1)뿐 아니라 "분류 능력" 자체를 보는 AUROC 지표를 함께 사용해 도구의 실질적 변별력을 평가
- 탐지된 결과가 실제 코드 수정 라인과 얼마나 겹치는지(repair-line overlap)까지 확인

**어떻게 작동하는가?**

1. 각 취약점에 대해 "취약한 버전"과 "수정된 버전" 코드 쌍을 수집
2. 서로 다른 연도에 출시된 CodeQL/Infer 버전과 Semgrep 설정을 고정한 채 전체 기간의 코드에 동일하게 실행
3. 각 도구가 취약 버전과 수정 버전을 얼마나 잘 구분하는지 F1과 AUROC로 측정
4. 코드 작성 연도가 최근으로 갈수록 탐지 성능이 어떻게 변하는지 추세 분석
5. 탐지된 경고가 실제로 수정된 코드 라인을 가리키는지 수동으로 대조

**강점**

- 단일 벤치마크가 아닌 10년치 실세계 코드 변화를 반영한 현실적인 평가 설계
- 세 가지 서로 다른 성격의 도구(쿼리 기반 CodeQL, 추상 해석 기반 Infer, 패턴 기반 Semgrep)를 동시에 비교해 일반화 가능성을 높임
- F1뿐 아니라 AUROC를 병행 제시해 "숫자는 좋아 보이지만 실은 재현율과 오탐률이 같이 오른 것"이라는 숨겨진 문제를 드러냄
- 탐지 결과와 실제 수정 라인의 일치 여부까지 확인해 "맞혔다"는 claim을 더 엄격하게 검증

**한계**

- C/C++ 언어와 특정 세 도구(CodeQL, Infer, Semgrep)에 한정된 결과로, 다른 언어·도구에는 그대로 일반화하기 어려움
- "취약/수정 코드 쌍"이라는 레이블링 자체가 완벽하지 않을 수 있음(수정이 다른 이유일 수도 있음)
- 분석 대상이 오픈소스 프로젝트 커밋 기록에 의존하므로, 비공개 소프트웨어 환경에는 적용성이 제한적

**알아둘 용어**

- SAST (정적 애플리케이션 보안 테스트): 코드를 실행하지 않고 소스 코드 자체를 분석해 취약점을 찾는 기법
- F1 스코어: 정밀도와 재현율의 조화평균으로, 탐지 성능을 하나의 숫자로 요약한 지표
- AUROC: 분류기가 양성과 음성을 얼마나 잘 구분하는지를 나타내는 지표(0.5면 무작위 수준)
- 재현율(recall): 실제 취약점 중 몇 퍼센트를 찾아냈는지
- 오탐률(false positive rate): 취약하지 않은 코드를 취약하다고 잘못 판단한 비율
- repair-line overlap: 도구가 지적한 위치가 실제로 개발자가 수정한 라인과 얼마나 겹치는지

**왜 주목할 만한가?**

많은 기업과 오픈소스 프로젝트가 몇 년 전에 도입한 보안 스캐너 설정을 그대로 유지하고 있습니다. 이 논문은 "도구가 한번 잘 작동했다고 계속 잘 작동하는 것은 아니다"라는 점을 구체적 데이터로 보여주며, 보안팀이 정기적으로 탐지기를 재검증해야 한다는 실무적 메시지를 던집니다.

---

## English Summary

**One-line summary**

This paper runs a large-scale, decade-spanning evaluation of static application security testing (SAST) tools — CodeQL, Infer, and Semgrep — to see whether a fixed detector configuration keeps finding real vulnerabilities as effectively as the C/C++ code it analyzes evolves over 2016–2025.

**Core idea**

Security teams typically configure a static analyzer once and keep using that same configuration for a long time. The paper asks a practical question under that realistic constraint: does a fixed, unchanged detector stay effective, runnable, and affordable as the codebase it scans keeps moving forward in time?

**What is new?**

- A longitudinal dataset of 20,000 vulnerable/fixed C/C++ code pairs drawn from 1,116 open-source projects spanning 2016–2025
- A controlled comparison across three CodeQL releases, three Infer releases, and one Semgrep configuration under identical conditions
- Use of AUROC alongside the more commonly reported F1 score, to check whether a tool's discriminative ability — not just its raw hit rate — is actually improving
- A check of "repair-line overlap," verifying whether a tool's flagged locations actually match the lines developers changed to fix the vulnerability

**How does it work?**

1. Collect matched pairs of vulnerable and patched code for each known vulnerability.
2. Run fixed, documented releases of CodeQL, Infer, and a Semgrep configuration across the full ten-year span of code without re-tuning them.
3. Measure each tool's ability to separate vulnerable from fixed code using both F1 and AUROC.
4. Track how detection quality trends as the analyzed code moves from older to more recent years.
5. Manually cross-check whether flagged warnings land on the actual lines developers modified to fix the bug.

**Strengths**

- A realistic, decade-long evaluation design rather than a single static benchmark snapshot
- Three structurally different tools (query-based CodeQL, abstract-interpretation-based Infer, pattern-based Semgrep) tested together, improving generalizability of the conclusions
- Reporting AUROC alongside F1 exposes a hidden problem: scores that look like "improvement" can actually come from recall and false-positive rate rising together, not from better discrimination
- Cross-checking flagged lines against actual repair lines adds a stricter, more meaningful notion of a "correct" detection

**Limitations**

- Results are specific to C/C++ and to three particular tools (CodeQL, Infer, Semgrep), so they may not generalize to other languages or analyzers
- The vulnerable/fixed labeling from commit history is not perfectly clean — some "fix" commits may address unrelated issues
- Reliance on open-source project history limits how directly the findings transfer to closed-source or proprietary codebases

**Terms to know**

- SAST (Static Application Security Testing): Analyzing source code without executing it to find potential vulnerabilities
- F1 score: The harmonic mean of precision and recall, summarizing detection performance in a single number
- AUROC: A metric describing how well a classifier distinguishes positives from negatives (0.5 means no better than random)
- Recall: The fraction of actual vulnerabilities a tool successfully flags
- False positive rate: The fraction of non-vulnerable code incorrectly flagged as vulnerable
- Repair-line overlap: Whether a tool's flagged location actually matches the line a developer changed to fix the bug

**Why it is worth watching**

Many organizations set up a security scanner once and leave its configuration untouched for years. This paper provides concrete longitudinal evidence that "a tool that worked well once" does not mean "a tool that keeps working well" — a practical reminder that detector configurations need periodic re-validation as codebases evolve.

---

## My take

이 논문은 화려한 신기술을 제시하기보다, 업계에서 당연하게 여겨지던 가정(정적 분석 도구는 한 번 설정하면 계속 신뢰할 수 있다)을 실증 데이터로 재검토한 점에서 가치가 있습니다. 특히 F1만 보면 성능이 향상된 것처럼 보이지만 AUROC로 보면 실질적인 변별력은 거의 그대로라는 지적은, 보안 도구 평가 관행 자체에 시사점을 줍니다. 다만 C/C++ 세 도구로 범위가 제한되어 있어, 다른 언어·다른 분석기에도 같은 결론이 적용될지는 추가 검증이 필요합니다.

This paper is less about a flashy new technique and more about empirically re-examining an assumption the industry often takes for granted — that a static analyzer, once configured, remains trustworthy indefinitely. The AUROC-versus-F1 contrast is a particularly useful methodological point for how SAST tools should be evaluated going forward. That said, the scope (three specific tools, C/C++ only) means the generality of the conclusion to other languages and analyzers still needs confirmation.
