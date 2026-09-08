# UID and GID

## UID

UID means **User ID**. Linux internally uses a numeric UID to identify a user.

## GID

GID means **Group ID**. A process/user also has a primary group identity represented by a numeric GID.

## Why this matters

You will see numeric identities in DevOps systems, especially containers and Kubernetes security settings. For example, a container may be configured to run with a specific numeric UID.

## Commands

```bash
id
id -u
id -g
id -G
```

- `id -u` → user ID
- `id -g` → primary group ID
- `id -G` → all supplementary group IDs

## Example mental model

```text
username: ashutosh
UID:      1000
primary group: developers
GID:      1000
```

The actual values depend on your Linux system.

## Practice

```bash
printf 'User: '; whoami
printf 'UID: '; id -u
printf 'GID: '; id -g
printf 'Groups: '; id -G
```
