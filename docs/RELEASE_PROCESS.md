# Release process

## Build once
Each service image is created from the merge commit and pushed with the Git SHA. Production should reference an immutable SHA/digest instead of rebuilding the same release for each environment.

## Promotion
1. Merge application code after CI passes.
2. CI publishes immutable service images.
3. Update staging desired-state image tag/digest in Git.
4. Argo CD reconciles staging.
5. Run smoke tests and soak period.
6. Promote the same artifact to production by changing production desired state.
7. Argo Rollouts gradually shifts production traffic.
8. Prometheus analysis can abort a release that violates the success-rate gate.

## Rollback
Rollback changes desired state or aborts/undoes the active Rollout. Do not rebuild an old release to roll back; deploy the previously known-good immutable artifact.

## Why this pattern
Separating artifact creation from deployment avoids environment-specific rebuild drift. Git records who promoted what, and the cluster-side GitOps controller retains deployment responsibility.
