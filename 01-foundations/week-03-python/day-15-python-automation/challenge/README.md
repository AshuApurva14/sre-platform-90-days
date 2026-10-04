
---

# Challenge

## `challenge/README.md`

```markdown
# Day 15 Challenge — Server Health Checker

## Objective

Build a server health checker without following the Lab 3 implementation.

---

# Requirements

The program must check:

- CPU
- Memory
- Disk

---

# Thresholds

| Usage | Status |
|---|---|
| < 80 | OK |
| 80–89 | WARNING |
| >= 90 | CRITICAL |

---

# Required Functions

Your program must contain:

```python
check_cpu()
check_memory()
check_disk()
overall_status()
main()