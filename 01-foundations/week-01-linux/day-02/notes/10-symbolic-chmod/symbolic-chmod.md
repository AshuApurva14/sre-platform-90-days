# Symbolic `chmod`

Symbolic mode changes selected permissions instead of replacing the full numeric mode.

## User classes

```text
u → owner/user
g → group
o → others
a → all
```

## Operators

```text
+ → add
- → remove
= → set exactly
```

## Examples

```bash
chmod u+x script.sh
chmod g+r application.log
chmod o-r private.txt
chmod a+x deploy.sh
```

## Inspect after each change

```bash
ls -l script.sh
```

## Exercise

1. Create `exercise.sh`.
2. Make it executable only for the owner.
3. Add read permission for the group.
4. Remove read permission from others.

Try using symbolic commands rather than a single numeric command.
