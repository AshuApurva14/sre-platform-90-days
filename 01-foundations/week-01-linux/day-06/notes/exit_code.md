# Understand exit codes

Run:
```bash
echo $?
```
The `$?` variable contains the exit status of the previous command.

Try:
```bash
ls /tmp
echo $?
```
Usually:
```bash
0
```
means success.


Now:

```bash
ls /does-not-exist
echo $?
```

You should get a non-zero value.

Mental model:

```bash
0       → success
non-zero → failure/error
```

This becomes extremely important in `CI/CD` later.

A `GitHub Actions` step, `shell script`, or `automation` tool needs to know whether an operation succeeded.


<img width="1935" height="430" alt="Image" src="https://github.com/user-attachments/assets/56b63350-a29f-488c-8ed2-3dca70454791" />