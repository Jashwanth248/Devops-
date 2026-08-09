#!/usr/bin/env bash
set -euo pipefail
URL=${1:-http://localhost:8080/work?delay_ms=100}
for i in $(seq 1 500); do curl -fsS "$URL" >/dev/null & done
wait
