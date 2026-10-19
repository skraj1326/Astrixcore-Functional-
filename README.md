# Astrixcore AX-1

Research and engineering prototype of a low-power, RISC-V-controlled neural
accelerator for industrial automated optical inspection (AOI).

**Status: Phase 1 (project foundation). No RTL, compiler or reference model exists yet.
Nothing here has been simulated, synthesized, FPGA-tested or measured.**

## Targets (aspirational, NOT achieved or verified)
2,048 INT8 MACs · 2 MiB on-chip SRAM · 2.4 TOPS peak · 1.2 W · <6 ms YOLOv8n ·
32-bit RISC-V control core · DRAM-less objective · possible future 28 nm.
See `docs/roadmap.md` for the feasibility review of these numbers.

## Layout
| Path | Purpose |
|---|---|
| `docs/` | architecture, microarchitecture, HW/SW interface, verification plan, roadmap, environment |
| `rtl/` | synthesizable SystemVerilog (Phase 3) |
| `compiler/` | Python reference model + ONNX compiler MVP (Phases 2, 5) |
| `verification/` | SV testbenches / cocotb (Phase 4) |
| `tests/` | automated tests |
| `fpga/` | constraints and scripts (Phase 7) |
| `scripts/` | environment check, test runner |

## Commands
```
make env     # report installed/missing tools
make test    # run the test suite (stdlib unittest, no dependencies)
```

## Rules of the project
Estimates, simulations, synthesis and measurements are labeled separately.
No claim of "verified", "synthesizable" or "silicon-ready" without evidence in `docs/`.
No proprietary PDKs, EDA tools or MIPI PHY IP are assumed; none belong in this repo.
