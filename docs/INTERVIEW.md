# Interview Walkthrough

Explain the project as a production delivery system, not a YAML collection:

1. Developer pushes code.
2. CI runs lint, tests, container build and vulnerability scanning.
3. A successful `main` build publishes the image to GitHub Container Registry.
4. Terraform provisions GKE and supporting infrastructure.
5. Git is the desired-state source; Argo CD reconciles Kubernetes.
6. HPA scales workloads; node autoscaling scales infrastructure.
7. Prometheus/Grafana expose service health and performance.
8. Security contexts, NetworkPolicy, Kyverno and image scanning add defense in depth.
9. Runbooks define incident response and rollback decisions.

## Strong talking points

- CI validates code; GitOps owns deployment state.
- Containers run non-root with privilege escalation disabled and a read-only filesystem.
- HPA handles pod-level demand while GKE node-pool autoscaling handles cluster capacity.
- PDB protects availability during voluntary disruptions.
- Trivy blocks HIGH/CRITICAL container vulnerabilities before publication.
- Metrics and runbooks reduce mean time to detection and recovery.

## Resume bullet

- Engineered a production-style cloud-native delivery platform using GitHub Actions, Docker, Terraform, GKE, Argo CD, Kustomize, Prometheus/Grafana, autoscaling and policy-as-code, with automated tests, vulnerability scanning, hardened Kubernetes workloads and incident runbooks.
