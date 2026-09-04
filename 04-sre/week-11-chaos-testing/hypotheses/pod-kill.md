# Chaos Hypothesis — Pod Kill

## Steady State

- Service is reachable
- Error rate is within SLO
- Latency is within normal range

## Hypothesis

If one application pod is terminated within the defined blast radius, Kubernetes should replace it and user-visible availability should remain within the agreed tolerance.

## Blast Radius

One replica of the test workload only.

## Success Criteria

- Replacement pod becomes Ready
- No sustained increase in user-facing errors
- Recovery occurs within the target window

## Abort Conditions

Stop the experiment if impact exceeds the agreed tolerance.
