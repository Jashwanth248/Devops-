#!/usr/bin/env bash
set -euo pipefail
BASE_URL=${1:-http://localhost:8080}
curl --fail --silent "$BASE_URL/healthz" >/dev/null
curl --fail --silent "$BASE_URL/api/orders" >/dev/null
echo "smoke test passed: $BASE_URL"
