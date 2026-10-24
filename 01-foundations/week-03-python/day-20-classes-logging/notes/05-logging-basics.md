# Logging

This is the most important Day 20 topic for your SRE path.

## Why isn't print() enough?

Until now we've written:

```
print("Command failed")
```

That tells us something failed.

But in production we need questions answered:

```
WHEN did it fail?
WHERE did it fail?
HOW severe was it?
WHAT command failed?
WHAT was the error?
```

Compare:

```
Command failed
```

with:

```
2026-10-18 17:25:10 ERROR command_runner Command failed: kubectl get pods
```

The second is operationally useful.

That's where logging comes in.