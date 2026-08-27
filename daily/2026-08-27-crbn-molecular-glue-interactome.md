---
title: "Proteome-wide identification of the druggable CRBN interactome"
date: 2026-08-27
topic: biotech
tags: [biotech, drug-discovery, molecular-glue-degraders, targeted-protein-degradation, chemoproteomics, cancer-therapeutics]
source: https://www.nature.com/articles/s41587-026-03237-7
---

Proteome-wide identification of the druggable CRBN interactome

* Date: 2026-08-27
* Source: https://www.nature.com/articles/s41587-026-03237-7
* Topic: Biotech / Drug discovery (targeted protein degradation)
* Why it matters: Researchers at EPFL combined an AI-based protein-surface comparison method with a high-throughput yeast assay to scan the entire human proteome for proteins that molecular glue degrader drugs can already latently bind, discovering 43 previously unknown binder proteins and giving drug developers a much larger set of starting points for a fast-growing class of cancer therapeutics.

## Korean Summary

**한줄 요약**

Nature Biotechnology에 2026년 8월 13일 게재된 이 논문은 스위스 EPFL(Thomä 연구팀)이 개발한 파이프라인으로, 분자 접착제(molecular glue) 항암제가 표적으로 삼는 E3 리가아제 어댑터 단백질 CRBN과 결합할 수 있는 인체 단백질을 프로테옴 전체 규모에서 찾아낸 연구를 다룬다. 이 방법으로 이미 알려진 6개 결합 단백질 외에 43개의 새로운 결합 후보를 발견했다.

**핵심 아이디어**

분자 접착제 분해제(molecular glue degrader, MGD)는 세포 내 단백질 분해 기계(E3 유비퀴틴 리가아제)를 이용해 질병 유발 단백질을 선택적으로 파괴하는 신약 계열이다. 그러나 어떤 단백질이 CRBN이라는 어댑터와 이미 '접착제 친화적인' 표면을 갖고 있는지는 잘 알려져 있지 않았다. 이 연구는 컴퓨터 기반 표면 유사성 탐색과 대규모 실험 검증을 결합해, 기존에 알려진 아연 손가락(zinc-finger) 계열을 넘어서는 잠재적 CRBN 결합 단백질을 체계적으로 찾아냈다.

**무엇이 새로운가?**

* GluePCA라는 고처리량 단백질 상보화 효모 분석법을 개발해 CRBN-분자접착제 유도 상호작용을 대규모로 측정
* MaSIF-mimicry라는 AI 기반 단백질 표면 비교 알고리즘으로, 서열이나 전체 구조가 아닌 국소 표면 형태의 유사성을 기준으로 프로테옴 전체를 스캔
* 약 7,000개 이상의 후보 단백질 도메인을 컴퓨터로 선별한 뒤 상위 1,959개를 실험적으로 검증
* 기존에 알려진 6개 CRBN-포말리도마이드 결합 단백질 외에 43개의 새로운 결합 단백질 도메인을 발견
* 일부 신규 후보는 기존 아연 손가락 모티프와 다른 방식으로 CRBN과 결합함을 확인

**어떻게 작동하는가?**

먼저 MaSIF-mimicry 알고리즘이 인체 프로테옴 전체를 대상으로, CRBN이 이미 인식하는 표면 형태와 국소적으로 닮은 작은 표면 영역을 가진 단백질 도메인을 컴퓨터로 탐색한다. 이렇게 추려진 수천 개의 후보 중 상위 후보들을 GluePCA 분석으로 실험 검증한다. GluePCA는 메토트렉세이트 내성 디하이드로엽산 환원효소(DHFR)를 두 조각으로 나누어 각각 미끼(bait) 단백질과 먹이(prey) 단백질에 융합시키고, 두 단백질이 분자접착제(포말리도마이드) 존재 하에 결합하면 DHFR 활성이 복원되어 효모가 자랄 수 있게 하는 방식으로 상호작용 여부를 판별한다.

**강점**

* 개별 후보를 하나씩 검증하는 기존 방식과 달리 프로테옴 전체를 체계적으로 스캔
* 컴퓨터 기반 사전 선별로 실험 검증 대상을 좁혀 효율적인 대규모 스크리닝 가능
* 서열 유사성이 아닌 표면 형태 유사성에 기반해, 기존에 놓쳤을 법한 비전형적 결합 단백질까지 발견
* 신약 개발 초기 단계에서 새로운 분자접착제 표적 후보를 직접 제공

**한계**

* 이번 연구는 포말리도마이드라는 특정 분자접착제와 CRBN 조합에 한정되어 검증되었으며, 다른 E3 리가아제나 다른 접착제 분자로 일반화되는지는 추가 검증이 필요
* 발견된 43개 신규 결합 단백질이 실제로 약리학적으로 유용한 분해 표적이 되는지는 후속 연구가 필요
* 원문 전체에 직접 접근하지 못해 정량적 결합 친화도나 통계적 유의성 등 세부 수치는 이번 요약에서 확인하지 못함

**알아둘 용어**

* CRBN(세레블론): 분자접착제 약물이 결합해 표적 단백질을 유비퀴틴-프로테아좀 분해 경로로 유도하는 E3 리가아제 어댑터 단백질
* 분자 접착제 분해제(molecular glue degrader, MGD): 두 단백질 사이에 새로운 결합을 유도해 표적 단백질을 세포 스스로 분해하게 만드는 약물 계열
* 단백질 상보화 분석(protein complementation assay): 두 단백질이 결합할 때만 신호(예: 효소 활성)가 복원되도록 설계한 상호작용 검출 기법
* 아연 손가락 모티프(zinc-finger motif): 기존에 알려진 CRBN 결합 단백질 대부분이 공유하는 구조적 특징
* 프로테옴(proteome): 한 생물이 발현하는 모든 단백질의 총집합
* 포말리도마이드(pomalidomide): CRBN을 표적으로 하는 대표적 분자접착제 약물

**왜 주목할 만한가?**

분자접착제 분해제는 기존에 '약물화 불가능'하다고 여겨지던 단백질까지 표적으로 삼을 수 있어 항암제 개발 분야에서 빠르게 주목받고 있다. 이번 연구는 어떤 단백질이 이미 CRBN과 결합 가능한 표면을 갖고 있는지를 프로테옴 규모로 지도화함으로써, 신약 개발 초기 단계의 표적 발굴 범위를 크게 넓혔다는 점에서 실질적 파급력이 크다.

---

## English Summary

**One-line summary**

A paper published in Nature Biotechnology on August 13, 2026 describes a pipeline from EPFL (Thomä lab) that scanned the entire human proteome for proteins already capable of binding the E3 ligase adapter CRBN in the presence of a molecular glue degrader, uncovering 43 previously unreported binder proteins beyond the six known ones.

**Core idea**

Molecular glue degraders (MGDs) are a drug class that hijacks a cell's protein-disposal machinery (E3 ubiquitin ligases) to destroy disease-causing proteins that are otherwise hard to target directly. Until now, it was largely unknown which human proteins already possess surfaces that CRBN-glue complexes can latently engage, beyond the well-studied zinc-finger protein family. This study combines computational surface-similarity search with large-scale experimental validation to systematically map that latent interactome.

**What is new?**

* A high-throughput yeast protein-complementation assay (GluePCA) that measures CRBN–glue-induced protein interactions at scale
* An AI-based surface-comparison algorithm (MaSIF-mimicry) that scans the proteome for local surface patches resembling CRBN's known binding interface, rather than relying on sequence or overall fold similarity
* Computational screening narrowed over 7,000 candidate protein domains down to 1,959 top candidates tested experimentally
* Discovery of 43 novel CRBN–pomalidomide binder domains alongside 6 previously known ones
* Some novel candidates bind CRBN through interfaces distinct from the canonical zinc-finger motif

**How does it work?**

MaSIF-mimicry first computationally scans the entire human proteome for protein domains with small surface regions that locally resemble the surface CRBN already recognizes, rather than searching by sequence homology. The top computational candidates are then tested experimentally with GluePCA, which splits a methotrexate-resistant dihydrofolate reductase (DHFR) enzyme into two fragments fused to a bait and a prey protein; when the bait and prey are brought together by the glue molecule (pomalidomide), DHFR activity is reconstituted, allowing yeast growth as a readout of interaction.

**Strengths**

* Systematically scans the whole proteome rather than testing candidates one at a time
* Computational pre-filtering makes large-scale experimental screening tractable
* Surface-shape-based search can surface atypical binders that sequence-based approaches would likely miss
* Directly supplies new candidate targets for early-stage molecular glue drug discovery

**Limitations**

* Validation was performed specifically for CRBN and pomalidomide; generalization to other E3 ligases or other glue molecules remains to be tested
* Whether the 43 newly identified binder domains are pharmacologically useful degradation targets requires further follow-up
* The full text was not directly accessible for this summary, so precise binding affinities and statistical detail could not be confirmed here

**Terms to know**

* CRBN (cereblon): the E3 ligase adapter protein that molecular glue drugs bind to redirect target proteins into the ubiquitin-proteasome degradation pathway
* Molecular glue degrader (MGD): a drug class that induces a new interaction between two proteins so that a cell's own machinery degrades the target protein
* Protein complementation assay: an interaction-detection technique where a signal (e.g., enzyme activity) is only restored when two proteins bind
* Zinc-finger motif: a structural feature shared by most previously known CRBN-binding proteins
* Proteome: the complete set of proteins expressed by an organism
* Pomalidomide: a well-studied molecular glue drug that targets CRBN

**Why it is worth watching**

Molecular glue degraders are gaining rapid attention in cancer drug development because they can target proteins previously considered "undruggable." By mapping, at proteome scale, which proteins already have CRBN-compatible surfaces, this work substantially widens the pool of candidate targets available at the earliest stage of drug discovery.

---

## My take

이 연구는 개별 후보를 하나씩 실험하던 기존 방식에서 벗어나, 컴퓨터 기반 표면 유사성 탐색과 대규모 효모 검증을 결합해 프로테옴 전체를 체계적으로 스캔했다는 점에서 방법론적으로 견고해 보인다. 다만 검증이 CRBN-포말리도마이드 조합 한 가지에 국한되어 있고, 발견된 신규 결합 단백질이 실제 신약 표적으로 이어질지는 아직 미지수이며, 원문 전체를 확인하지 못해 정량적 세부사항은 검증하지 못했다.

The methodology is sound: combining computational surface-similarity search with large-scale experimental validation to scan an entire proteome is a meaningful step up from one-candidate-at-a-time approaches. That said, validation is limited to a single CRBN–pomalidomide pairing, whether the newly found binders translate into real drug targets is still open, and this summary could not confirm quantitative details from the full paper.
