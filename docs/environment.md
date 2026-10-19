# Development environment

Status: measured on the build container used for Phase 1 (`make env`). Re-run on your own machine.

| Tool | Status in build container | Needed for |
|---|---|---|
| git 2.43.0, python 3.12.3, make 4.3 | present | everything |
| numpy 2.4.4 | present | Phase 2 reference model |
| pytest, cocotb, onnx | **missing** (no network) | Phases 4, 5 (unittest is used until then) |
| verilator, iverilog | **missing** | RTL simulation / lint (Phase 3-4) |
| yosys, sby | **missing** | synthesis estimate, formal (Phase 3, 7) |
| riscv32 gcc toolchain | **missing** | firmware for the control core |
| vivado / nextpnr | **missing** | FPGA flow (Phase 7) |

Consequence: until a simulator is available, RTL can be written but **not** claimed to pass tests.
Recommended local install: Verilator + Icarus + Yosys + SymbiYosys + cocotb + a RISC-V GCC.
