# PulseCart Production Architecture

## Workload
PulseCart models a small commerce platform with a public gateway, internal order service, background worker, PostgreSQL and Redis. The application is intentionally small; the project is about operating it safely.

## Delivery
Pull requests run CI. Images are built once and identified immutably. Git stores desired state. Argo CD reconciles Kubernetes. Production uses Argo Rollouts for progressive delivery instead of replacing all pods at once.

## Environments
Staging and production have separate configuration and Terraform composition. Production has stricter replica counts, disruption budgets, policy checks, and rollout gates.

## Reliability
Every HTTP service exposes health/readiness/metrics. Kubernetes uses requests/limits, HPA and PDB. Prometheus rules monitor error rate and availability. Runbooks define diagnosis and rollback.

## Security
Containers run non-root with read-only filesystems and dropped capabilities. NetworkPolicy limits lateral traffic. Kyverno enforces baseline workload policy. GitHub OIDC is the intended cloud-authentication path.

## Observability
Services export metrics and OTLP telemetry to an OpenTelemetry Collector. The collector is the vendor-neutral telemetry gateway; Prometheus/Grafana provide metrics and dashboards while a trace backend can be attached without changing application deployment patterns.
