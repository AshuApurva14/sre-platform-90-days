# Troubleshooting Table

| Symptom        |         Likely Area                 |            First Commands           |
|----------------|-------------------------------------|-------------------------------------|    
|
Symptom	Likely area	First command
Could not resolve host	DNS	dig
NXDOMAIN	DNS	dig
No route to host	Routing/network	ip route
Connection refused	TCP/service	nc -vz
Connection timed out	Firewall/network/LB	nc -vz
TLS handshake failure	TLS	openssl s_client
Certificate error	TLS/certificate	openssl s_client
400	HTTP/application	curl -v
401	Authentication	curl -v
403	Authorization	curl -v
404	URL/routing/application	curl -v
502	Proxy/upstream	LB/Ingress/backend
503	Service unavailable	Kubernetes/service/pods
504	Upstream timeout	network/backend/application

This table should eventually become part of your personal DevOps troubleshooting handbook.