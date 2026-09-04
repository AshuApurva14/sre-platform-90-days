# Capstone — Reliable Service Platform

## Objective

Build one deployable service and demonstrate the complete operational lifecycle.

## Lifecycle

1. Build service
2. Add tests
3. Add CI
4. Build container
5. Deploy to Kubernetes
6. Add metrics/logs/traces
7. Define SLO
8. Introduce controlled failure
9. Diagnose and mitigate
10. Write runbook
11. Automate repeated steps
12. Document trade-offs

## Architecture

See `architecture/architecture.md`.

## Acceptance Criteria

- [ ] Health endpoint works
- [ ] Unit tests run locally and in CI
- [ ] Image builds reproducibly
- [ ] Deployment has readiness/liveness probes
- [ ] Resources are defined
- [ ] Dashboard shows core signals
- [ ] SLO is documented
- [ ] Alert has an actionable response
- [ ] At least one controlled failure is tested
- [ ] Rollback works
- [ ] Runbook exists
- [ ] No secrets are stored in Git
