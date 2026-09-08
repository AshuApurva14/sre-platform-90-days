# `chown` — Change Ownership

`chown` changes the owner of a file or directory and can also change its group.

## Change owner

```bash
sudo chown linuxuser file.txt
```

## Change owner and group

```bash
sudo chown linuxuser:devops file.txt
```

## Verify

```bash
ls -l file.txt
```

## When to use it

Use `chown` when the access problem is ownership-related and the ownership model is actually supposed to change.

Do not use it blindly. First determine who should own the resource.

## Help

```bash
man chown
chown --help
```
