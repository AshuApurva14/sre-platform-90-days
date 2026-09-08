# `chmod` — Change File Permissions

`chmod` changes access permissions on files and directories.

## Numeric form

```bash
chmod 644 file.txt
chmod 600 secrets.txt
chmod 755 script.sh
```

Verify:

```bash
ls -l file.txt secrets.txt script.sh
```

## Why `chmod 777` should not be the default fix

`777` grants `rwx` to owner, group, and others. That is usually much broader access than required. Prefer the minimum permission needed for the task.

## Practice

```bash
touch demo.txt
chmod 600 demo.txt
ls -l demo.txt
chmod 644 demo.txt
ls -l demo.txt
```

## Help

```bash
man chmod
chmod --help
```
