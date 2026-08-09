# Runbook: Gateway high 5xx rate

## Trigger
`GatewayHigh5xxRate` fires when the 5xx ratio stays above 2% for 10 minutes.

## First five minutes
1. Confirm customer impact and current error ratio.
2. Check whether a rollout is active.
3. Compare stable vs canary error rate.
4. Check orders-service health and dependency errors.
5. Check pod restarts, saturation and recent config changes.

## Rollback
If the incident started with a release, abort the rollout:

```bash
kubectl argo rollouts abort gateway -n pulsecart-production
kubectl argo rollouts undo gateway -n pulsecart-production
```

## Dependency checks

```bash
kubectl get pods -n pulsecart-production
kubectl top pods -n pulsecart-production
kubectl logs deploy/gateway -n pulsecart-production --since=10m
kubectl logs deploy/orders -n pulsecart-production --since=10m
```

## Resolution criteria
- 5xx rate below 1% for at least 15 minutes
- no unhealthy rollout
- dependency health normal
- error budget burn returned to acceptable rate

## Follow-up
Create a post-incident review including timeline, contributing factors, detection quality, recovery time and preventive actions.
