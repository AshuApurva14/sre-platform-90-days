# `/etc/passwd` and `/etc/group`

## `/etc/passwd`

Local Linux account information is commonly represented in `/etc/passwd`. A typical entry looks like:

```text
root:x:0:0:root:/root:/bin/bash
```

Conceptually the fields are:

```text
username
password placeholder / account field
UID
GID
GECOS/description
home directory
login shell
```

Inspect it with:

```bash
cat /etc/passwd
grep "^$(whoami):" /etc/passwd
```

## `/etc/group`

Group information is commonly represented in `/etc/group`.

```bash
cat /etc/group
getent group
getent group devops
```

## Important safety note

Do not edit `/etc/passwd` or `/etc/group` manually during this lab. Learn to use account-management commands such as `useradd`, `usermod`, and `groupadd`.
