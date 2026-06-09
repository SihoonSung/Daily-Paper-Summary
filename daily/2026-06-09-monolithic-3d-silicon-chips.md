---
title: "Monolithic three-dimensional integration of silicon transistors"
date: 2026-06-09
topic: semiconductors
tags: [semiconductors, chip-design, Moore's-law, 3D-integration, silicon, nanomembrane, fabrication, VLSI]
source: https://www.nature.com/articles/s41586-026-10496-6
---

# Monolithic three-dimensional integration of silicon transistors

* Date: 2026-05-28 (Nature)
* Source: https://www.nature.com/articles/s41586-026-10496-6
* Topic: Semiconductor Fabrication / Chip Design
* Why it matters: 트랜지스터 소형화(무어의 법칙)가 물리적 한계에 부딪힌 상황에서, 일리노이 대학교 연구팀이 고품질 단결정 실리콘을 저온(200°C 이하)에서 기존 회로 위에 직접 적층하는 방법을 처음으로 실증했다. IBM·인텔·TSMC가 참여하는 산학 협력 센터가 이 연구를 뒷받침하며, 수직 방향으로 트랜지스터 밀도를 높이는 실질적인 경로를 열었다는 점에서 반도체 업계 전반에 영향을 미칠 수 있는 결과다.

---

## Korean Summary

**한줄 요약**

무어의 법칙이 평면적 소형화의 한계에 봉착한 가운데, 일리노이 대학교 어바나-샴페인(UIUC) 연구팀이 두께 10 nm 이하의 초박형 단결정 실리콘 나노멤브레인을 200°C 이하의 저온 공정으로 기존 회로 위에 전사(transfer)·적층하는 방식을 통해, 대안 소재 대비 3~4배 높은 전류 밀도를 가지며 98~100% 수율을 보이는 3층 실리콘 트랜지스터 스택을 처음으로 실증했다.

**핵심 아이디어**

무어의 법칙은 수십 년간 트랜지스터를 더 작게 만드는 방식으로 컴퓨팅 성능을 향상시켜 왔지만, 트랜지스터 크기가 원자 몇 개 수준에 가까워지면서 양자 터널링 효과와 리소그래피 한계 등으로 평면적 소형화는 갈수록 어려워지고 있다. 이 논문의 핵심 아이디어는 "더 작게"가 아니라 "더 높이"다. 기존 회로 위에 실리콘 회로층을 직접 쌓는 모놀리식 3D 집적은 예전부터 제안된 개념이지만, 최대 장벽은 "열 예산(thermal budget)" 문제였다. 상단층을 만드는 공정 온도가 너무 높으면 이미 완성된 하단층의 금속 배선이 손상된다. 기존 연구들은 2D 소재나 산화물 반도체 등 대안 소재를 활용했지만 실리콘 대비 성능이 크게 떨어졌다. 이 연구는 도너(donor) 웨이퍼에서 미리 고품질로 형성한 초박형 단결정 실리콘 나노멤브레인을 물리적으로 분리해 롤러로 리시버(receiver) 기판에 전사하는 방식으로, 실리콘의 고품질을 유지하면서도 접합 형성이 필요 없는 무접합(junctionless) 트랜지스터 구조를 통해 공정 온도를 200°C 이하로 낮추는 데 성공했다.

**무엇이 새로운가?**

- 열 예산(≤200°C) 제약을 지키면서도 단결정 실리콘 트랜지스터만을 이용한 모놀리식 3D 집적을 최초로 실증
- 두께 10 nm 이하의 초박형 실리콘 나노멤브레인을 롤러로 전사하는 저온 공정 기술 개발
- 무접합(junctionless) 트랜지스터 구조를 채택해 고온 도핑 어닐링 공정 없이도 우수한 전기적 특성 확보
- 625개 트랜지스터로 구성된 3개 층을 98~100% 수율로 적층, 통상 실리콘 소자와 동등한 전류 밀도 달성
- 대안 소재 기반 모놀리식 소자 대비 전류 밀도가 3~4배 높아, 고성능 실리콘 트랜지스터가 3D 집적에 실용적임을 입증

**어떻게 작동하는가?**

1. **나노멤브레인 준비:** 도너 실리콘 웨이퍼에서 두께 10 nm 이하의 초박형 단결정 실리콘 나노멤브레인을 점착 테이프로 분리한다. 이 나노멤브레인은 도너 웨이퍼에서 고온으로 형성된 고품질 결정 구조를 그대로 유지한다.
2. **저온 전사:** 롤 라미네이터(roller-based roll laminator)를 사용해 나노멤브레인을 이미 회로가 완성된 리시버 기판(receiving substrate) 위에 200°C 이하의 온도에서 전사·접합한다. 이 온도는 하단층의 금속 배선(주로 구리)을 손상시키지 않는다.
3. **무접합 트랜지스터 제작:** 전사된 실리콘 나노멤브레인을 패터닝하여 무접합(junctionless) 트랜지스터를 제작한다. 무접합 구조는 p-n 접합 형성에 필요한 고온 어닐링 없이도 게이트 전계로 박막 채널의 전하를 제어함으로써 동작한다.
4. **반복 적층:** 1~3단계를 반복해 여러 층의 실리콘 회로층을 순차적으로 쌓는다. 이 연구에서는 층당 625개 트랜지스터로 구성된 3층 스택을 시연했다.
5. **특성 검증:** 각 층 트랜지스터의 전기적 특성(전류 밀도, 수율, 균일성)을 측정해 통상 공정 실리콘 소자 및 대안 소재 기반 모놀리식 소자와 비교했다.

**강점**

- 반도체 업계 표준인 단결정 실리콘을 사용해 기존 CMOS 제조 인프라와의 호환성이 높음
- 열 예산 제약을 충족하므로 이미 완성된 로직·메모리 회로 위에 추가 층을 직접 적층하는 시나리오가 현실적
- 98~100%에 달하는 높은 수율과 낮은 소자 변동성은 양산성 측면에서 긍정적 신호
- IBM·인텔·TSMC 등 주요 반도체 기업이 참여하는 산학 연구로, 공정 전환(foundry transfer)을 다음 단계로 준비 중
- 평면 소형화의 물리적 한계를 우회해 트랜지스터 밀도를 수직 방향으로 늘리는 구체적이고 확장 가능한 경로를 제시

**한계**

- 현재 시연은 3층 × 625개(층당) 트랜지스터라는 소규모 테스트 회로에 그치며, 상업용 집적회로 수준(수십억 개 트랜지스터)의 검증은 아직 이루어지지 않음
- 공정의 산업 이전(foundry transfer)은 준비 중이지만, 실제 양산 가능 여부와 시기는 미확정
- 무접합 트랜지스터는 일반 MOSFET 대비 도핑 농도, 채널 두께 등의 공정 제어에 민감하여 대면적 균일성 확보가 과제
- 논문에서는 625개 트랜지스터 수준의 소자 수율을 보고했지만, 억~조 개 규모의 집적 시 수율·균일성 유지 여부는 추가 연구가 필요
- 실리콘 나노멤브레인과 기판 사이의 계면(interface) 품질 및 기계적 신뢰성에 대한 장기 데이터가 아직 제한적

**알아둘 용어**

- **무어의 법칙 (Moore's Law):** 반도체 칩의 트랜지스터 수가 약 2년마다 2배로 증가한다는 경험칙. 현재는 소형화 한계 때문에 이 흐름이 둔화되고 있다.
- **모놀리식 3D 집적 (Monolithic 3D Integration, M3D):** 트랜지스터를 포함한 여러 층의 회로를 동일 기판 위에 순차적으로 직접 제작·적층하는 방식. 단순히 별도 제작된 칩을 이어 붙이는 2.5D/3D 패키징(칩렛 등)과 구별된다.
- **열 예산 (Thermal Budget):** 반도체 공정에서 온도와 시간의 조합. 이미 완성된 회로를 손상시키지 않으면서 새 층을 추가하기 위해 허용되는 최대 공정 온도·시간. 일반적으로 BEOL 단계에서 400°C 이하, 이 연구에서는 200°C 이하를 달성했다.
- **실리콘 나노멤브레인 (Silicon Nanomembrane):** 두께가 수 나노미터(이 연구에서는 10 nm 이하)에 불과한 초박형 단결정 실리콘 박막. 일반 웨이퍼(500~700 μm)에 비해 두께가 5만~7만 배 이상 얇다.
- **무접합 트랜지스터 (Junctionless Transistor):** p-n 접합 없이 얇은 반도체 채널 전체를 균일하게 도핑하고 게이트 전계로 채널 내 전하를 제어하는 트랜지스터. 고온 접합 형성 공정이 불필요해 저온 3D 집적에 유리하다.
- **BEOL (Back-End-Of-Line):** 반도체 제조 공정에서 트랜지스터 형성 이후 금속 배선을 형성하는 단계. 이 단계에서는 구리 등 금속 배선 손상을 막기 위해 낮은 열 예산이 요구된다.
- **전류 밀도 (Current Density):** 단위 폭(width)당 트랜지스터가 공급할 수 있는 전류량. 트랜지스터 성능의 핵심 지표 중 하나다.

**왜 주목할 만한가?**

반도체 산업은 수십 년간 트랜지스터를 더 작게 만드는 방식으로 성능을 높여왔지만, 이제 실리콘의 물리적 특성과 양자역학적 한계로 인해 평면 소형화의 한계에 다가서고 있다. 3D 집적은 오래전부터 대안으로 제시됐지만, 지금까지 고성능 실리콘 트랜지스터를 저온에서 적층하는 것은 불가능하거나 성능이 크게 떨어지는 대안 소재에 의존해야 했다. 이 연구는 업계 표준 소재인 단결정 실리콘으로 열 예산 제약을 지키면서도 실용적인 전류 밀도와 수율을 달성했다는 점에서 M3D 기술의 실현 가능성을 한 단계 높였다. IBM·인텔·TSMC의 참여와 파운드리 이전 계획은 단순한 학술 시연을 넘어 실제 제품화 경로를 염두에 둔 연구임을 시사한다.

---

## English Summary

**One-line summary**

A team at the University of Illinois Urbana-Champaign has demonstrated the first monolithic three-dimensional (3D) integration of high-performance single-crystalline silicon transistors that meets the thermal budget constraint of existing circuits, using ultrathin silicon nanomembranes transferred at temperatures no higher than 200 °C. Three stacked silicon layers, each containing 625 transistors, were fabricated with 98–100% device yield and current densities matching conventional bulk-silicon transistors — a result that opens a practical vertical path for extending Moore's Law when lateral transistor shrinking hits physical limits.

**Core idea**

Moore's Law has driven decades of computing progress by shrinking transistors, but as contacted gate pitch approaches fundamental limits imposed by quantum tunneling and lithography, planar scaling is slowing. The alternative is to build upward: stacking multiple layers of transistors monolithically on the same substrate. The central challenge has always been the thermal budget — the maximum process temperature and time that can be applied to a new layer without damaging the metal interconnects (mainly copper) of already-completed circuits below. Previous monolithic 3D attempts relied on alternative semiconductors (2D materials, amorphous/polycrystalline oxides) to avoid high-temperature crystallization steps, but those materials lag far behind silicon in carrier mobility and device performance. This paper's key insight is to separate material formation from device integration: form high-quality single-crystal silicon at high temperature on a dedicated donor wafer, then peel off ultrathin nanomembranes (<10 nm) and transfer them onto a completed receiver substrate at ≤200 °C using a roll laminator, preserving silicon's quality without any high-temperature step applied to existing circuits.

**What is new?**

- First reported monolithic 3D integration of silicon transistors (not alternative materials) that meets the BEOL-compatible thermal budget (≤200 °C)
- Transfer of ultrathin (<10 nm) single-crystalline silicon nanomembranes via a low-temperature roller-based process, preserving crystalline quality
- Use of junctionless transistors to avoid the high-temperature dopant-activation annealing needed for conventional p-n junction formation
- Three stacked silicon layers (625 transistors each) demonstrated with 98–100% yield and low variability
- Current densities comparable to standard bulk-silicon transistors and 3–4× higher than state-of-the-art alternative-material monolithic devices

**How does it work?**

1. **Nanomembrane preparation:** Ultrathin (<10 nm) single-crystalline silicon nanomembranes are peeled from a donor silicon wafer using adhesive tape. Because the donor wafer was fabricated at high temperature using standard processes, the nanomembranes retain high crystalline quality.
2. **Low-temperature transfer:** A roll laminator bonds the nanomembrane onto a receiver substrate — one that already carries completed circuitry — at temperatures ≤200 °C. This stays well within the thermal budget for back-end-of-line (BEOL) integration, avoiding damage to copper interconnects below.
3. **Junctionless transistor fabrication:** The transferred nanomembrane is patterned into junctionless transistors. Unlike conventional MOSFETs, junctionless transistors operate by depleting an uniformly doped thin semiconductor channel with a gate field, requiring no high-temperature p-n junction annealing.
4. **Sequential stacking:** Steps 1–3 are repeated to add further layers. The paper demonstrates three vertically stacked silicon circuit layers.
5. **Characterization:** Device yield, uniformity, and current density are measured and compared against conventional silicon transistors and best-in-class alternative-material monolithic devices.

**Strengths**

- Uses industry-standard single-crystalline silicon, maximizing compatibility with existing CMOS manufacturing infrastructure and reducing adoption barriers
- Meeting the ≤200 °C thermal budget makes it directly applicable to real integrated circuits without sacrificing performance layers below
- 98–100% device yield and low variability are promising signals for eventual manufacturability
- Backed by IBM, Intel, and TSMC through UIUC's CASCADE center, with foundry transfer as the stated next step — not a purely academic result
- Vertical stacking provides a concrete and scalable density-scaling path orthogonal to continued planar miniaturization

**Limitations**

- The demonstration is limited to 3 layers of 625 transistors each — far from the billions of transistors in commercial logic chips; scaling to full-chip complexity remains to be shown
- Foundry transfer is planned but not yet complete; actual manufacturability at scale is unconfirmed
- Junctionless transistors are sensitive to doping uniformity and nanomembrane thickness variation, which may be challenging to control over large wafer areas
- Long-term reliability data for the nanomembrane-substrate interface under electrical and thermal stress is not yet reported
- Interconnect density between stacked layers (vertical vias) and its impact on area and performance are not detailed in available coverage of the paper

**Terms to know**

- **Moore's Law:** The empirical observation that the number of transistors on a chip roughly doubles every two years. Planar transistor scaling is now slowing due to quantum-mechanical and lithographic limits.
- **Monolithic 3D Integration (M3D):** Sequential fabrication of multiple transistor layers directly on the same substrate, as opposed to bonding separately fabricated chips (chiplets, 3D packaging). Achieves far denser vertical connections.
- **Thermal Budget:** The combination of temperature and time a semiconductor process can apply to a wafer at a given fabrication stage. BEOL-compatible thermal budgets are typically ≤400 °C, and this work achieves ≤200 °C — a significantly tighter constraint.
- **Silicon Nanomembrane:** An ultrathin (<10 nm in this work) sheet of single-crystalline silicon, compared to a standard wafer's 500–700 μm thickness. Enables physical transfer at low temperature while preserving crystal quality.
- **Junctionless Transistor:** A transistor with no p-n junction, operating by electrostatically depleting a uniformly doped thin semiconductor channel. Avoids the high-temperature annealing required to activate dopants in conventional MOSFETs.
- **BEOL (Back-End-Of-Line):** The phase of chip fabrication in which metal interconnects are formed after transistors are completed. Low thermal budgets are required to protect copper wires already in place.
- **Contacted Gate Pitch:** The minimum center-to-center distance between neighboring transistor gates in a planar layout. It is one of the primary metrics of transistor density, and lateral scaling of this metric is nearing physical limits.

**Why it is worth watching**

The semiconductor roadmap has long anticipated that Moore's Law through lateral scaling will eventually stall — and by most measures that inflection is already underway, as the contacted gate pitch in leading-edge nodes is barely advancing. Monolithic 3D integration has been proposed for years as the natural next axis for density scaling, offering shorter vertical interconnects (better latency and power than chiplet-style 3D packaging) and fundamentally higher transistor density. But the field was stuck on the thermal budget problem: high-quality silicon couldn't be formed in place at low temperature. This paper breaks that deadlock by separating silicon quality from integration temperature. With near-perfect yields, silicon-competitive performance, and industry partners actively planning foundry transfer, this is one of the clearest signals yet that vertical stacking of silicon logic is moving from a research target toward an engineering program.

**My take**

한국어: 이 연구의 핵심 가치는 "실리콘으로, 저온에서, 높은 수율로"라는 세 조건을 동시에 충족했다는 점이다. 열 예산 문제는 반도체 업계가 오랫동안 머리를 싸매온 난제였으며, 그 해법이 기존 소재와 도구를 재조합한 비교적 우아한 방식(나노멤브레인 전사 + 무접합 트랜지스터)에서 나왔다는 점은 인상적이다. 다만 625개 트랜지스터 시연과 수십억 개 규모의 상업 칩 사이의 간극은 아직 크고, 파운드리 이전이 실제로 어떤 형태로 이루어질지는 지켜봐야 한다. IBM·인텔·TSMC가 이미 파트너로 참여한다는 사실은 이 연구가 단순 논문 이상의 산업적 맥락을 가진다는 강한 신호다.

English: The real value here is meeting all three constraints simultaneously — silicon, low temperature, near-perfect yield — which had not been achieved before. The thermal budget problem has been a long-standing barrier in the field, and the solution emerging from a relatively elegant combination of existing tools (nanomembrane transfer plus junctionless devices) is notable. The gap between a 625-transistor three-layer demo and a commercial logic chip with billions of transistors is still substantial, and the path through foundry transfer involves many unsolved engineering challenges. That said, the active involvement of IBM, Intel, and TSMC as partners is a strong indicator that this is being treated as an industrially serious program, not just a lab curiosity.
