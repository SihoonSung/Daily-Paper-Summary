---
title: "Reconfigurable mmWave microchips co-integrating hBN switches on GaN"
date: 2026-10-10
topic: networking
tags: [networking, materials-science, 6g, memristor, gan, wireless-hardware]
source: https://www.nature.com/articles/s41586-026-10761-8
---

Reconfigurable mmWave microchips co-integrating hBN switches on GaN

- Date: 2026-10-10
- Source: https://www.nature.com/articles/s41586-026-10761-8
- Topic: networking (reconfigurable RF/mmWave hardware for 5G/6G)
- Why it matters: An international team (Tyndall National Institute, University College Cork, National University of Singapore, UTN.BA, KAUST) built working millimetre-wave communication circuits that co-integrate ultra-compact, non-volatile hexagonal boron nitride (hBN) memristor switches directly onto commercial gallium-nitride (GaN) chips — a concrete hardware step toward programmable, near-zero-standby-power RF front ends for 6G.

## Korean Summary

**한줄 요약**

Tyndall 국립연구소, 코크대학교(UCC), 싱가포르국립대학교(NUS) 등이 참여한 국제 연구팀이 2차원 소재인 육방정계 질화붕소(hBN) 기반 멤리스터 스위치를 상용 질화갈륨(GaN) 반도체 칩 위에 직접 집적해, 실제로 동작하는 밀리미터파(mmWave) 통신 회로를 구현했다. 이 연구는 2026년 Nature에 게재되었으며, 100 GHz까지의 주파수에서 동작이 확인되어 5G는 물론 6G 하드웨어에도 적용 가능성을 보였다.

**핵심 아이디어**

기존 RF(무선주파수) 스위치는 상태를 유지하기 위해 계속 전력을 소모하거나, 성능과 전력 효율을 동시에 만족시키기 어려웠다. 연구팀은 전압 펄스로 hBN 박막 내부에 나노미터 크기의 금속 필라멘트를 형성·제거함으로써 저항 상태를 바꾸는 비휘발성 멤리스터 스위치를 GaN 기반 밀리미터파 집적회로(MMIC) 위에 직접 쌓아 올렸다. 전원이 끊겨도 설정된 상태가 유지되기 때문에, 대기 전력을 거의 쓰지 않으면서도 회로의 동작 방식을 소프트웨어처럼 재구성할 수 있다.

**무엇이 새로운가?**

- hBN 멤리스터 스위치를 완성된 상용 GaN MMIC의 상부 배선층에 직접 집적해, 기존 트랜지스터 회로를 그대로 유지하면서 재구성 기능을 추가
- 각 hBN 스위치 소자의 크기가 2×2 마이크로미터에 불과할 정도로 초소형
- 최대 100 GHz 주파수까지 동작 확인, 삽입손실(insertion loss) 최저 0.3 dB(신호의 약 93%가 그대로 통과), 격리도(isolation) 15 dB 이상 달성
- 175°C의 고온에서도 온(on) 상태 저항이 안정적으로 유지되고, 2주간 상태 보존(retention) 확인
- 1-트랜지스터-1-멤리스터(1T1R) 구동 셀로 3,250회의 스위칭 내구성(endurance)을 실증하고, 이를 활용해 재구성 가능한 감쇠기(attenuator), 전력 분배기, 프로그래머블 공진기 등 실제 회로 구성 요소를 제작

**어떻게 작동하는가?**

1. 상용으로 제작된 GaN MMIC 웨이퍼를 준비하고, 기존 트랜지스터 회로 구조는 그대로 둔 채 상부 배선층에 hBN 멤리스터 스위치를 추가로 집적
2. 짧은 전압 펄스를 가해 hBN 박막 내부에 나노 스케일의 금(혹은 금속) 필라멘트를 형성하거나 끊어, 스위치의 저항 상태(온/오프)를 설정
3. 1-트랜지스터-1-멤리스터 구조의 구동 셀로 각 스위치를 개별 제어해, 외부 신호 없이도 설정된 상태를 비휘발적으로 유지
4. 이렇게 재구성 가능한 스위치들을 이용해 감쇠기, 전력 분배기, 공진기 등 밀리미터파 대역에서 동작하는 실제 RF 회로 블록을 구성
5. 주파수 응답(최대 100 GHz), 삽입손실, 격리도, 내구성, 고온 안정성 등을 측정해 상용 통신 하드웨어 적용 가능성을 검증

**강점**

- 실험실 단계의 소재 수준 검증을 넘어, 상용 GaN 공정 위에서 실제로 동작하는 완성된 RF 회로로 통합을 입증한 점이 실용적
- 비휘발성 특성으로 대기 전력이 거의 필요 없어, 전력 소모가 중요한 차세대 무선·위성 통신 하드웨어에 적합
- 소자 크기(2×2 μm)가 매우 작아 집적도가 높고, 100 GHz급 고주파에서도 낮은 삽입손실과 높은 격리도를 동시에 달성
- 아일랜드, 싱가포르, 아르헨티나, 사우디아라비아의 여러 기관이 협력한 국제 공동연구로, Nature에 게재되어 동료 평가를 통과

**한계**

- 3,250회의 스위칭 내구성은 상용 RF 스위치의 요구 수명(통상 수백만~수십억 회 수준)에 비해 현저히 낮아, 실제 제품화에는 추가적인 내구성 개선이 필요할 것으로 보임
- 2주간의 상태 보존 실험은 장기 신뢰성(수년 단위)을 보장하기에는 아직 짧은 검증 기간
- 현재 공개된 2차 보도 자료만으로는 전체 통신 시스템(송수신기, 안테나 등) 수준에서의 실증 여부는 명확하지 않으며, 논문 원문 확인이 필요
- 상용 파운드리에서의 대량 생산성, 수율, 공정 변동에 대한 영향은 아직 충분히 다뤄지지 않음

**알아둘 용어**

- 멤리스터(Memristor): 과거에 흐른 전류 이력에 따라 저항 상태가 바뀌고 그 상태를 유지하는 비휘발성 전자 소자
- 육방정계 질화붕소(hexagonal Boron Nitride, hBN): 그래핀과 유사한 층상 구조의 2차원 절연/반도체 소재로, 얇은 필름 형태로 소자에 활용
- 질화갈륨(Gallium Nitride, GaN): 고주파·고전력 RF 소자에 널리 쓰이는 와이드밴드갭 반도체 소재
- 밀리미터파 집적회로(mmWave MMIC): 수십~수백 GHz의 밀리미터파 대역에서 동작하도록 설계된 단일 칩 집적회로
- 삽입손실(Insertion Loss)·격리도(Isolation): 신호가 회로를 통과할 때 손실되는 정도(삽입손실)와, 스위치가 꺼졌을 때 신호를 얼마나 차단하는지(격리도)를 나타내는 RF 성능 지표
- 비휘발성(Non-volatile): 전원이 꺼져도 저장된 상태(설정값)가 그대로 유지되는 특성

**왜 주목할 만한가?**

6G를 비롯한 차세대 무선·위성 통신은 더 높은 주파수와 유연한 재구성 능력을 동시에 요구하지만, 이는 곧 전력 소모 증가로 이어지기 쉽다. 이 연구는 비휘발성 2차원 소재 스위치를 상용 GaN 공정에 직접 얹어, 대기 전력을 거의 쓰지 않으면서도 회로를 소프트웨어처럼 재구성할 수 있음을 실제 동작하는 칩으로 보여줬다는 점에서, 시뮬레이션이 아닌 하드웨어 수준의 구체적 진전이라 할 수 있다.

---

## English Summary

**One-line summary**

An international team led by researchers at Tyndall National Institute, University College Cork, and the National University of Singapore (with UTN.BA and KAUST) co-integrated ultra-compact, non-volatile hexagonal boron nitride (hBN) memristor switches directly onto commercial gallium-nitride (GaN) chips, demonstrating working millimetre-wave RF circuits. The work was published in Nature in 2026 and operates at frequencies up to 100 GHz, relevant to both 5G and future 6G hardware.

**Core idea**

Conventional RF switches struggle to combine low standby power with good high-frequency performance, since many designs require continuous power to hold a state. The team built non-volatile memristor switches from thin-film hBN, where a short voltage pulse forms or breaks a nanoscale metallic filament inside the material to set its resistance state, and stacked these switches directly onto the upper wiring layers of finished, commercially fabricated GaN mmWave integrated circuits (MMICs). Because the switch state persists without power, the resulting circuits can be reconfigured like software while consuming almost no standby energy.

**What is new?**

- First demonstration of hBN memristor switches co-integrated onto the upper metal layers of commercial GaN MMICs, leaving the underlying transistor circuitry untouched
- Individual hBN switch elements as small as 2×2 micrometres
- Verified operation up to 100 GHz, with insertion loss as low as 0.3 dB (roughly 93% of signal power passed through) and isolation better than 15 dB
- Stable on-state resistance at 175°C and state retention demonstrated over two weeks
- A one-transistor-one-memristor (1T1R) driver cell reaching 3,250 switching cycles, used to build real reconfigurable circuit blocks — attenuators, power dividers, and programmable resonators

**How does it work?**

1. Start from commercially fabricated GaN MMIC wafers, keeping the existing transistor circuitry intact
2. Add hBN memristor switches on the chip's upper wiring layers through additional back-end processing
3. Apply short voltage pulses to form or break nanoscale conductive filaments inside the hBN film, setting each switch's on/off resistance state
4. Control each switch individually with a 1T1R driver cell, which holds the set state non-volatilely without continuous power
5. Assemble these reconfigurable switches into mmWave-band RF building blocks (attenuators, power dividers, resonators) and measure frequency response (up to 100 GHz), insertion loss, isolation, endurance, and high-temperature stability

**Strengths**

- Moves beyond isolated materials-level demonstrations to show real RF circuit integration on a commercial GaN process
- Non-volatility means near-zero standby power, attractive for power-constrained next-generation wireless and satellite communication hardware
- Very small device footprint (2×2 μm) combined with low insertion loss and good isolation at frequencies up to 100 GHz
- International, peer-reviewed collaboration (Ireland, Singapore, Argentina, Saudi Arabia) published in Nature

**Limitations**

- The demonstrated 3,250-cycle switching endurance is far below the millions-to-billions of cycles typically required of commercial RF switches, so further durability work is likely needed before productization
- Two weeks of retention testing is still short relative to the multi-year reliability typically expected of deployed hardware
- Available secondary coverage does not make clear whether full system-level demonstrations (transceivers, antennas) were performed; this would need checking against the full paper
- Manufacturing yield, process variation, and scalability in commercial foundries are not yet well addressed in available summaries

**Terms to know**

- Memristor: a non-volatile electronic device whose resistance state depends on, and persists based on, its history of applied current/voltage
- Hexagonal boron nitride (hBN): a graphene-like layered 2D insulating/semiconducting material, used here as a thin switching film
- Gallium nitride (GaN): a wide-bandgap semiconductor material widely used for high-frequency, high-power RF devices
- mmWave MMIC: a monolithic microwave integrated circuit designed to operate at millimetre-wave frequencies (tens to hundreds of GHz)
- Insertion loss / isolation: RF performance metrics describing how much signal is lost passing through a circuit (insertion loss) and how well a switch blocks signal when off (isolation)
- Non-volatile: a property where a stored state persists even after power is removed

**Why it is worth watching**

Next-generation wireless and satellite links, including 6G, need both higher operating frequencies and flexible reconfigurability, which conventionally comes at the cost of higher power consumption. This work shows, in a working chip rather than simulation, that non-volatile 2D-material switches can be layered onto commercial GaN hardware to enable software-like reconfigurability with near-zero standby power — a concrete hardware step rather than a conceptual proposal.

---

## My take

이 연구는 2차원 소재 멤리스터를 실험실 샘플이 아니라 상용 GaN 공정 위에 직접 올려 실제 동작하는 RF 회로로 구현했다는 점에서 구체성이 돋보인다. 다만 공개된 2차 보도 자료 수준에서는 스위칭 내구성(3,250회)이 상용 요구 수준에 비해 낮게 보이고, 전체 통신 시스템 단위의 검증 여부도 불분명해, 실제 상용화까지는 추가적인 신뢰성 검증이 필요해 보인다.

This work stands out for demonstrating 2D-material memristors integrated directly onto a commercial GaN process as a working RF circuit, rather than an isolated lab sample. That said, based on available secondary coverage, the reported switching endurance (3,250 cycles) looks low relative to commercial RF switch requirements, and it's unclear whether full system-level validation was performed — additional reliability work would likely be needed before this moves toward real deployment.
