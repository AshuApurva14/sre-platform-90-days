# Directory Permissions

Directory permissions deserve special attention because `r`, `w`, and `x` mean different things operationally than for regular files.

## Meaning

```text
r → list directory entries
w → create/delete/rename entries (with suitable traversal access)
x → traverse/enter/access the directory
```

## Inspect a directory itself

```bash
mkdir testdir
ls -ld testdir
```

Use `ls -ld`, not just `ls -l`, when you want the permissions of the directory itself.

## Example scenario

A process can have permission on `/opt/app/file.txt` but still fail because it cannot traverse one of the parent directories.

Inspect each path component when debugging.

## Exercise

```bash
mkdir -p dir-lab/a/b
touch dir-lab/a/b/file.txt
ls -ld dir-lab dir-lab/a dir-lab/a/b
```

Then experiment carefully with directory modes such as `700` and `755` and observe the effect.
