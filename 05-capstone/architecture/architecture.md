# Capstone Architecture

```text
Developer
   |
   v
GitHub -> GitHub Actions -> Container Registry
   |
   v
Kubernetes -> Service -> Application
                  |
          +-------+-------+
          |       |       |
       Metrics   Logs   Traces
          |       |       |
       Prometheus Loki OpenTelemetry/trace backend
          \        |      /
           \       |     /
             Grafana
                 |
              Alerts
                 |
            Incident/Runbook
```

Replace components with the ones available in your lab environment.
