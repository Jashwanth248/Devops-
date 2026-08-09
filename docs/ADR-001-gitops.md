# ADR-001: GitOps owns cluster deployment

## Status
Accepted

## Context
CI needs to build and verify artifacts, but giving CI broad Kubernetes credentials increases deployment coupling and credential risk.

## Decision
GitHub Actions builds/tests/scans artifacts. Git stores desired deployment state. Argo CD reconciles that state into clusters.

## Consequences
- audit trail is Git history
- rollbacks are Git/revision based
- cluster credentials stay with the GitOps controller
- deployment requires healthy Argo CD and repository access
