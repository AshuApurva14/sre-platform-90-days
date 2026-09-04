# Runbook — High Latency

## Symptoms

High p95/p99 latency.

## First checks

1. Confirm user impact.
2. Determine affected scope.
3. Check recent deployments/config changes.
4. Check dependency health.
5. Inspect metrics, traces, then logs.

## Mitigation Options

- Roll back release
- Reduce traffic
- Add capacity
- Rate limit
- Revert configuration

## Recovery Verification

- Error rate normal
- Latency normal
- Health checks green
- Dashboard stable

## Follow-up

Open a postmortem and create owned action items.
