---
title: "Hybrid bioprinting of hierarchical vascular networks at capillary-scale resolution"
date: 2026-08-13
topic: biotech
tags: [biotech, bioprinting, tissue-engineering, vascularization, regenerative-medicine, machine-learning, additive-manufacturing]
source: https://www.nature.com/articles/s44286-026-00396-x
---

Hybrid bioprinting of hierarchical vascular networks at capillary-scale resolution

* Date: 2026-08-13
* Source: https://www.nature.com/articles/s44286-026-00396-x
* Topic: Biotech / Bioprinting & Tissue Engineering
* Why it matters: Bioprinted tissue constructs typically die from the inside out because oxygen and nutrients cannot diffuse far enough to reach interior cells without a built-in blood-vessel network; this work combines two printing methods with machine-learning-guided control to print branching vascular channels down to true capillary scale (under 10 micrometers) inside a single construct, and lines them with living cells.

## Korean Summary

**한줄 요약**

노터데임대학교(University of Notre Dame)의 Yanliang Zhang 교수 연구팀이 하버드 의과대학·브리검여성병원의 Y. Shrike Zhang 교수팀과 공동으로, 압출(extrusion) 프린팅과 에어로졸젯 프린팅(aerosol jet printing, AJP)을 결합하고 머신러닝으로 인쇄 조건을 자동 최적화하는 하이브리드 바이오프린팅 기법을 개발해 Nature Chemical Engineering에 발표했다. 이 기법은 사람 모발보다 가는 10마이크로미터 이하 굵기의 모세혈관 수준 채널을 인쇄해 살아있는 세포로 내벽을 덮는 데 성공했다.

**핵심 아이디어**

조직공학에서 세포를 3D로 인쇄해 조직이나 장기를 만들 때 가장 큰 걸림돌은, 배양액이나 주변 조직에서 산소와 영양분이 확산으로 도달할 수 있는 거리가 제한적이어서(대략 수백 마이크로미터 이내) 두꺼운 구조물 내부의 세포가 죽어버린다는 점이다. 실제 인체 조직은 굵은 혈관에서 모세혈관까지 계층적으로 가지치는 혈관망을 통해 이 문제를 해결한다. 이 연구는 서로 다른 두 가지 프린팅 기술의 장점(압출 프린팅의 구조 형성 능력과 AJP의 미세 해상도)을 결합하고, 머신러닝으로 각 혈관 형상에 맞는 인쇄 변수를 자동으로 찾아냄으로써, 굵은 혈관부터 모세혈관까지 이어지는 계층적 혈관망을 한 번에 인쇄하는 것을 목표로 한다.

**무엇이 새로운가?**

* 압출 프린팅(젤 형태의 조직 모사 매트릭스를 층층이 쌓는 방식)과 에어로졸젯 프린팅(젤라틴 희생 섬유를 매트릭스 내부에 미세하게 배치하는 방식)을 하나의 공정으로 결합한 하이브리드 바이오프린팅 전략
* 머신러닝을 이용해 원하는 혈관 형상마다 인쇄 조건을 사람이 일일이 조정하지 않고 자동으로 최적화
* 채널 굵기 10마이크로미터 미만, 일부는 5~6마이크로미터까지 달성 — 실제 인체 모세혈관과 비슷한 수준이며 사람 머리카락보다도 가늚
* 1차원·2차원·3차원 형태의 안정적인 혈관 구조물을 모두 구현
* 인쇄된 채널 내부에 살아있는 내피세포를 배양해 내벽을 형성(내피화, endothelialization)하는 데 성공

**어떻게 작동하는가?**

먼저 조직과 비슷한 부드러운 젤 형태의 매트릭스를, 압력으로 재료를 밀어내는 압출 프린팅 방식으로 한 층씩 쌓아 올린다. 매트릭스의 한 구간이 인쇄될 때마다, 에어로졸젯 프린팅으로 가느다란 젤라틴 실을 매트릭스 내부의 정해진 위치에 미세하게 증착한다. 이 젤라틴 실은 나중에 제거되어 속이 빈 채널(관)로 남을 "희생 재료" 역할을 한다. 전체 구조물의 인쇄가 끝나면 따뜻한 물에 담가 젤라틴을 녹여 씻어내는데, 그 결과 매트릭스 안에는 정교하게 배치된 빈 채널망만 남는다. 이 과정에서 머신러닝 모델이 원하는 혈관 형상(굵기, 분기 구조 등)에 맞춰 AJP의 인쇄 변수를 자동으로 조정해, 사람이 매번 시행착오로 조건을 맞출 필요를 줄인다. 완성된 채널에는 살아있는 내피세포를 흘려 넣어 벽면에 부착·증식시킴으로써, 실제 혈관과 유사하게 내벽이 세포로 덮인 구조를 만든다.

**강점**

* 두 프린팅 기술을 결합해 굵은 구조와 미세 구조를 한 공정 안에서 함께 구현
* 모세혈관 수준(10마이크로미터 미만)의 해상도를 달성했다고 보고된 점이 조직공학 분야에서 특히 의미가 큼
* 머신러닝 기반 자동 최적화로 다양한 혈관 형상에 대한 재현성과 확장성을 높일 잠재력
* 채널에 실제 살아있는 세포를 입혀 단순한 빈 관이 아니라 생물학적 혈관에 가까운 구조를 시연

**한계**

* 현재까지는 실험실 수준의 시연으로, 두껍고 기능적인 조직·장기 구조물 전체에 이 혈관망을 적용해 실제로 세포 생존율을 높였는지에 대한 구체적 데이터는 2차 보도 자료만으로는 확인하기 어려움
* 생리적 압력 하에서의 실제 혈류 관류(perfusion), 장기간 채널 개통 유지, 숙주 혈관과의 문합(anastomosis) 등 생체 내(in vivo) 검증 여부는 명확히 확인되지 않음
* 머신러닝 최적화가 특정 재료·프린터 조합에 맞춰진 것인지, 다른 바이오잉크나 장비로 일반화될 수 있는지는 불명확
* 이 세션은 네트워크 접근이 제한되어 논문 원문에 직접 접근하지 못했으며, 저널 목록 정보와 노터데임대학교 보도자료, 3D 프린팅 전문 매체 등 2차 보도에 근거해 작성됨

**알아둘 용어**

* 바이오프린팅(bioprinting): 세포와 생체적합성 소재를 3D 프린터로 층층이 쌓아 조직 유사 구조물을 만드는 기술
* 압출 프린팅(extrusion printing): 압력으로 재료를 노즐 밖으로 밀어내며 인쇄하는 3D 프린팅 방식
* 에어로졸젯 프린팅(aerosol jet printing, AJP): 재료를 미세한 에어로졸 입자로 만들어 매우 가는 선폭으로 증착하는 정밀 인쇄 기술
* 희생 재료(sacrificial material): 인쇄 후 제거되어 빈 공간(채널 등)을 남기기 위해 임시로 사용하는 재료(이 연구에서는 젤라틴)
* 내피화(endothelialization): 혈관 안쪽 벽에 내피세포가 자리 잡아 실제 혈관과 유사한 세포층을 형성하는 과정
* 관류(perfusion): 혈관이나 채널을 통해 액체(혈액 등)가 실제로 흐르며 조직에 산소·영양분을 공급하는 현상
* 계층적 혈관망(hierarchical vascular network): 굵은 혈관에서 점점 가늘어지는 모세혈관까지 가지치듯 이어지는 혈관 구조

**왜 주목할 만한가?**

두꺼운 조직이나 장기를 인쇄해도 내부 세포까지 산소와 영양분을 공급할 방법이 없다는 점은 바이오프린팅이 실제 이식 가능한 조직·장기로 나아가는 데 가장 큰 장벽 중 하나로 꼽혀 왔다. 이 연구는 완전히 새로운 재료를 발명하지 않고도, 서로 다른 두 프린팅 기술과 머신러닝을 조합해 모세혈관 수준의 해상도에 도달했다는 점에서, 향후 실제로 기능하는 관류 가능한 조직 모델이나 이식용 조직으로 발전할 수 있는 실용적인 경로를 제시한다.

---

## English Summary

**One-line summary**

A team led by Yanliang Zhang at the University of Notre Dame, working with Y. Shrike Zhang at Harvard Medical School and Brigham and Women's Hospital, developed a hybrid bioprinting method that combines extrusion printing with aerosol jet printing (AJP) and uses machine learning to automatically tune print parameters, published in Nature Chemical Engineering. The method prints branching vascular channels finer than a human hair — under 10 micrometers in diameter — and lines them with living cells.

**Core idea**

A central obstacle in 3D-printing tissues and organs is that oxygen and nutrients can only diffuse a limited distance (roughly hundreds of micrometers) from a culture medium or surrounding tissue, so cells deep inside a thick printed construct die without an internal supply network. Real human tissue solves this with a hierarchical vascular network that branches from large vessels down to capillaries. This work combines the complementary strengths of two printing techniques — extrusion printing for building structure and AJP for fine resolution — and uses machine learning to automatically find the right print settings for each desired vascular shape, aiming to print that full hierarchy, from larger vessels down to capillary scale, in a single construct.

**What is new?**

* A hybrid bioprinting strategy that combines extrusion printing (layer-by-layer deposition of a gel-like tissue-mimicking matrix) with aerosol jet printing (fine deposition of sacrificial gelatin fibers inside the matrix) in one workflow
* Machine learning that automatically optimizes print parameters for each target vascular configuration, rather than requiring manual, trial-and-error tuning
* Channel diameters under 10 micrometers, in some cases 5–6 micrometers — comparable to real human capillaries and finer than a human hair
* Stable one-, two-, and three-dimensional vascular network structures demonstrated
* Living endothelial cells successfully cultured to line the printed channels (endothelialization)

**How does it work?**

A soft, gel-like matrix that mimics tissue is first built up layer by layer using extrusion printing, which dispenses material under pressure. As each section of the matrix is printed, aerosol jet printing deposits thin gelatin fibers at precise locations inside it; these fibers serve as a sacrificial template. Once printing is complete, the whole construct is immersed in warm water, which liquefies and washes away the gelatin, leaving behind a network of hollow channels arranged exactly where the fibers had been. Throughout this process, a machine-learning model automatically adjusts the AJP print parameters to match the desired channel geometry and branching pattern, reducing the need for manual trial and error. The finished channels are then seeded with living endothelial cells, which attach to and grow along the channel walls, producing a structure that more closely resembles a real, cell-lined blood vessel.

**Strengths**

* Combines two printing techniques so both larger structural features and fine microscale channels can be produced within the same process
* Reports capillary-scale resolution (sub-10-micrometer channels), a level of precision that has been particularly hard to achieve in tissue engineering
* Machine-learning-based parameter optimization has the potential to improve reproducibility and extend the approach to varied vascular geometries
* Demonstrates channels lined with real living cells, not just empty hollow tubes, moving closer to a functional blood-vessel-like structure

**Limitations**

* This remains a lab-scale demonstration; secondary coverage does not provide detailed data on whether the vascular network actually improved cell survival throughout a thick, functional tissue or organ construct
* It is not clear from available reporting whether physiological perfusion under real blood-flow pressure, long-term channel patency, or anastomosis (connection) with a host's own vasculature has been demonstrated in vivo
* Whether the machine-learning optimization generalizes beyond the specific materials and printer setup used, to other bioinks or printing platforms, is unclear
* This summary was written without direct access to the full paper, due to network access restrictions in this session; it relies on the journal listing plus university press coverage and secondary reporting from 3D-printing trade press

**Terms to know**

* Bioprinting: 3D printing that deposits cells and biocompatible materials layer by layer to build tissue-like structures
* Extrusion printing: a 3D printing method that dispenses material through a nozzle under pressure
* Aerosol jet printing (AJP): a precision printing technique that deposits material as fine aerosol droplets to achieve very narrow line widths
* Sacrificial material: a material (gelatin, in this study) printed temporarily and later removed to leave behind hollow channels or cavities
* Endothelialization: the process by which endothelial cells attach to and line a channel or vessel wall, forming a layer resembling a real blood vessel
* Perfusion: the actual flow of fluid (such as blood) through vessels or channels to deliver oxygen and nutrients to tissue
* Hierarchical vascular network: a branching vessel structure that narrows from large vessels down to fine capillaries

**Why it is worth watching**

The inability to supply oxygen and nutrients to cells deep inside a printed tissue has long been one of the biggest barriers preventing bioprinting from producing genuinely implantable tissues or organs. Without inventing an entirely new material, this work reaches capillary-scale resolution by combining two existing printing techniques with machine-learning-guided optimization, pointing toward a practical path for eventually building perfusable, functional tissue models or transplantable tissue.

---

## My take

이 연구는 새로운 재료를 발명하기보다 서로 다른 두 프린팅 기술과 머신러닝을 조합해, 조직공학에서 오랫동안 어려웠던 모세혈관 수준의 해상도를 달성했다는 점에서 실용적 가치가 크다. 다만 이는 채널 자체의 해상도와 내피세포 정착을 보여준 시연이며, 실제 두꺼운 조직·장기 구조물 전체에 적용해 세포 생존율을 얼마나 높였는지, 생체 내에서 실제 혈류를 견디며 숙주 혈관과 연결될 수 있는지는 아직 확인되지 않은 것으로 보인다. 또한 이번 세션에서는 네트워크 접근 제한으로 논문 원문을 직접 확인하지 못해, 저널 목록 정보와 대학 보도자료 및 2차 언론 보도에 의존해 작성되었다는 점을 밝혀둔다.

This work's main value lies in reaching capillary-scale resolution — long a hard problem in tissue engineering — by combining two existing printing techniques with machine-learning-guided optimization, rather than inventing a new material. That said, what has been demonstrated so far is channel resolution and endothelial lining; it is not yet clear how much this improves cell survival across a full, thick tissue or organ construct, or whether the channels can sustain real blood flow and connect with a host's vasculature in vivo. This summary was also written without direct access to the full paper text, due to network access restrictions in this session, relying instead on the journal listing plus university press coverage and secondary reporting.
