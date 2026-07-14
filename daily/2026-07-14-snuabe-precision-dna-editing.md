---
title: "Engineered ADARs Enable Precision A-to-G Base Editing of DNA"
date: 2026-07-14
topic: biotech
tags: [genome-editing, CRISPR, base-editing, ADAR, gene-therapy]
source: https://www.nature.com/articles/s41587-026-03223-z
---

Engineered ADARs Enable Precision A-to-G Base Editing of DNA

* Date: 2026-07-14
* Source: https://www.nature.com/articles/s41587-026-03223-z
* Topic: biotech (genome / base editing)
* Why it matters: Conventional adenine base editors correct disease-causing mutations but also convert nearby "bystander" adenines they were not aimed at, which limits their safety for therapeutic use. This paper builds a new class of adenine base editor around an RNA-editing enzyme (ADAR) instead of the usual DNA-editing enzyme (TadA), and shows it can make single-nucleotide-precise edits with far fewer bystander and off-target changes.

## Korean Summary

**한줄 요약**

연구진은 기존 아데닌 염기교정기(adenine base editor, ABE)가 겪는 "바이스탠더(bystander)" 편집 문제를 해결하기 위해, DNA에 작용하는 TadA 대신 RNA:DNA 하이브리드에 작용하는 ADAR 탈아미노효소를 이용한 새로운 염기교정기 snuABE(single-nucleotide resolution ABE)를 개발했습니다. HEK293T 세포 32개 표적에서 중간값 5.4%, 최대 50.0%의 편집 효율을 보였으며, 기존 ABE8e 대비 오프타깃 및 바이스탠더 편집이 크게 줄었습니다.

**핵심 아이디어**

기존 ABE는 nCas9-TadA 융합 단백질이 넓게 열린 DNA 단일가닥 영역에 결합해 여러 아데닌을 동시에 편집하는 경향이 있어, 원하는 표적 외에 인접한 아데닌까지 바뀌는 부작용이 발생합니다. snuABE는 TadA 대신 이중가닥 RNA(또는 RNA:DNA 하이브리드)에 작용하는 ADAR의 탈아미노효소 도메인을 nCas9(H840A)에 붙이고, 표적 아데닌 위치에만 의도적으로 미스매치를 만드는 "tagRNA(target-adenine guide RNA)"를 사용해 ADAR이 정확히 그 위치 하나만 인식하도록 유도합니다.

**무엇이 새로운가?**

* TadA(단일가닥 DNA 탈아미노효소) 대신 ADAR(이중가닥 RNA/하이브리드 탈아미노효소)를 염기교정 엔진으로 사용하는 새로운 설계
* 표적 아데닌에만 미스매치를 만들어 편집 위치를 하나로 좁히는 tagRNA 가이드 설계
* AI 기반 단백질 진화 알고리즘 EvolvePro로 이(lice) 유래 ADAR을 개량해 활성 향상
* tagRNA 3' 말단 보호를 통한 추가 활성 증대
* Cas-OFFinder로 예측한 오프타깃 부위 및 R-loop 어세이 검증을 통해 ABE8e 대비 오프타깃·바이스탠더 편집이 뚜렷이 감소함을 확인

**어떻게 작동하는가?**

1. nCas9(H840A, 니케이스)가 가이드 RNA를 이용해 표적 DNA 서열에 결합하고 한쪽 가닥에만 니크(nick)를 냅니다.
2. tagRNA가 표적 아데닌 위치에 의도적인 미스매치를 형성하며 국소적인 RNA:DNA 이중구조를 만듭니다.
3. nCas9에 융합된 ADAR 탈아미노효소 도메인이 이 미스매치 구조를 인식해 표적 아데닌 하나만 이노신(추후 구아닌으로 읽힘)으로 전환합니다.
4. Pediculus humanus(이) 유래 ADAR을 EvolvePro로 진화시키고 tagRNA 3' 말단을 보호해 편집 활성을 높인 개선판(snuABE3.1 등)을 만듭니다.
5. HEK293T 세포 32개 표적에서 효율을 측정하고, Cas-OFFinder 예측 오프타깃 부위 및 R-loop 어세이로 ABE8e와 특이성을 비교합니다.

**강점**

* 바이스탠더 편집을 크게 줄여 치료용 유전자 교정의 안전성을 높일 잠재력
* 오프타깃 활성이 기존 ABE8e보다 뚜렷이 낮음
* AI 단백질 진화(EvolvePro)를 실제 효소 최적화에 적용한 사례로, 계산 기반 설계와 습식 실험을 결합한 실용적 워크플로우 제시
* 새로운 탈아미노효소 계열(ADAR)을 염기교정에 도입해 후속 엔지니어링의 새로운 설계 공간을 열어줌

**한계**

* 편집 효율이 중간값 5.4%로 낮아, 임상 적용 가능성이 검증된 고효율 ABE8e 등에 비해 아직 실용적 효능이 부족함
* 32개 표적, HEK293T 세포주라는 제한된 조건에서만 검증되어 다양한 유전자좌·세포종·생체 내(in vivo) 환경에서의 일반화 여부는 불확실
* 최대 효율(50.0%)과 중간값(5.4%) 간 큰 편차는 표적 서열 의존성이 크다는 것을 시사하며, 어떤 서열 특성이 고효율을 만드는지 아직 충분히 규명되지 않음
* RNA 편집효소 유래 도메인이라는 새로운 구성 요소가 세포 내 다른 RNA 편집 경로에 미치는 영향(예상치 못한 RNA 탈아미노화)은 이번 논문에서 충분히 다뤄지지 않음

**알아둘 용어**

* 아데닌 염기교정기(Adenine Base Editor, ABE): DNA의 A·T 염기쌍을 G·C로 바꾸는 유전자 교정 도구
* 바이스탠더 편집(bystander editing): 의도한 표적 염기 외에 인접한 염기까지 함께 바뀌는 부작용
* ADAR(Adenosine Deaminase Acting on RNA): 원래 이중가닥 RNA의 아데노신을 이노신으로 바꾸는 효소로, 이 논문에서는 DNA 편집에 재활용됨
* 니케이스 Cas9(nCas9): DNA 이중나선 중 한 가닥에만 절단(니크)을 내는 변형 Cas9
* tagRNA(target-adenine guide RNA): 표적 아데닌 위치에만 미스매치를 만들어 편집 위치를 특정하는 가이드 RNA
* EvolvePro: 실험 데이터를 학습해 단백질 서열을 반복적으로 개선하는 AI 기반 단백질 진화 도구
* R-loop 어세이: RNA:DNA 하이브리드 구조(R-loop) 형성 여부와 위치를 검증하는 실험 기법

**왜 주목할 만한가?**

정밀한 단일 염기 교정은 겸상적혈구빈혈증, 낭포성 섬유증 등 단일 돌연변이 질환 치료의 핵심 기술로 꼽히지만, 바이스탠더·오프타깃 편집은 임상 도입의 큰 걸림돌이었습니다. TadA 대신 ADAR을 쓰는 이 접근은 아직 효율 면에서 개선이 필요하지만, 편집 특이성을 근본적으로 다른 방식으로 확보할 수 있음을 보여주어 향후 치료용 염기교정기 설계에 새로운 방향을 제시합니다.

---

## English Summary

**One-line summary**

Researchers built a new adenine base editor, snuABE (single-nucleotide resolution ABE), by replacing the DNA-acting TadA deaminase used in conventional editors with the RNA-acting ADAR deaminase, aiming to fix the long-standing bystander-editing problem. In HEK293T cells across 32 target sites it reached a median editing efficiency of 5.4% (max 50.0%) with markedly reduced off-target and bystander editing compared to ABE8e.

**Core idea**

Conventional adenine base editors fuse a Cas9 nickase to TadA, a deaminase that acts on single-stranded DNA; because TadA has no way to distinguish the intended target adenine from nearby ones in the exposed DNA window, it often edits several adenines at once (bystander editing). snuABE instead fuses the Cas9 nickase to the deaminase domain of ADAR, an enzyme that acts on double-stranded RNA (or RNA:DNA hybrids), and pairs it with a specially designed guide RNA (tagRNA) that creates a mismatch only at the intended target adenine — giving the enzyme a structural cue to edit that single position.

**What is new?**

* A new deaminase choice for base editing: ADAR (acts on RNA:DNA hybrids) in place of TadA (acts on single-stranded DNA)
* A guide RNA design (tagRNA) that introduces a deliberate mismatch at the target adenine to localize editing to a single nucleotide
* Use of the AI-driven protein evolution tool EvolvePro to engineer a more active ADAR variant from the body louse (Pediculus humanus)
* An additional activity boost from protecting the 3′ end of the tagRNA
* Off-target profiling via Cas-OFFinder-predicted sites plus an orthogonal R-loop assay, showing reduced off-target and bystander editing relative to ABE8e

**How does it work?**

1. A Cas9 nickase (nCas9-H840A) binds the target DNA sequence via its guide RNA and nicks one strand.
2. The tagRNA hybridizes to form a local RNA:DNA structure with a deliberate mismatch positioned exactly at the target adenine.
3. The ADAR deaminase domain fused to nCas9 recognizes this mismatch structure and converts only that single adenine to inosine (read as guanine).
4. The ADAR domain (from Pediculus humanus) is further engineered with EvolvePro, and the tagRNA's 3′ end is protected, yielding higher-activity variants such as snuABE3.1.
5. Efficiency is measured across 32 target sites in HEK293T cells, and specificity is compared against ABE8e using Cas-OFFinder-predicted off-target sites and an R-loop assay.

**Strengths**

* Substantially reduces bystander editing, a key safety concern for therapeutic base editing
* Off-target activity is markedly lower than that of the widely used ABE8e
* Demonstrates a practical workflow combining AI-based protein evolution (EvolvePro) with wet-lab enzyme engineering
* Introduces a new deaminase family (ADAR) into the base-editing toolbox, opening a new design space for future editors

**Limitations**

* Median editing efficiency (5.4%) is low compared to clinically relevant ABEs like ABE8e, limiting near-term therapeutic applicability
* Validated only in HEK293T cells across 32 loci; generalization to other cell types, loci, and in vivo settings remains unproven
* The large gap between median (5.4%) and maximum (50.0%) efficiency suggests strong sequence dependence that is not yet well characterized
* Repurposing an RNA-editing enzyme domain raises an open question, not fully addressed in the paper, about potential unintended effects on native cellular RNA editing pathways

**Terms to know**

* Adenine base editor (ABE): a gene-editing tool that converts A·T base pairs to G·C without cutting both DNA strands
* Bystander editing: unwanted conversion of nucleotides near, but not at, the intended target site
* ADAR (Adenosine Deaminase Acting on RNA): an enzyme that normally converts adenosine to inosine in double-stranded RNA, repurposed here for DNA editing
* Nickase Cas9 (nCas9): a modified Cas9 that cuts only one strand of the DNA double helix
* tagRNA (target-adenine guide RNA): a guide RNA engineered to create a mismatch specifically at the target adenine
* EvolvePro: an AI-driven protein evolution tool that iteratively improves protein sequences using experimental data
* R-loop assay: an experimental method to detect and localize RNA:DNA hybrid structures (R-loops)

**Why it is worth watching**

Precise single-nucleotide correction is central to treating diseases caused by single point mutations, but bystander and off-target editing have been a major barrier to clinical use of base editors. Using ADAR instead of TadA is a structurally different route to specificity, and while efficiency still needs substantial improvement, the result points to a new design direction for safer therapeutic base editors.

---

## My take

이 논문은 획기적인 치료 적용이라기보다는, 염기교정 특이성 문제를 다른 각도(효소 자체를 바꾸는 방식)로 접근한 흥미로운 개념 증명에 가깝습니다. 오프타깃·바이스탠더 감소는 고무적이지만 5.4%라는 낮은 중간 효율은 임상 적용까지 상당한 추가 개선이 필요함을 보여줍니다. AI 기반 단백질 진화(EvolvePro)를 실제 효소 개량에 결합한 점은 최근 생명공학 연구 흐름을 잘 보여주는 사례입니다.

This reads as a solid proof-of-concept rather than a clinic-ready tool: swapping the deaminase engine (TadA → ADAR) is a genuinely different way to attack the bystander-editing problem, and the off-target/bystander improvements over ABE8e are encouraging. But the low median efficiency (5.4%) means substantial further engineering is needed before this could compete with established ABEs in therapeutic settings. The combination of AI-driven protein evolution (EvolvePro) with traditional enzyme engineering is a good example of how computational tools are now routinely folded into wet-lab biotech research.
