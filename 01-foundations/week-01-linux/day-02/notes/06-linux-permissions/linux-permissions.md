# Linux File Permissions

Linux permissions control who can read, modify, or execute a file and who can access a directory.

The three classes are:

```text
Owner
Group
Others
```

Example:

```text
-rwxr-x---
```

Breakdown:

```text
Owner  → rwx
Group  → r-x
Others → ---
```

## Why permissions matter

Permissions are part of least-privilege security. A production application should receive only the access it needs.

## Common examples

```text
644 → rw-r--r--
600 → rw-------
755 → rwxr-xr-x
700 → rwx------
```

## First troubleshooting principle

When you see `Permission denied`, inspect the user, ownership, group membership, permissions, and parent-directory traversal permissions before changing anything.
