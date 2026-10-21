---
title: "HOMARD: Hammering Off-chip Memory via Aggregate power Rail Disclosure"
date: 2026-10-21
topic: security
tags: [security, hardware, side-channel, dram, power-analysis, rowhammer]
source: https://arxiv.org/abs/2610.12621
---

# HOMARD: Hammering Off-chip Memory via Aggregate power Rail Disclosure

- Date: 2026-10-21
- Source: https://arxiv.org/abs/2610.12621
- Topic: Security (hardware side-channels)
- Why it matters: It shows that the on-chip power/energy sensors built into modern Arm SoCs (and similar monitors on other platforms) are precise enough to reconstruct DRAM address mappings and leak data-dependent memory contents without using timing at all, undercutting a whole generation of defenses that assume blocking precise timers is enough to stop these attacks.

## Korean Summary

**한줄 요약**

Daniel Gruss(그라츠 공대, Rowhammer·Meltdown 등 사이드채널 연구로 유명한 연구자)가 포함된 연구팀이 2026년 10월 8일 arXiv에 HOMARD 논문을 공개했다. 이 논문은 최신 Arm SoC 등에 내장된 저해상도(밀리초·밀리암페어 단위) 전력 센서만으로도 DRAM 주소 매핑을 역공학하고, 타이머 없이도 데이터 의존적 메모리 접근을 알아낼 수 있음을 보여준다.

**핵심 아이디어**

최근 몇 년간 많은 DRAM 사이드채널·Rowhammer 공격은 정밀한 타이머로 메모리 접근 시간을 측정하는 방식에 의존했고, 이에 대응해 운영체제·하드웨어 제조사들은 사용자 공간에서 고정밀 타이머에 대한 접근을 제한하는 방향으로 방어를 강화해 왔다. HOMARD는 이런 "타이머 차단" 방어를 무력화한다. 공격자가 칩에 이미 내장되어 있고 비특권 소프트웨어도 읽을 수 있는 전력/에너지 모니터링 센서의 값을 관찰하기만 해도, 메모리 접근 패턴에 따라 달라지는 전력 소비의 미세한 차이를 통해 같은 정보를 알아낼 수 있다는 것이다.

**무엇이 새로운가?**

- 타이밍이 아니라 내장 전력 센서를 정보 유출 경로로 사용하는 새로운 DRAM 사이드채널 공격 범주를 제시했다.
- HOMARD-RE: 전력 데이터만으로 DRAM 주소 매핑 함수(어떤 물리 주소가 어떤 뱅크/채널에 매핑되는지)를 역공학하는 기법.
- HOMARD-DATA: 상관 전력 분석(Correlation Power Analysis, CPA)을 이용해 캐시 라인의 해밍 웨이트(1비트의 개수)와 비밀 바이트 값을 전력 신호에서 복원하는 기법.
- Raspberry Pi 5뿐 아니라 AMD ZCU102, NVIDIA Jetson TX2 등 서로 다른 아키텍처·제조사의 보드에서도 공격이 통함을 보여, 특정 칩에 국한된 문제가 아님을 시사했다.
- 기존 방어(사용자 공간 고정밀 타이머 차단)가 이런 류의 공격에는 효과가 없다는 점을 실증적으로 드러냈다.

**어떻게 작동하는가?**

1. 공격자는 비특권 프로세스로서 SoC에 내장된 전력/에너지 모니터링 레지스터(원래는 전력 관리·열 관리 목적으로 제공됨)를 주기적으로 읽는다.
2. HOMARD-RE 단계에서는, 알고 있는 패턴으로 메모리를 반복 접근시키면서 전력 신호의 변화를 관찰해 물리 주소가 DRAM의 어느 뱅크/채널/로우에 매핑되는지 추론한다. (이는 Rowhammer 등 뱅크 충돌 기반 공격에 필요한 사전 정보다.)
3. HOMARD-DATA 단계에서는, 특정 캐시 라인을 반복적으로 적재(fetch)시키면서 그 순간의 전력 소비를 다수 샘플 수집하고, 상관 전력 분석 기법으로 데이터의 해밍 웨이트와 개별 바이트 값을 통계적으로 복원한다.
4. 실험에서는 Raspberry Pi 5 기준 9단계의 해밍 웨이트 값을 81.5% 정확도로 분류하는 데 성공했으며, 다른 보드(AMD ZCU102, NVIDIA Jetson TX2)에서도 유사한 방식이 적용됨을 보였다.

**강점**

- 저명한 사이드채널 연구자(Daniel Gruss)가 참여해 방법론적 신뢰도가 높다.
- 하나의 칩이 아니라 Arm 기반 SoC, AMD FPGA 보드, NVIDIA 임베디드 보드 등 여러 플랫폼에서 공격이 작동함을 보여 일반성을 입증했다.
- "타이머 차단만으로 DRAM 사이드채널을 막을 수 있다"는 업계의 암묵적 가정에 구체적 반례를 제시해, 방어 설계 방향을 재검토하게 만든다.
- 두 가지 독립된 공격 기법(주소 매핑 역공학, 데이터 복원)으로 공격의 범위를 체계적으로 보였다.

**한계**

- HOMARD-DATA의 81.5% 정확도는 9단계 해밍 웨이트 분류 기준으로, 완전한 바이트 값 복원의 실제 성공률이나 실환경 조건(잡음, 멀티태스킹 환경)에서의 성능은 추가 검증이 필요하다.
- 공격에는 비특권 상태에서라도 칩이 제공하는 전력 센서 레지스터에 접근 가능해야 하므로, 센서 접근을 제한하거나 해상도를 낮추는 플랫폼에서는 효과가 달라질 수 있다.
- 이 논문은 2026년 10월 8일 제출된 arXiv 프리프린트로, 동료 심사를 거친 학회 발표 여부나 정식 출판 여부는 이 요약 작성 시점에 확인되지 않았다.
- 전력 센서 접근을 완전히 차단하는 것이 실질적 완화책이 될 수 있는지, 그로 인한 전력/열 관리 기능 손실과의 트레이드오프는 논문에서 충분히 다뤄지지 않았을 수 있다.

**알아둘 용어**

- 사이드채널 공격(Side-channel attack): 프로그램이 다루는 데이터 자체가 아니라 실행 중 발생하는 부가적 물리 신호(시간, 전력, 전자기파 등)를 관찰해 비밀 정보를 추론하는 공격.
- 상관 전력 분석(Correlation Power Analysis, CPA): 암호 하드웨어 분석 등에 쓰이던 기법으로, 다수의 전력 소비 측정값과 가정한 데이터 값 사이의 통계적 상관관계를 이용해 비밀 값을 추정하는 방법.
- 해밍 웨이트(Hamming weight): 이진수에서 값이 1인 비트의 개수. 데이터 값에 따라 전력 소비가 달라지는 이유 중 하나다.
- DRAM 주소 매핑(DRAM address mapping): 운영체제가 보는 물리 주소를 실제 DRAM 칩의 뱅크·채널·로우·컬럼으로 변환하는 규칙으로, Rowhammer 등 공격에 필수적인 사전 지식이다.
- Rowhammer: DRAM의 특정 로우를 반복적으로 접근해 인접 로우의 데이터를 변형시키는 하드웨어 결함 기반 공격.
- SoC(System on Chip): CPU, 메모리 컨트롤러, 전력 관리 유닛 등을 하나의 칩에 통합한 시스템.

**왜 주목할 만한가?**

업계는 지난 몇 년간 사용자 공간에서 고정밀 타이머 접근을 제한하는 식으로 DRAM 타이밍 사이드채널에 대응해 왔다. HOMARD는 전력 센서라는, 애초에 보안 위협으로 간주되지 않았던 관리 기능이 동일한 수준의 정보를 유출할 수 있음을 보여줌으로써, "타이머만 막으면 된다"는 방어 전략 전체를 재검토하게 만든다. 이는 향후 SoC 설계와 운영체제 수준 방어 모두에서 전력/에너지 모니터링 인터페이스에 대한 접근 제어를 고려해야 함을 시사한다.

---

## English Summary

**One-line summary**

A research team including Daniel Gruss (Graz University of Technology, known for prior work on Rowhammer and Meltdown-class side channels) posted the HOMARD paper to arXiv on October 8, 2026. It shows that the coarse-grained (millisecond/milliamp-resolution) power sensors built into modern Arm SoCs are precise enough to reverse-engineer DRAM address mappings and recover data-dependent memory access information without using timers at all.

**Core idea**

Many recent DRAM side-channel and Rowhammer-style attacks have relied on precise timers to measure memory access latency, which pushed OS vendors and chipmakers to restrict userspace access to high-resolution timers as a defense. HOMARD shows that defense is insufficient: an attacker only needs to read the power/energy monitoring registers that are already built into the chip and accessible to unprivileged software, since memory access patterns cause small but measurable variations in power consumption that leak the same kind of information timers would have.

**What is new?**

- Introduces a new category of DRAM side-channel attack that uses built-in power sensors, not timing, as the leakage channel.
- HOMARD-RE: a technique to reverse-engineer DRAM address mapping functions (which physical addresses map to which bank/channel) purely from power measurements.
- HOMARD-DATA: a technique using Correlation Power Analysis (CPA) to recover the Hamming weight of a fetched cache line and individual secret byte values from the power signal.
- Demonstrates the attack across multiple, architecturally different platforms — Raspberry Pi 5, an AMD ZCU102 board, and an NVIDIA Jetson TX2 — suggesting the issue is not specific to a single chip.
- Empirically shows that existing defenses based on blocking high-resolution userspace timers do not stop this class of attack.

**How does it work?**

1. The attacker, running as an unprivileged process, periodically reads the SoC's built-in power/energy monitoring registers, which exist for power and thermal management purposes.
2. In the HOMARD-RE step, the attacker drives memory accesses in known patterns and observes the resulting changes in the power signal to infer which bank, channel, and row a given physical address maps to — information normally needed to mount bank-conflict attacks such as Rowhammer.
3. In the HOMARD-DATA step, the attacker repeatedly triggers fetches of a target cache line, collects many power samples around those fetches, and applies correlation power analysis to statistically recover the data's Hamming weight and individual byte values.
4. In experiments, HOMARD-DATA classified 9 Hamming-weight levels with 81.5% accuracy on a Raspberry Pi 5, and the authors report similar applicability on the AMD ZCU102 and NVIDIA Jetson TX2 boards.

**Strengths**

- Methodological credibility from the involvement of a well-known side-channel researcher (Daniel Gruss) with a track record in this space.
- Generality: the attack is shown to work across multiple platforms (an Arm-based SBC, an AMD FPGA board, and an NVIDIA embedded board), not just one chip.
- Provides a concrete counterexample to the implicit industry assumption that blocking precise timers is sufficient to stop DRAM side-channel attacks, which should prompt a rethink of defense strategy.
- Demonstrates two independent attack primitives (address-mapping recovery and data recovery), giving a fairly complete picture of what the channel can leak.

**Limitations**

- The reported 81.5% figure is for a 9-level Hamming-weight classification task, not full byte-value recovery; real-world accuracy under noisier or multitasking conditions needs further validation.
- The attack requires the chip to expose power-sensor registers to unprivileged software; platforms that restrict or coarsen access to these sensors may not be vulnerable in the same way.
- This is an arXiv preprint submitted October 8, 2026; at the time of this summary, independent peer review or formal publication status was not confirmed.
- The paper may not fully address the trade-offs of the most direct mitigation (restricting power-sensor access), such as the resulting loss of legitimate power/thermal management functionality.

**Terms to know**

- Side-channel attack: An attack that infers secret information from incidental physical signals produced during computation (timing, power, electromagnetic emissions) rather than from the data itself.
- Correlation Power Analysis (CPA): A technique, originally developed for attacking cryptographic hardware, that statistically correlates many power measurements with hypothesized data values to recover secrets.
- Hamming weight: The number of 1-bits in a binary value; one reason power consumption varies with the data being processed.
- DRAM address mapping: The rule that translates OS-visible physical addresses into actual DRAM bank/channel/row/column locations; prerequisite knowledge for attacks like Rowhammer.
- Rowhammer: A hardware-level DRAM fault-injection attack that repeatedly accesses a row to flip bits in physically adjacent rows.
- SoC (System on Chip): A chip integrating the CPU, memory controller, power management unit, and other components into a single package.

**Why it is worth watching**

For several years, the industry's main response to DRAM timing side-channels has been to restrict userspace access to high-resolution timers. HOMARD demonstrates that a different, previously-overlooked interface — built-in power monitoring meant for power/thermal management — can leak comparable information, which calls into question whether "block the timers" is a sufficient defense strategy at all. This points toward a need for SoC designers and OS-level defenses to also consider access control over power/energy monitoring interfaces going forward.

---

## My take

이 논문은 특정 소프트웨어 버그가 아니라 "방어의 범위를 잘못 설정했다"는 더 근본적인 문제를 짚는다는 점에서 가치가 있다. 전력 센서는 원래 보안과 무관한 관리 기능으로 설계되었는데, 이것이 타이머와 동등한 정보 유출 경로가 될 수 있다는 것은 향후 칩 설계 시 "비특권 소프트웨어가 읽을 수 있는 모든 내부 모니터링 인터페이스"를 보안 위협 모델에 포함시켜야 한다는 교훈을 준다. 다만 81.5%라는 수치는 해밍 웨이트 분류에 한정된 것이고 아직 동료 심사를 거치지 않은 프리프린트이므로, 실제 비밀 데이터 복원의 실용성은 후속 검증을 지켜볼 필요가 있다.

This paper is valuable less for pointing to a single software bug than for exposing a mis-scoped defense: power-monitoring registers, designed purely for power/thermal management, turn out to be an information-leakage channel on par with timers. The lesson for future chip design is that any internal monitoring interface readable by unprivileged software needs to be in the security threat model, not just timers. That said, the 81.5% figure is limited to Hamming-weight classification, and this is still an unreviewed preprint, so how practical full secret-data recovery is in real deployments remains to be seen.
