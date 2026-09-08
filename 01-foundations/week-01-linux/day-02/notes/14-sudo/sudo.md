# `sudo` — Run a Command with Elevated Privileges

`sudo` lets an authorized user execute a command with elevated privileges, commonly as root.

## Example

```bash
whoami
sudo whoami
```

Typical result:

```text
normal user
root
```

## Why it matters

Administrative tasks such as creating users, creating groups, changing ownership of files owned by another user, and managing services may require elevated privileges.

## Good habit

Do not use `sudo` for everything. Ask:

> Does this command genuinely require elevated privileges?

Prefer a normal user for routine work and elevate only the command that needs it.

## Exercise

```bash
whoami
sudo whoami
sudo id
```

Compare the identity information.
