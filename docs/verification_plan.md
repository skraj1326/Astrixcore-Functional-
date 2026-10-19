# Verification Plan (draft)

Status: DRAFT. No tests of hardware exist yet.

| Level | What | Tool (when available) |
|---|---|---|
| Reference model | INT8 arithmetic, saturation, requant vs. independent checks | Python unittest |
| RTL unit | MAC, accumulator, FSM, registers: boundaries, signed corners, reset, backpressure, invalid commands | Verilator/Icarus + cocotb |
| RTL vs model | randomized + directed vectors, seeds logged | cocotb |
| Integration | compiler output executed on RTL sim, cycle count reported | cocotb |
| Formal (later) | handshake and FSM properties | SymbiYosys |

Rules: a test counts only if executed; results are recorded in `docs/verification_results.md` (created when the first RTL test runs) with tool versions and commands.
