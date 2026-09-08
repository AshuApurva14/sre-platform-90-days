# Numeric Permissions

Linux can represent `rwx` permissions with numbers.

```text
r = 4
w = 2
x = 1
```

Add the values:

```text
7 = rwx
6 = rw-
5 = r-x
4 = r--
3 = -wx
2 = -w-
1 = --x
0 = ---
```

Three digits represent:

```text
owner group others
```

## Common modes

### 644

```text
6 4 4
rw- r-- r--
```

### 600

```text
6 0 0
rw- --- ---
```

### 755

```text
7 5 5
rwx r-x r-x
```

## Exercise

Without looking at notes, translate these into `rwx` strings:

```text
640
660
750
700
```
