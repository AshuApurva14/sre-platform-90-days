# File Ownership

Every file has an owner and an associated group.

Example:

```text
-rw-r--r-- 1 appuser developers 120 Sep 8 20:00 app.log
```

Here:

```text
Owner → appuser
Group → developers
```

Inspect ownership with:

```bash
ls -l app.log
```

## Why ownership matters

When Linux checks access, it needs to know which user and group permissions apply.

## Practice

```bash
touch ownership.txt
ls -l ownership.txt
sudo chown linuxuser ownership.txt
ls -l ownership.txt
```

Then restore ownership to your normal lab user if needed.
