# Hardware/Software Interface (draft)

Status: DRAFT. Not frozen. Compiler emits nothing until this is frozen and matched by RTL.

## Principles
- The compiler only generates commands for operators the current RTL supports.
- Unsupported operators are reported with a clear error (later: CPU fallback).

## Initial operator set (proposal, MVP)
| Operator | Layout | Status |
|---|---|---|
| Int8 matmul / dense | row-major | planned Phase 2-3 |
| Int8 conv2d (stride/pad) | NHWC | planned after matmul |
| ReLU | elementwise | planned |
| Everything else (incl. arbitrary ONNX) | - | NOT supported |

## To define before Phase 5
Command descriptor encoding, CSR map, SRAM address map, completion IRQ and error codes, quantization parameter format (scale as int32 multiplier + shift, zero point), model load/execute lifecycle. Each gets a bit-exact table here.
