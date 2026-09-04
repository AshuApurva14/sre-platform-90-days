import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent

files = [
    "README.md",
    "00-roadmap/90-day-roadmap.md",
    "00-roadmap/weekly-goals.md",
    "00-roadmap/progress.md",

    # Week 1
    "01-foundations/week-01-linux/README.md",
    "01-foundations/week-01-linux/notes/processes.md",
    "01-foundations/week-01-linux/notes/signals.md",
    "01-foundations/week-01-linux/notes/permissions.md",
    "01-foundations/week-01-linux/notes/users-groups.md",
    "01-foundations/week-01-linux/scripts/process-demo.sh",
    "01-foundations/week-01-linux/scripts/system-info.sh",
    "01-foundations/week-01-linux/exercises/troubleshooting.md",
    # Week 2
    "01-foundations/week-02-networking/README.md",
    "01-foundations/week-02-networking/notes/http.md",
    "01-foundations/week-02-networking/notes/dns.md",
    "01-foundations/week-02-networking/notes/tls.md",
    "01-foundations/week-02-networking/notes/tcp.md",
    "01-foundations/week-02-networking/labs/.gitkeep",
    "01-foundations/week-02-networking/troubleshooting/.gitkeep",
    # Week 3
    "01-foundations/week-03-python/README.md",
    "01-foundations/week-03-python/basics/.gitkeep",
    "01-foundations/week-03-python/exceptions/.gitkeep",
    "01-foundations/week-03-python/modules/.gitkeep",
    "01-foundations/week-03-python/files/.gitkeep",
    "01-foundations/week-03-python/subprocess/.gitkeep",
    "01-foundations/week-03-python/classes/.gitkeep",
    "01-foundations/week-03-python/logging/.gitkeep",
    "01-foundations/week-03-python/argparse/.gitkeep",
    "01-foundations/week-03-python/pytest/.gitkeep",
    # Week 4
    "01-foundations/week-04-docker/README.md",
    "01-foundations/week-04-docker/Dockerfile",
    "01-foundations/week-04-docker/app/.gitkeep",
    "01-foundations/week-04-docker/scripts/.gitkeep",
    "01-foundations/week-04-docker/notes/.gitkeep",
    # Week 5
    "02-delivery/week-05-ci-cd/README.md",
    "02-delivery/week-05-ci-cd/app/.gitkeep",
    "02-delivery/week-05-ci-cd/tests/.gitkeep",
    "02-delivery/week-05-ci-cd/.github/workflows/.gitkeep",
    # Week 6
    "02-delivery/week-06-kubernetes/README.md",
    "02-delivery/week-06-kubernetes/manifests/.gitkeep",
    "02-delivery/week-06-kubernetes/deployment.yaml",
    "02-delivery/week-06-kubernetes/service.yaml",
    "02-delivery/week-06-kubernetes/ingress.yaml",
    "02-delivery/week-06-kubernetes/notes/.gitkeep",
    # Week 7
    "02-delivery/week-07-release-engineering/README.md",
    "02-delivery/week-07-release-engineering/health-checks/.gitkeep",
    "02-delivery/week-07-release-engineering/rollback/.gitkeep",
    "02-delivery/week-07-release-engineering/release-checklist.md",
    "02-delivery/week-07-release-engineering/deployment-strategy.md",
    # Week 8
    "03-observability/week-08-observability/README.md",
    "03-observability/week-08-observability/prometheus/.gitkeep",
    "03-observability/week-08-observability/grafana/.gitkeep",
    "03-observability/week-08-observability/loki/.gitkeep",
    "03-observability/week-08-observability/logs/.gitkeep",
    "03-observability/week-08-observability/metrics/.gitkeep",
    "03-observability/week-08-observability/traces/.gitkeep",
    "03-observability/dashboards/service-dashboard.md",
    "03-observability/dashboards/infrastructure-dashboard.md",
    # Week 9
    "04-sre/week-09-slo-alerting/README.md",
    "04-sre/week-09-slo-alerting/slo.md",
    "04-sre/week-09-slo-alerting/error-budget",
    "04-sre/week-09-slo-alerting/alerting.md",
    # Week 10
    "04-sre/week-10-incident-response/README.md",
    "04-sre/week-10-incident-response/incidents/incident-response.md",
    "04-sre/week-10-incident-response/incidents/post-mortem.md",
    "04-sre/week-10-incident-response/incidents/communication.md",
    "04-sre/week-10-incident-response/runbooks/high_latency.md",
    "04-sre/week-10-incident-response/runbooks/high_cpu.md",
    "04-sre/week-10-incident-response/runbooks/high_memory.md",
    "04-sre/week-10-incident-response/runbooks/disk_full.md",
    "04-sre/week-10-incident-response/runbooks/network_outage.md",
    "04-sre/week-10-incident-response/runbooks/service_down.md",
    "04-sre/week-10-incident-response/runbooks/database_down.md",
    "04-sre/week-10-incident-response/runbooks/api_errors.md",
    "04-sre/week-10-incident-response/runbooks/ssl_certificate_expired.md",
    "04-sre/week-10-incident-response/runbooks/deployment_failure.md",
    "04-sre/week-10-incident-response/runbooks/third_party_service_outage.md",
    "04-sre/week-10-incident-response/runbooks/data_loss.md",
    "04-sre/week-10-incident-response/runbooks/security_breach.md",
    "04-sre/week-10-incident-response/runbooks/denial_of_service_attack.md",
    "04-sre/week-10-incident-response/runbooks/unauthorized_access.md",
    "04-sre/week-10-incident-response/runbooks/critical_bug.md",
    "04-sre/week-10-incident-response/runbooks/slow_response_time.md",
    "04-sre/week-10-incident-response/runbooks/memory_leak.md",
    "04-sre/week-10-incident-response/runbooks/high_disk_io.md",
    "04-sre/week-10-incident-response/runbooks/high_network_latency.md",
    "04-sre/week-10-incident-response/runbooks/high_error_rate.md",
    "04-sre/week-10-incident-response/runbooks/high_database_load.md",
    "04-sre/week-10-incident-response/runbooks/high_api_latency.md",
    "04-sre/week-10-incident-response/runbooks/high_queue_length.md",
    "04-sre/week-10-incident-response/postmortems/README.md",

    # Week 11
    "04-sre/week-11-chaos-engineering/README.md",
    "04-sre/week-11-chaos-engineering/experiments/pod_failure.md",
    "04-sre/week-11-chaos-engineering/experiments/container_kill.md",
    "04-sre/week-11-chaos-engineering/experiments/network_delay.md",
    "04-sre/week-11-chaos-engineering/experiments/dependency_failure.md",
    "04-sre/week-11-chaos-engineering/hypotheses/README.md",
    "04-sre/week-11-chaos-engineering/results/README.md",

    # week 12
    "04-capstone/week-12-capstone/README.md",
    "04-capstone/week-12-capstone/application/.gitkeep",
    "04-capstone/week-12-capstone/tests/.gitkeep",
    "04-capstone/week-12-capstone/Dockerfile",
    "04-capstone/week-12-capstone/Kubernetes/.gitkeep",
    "04-capstone/week-12-capstone/Helm/.gitkeep",
    "04-capstone/week-12-capstone/Monitoring/.gitkeep",
    "04-capstone/week-12-capstone/Observability/.gitkeep",
    "04-capstone/week-12-capstone/CI-CD/.gitkeep",
    "04-capstone/week-12-capstone/chaos-engineering/.gitkeep",
    "04-capstone/week-12-capstone/incidents/.gitkeep",
    "04-capstone/week-12-capstone/runbooks/.gitkeep",
    "04-capstone/week-12-capstone/architecture/architecture.md",

    "06-cheatsheets/README.md",
    "06-cheatsheets/linux.md",
    "06-cheatsheets/week-12-cheatsheets/networking.md",
    "06-cheatsheets/week-12-cheatsheets/python.md",
    "06-cheatsheets/week-12-cheatsheets/docker.md",
    "06-cheatsheets/week-12-cheatsheets/kubernetes.md",
    "06-cheatsheets/week-12-cheatsheets/ci-cd.md",
    "06-cheatsheets/week-12-cheatsheets/observability.md",
    "06-cheatsheets/week-12-cheatsheets/sre.md",
    "06-cheatsheets/week-12-cheatsheets/chaos-engineering.md",
    "06-cheatsheets/week-12-cheatsheets/capstone.md",
    "06-cheatsheets/week-12-cheatsheets/architecture.md",
    "06-cheatsheets/week-12-cheatsheets/incident-response.md",
    "06-cheatsheets/week-12-cheatsheets/release-engineering.md",
    "06-cheatsheets/week-12-cheatsheets/monitoring.md",
    "06-cheatsheets/week-12-cheatsheets/logging.md",
    "06-cheatsheets/week-12-cheatsheets/metrics.md",
    "06-cheatsheets/week-12-cheatsheets/tracing.md",
    "06-cheatsheets/week-12-cheatsheets/slo-alerting.md",

    "07-interviews-prep/week-12-interviews/README.md",
    "07-interviews-prep/week-12-interviews/linux.md",
    "07-interviews-prep/week-12-interviews/networking.md",
    "07-interviews-prep/week-12-interviews/python.md",
    "07-interviews-prep/week-12-interviews/docker.md",
    "07-interviews-prep/week-12-interviews/kubernetes.md",
    "07-interviews-prep/week-12-interviews/ci-cd.md",
    "07-interviews-prep/week-12-interviews/observability.md",
    "07-interviews-prep/week-12-interviews/sre.md",
    "07-interviews-prep/week-12-interviews/chaos-engineering.md",
    "07-interviews-prep/week-12-interviews/capstone.md",

    "08-daily-learning/2026-09-07.md",
    "08-daily-learning/2026-09-08.md",
    "08-daily-learning/2026-09-09.md",
    "08-daily-learning/2026-09-10.md",
    "08-daily-learning/2026-09-11.md",
    "08-daily-learning/2026-09-12.md",
    


    
    ]

for files_path in files:
    file_path = base_dir / files_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch(exist_ok=True)

print(f"Created files in: {base_dir}/")
