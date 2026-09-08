# `r`, `w`, and `x` Permissions

## Regular files

```text
r → read
w → write
x → execute
```

Examples:

```text
rw- → read + write
r-x → read + execute
r-- → read only
--- → no access
```

### Read

Allows reading file contents, for example with `cat`.

### Write

Allows modifying file contents.

### Execute

Allows executing a program/script when other conditions also permit it.

## Directories

Directory permissions have operationally different meanings:

```text
r → list names/entries
w → create/delete/rename entries when combined with appropriate traversal access
x → traverse/access entries
```

The directory `x` permission is especially important when troubleshooting access to files inside nested directories.
