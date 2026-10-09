# Lab 1 Architectural breakdown

Previously:

```
health_check.py
```

contained everything.

We're going to split it.

```
lab-01-split-health-check/
├── main.py
├── health.py
└── validation.py
```

Responsibilities:

```
validation.py
      ↓
Validate input

health.py
      ↓
Calculate health status

main.py
      ↓
Control the application
```

This is your first step toward real software structure.

Notice what happened.

health.py doesn't need to duplicate:

```
if not isinstance(...)
```

Instead:

```
from validation import validate_percentage
```

and then:
```
validate_percentage(cpu, "CPU")
```

This is code reuse.

---

## Understand the import chain

This is the most important part of today's lab.

When you execute:

```
python main.py
```

Python does roughly:

```
main.py
   │
   ├── import health
   │       │
   │       └── import validation
   │
   └── main()
         │
         ├── check_cpu()
         ├── check_memory()
         ├── check_disk()
         └── overall_status()

So your application becomes:

                 main.py
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
       health.py          validation.py
          │
          └───────────────→ validation.py
```

This is the foundation of larger Python applications.