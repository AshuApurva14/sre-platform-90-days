# Day 14 — End-to-End Network Troubleshooting

## Objective

Build and troubleshoot a complete application request path:

DNS → TCP → TLS → HTTP → Kubernetes → Application

## Topics

- DNS troubleshooting
- TCP troubleshooting
- HTTP troubleshooting
- TLS troubleshooting
- Kubernetes Service
- Kubernetes Endpoints
- Pod readiness
- Ingress
- Connection refused
- Connection timeout
- HTTP 5xx
- End-to-end troubleshooting

## Core Methodology

Symptom
→ Define impact
→ DNS
→ Routing
→ TCP
→ TLS
→ HTTP
→ Load Balancer
→ Ingress
→ Service
→ Endpoints
→ Pod
→ Application

## Practical Labs

1. Build nginx application
2. Test DNS
3. Test TCP
4. Test HTTP
5. Test Kubernetes Service
6. Break Service selector
7. Troubleshoot no endpoints
8. Delete pod
9. Observe Kubernetes recovery
10. Simulate production incident

## Definition of Done

- [ ] Understand complete request flow
- [ ] Troubleshoot DNS
- [ ] Troubleshoot TCP
- [ ] Troubleshoot TLS
- [ ] Troubleshoot HTTP
- [ ] Troubleshoot Kubernetes Service
- [ ] Troubleshoot endpoints
- [ ] Explain connection refused
- [ ] Explain connection timeout
- [ ] Explain 502/503/504
- [ ] Complete production incident simulation
- [ ] Document root cause and fix
- [ ] Complete interview questions