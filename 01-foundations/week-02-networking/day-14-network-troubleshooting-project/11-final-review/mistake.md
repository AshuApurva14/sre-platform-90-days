# Day 14 Mistakes

Record mistakes honestly.

Examples:

## Mistake 1

I initially checked Kubernetes before checking DNS.

### Correct approach

Start from the request path and collect evidence.

---

## Mistake 2

I confused connection refused and timeout.

### Correct understanding

Refused:
Destination reached but port isn't accepting.

Timeout:
No response received.

---

## Mistake 3

I assumed Running means Ready.

### Correct understanding

Running != Ready.

---

## Mistake 4

I didn't check Service endpoints.

### Correct approach

Whenever Service traffic is failing:

Service
→ Endpoints
→ Pod