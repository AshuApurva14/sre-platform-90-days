# Linux Groups

## What is a group?

A group is a collection of users used to manage shared access. Instead of giving permissions separately to every user, a file or directory can be assigned to a group.

## Useful commands

```bash
groups
id
getent group
getent group <group>
```

## Create a lab group

```bash
sudo groupadd devops
getent group devops
```

## Add a user to a supplementary group

```bash
sudo usermod -aG devops linuxuser
```

Important: `-G` specifies supplementary groups and `-a` appends instead of replacing the existing supplementary group list.

## Verify

```bash
id linuxuser
```

## Example

```text
users → alice, bob, carol
        ↓
group → developers
        ↓
shared project files
```

## Exercise

Create a group called `devops`, add `linuxuser`, and verify the membership.
