# `chgrp` — Change Group Ownership

`chgrp` changes the group associated with a file or directory.

Example:

```bash
sudo chgrp devops application.log
```

Verify:

```bash
ls -l application.log
```

Mental model:

```text
chmod → access permissions
chown → owner and/or group ownership
chgrp → group ownership
```

## Exercise

1. Create `shared.txt`.
2. Create or reuse a `devops` group.
3. Change `shared.txt` to group `devops`.
4. Set group-friendly permissions.
5. Verify with `ls -l`.
