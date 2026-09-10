# Inspecting Files: `ls` and `stat`

## `ls -l`

Use `ls -l` for a compact view of file type, permissions, owner, group, size, and timestamps.

```bash
ls -l file.txt
```

## `ls -ld`

Use `ls -ld directory` to inspect the directory itself.

```bash
ls -ld /tmp
```

## `stat`

`stat` provides more detailed metadata.

```bash
stat file.txt
```

Useful when you need detailed information such as numeric UID/GID and precise timestamps.

## Exercise

```bash
touch inspect.txt
chmod 640 inspect.txt
ls -l inspect.txt
stat inspect.txt
```

Compare the high-level view from `ls -l` with the detailed output from `stat`.


## solution

<img width="1139" height="427" alt="Image" src="https://github.com/user-attachments/assets/32f67e32-32e4-4103-ae30-255ebb431a38" />