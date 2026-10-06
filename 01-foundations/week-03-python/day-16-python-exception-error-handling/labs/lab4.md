## Lab 4 Architecture

```
             server data
                    │
                    ▼
             ┌─────────────┐
             │ Validate    │
             │ input       │
             └──────┬──────┘
                    │
          ┌─────────┴─────────┐
          │                   │
       valid                invalid
          │                   │
          ▼                   ▼
    Check resources      Handle error
          │                   │
          ▼                   ▼
    CPU / Memory /       Useful error
       Disk                  message
          │
          ▼
    Overall status
```

This is the pattern I want you to remember:

```
Validate → Process → Handle failure → Report clearly
```