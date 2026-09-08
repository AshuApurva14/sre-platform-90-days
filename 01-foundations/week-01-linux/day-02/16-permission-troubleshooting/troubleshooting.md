# Permission Troubleshooting

## Symptom

A command or application reports:

```text
Permission denied
```

## Do not jump to `chmod 777`

Use an evidence-based sequence.

## Step 1 — Identify the current user

```bash
whoami
id
```

## Step 2 — Inspect the file

```bash
ls -l <file>
```

Ask:

- Who owns it?
- What group owns it?
- What are the owner/group/other permissions?

## Step 3 — Inspect the path

```bash
ls -ld <directory>
```

For nested paths, inspect the parent directories too.

## Step 4 — Check group membership

```bash
groups
id
```

## Step 5 — Decide what the intended access model is

Ask:

```text
Who should access it?
What operation is required?
What is the minimum permission?
Should ownership or group membership change?
```

## Step 6 — Fix

Choose the narrowest correct change:

```bash
chmod ...
chown ...
chgrp ...
```

## Step 7 — Verify

Test the original operation again.

## Incident template

### Problem

### Expected behavior

### Actual behavior

### Investigation

### Root cause

### Fix

### Verification

### Lesson learned
