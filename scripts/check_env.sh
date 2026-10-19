#!/usr/bin/env bash
# Report which development tools are present. Does not install anything.
cd "$(dirname "$0")/.."
printf "%-26s %s\n" TOOL STATUS
for t in git python3 make verilator iverilog yosys sby gtkwave \
         riscv32-unknown-elf-gcc riscv64-unknown-elf-gcc vivado nextpnr-ice40 nextpnr-ecp5; do
  if command -v "$t" >/dev/null 2>&1; then
    printf "%-26s %s\n" "$t" "$("$t" --version 2>&1 | head -1)"
  else
    printf "%-26s %s\n" "$t" "MISSING"
  fi
done
for m in numpy onnx cocotb pytest; do
  v=$(python3 -c "import $m;print($m.__version__)" 2>/dev/null) || v=MISSING
  printf "%-26s %s\n" "py:$m" "$v"
done
