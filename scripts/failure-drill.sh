#!/usr/bin/env bash
set -euo pipefail
NS=${1:-pulsecart-staging}
echo "Failure drill: scaling orders to zero in $NS"
kubectl scale deployment orders --replicas=0 -n "$NS"
echo "Observe gateway errors/alerts, then restore with:"
echo "kubectl scale deployment orders --replicas=2 -n $NS"
