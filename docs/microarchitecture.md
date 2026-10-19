# AX-1 Microarchitecture (draft)

Status: DRAFT. MVP scope only; nothing implemented or verified.

## MVP datapath (Phase 3 target)
- `mac_pe`: signed INT8 x signed INT8 -> signed 16-bit product, accumulated into a signed 32-bit accumulator.
- Accumulator: 32-bit two's complement. Overflow behavior to be fixed in Phase 2 (proposal: saturating on write-back, wrap-free by bounding K; accumulation depth limit documented).
- Requantization (proposal): int32 acc -> multiply by int32 scale -> arithmetic right shift with round-half-away-from-zero -> add zero point -> saturate to int8. Exact definition is frozen by the Python reference model first, then RTL matches it.
- Array: small parameterized `ROWS x COLS` (start 4x4). Scale only after correctness and resource estimates.
- Control FSM: IDLE -> LOAD -> COMPUTE -> DRAIN -> DONE/ERROR, with timeout and illegal-command error state.
- Register interface and a simple single-port memory interface; handshake is valid/ready with defined backpressure.

## INT4
Deferred until INT8 is verified end-to-end.
