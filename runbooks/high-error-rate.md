# Runbook: High HTTP 5xx Rate

## Trigger
5xx error ratio exceeds 2% for 10 minutes.

## Triage
1. Check deployment status and recent rollouts.
2. Inspect request/error metrics and latency.
3. Inspect pod restarts, readiness, CPU and memory saturation.
4. Compare current image/version to last healthy deployment.

## Mitigation
- Roll back the deployment if correlated with a release.
- Scale replicas/nodes if saturation is causal.
- Disable the failing downstream integration if supported.

## Verify recovery
Confirm error rate and p95 latency return below SLO thresholds for 15 minutes.
