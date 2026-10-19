#!/usr/bin/env bash
# Single documented test entry point. Uses stdlib unittest so it runs
# with no third-party dependencies.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m unittest discover -s tests -p 'test_*.py' -v
