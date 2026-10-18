# Exercise A — command doesn't exist


```python
subprocess.run(["kubectlll", "get", "pods"])
```

Investigate:

```
Exception:
Root cause:
Fix:
Production impact:
```

Don't just say "typo."

Think about production:

- What happens if a Kubernetes health-check container doesn't have kubectl installed?