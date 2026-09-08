# Linux Users

## What is a Linux user?

A Linux user is an identity used by the operating system to associate processes and resources with a person, service, or other account. Every local user has a numeric UID.

## Why users matter in DevOps

Applications and services should not automatically run as root. A service can run as a dedicated user such as `appuser`, allowing access to only the resources it needs.

## Useful commands

```bash
whoami
id
id -u
getent passwd <username>
```

### `whoami`

Shows the effective username of the current shell/process.

### `id`

Shows the current user ID, primary group ID, and supplementary groups.

### `getent passwd`

Queries the system account database using the configured name service sources.

## Practice

```bash
whoami
id
id -u
getent passwd "$(whoami)"
```

## Questions

- Which user am I?
- What is my UID?
- What is my primary group?
- Which supplementary groups do I have?
