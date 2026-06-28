---
title: "IBM NanoStack: World's First Sub-1 Nanometer Chip Technology"
date: 2026-06-28
topic: semiconductor
tags: [semiconductor, chip-design, Moore's-law, CFET, 3D-stacking, transistors, VLSI, fabrication, nanostack, IBM]
source: https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology
---

# IBM NanoStack: World's First Sub-1 Nanometer Chip Technology

* Date: 2026-06-25
* Source: https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology
* Topic: Semiconductor / Chip Architecture
* Why it matters: IBM가 2026년 6월 25일 VLSI 심포지엄에서 세계 최초 1nm 이하 칩 기술인 NanoStack(0.7nm)을 공개했다. NFET과 PFET 트랜지스터를 수직으로 쌓는 3D CFET 방식으로 2nm 대비 50% 성능 향상 또는 70% 전력 절감을 달성하며, AI 가속기 성능을 현재의 5배 수준(7,000 TOPS)으로 높일 수 있는 잠재력을 제시해 무어의 법칙 연장에 새로운 경로를 열었다.

---

## Korean Summary

**한줄 요약**

IBM이 2026년 6월 VLSI 심포지엄에서 0.7nm(7옹스트롬) 공정 노드 기반 NanoStack 아키텍처를 공개하며 세계 최초 1nm 미만 칩 기술을 선보였다. NFET과 PFET 트랜지스터를 z축으로 적층하는 3D 스태거드(staggered) CFET 방식으로 단일 공정 내 트랜지스터 밀도를 획기적으로 높였으며, 손톱 크기 칩에 약 1,000억 개의 트랜지스터를 집적하고 기존 2nm 대비 50% 높은 성능 또는 70% 낮은 전력 소비를 달성했다.

**핵심 아이디어**

반도체 업계는 수십 년간 트랜지스터를 더 작게 만드는 2D 평면 소형화(무어의 법칙)로 성능을 높여왔지만, 이제 물리적·리소그래피 한계에 직면해 수평적 확장은 갈수록 어려워지고 있다. NanoStack의 핵심은 "더 작게"가 아니라 "더 높이(z축)" 방향으로의 전환이다. 기존 트랜지스터 배치에서 NFET과 PFET은 같은 평면에 나란히 놓여 상당한 수평 공간을 차지한다. NanoStack은 PFET을 NFET 바로 위에 쌓아 이 수평 간격을 얇은 수직 접합 유전체(bonding dielectric)로 대체하며, 동일한 리소그래피 패터닝 능력을 유지하면서 트랜지스터 밀도를 두 배 수준으로 높인다. 상·하층이 서로 다른 반도체 채널 소재를 사용할 수 있어 NFET(실리콘)과 PFET(실리콘-게르마늄 또는 기타 소재)의 전자·정공 이동도를 각각 독립적으로 최적화할 수 있다는 것도 주요 강점이다.

**무엇이 새로운가?**

- **세계 최초 1nm 미만 칩 기술 실증**: 0.7nm(7옹스트롬) 공정 노드를 구현하여 기존 업계 로드맵상의 1nm 장벽을 처음으로 넘은 집적회로 기술 발표
- **3D 스태거드 CFET(Complementary FET) 아키텍처**: NFET을 하단, PFET을 상단에 수직 적층하여 N-P 수평 간격 제약을 제거하고 동일 리소그래피로 약 50% 로직 면적 절감
- **이중 채널 소재 독립 최적화**: 상하층에 서로 다른 반도체 채널 소재를 사용해 NFET(고전자 이동도)과 PFET(고정공 이동도)를 각각 최적화하는 이중 채널 엔지니어링 최초 실증
- **VLSI 2026 SRAM 40% 축소**: Zhang 등이 VLSI 2026에 발표한 논문에서 NanoStack 기반 SRAM 셀 높이를 최신 비적층 셀 대비 40% 이상 줄여 10년 이상 만의 최대 SRAM 스케일링 개선을 달성
- **AI 가속기 5배 성능 잠재력**: 현재 AI 가속기 수준인 1,500 TOPS에서 7,000 TOPS로의 향상을 전망하며, LLM 학습 시간을 현재 3개월에서 2주로 단축할 가능성을 제시

**어떻게 작동하는가?**

1. **CFET 수직 적층**: 기존 평면형 GAA(Gate-All-Around) 트랜지스터 배치에서 NFET과 PFET은 같은 레이어에 나란히 위치해 수평 공간을 점유한다. NanoStack은 NFET을 하단, PFET을 상단에 쌓아(z축) 두 소자 사이를 얇은 절연 접합층(dielectric bonding layer)으로 연결한다. 이로써 수평 방향 N-P 간격이 사라지고 동일 레이아웃 면적에 두 배 가량의 트랜지스터를 배치할 수 있다.
2. **초박형 유전체 웨이퍼 접합**: 상단 층을 하단 층 위에 붙이기 위해 결함이 거의 없는 극히 얇은 유전체 접합층을 사용한다. IBM 연구팀이 VLSI 2026에서 이 기술의 신뢰성과 낮은 결함 밀도를 실증했다.
3. **이중 채널 소재 엔지니어링**: NFET층에는 실리콘(전자 이동도 우수), PFET층에는 실리콘-게르마늄 또는 대안 소재(정공 이동도 우수)를 독립 적용하여 각 소자의 전기적 성능을 별도 최적화한다. SRAM의 경우 읽기/쓰기 마진을 로직과 독립적으로 튜닝할 수 있어 저전압 동작에도 유리하다.
4. **동일 패터닝 내 밀도 향상**: 수평 소형화가 아닌 z축 적층으로 밀도를 높이기 때문에, 현재 양산 중인 EUV 리소그래피 장비로도 구현 가능하다. IBM은 이미 2025년부터 테스트 웨이퍼 생산을 시작했다.
5. **독립 트랜지스터 최적화**: 각 층의 트랜지스터가 독립적으로 최적화되므로, 로직 소자와 SRAM 소자를 같은 칩에서 서로 다른 동작 전압과 성능 특성으로 설계할 수 있다.

**강점**

- 수평 소형화의 물리적 한계를 z축 적층으로 우회하여 무어의 법칙 연장에 실질적인 경로를 제시
- 50% 로직 스케일링, 40% SRAM 스케일링으로 기존 2nm 대비 획기적 밀도 향상
- 현재 EUV 리소그래피 패터닝 능력 내에서 구현 가능하여 제조 인프라 호환성 확보
- NFET/PFET 독립 소재 최적화로 로직·메모리 모두에서 전력 효율 개선
- 2nm 대비 50% 성능 향상 또는 70% 전력 절감으로 AI 칩 수요 대응 가능
- AI 가속기 TOPS 최대 5배, LLM 학습 속도 약 6배 향상 전망

**한계**

- IBM은 자체 반도체 생산 공장이 없어 양산은 삼성·인텔 등 외부 파운드리와의 협력 필요
- 실험실 실증 단계이며 고속 양산까지는 통상 5~10년 소요 예상 — IBM은 최초 상업 도입을 약 5년 후로 전망
- 상하층 접합 유전체의 장기 신뢰성 및 전기적 특성 변동성은 추가 검증 필요
- 칩 설계 도구(EDA)와 제조 공정 모두를 3D 스택 아키텍처에 맞게 업데이트해야 하는 소프트웨어·공정 복잡도 증가
- 동일 공정 온도 관리, 상하층 정렬 정밀도 등 제조 난이도가 기존 2D 공정보다 현저히 높음
- Intel, Samsung, TSMC, IMEC 등이 유사한 순차형 CFET 아키텍처를 별도로 개발 중으로, IBM이 최종 양산 우선권을 갖는다는 보장 없음

**알아둘 용어**

- **CFET(Complementary FET, 상보형 전계 효과 트랜지스터)**: NFET과 PFET을 수직으로 쌓아 면적 효율을 극대화한 차세대 트랜지스터 구조. 기존 FinFET이나 GAA(나노시트) 이후의 다음 단계로 꼽힌다.
- **GAA(Gate-All-Around, 게이트 올-어라운드)**: 채널 사면이 게이트로 둘러싸인 나노시트/나노와이어 트랜지스터 구조. TSMC 2nm, Samsung SF3 등 현재 최첨단 공정에서 채택.
- **공정 노드(Process Node)**: 칩 제조 세대를 나타내는 명칭(nm). 현재의 "nm" 수치는 물리적 게이트 길이보다는 마케팅·밀도 지표에 가깝다. 0.7nm = 7옹스트롬.
- **SRAM(Static Random Access Memory, 정적 RAM)**: 칩 내부에 캐시 메모리로 사용되는 고속 온칩 메모리. 셀 크기가 작을수록 같은 면적에 더 많은 캐시를 집적할 수 있어 성능에 직접 영향.
- **EUV 리소그래피(Extreme Ultraviolet Lithography, 극자외선 리소그래피)**: ASML의 13.5nm 파장 EUV 광원으로 초미세 회로를 웨이퍼에 새기는 최신 노광 기술. 현재 최첨단 반도체 패터닝의 핵심.
- **TOPS(Tera Operations Per Second, 초당 조 연산 횟수)**: AI 가속기의 처리 성능 단위. 값이 높을수록 딥러닝 추론·학습 처리 속도가 빠르다.
- **무어의 법칙(Moore's Law)**: 1965년 고든 무어가 제시한 경험적 법칙으로, 집적회로의 트랜지스터 수가 약 2년마다 2배로 늘어난다는 관측. 현재는 물리적 한계로 속도가 느려지고 있으며, 3D 적층은 이를 극복하는 대안 경로 중 하나다.

**왜 주목할 만한가?**

반도체 업계의 무어의 법칙은 수평 소형화의 한계에 봉착해 있다. 0.7nm 공정은 원자 몇 개 수준의 구조를 다루며, 이 영역에서는 양자 터널링 등 물리적 효과가 트랜지스터 동작을 방해한다. IBM NanoStack은 수평이 아닌 수직(z축)으로의 전환을 통해 같은 패터닝 기술로 밀도를 약 두 배로 높이는 실질적인 해법을 제시했다. AI 모델의 규모가 기하급수적으로 커지면서 AI 칩의 성능·전력 효율 개선 수요가 절박한 시점에, 10년 이상 만의 최대 SRAM 스케일링을 포함한 이번 결과는 업계 전반에 z축 집적 로드맵을 구체화할 중요한 이정표가 된다.

---

## English Summary

**One-line summary**

On June 25, 2026, IBM unveiled NanoStack — the world's first sub-1 nanometer chip technology — at the VLSI Symposium, using a staggered sequential CFET architecture that stacks NFET and PFET transistors vertically on the z-axis. The 0.7 nm node packs approximately 100 billion transistors onto a fingernail-sized chip with up to 50% higher performance or 70% greater energy efficiency than IBM's 2 nm node, and projects AI accelerator throughput improvements from 1,500 to 7,000 TOPS.

**Core idea**

Moore's Law — the observation that transistor density roughly doubles every two years through planar scaling — is running into fundamental physical limits: at sub-1 nm dimensions, quantum tunneling, lithography resolution, and atomic-scale variability all constrain further horizontal shrinking. IBM NanoStack's answer is to scale vertically rather than horizontally. In conventional transistor layouts, NFET and PFET devices sit side by side in the same plane, occupying significant horizontal area. NanoStack stacks the PFET directly on top of the NFET, replacing the lateral N-P spacing with a thin vertical bonding dielectric, effectively doubling transistor density within today's lithography capability. Each stacked layer can use a different semiconductor channel material, allowing independent optimization of electron mobility (NFET layer, typically silicon) and hole mobility (PFET layer, silicon-germanium or alternatives) — something impossible in a single planar layout.

**What is new?**

- **World's first sub-1 nm chip technology**: IBM demonstrated functional devices at the 0.7 nm (7 Angstrom) process node, crossing the 1 nm barrier for the first time in a semiconductor research context
- **Staggered sequential CFET architecture**: NFET stacked directly beneath PFET, connected by an ultra-thin dielectric bonding layer, eliminating the N-P lateral spacing constraint and achieving ~50% logic area reduction within current patterning capabilities
- **Dual-channel material engineering**: Independent channel material selection per layer allows NFET (silicon, high electron mobility) and PFET (silicon-germanium or alternatives, high hole mobility) to each be optimized separately — the first demonstration of this technique in a stacked CFET structure
- **40% SRAM cell-height reduction (VLSI 2026)**: A paper by Chen Zhang et al. at VLSI 2026 demonstrated over 40% reduction in SRAM cell height versus state-of-the-art non-stacked cells — the largest SRAM scaling improvement in more than a decade
- **AI accelerator roadmap impact**: IBM projects NanoStack-class chips could enable 7,000 TOPS AI accelerators (versus ~1,500 TOPS today) and cut LLM training times from roughly three months to two weeks

**How does it work?**

1. **CFET vertical stacking**: Rather than placing NFET and PFET side by side in the same plane, the N device is built first, then the P device is stacked directly on top of it, separated by a thin dielectric bonding layer. This removes the horizontal N-P spacing constraint that limits traditional layout density.
2. **Ultra-thin dielectric wafer bonding**: A critical manufacturing challenge is joining the two layers with a bonding dielectric thin enough that it does not degrade transistor performance. IBM's VLSI 2026 results demonstrated low-defect ultra-thin bonding interfaces with acceptable electrical characteristics.
3. **Dual-channel material engineering**: Because the N and P layers are built sequentially and independently, each can use a different channel semiconductor. Silicon handles electron transport well; silicon-germanium or other III-V alternatives can improve hole transport in the PFET layer. This independent optimization was not feasible in co-planar designs.
4. **Patterning within existing EUV capability**: Because the density gain comes from z-axis stacking rather than shrinking feature sizes in x/y, NanoStack can in principle achieve its density improvement using the same EUV lithography tools already in production — a key practical advantage over approaches that require next-generation patterning.
5. **Independent logic/memory tuning**: SRAM cells built with stacked transistors can tune read/write margins independently from logic, enabling lower-voltage operation for improved energy efficiency while maintaining the performance needed for cache access.

**Strengths**

- Provides a concrete path to extend Moore's Law via z-axis scaling when horizontal shrinkage approaches atomic limits
- 50% logic scaling and 40% SRAM scaling versus 2 nm represent among the largest density gains in the industry in a decade
- Compatible with existing EUV lithography infrastructure — no requirement for next-generation patterning tools
- Independent N/P channel material optimization unlocks transistor performance gains not achievable in conventional planar layouts
- Up to 50% higher performance or 70% greater energy efficiency versus IBM's 2 nm node at the system level
- Demonstrated functional CMOS inverter operation validates that basic building blocks work as expected
- VLSI 2026 SRAM results are peer-reviewed and provide quantitative validation

**Limitations**

- IBM no longer operates its own fabs; commercial manufacturing will require partnerships with foundries such as Samsung or Intel, adding technology transfer risk
- This is a research demonstration: typical lab-to-production timelines in semiconductors are 5–10 years, and IBM projects earliest commercial adoption around 2031
- Long-term reliability of the bonding dielectric interface and its electrical stability across temperature cycles require further validation
- Chip design tools (EDA software) and full process design kits (PDKs) for stacked CFET are immature — the full software ecosystem must be rebuilt for 3D architectures
- Manufacturing complexity increases significantly: aligning two stacked layers to atomic precision and managing thermal budgets during sequential processing introduce new yield challenges
- Intel, Samsung, TSMC, and IMEC are independently developing similar sequential CFET or stacked transistor approaches; IBM's research leadership does not guarantee it will be first to volume production

**Terms to know**

- **CFET (Complementary FET)**: A transistor architecture that stacks NFET and PFET vertically rather than placing them side by side, dramatically increasing transistor density. Considered the successor to GAA (Gate-All-Around) nanosheet transistors.
- **GAA (Gate-All-Around)**: A transistor design where the gate electrode surrounds all four sides of the channel, improving electrostatic control versus FinFET. Used in TSMC 2 nm and Samsung SF3 — the current leading-edge production nodes.
- **Process node**: The generation label for a semiconductor manufacturing process (e.g., 2 nm, 0.7 nm). Modern "nm" numbers are density and marketing metrics rather than literal physical gate lengths.
- **SRAM (Static RAM)**: High-speed on-chip cache memory fundamental to processor performance. Smaller SRAM cells allow more cache capacity at the same die area, directly improving processor speed.
- **EUV lithography**: The current leading-edge chip patterning technology, using 13.5 nm extreme ultraviolet light to etch features onto silicon wafers. All leading-edge nodes below ~7 nm require EUV.
- **TOPS (Tera Operations Per Second)**: Standard throughput metric for AI accelerators. IBM's projection of 7,000 TOPS represents approximately a 5× improvement over today's leading AI chips.
- **Moore's Law**: Gordon Moore's 1965 observation that transistor count roughly doubles every two years. The rate has slowed significantly as physical limits constrain planar scaling; 3D stacking is one approach to continuing the effective density doubling.

**Why it is worth watching**

AI model size has grown roughly 10× per year, and the computational demand for training and inference is outpacing current chip scaling rates. At the same time, the semiconductor roadmap faces a genuine impasse: below ~1 nm, conventional planar transistor shrinkage is physically difficult and increasingly impractical. IBM NanoStack addresses both pressures directly: it offers the largest SRAM scaling leap in over a decade using today's lithography infrastructure, and it opens a concrete z-axis roadmap for the next decade of density improvements. If the approach successfully transfers to volume manufacturing, it could sustain the cost-per-computation improvements that the AI industry currently takes for granted. The 5-year commercial timeline is long but not unusual for semiconductor research, and the fact that multiple industry players (IMEC, Intel, Samsung, TSMC) are independently pursuing similar stacked CFET approaches validates that this architectural direction is broadly accepted as the next node beyond GAA.

**My take**

NanoStack는 연구 발표이지만 그 의의는 크다. 무어의 법칙을 수평이 아닌 수직으로 연장하겠다는 방향성은 업계 컨센서스가 되어가고 있으며, IBM이 VLSI 2026에서 정량적 SRAM 결과를 공개했다는 점은 단순한 개념 발표가 아니라는 신뢰성을 준다. 다만 IBM 자체 팹이 없다는 사실은 결정적 약점이다. TSMC, Samsung, Intel 모두 유사한 CFET 연구를 진행 중이며, 이들은 제조 인프라까지 보유하고 있어 상업 양산 레이스에서는 IBM의 연구 우위가 그대로 이어지지 않을 가능성이 높다.

NanoStack is an impressive research milestone with quantitative backing — the VLSI 2026 SRAM result is hard to dismiss. But the gap between IBM's lab and a commercial fab is substantial: IBM stopped manufacturing its own chips years ago, so this architecture will only reach products if a major foundry licenses and executes it. Given that TSMC, Samsung, and Intel are all developing their own stacked-transistor roadmaps with full manufacturing control, the more likely outcome is that IBM's NanoStack accelerates the industry's collective movement toward CFET without IBM necessarily being the company that ships the first products at scale. Either way, the direction is clearly right, and the timeline is earlier than many had expected.
