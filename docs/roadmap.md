# Roadmap

Status: Phase 1 complete (see below). Later phases are plans, not results.

| Phase | Goal | State |
|---|---|---|
| 1 | Foundation: repo, docs, scripts, CI | **done** (structure test only) |
| 2 | Python INT8 reference model + unit tests | next |
| 3 | Minimal parameterized RTL (MAC, acc, FSM, regs) | not started (needs simulator) |
| 4 | Self-checking tests vs reference | not started |
| 5 | ONNX compiler MVP | not started |
| 6 | End-to-end small network on RTL sim | not started |
| 7 | FPGA synthesis/constraints | not started |
| 8 | Scaling + target feasibility (see architecture.md section 3) | not started |
| 9 | ASIC readiness assessment | not started |

## Top risks
1. YOLOv8n INT8 weights (~3 MiB) exceed the 2 MiB SRAM target.
2. <6 ms needs >=~60% sustained utilization at ~586 MHz.
3. 1.2 W unsupported by any power methodology yet.
4. No RTL simulator/formal tools in the current environment.
5. MIPI PHY and 28 nm PDK/SRAM macros are external dependencies.
