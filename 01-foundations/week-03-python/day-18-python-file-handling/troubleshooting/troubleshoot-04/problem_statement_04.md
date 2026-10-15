# Broken #4 — Path problem

## Issue

<img width="1988" height="208" alt="Image" src="https://github.com/user-attachments/assets/3ae6a542-23d0-4c44-97d6-378b616c0cf5" />


---
This is particularly important for DevOps engineers.

Suppose:

```python
project/
├── data/
│   └── servers.txt
└── main.py
```

This won't necessarily be correct:

```python
open("servers.txt")
```

because the file is under:

```python
data/servers.txt
```

You may need:
```python
open("data/servers.txt")
```

Later we'll improve this using:
```python
pathlib
```


because filesystem paths become important in production automation.
