---
title: "VeriCache: Turning Lossy KV Cache into Lossless LLM Inference"
date: 2026-05-25
topic: AI
tags: [AI, inference, KV-cache, speculative-decoding, LLM, efficiency, systems, memory-management]
source: https://arxiv.org/abs/2605.17613
---

# VeriCache: Turning Lossy KV Cache into Lossless LLM Inference

* Date: 2026-05-25
* Source: https://arxiv.org/abs/2605.17613
* Topic: AI / LLM Inference Systems
* Why it matters: KV cache compression is one of the most widely deployed techniques for serving LLMs on long contexts, but it is inherently lossy — causing silent, compounding failures in code generation and tool calling as outputs grow longer. VeriCache is the first system to guarantee identical outputs to full-KV inference while achieving up to 3.82× higher throughput by combining CPU-offloaded full KV storage with a speculative-decode-and-verify scheme.

## Korean Summary

**한줄 요약**

VeriCache는 LLM 추론의 핵심 병목인 KV 캐시를 압축해 처리량을 높이면서도, 압축된 캐시로 초안 토큰을 생성하고 전체 KV 캐시로 검증하는 방식으로 출력 품질을 풀(full) KV 추론과 완전히 동일하게 보장하는 최초의 추론 프레임워크이다. Llama-70B에서 최대 3.82배 처리량 향상을 달성하면서 KL 발산을 0.01 nats 미만으로 유지한다.

**핵심 아이디어**

기존 KV 캐시 압축(토큰 드롭핑, 양자화 등)은 짧은 출력에서는 품질 저하가 거의 없어 보이지만, 출력이 길어질수록 전체 KV와의 편차가 누적되어 코드 생성, 도구 호출 등에서 치명적 실패를 일으킨다. VeriCache는 이 문제를 완전히 다른 방식으로 접근한다: GPU HBM에는 압축 KV 캐시만 두고, 전체 KV 캐시는 CPU RAM에 오프로드한 뒤, 압축 캐시로 토큰 초안을 빠르게 생성하는 것과 CPU→GPU 전체 KV 스왑을 병렬로 실행해 검증한다. 두 작업이 각각 HBM 대역폭과 PCIe 대역폭이라는 서로 다른 하드웨어 병목을 사용하므로 오버랩이 가능하다. 틀린 초안 토큰은 수정되므로 최종 출력이 풀 KV 추론과 완전히 동일하다.

**무엇이 새로운가?**

- **손실 압축을 무손실 추론으로 전환**: 기존 KV 압축 방식(KVzip, KIVI 등)의 손실 문제를 추론 레이어에서 검증으로 해결한 첫 번째 프레임워크
- **초안-검증 패러다임의 KV 캐시 적용**: 기존 투기적 디코딩(작은 초안 모델 + 큰 검증 모델)과 달리, 동일 모델에서 압축 캐시를 초안, 전체 캐시를 검증자로 활용
- **이종 대역폭 병렬화**: 압축 KV 디코딩(HBM 대역폭 바운드)과 전체 KV CPU→GPU 스왑(PCIe 대역폭 바운드)을 동시에 실행하는 시스템 최적화
- **범용 압축 호환성**: 특정 압축 알고리즘에 묶이지 않고 다양한 기존 KV 압축 방법을 초안 엔진으로 그대로 활용 가능
- **장문 출력 정확도 보장**: ComplexFuncBench 함수 호출 벤치마크에서 긴 컨텍스트 코드 생성 및 도구 호출 태스크에서 완전한 정확도 유지 확인

**어떻게 작동하는가?**

1. **오프로드 구성**: 전체 KV 캐시는 CPU RAM(또는 호스트 메모리)에 보관. GPU HBM에는 압축된 KV 캐시만 유지.
2. **초안 생성**: 매 디코딩 스텝에서 압축 KV 캐시를 이용해 다음 토큰 후보(초안)를 빠르게 생성. 이 단계는 GPU HBM 대역폭에 묶여 있음.
3. **병렬 스왑**: 초안 생성과 동시에, 전체 KV 캐시를 PCIe를 통해 CPU RAM에서 GPU로 전송. PCIe 대역폭은 HBM과 독립적이므로 두 작업이 중첩(overlap)됨.
4. **검증**: 전체 KV 캐시가 GPU에 도착하면, 동일 모델로 동일 입력을 재계산해 초안 토큰이 풀 KV 추론 결과와 일치하는지 확인.
5. **수정 및 재시작**: 초안이 틀린 경우 정확한 토큰으로 대체하고 계속 진행. 맞는 경우 해당 토큰 확정 후 다음 스텝으로.
6. **반복**: 모든 출력 토큰에 걸쳐 반복. 최종 출력은 풀 KV 추론과 비트 단위로 동일(하드웨어 비결정성 제외).

**강점**

- 출력 품질을 풀 KV 추론과 동일하게 보장 — 정확도-처리량 트레이드오프 없음
- Llama-70B에서 최대 3.82배 처리량 향상이라는 구체적이고 측정 가능한 결과
- KVzip, KIVI 등 기존 손실 압축 알고리즘을 초안 엔진으로 재활용 가능 — 추가 학습 불필요
- 코드 생성, 함수 호출 등 긴 출력이 필요한 고위험 태스크에서 손실 방식의 치명적 실패 완전 방지
- HBM과 PCIe라는 서로 다른 병목의 병렬화라는 시스템 설계 통찰이 일반적으로 적용 가능

**한계**

- CPU RAM에 전체 KV 캐시를 보유해야 하므로 메모리 용량 요구가 크다 (128K 토큰 컨텍스트에서 수십 GB에 달할 수 있음)
- PCIe 대역폭이 검증 속도의 실질적 병목 — PCIe 4.0/5.0 세대나 GPU 서버 환경에 따라 오버헤드가 다를 수 있음
- 압축 품질이 낮아 초안 수용률(accept rate)이 낮아지면 처리량 향상이 크게 줄어듦
- 멀티-GPU 서버에서 GPU 간 NVLink와 PCIe 토폴로지가 다를 경우 최적화 전략이 달라질 수 있음
- 추론 런타임 시스템 통합 복잡도가 순수 압축 방식보다 높음

**알아둘 용어**

- **KV 캐시 (KV Cache)**: 트랜스포머 어텐션에서 이전 토큰의 키(Key)·값(Value) 텐서를 저장해 재계산을 생략하는 메모리 구조. 컨텍스트 길이에 비례해 GPU 메모리를 소비함
- **KV 캐시 압축 (KV Cache Compression)**: 토큰 드롭핑(덜 중요한 KV 항목 제거) 또는 양자화(비트 수 축소)를 통해 KV 캐시 크기를 줄이는 기술
- **투기적 디코딩 (Speculative Decoding)**: 작은 초안 모델이 후보 토큰을 빠르게 생성하고, 큰 검증 모델이 이를 병렬로 확인하는 추론 가속 기법
- **토큰 수용률 (Accept Rate)**: 투기적 디코딩에서 초안 토큰이 검증을 통과하는 비율. 높을수록 처리량 향상이 크다
- **HBM (High Bandwidth Memory)**: 현대 GPU에 탑재된 고대역폭 온칩 메모리. 용량이 크지 않지만 매우 빠름
- **PCIe (PCI Express)**: CPU와 GPU 사이의 데이터 버스. HBM보다 훨씬 느리지만 대용량 호스트 메모리와 연결됨
- **KL 발산 (KL Divergence)**: 두 확률 분포 간의 차이를 측정하는 지표. VeriCache에서는 압축 추론과 풀 KV 추론의 출력 분포 차이를 측정하는 데 사용됨

**왜 주목할 만한가?**

LLM 서빙 시스템은 긴 컨텍스트 요청이 늘면서 KV 캐시 압축을 거의 필수적으로 사용하고 있다. 그러나 기존 압축 방식은 품질 저하를 감수하는 것이 전제였고, 코드 생성이나 멀티턴 도구 호출처럼 긴 출력이 필요한 태스크에서는 이 손실이 치명적으로 누적되는 문제가 있었다. VeriCache는 "손실 압축의 처리량"과 "풀 KV의 정확도"를 동시에 달성할 수 있음을 실제 하드웨어에서 증명했다. 이 접근 방식은 추론 엔진(vLLM, SGLang 등)에 통합되면 현재 배포된 LLM 서비스의 신뢰성과 효율성을 동시에 높이는 실용적 경로를 제시한다.

---

## English Summary

**One-line summary**

VeriCache is the first LLM inference framework that guarantees bit-identical outputs to full-KV-cache decoding while achieving up to 3.82× higher throughput on Llama-70B, by using CPU-offloaded full KV as a verifier for tokens drafted by a compressed in-GPU KV cache.

**Core idea**

Existing KV cache compression methods (token dropping, quantization) are inherently lossy: they look acceptable on short outputs but diverge catastrophically over long ones, causing failures in code generation and tool calling. VeriCache reframes this as a speculative-decoding problem: the compressed KV cache in GPU HBM acts as a fast but imperfect draft engine, while the full KV cache is stored in CPU RAM and swapped into GPU memory for verification. The key insight is that compressed-KV decoding is HBM-bandwidth-bound while the CPU-to-GPU swap is PCIe-bandwidth-bound — these two bottlenecks are on different hardware paths and can therefore be overlapped. Wrong draft tokens are corrected, so the final output is identical to full-KV inference.

**What is new?**

- **Lossless guarantee on top of lossy compression**: The first framework to convert any KV cache compression algorithm into a provably lossless inference path, without retraining or modifying the model
- **KV-as-draft, full-KV-as-verifier**: Adapts the speculative decoding paradigm to the same model with two KV representations, rather than requiring a separate smaller model
- **Heterogeneous-bandwidth parallelism**: Explicitly exploits the independence of HBM (drafting) and PCIe (full-KV swap) bandwidth to overlap compute and memory transfer
- **Algorithm-agnostic design**: Works as a wrapper around existing KV compression algorithms (KVzip, KIVI, etc.) without modifying them
- **Demonstrated on long-context reliability tasks**: Validated on ComplexFuncBench function-calling and code generation tasks where lossy methods produce catastrophic failure

**How does it work?**

1. **Offload setup**: At context encoding time, the full KV cache is stored in CPU RAM. Only the compressed KV cache (via token dropping or quantization) is kept in GPU HBM.
2. **Draft phase**: Each decoding step uses the compressed KV cache to rapidly generate draft tokens. This step is bounded by GPU HBM bandwidth.
3. **Parallel swap**: While drafting proceeds, the full KV cache is asynchronously transferred from CPU RAM to GPU over PCIe. Because PCIe and HBM are independent bandwidth resources, the two phases overlap with minimal interference.
4. **Verification phase**: Once the full KV cache is available, the model re-runs attention with the complete cache to verify whether each draft token matches what full-KV decoding would have produced.
5. **Correction**: Tokens that fail verification are replaced with the correct full-KV outputs. Accepted tokens are committed. Decoding continues.
6. **Result**: The complete output sequence is bit-identical to full-KV inference (within hardware non-determinism), measured at KL divergence < 0.01 nats.

**Strengths**

- Provably identical outputs to full-KV inference — eliminates the accuracy-throughput tradeoff for the first time
- Concrete 3.82× throughput gain on Llama-70B measured on real hardware
- Reuses existing compression algorithms as drop-in draft engines, requiring no retraining
- Eliminates catastrophic failure modes of lossy compression in high-stakes long-output tasks (code, tool use)
- The parallelism insight (HBM vs PCIe) is broadly applicable to other heterogeneous memory system optimizations

**Limitations**

- Requires sufficient CPU RAM to hold the full KV cache — this can be tens of gigabytes for long contexts (e.g., 128K tokens on a 70B model)
- PCIe bandwidth is the real bottleneck for verification latency; performance will vary significantly by server generation and GPU interconnect topology
- Accept rate depends on compression quality: aggressive compression producing poor drafts reduces effective throughput gain
- Multi-GPU NVLink topologies may require different system engineering to fully exploit the parallelism
- Higher system integration complexity compared to pure compression approaches

**Terms to know**

- **KV cache**: The stored key and value tensors from transformer attention over past tokens; avoids recomputation but consumes GPU memory proportional to context length
- **KV cache compression**: Techniques that reduce KV cache size via token eviction (dropping less-attended entries) or quantization (reducing bit width), at the cost of output quality
- **Speculative decoding**: An inference technique where a fast draft model proposes token candidates that a larger verifier model checks in parallel, accepting correct drafts to speed up overall throughput
- **Accept rate**: The fraction of draft tokens that pass verification; higher accept rates yield greater speedup in speculative decoding schemes
- **HBM (High Bandwidth Memory)**: The high-speed on-package memory on modern GPUs, offering very high bandwidth but limited total capacity
- **PCIe (PCI Express)**: The bus connecting CPU and GPU; much lower bandwidth than HBM but provides access to the much larger host DRAM
- **KL divergence**: A measure of difference between two probability distributions; used here to quantify how much compressed-cache outputs diverge from full-KV outputs (VeriCache keeps this under 0.01 nats)

**Why it is worth watching**

LLM serving infrastructure has broadly adopted KV cache compression to handle growing context windows, but practitioners have always faced a hidden risk: quality degradation that compounds silently over long outputs, and fails catastrophically in production tasks like code generation, multi-turn agents, and function calling. VeriCache demonstrates that this tradeoff is not fundamental — with the right system design, you can have compression-level throughput and full-KV-level correctness simultaneously. If integrated into production inference engines like vLLM or SGLang, this approach could let operators deploy more aggressive compression without sacrificing output reliability, directly improving the cost and quality of long-context LLM services.

**My take**

이 논문은 KV 캐시 압축의 손실 문제를 "더 좋은 압축 알고리즘"이 아닌 "시스템 설계"로 해결한 점이 독창적이다. HBM과 PCIe라는 서로 다른 병목을 의도적으로 활용한 병렬화 통찰은 우아하고 실용적이며, 기존 압축 알고리즘을 그대로 재활용한다는 점에서 배포 마찰이 낮다. 다만 CPU RAM 요구량과 PCIe 의존성은 엣지 환경이나 소형 서버에서 제약이 될 수 있고, 수용률 저하 시 처리량 이점이 감소한다는 한계는 실제 운용 시 주의해야 한다.

VeriCache is an elegant systems paper that solves a real production problem — lossy KV cache compression causing silent failures — through hardware-aware design rather than a better algorithm. The insight of parallelizing HBM-bound and PCIe-bound operations is clean and immediately implementable. The main practical constraint is the CPU RAM requirement, which may limit deployment in memory-constrained settings, and the accept rate dependency, which means heavily compressed caches may see diminishing returns. Overall, this is a compelling contribution to the LLM serving stack.
