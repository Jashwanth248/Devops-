# PulseCart Platform Explanation

This document explains how the PulseCart production platform is designed, deployed, secured, observed, scaled, and recovered.

## 1. Business context

PulseCart is a small commerce platform with three application workloads:

- **gateway** receives customer-facing requests.
- **orders** owns order-processing logic and persists order data.
- **worker** handles asynchronous background work.

PostgreSQL stores transactional order data. Redis is used to decouple background processing from request handling.

The application code is intentionally simple so the repository can focus on platform engineering and production operations.

## 2. Continuous integration

Pull requests run automated validation before code is accepted. The delivery pipeline is designed to:

1. lint and test each service;
2. build container images;
3. scan images for high and critical vulnerabilities;
4. tag artifacts immutably using the source commit;
5. publish approved images to the container registry.

The artifact is built once and promoted through environments instead of being rebuilt separately for staging and production.

## 3. Infrastructure as code

Terraform modules define the cloud foundation, including networking, GKE, and registry resources.

Staging and production compose these modules separately so each environment can have independent configuration and a smaller blast radius.

The infrastructure layout is intended to make changes reviewable, reproducible, and version controlled.

## 4. GitOps deployment model

Argo CD owns deployment reconciliation.

Git stores the desired state of each environment. Argo CD compares that state with the Kubernetes cluster and reconciles differences automatically.

This separates responsibilities:

- CI validates and produces software artifacts.
- Git records desired deployment state.
- Argo CD deploys and reconciles Kubernetes resources.

This design avoids giving the CI pipeline broad, permanent cluster-administrator credentials.

## 5. Progressive delivery

Production releases use Argo Rollouts rather than immediately replacing every running instance.

The gateway can be released progressively through canary stages such as:

```text
10% → 25% → 50% → 100%
```

Prometheus metrics are evaluated during the rollout. If error-rate or availability conditions fail, the rollout can stop before the new version reaches all customer traffic.

## 6. Reliability controls

The Kubernetes workloads use multiple reliability mechanisms:

- readiness probes prevent unhealthy pods from receiving traffic;
- liveness checks help recover stuck processes;
- resource requests and limits support predictable scheduling;
- Horizontal Pod Autoscaling adjusts replica capacity under load;
- PodDisruptionBudgets protect availability during voluntary disruptions;
- multiple replicas reduce dependence on a single pod;
- environment isolation limits the impact of configuration mistakes.

The project also defines service-level objectives and error-budget concepts so reliability is measured from the service perspective rather than only from infrastructure health.

## 7. Security model

The workload is hardened with defense-in-depth controls:

- containers run as non-root users;
- root filesystems are read-only where possible;
- unnecessary Linux capabilities are dropped;
- NetworkPolicy limits allowed network communication;
- Kyverno enforces Kubernetes policy rules;
- container images are vulnerability scanned;
- service identities follow least-privilege principles;
- short-lived/OIDC-based cloud identity is preferred over long-lived static credentials.

## 8. Observability

OpenTelemetry provides a common telemetry path for the application services.

The observability architecture connects application telemetry to Prometheus and Grafana so platform operators can correlate service behavior with infrastructure changes and releases.

Prometheus rules focus on customer-impacting signals such as availability and elevated server-error rates.

## 9. Incident response

The repository contains runbooks and failure drills so operational behavior is documented before an outage occurs.

A typical incident flow is:

```text
alert
  ↓
identify affected service
  ↓
check recent deployment/configuration changes
  ↓
inspect metrics and workload health
  ↓
mitigate or roll back
  ↓
verify recovery
  ↓
document follow-up actions
```

Failure-drill scripts intentionally create controlled problems so the detection and recovery path can be exercised rather than existing only as documentation.

## 10. Architectural tradeoffs

This project uses managed GKE to reduce Kubernetes control-plane operational overhead while retaining standard Kubernetes deployment patterns.

GitOps separates artifact creation from deployment reconciliation, improving auditability and reducing direct deployment credentials in CI.

OpenTelemetry keeps telemetry instrumentation portable, while Prometheus provides metric-based monitoring and release analysis.

The platform is intentionally not a full-scale commerce product. Its purpose is to demonstrate the operational architecture around a realistic multi-service workload: infrastructure provisioning, delivery, security, reliability, observability, scaling, and recovery.

## End-to-end flow

```text
Developer change
      ↓
Pull request
      ↓
CI validation + security scanning
      ↓
Immutable container artifact
      ↓
Git environment configuration
      ↓
Argo CD reconciliation
      ↓
Staging validation
      ↓
Production canary rollout
      ↓
Prometheus analysis
      ↓
Full promotion or automatic stop
      ↓
Continuous SLO monitoring
```

This flow represents the central engineering idea of PulseCart: application delivery and production operations are treated as one controlled, observable system.
