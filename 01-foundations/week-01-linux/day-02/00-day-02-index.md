# Day 2 — Linux Users, Groups & Permissions

## Learning path

1. [Linux Users](01-linux-users/users.md)
2. [UID and GID](02-uid-gid/uid-gid.md)
3. [Groups](03-groups/groups.md)
4. [/etc/passwd and /etc/group](04-etc-passwd-group/account-files.md)
5. [File Ownership](05-file-ownership/file-ownership.md)
6. [Linux Permissions](06-linux-permissions/linux-permissions.md)
7. [r, w, x Permissions](07-permission-rwx/rwx.md)
8. [Numeric Permissions](08-numeric-permissions/numeric-permissions.md)
9. [chmod](09-chmod/chmod.md)
10. [Symbolic chmod](10-symbolic-chmod/symbolic-chmod.md)
11. [Directory Permissions](11-directory-permissions/directory-permissions.md)
12. [chown](12-chown/chown.md)
13. [chgrp](13-chgrp/chgrp.md)
14. [sudo](14-sudo/sudo.md)
15. [Inspecting Files with ls/stat](15-inspecting-files/inspect-files.md)
16. [Permission Troubleshooting](16-permission-troubleshooting/troubleshooting.md)
17. [Hands-on Day 2 Lab](17-day02-lab/day02-lab.md)
18. [Day 2 Completion Checklist](18-day02-checklist/checklist.md)

## Recommended order

Study each file in order. Do the commands yourself in a disposable Ubuntu/WSL lab.

## Core mental model

```text
User
  ↓
Owner / Group / Others
  ↓
Permissions
  ↓
chmod / chown / chgrp
  ↓
Test access
  ↓
Troubleshoot Permission denied
```
