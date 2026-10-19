# AX-1 Architecture (draft)

Status: DRAFT. Proposals and open decisions only; nothing implemented or verified.

## 1. Block diagram (proposed)
```
 pixel source (synthetic / bridge) -> stream adapter -> [ SRAM banks ] <-> DMA
                                                          ^   |
 RISC-V RV32 core -- bus (AXI4-Lite ctrl, wide data path) -+   v
        |                                              neural core
   CSR / IRQ / debug                       (PE array -> accumulators -> requant/activation)
```

## 2. Counting convention (decided for this project)
1 MAC = 2 operations (multiply + add). Peak TOPS = MACs x f_clk x 2.

## 3. Feasibility arithmetic (analytical, not simulated)
- 2.4 TOPS / (2048 x 2) = ~586 MHz required clock at 100% utilization.
- A 28 nm target at ~586 MHz with 2 MiB SRAM is plausible to attempt but unproven; needs PDK data we do not have.
- YOLOv8n (public model card, to be re-verified from the actual model file): ~3.2 M parameters, ~8.7 GFLOPs at 640x640, i.e. ~4.35 GMAC.
  - 4.35 GMAC / 2048 = ~2.1 M cycles ideal = ~3.6 ms at 586 MHz.
  - Meeting <6 ms therefore needs sustained utilization >= ~60% *including* all memory stalls and non-conv layers.
- **Capacity risk:** ~3.2 M INT8 weights is ~3.05 MiB, exceeding 2 MiB before counting activations. A DRAM-less claim needs INT4 weights, pruning, a smaller input/model, or weight streaming from external flash. This must be resolved in Phase 8 before committing to the SRAM size.

## 4. Decisions
| ID | Topic | Status |
|---|---|---|
| D1 | MAC counting convention (1 MAC = 2 ops) | decided |
| D2 | Array shape and dataflow (weight- vs output-stationary) | OPEN, decide in Phase 3 after reference model |
| D3 | Control core: pick an existing permissively licensed RV32 core (candidates to evaluate: PicoRV32, Ibex, VexRiscv) | OPEN; record license + interface here |
| D4 | Control bus: AXI4-Lite for CSRs; wide streaming/SRAM path TBD | OPEN |
| D5 | Camera: synthetic stream source first; MIPI CSI-2 PHY is a separate future work package needing licensed IP | decided |
| D6 | First FPGA family/toolchain | OPEN (open-source flow preferred if feasible) |

## 5. Clock/reset (assumption)
Single clock domain and single synchronous active-low reset for the MVP. Additional domains (sensor, host) are added only with a documented CDC plan.
