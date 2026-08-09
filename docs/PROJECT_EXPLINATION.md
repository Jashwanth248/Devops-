# 10-minute production-platform walkthrough

1. **Business context** — PulseCart has a customer gateway, order service and async worker. PostgreSQL stores orders and Redis decouples background work.
2. **CI** — PRs test/lint/scan; artifacts are built once and tagged immutably.
3. **Infrastructure** — Terraform modules create shared network, GKE and registry resources; environments compose modules separately.
4. **GitOps** — Argo CD owns deployment reconciliation. CI does not need broad cluster-admin access.
5. **Progressive delivery** — production gateway uses a canary rollout. Prometheus analysis can stop a bad release.
6. **Reliability** — probes, requests/limits, HPA, PDB and anti-fragile replica configuration protect availability.
7. **Security** — non-root containers, read-only root filesystem, NetworkPolicy, Kyverno and OIDC provide defense in depth.
8. **Observability** — OpenTelemetry centralizes telemetry; Prometheus rules alert on customer-impacting failures.
9. **Incident response** — failure drills intentionally create an incident, then the runbook guides diagnosis and rollback.
10. **Tradeoffs** — this repository uses managed GKE and open standards to reduce control-plane toil while retaining portable deployment and telemetry patterns.

## Strong interview sentence

> I built this as if I were the platform engineer supporting a small commerce team. The application is deliberately simple; the project demonstrates how I would provision, release, secure, observe, scale and recover a production workload.
