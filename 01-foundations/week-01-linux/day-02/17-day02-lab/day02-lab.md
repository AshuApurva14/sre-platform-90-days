# Day 2 Hands-On Lab

## Goal

Create a safe lab that demonstrates users, groups, ownership, permissions, and a realistic `Permission denied` recovery.

## 1. Create a lab user

```bash
sudo useradd --create-home linuxuser
sudo passwd linuxuser
id linuxuser
ls -ld /home/linuxuser
```

If the user already exists, do not recreate it; continue with the existing account.

## 2. Create the group

```bash
sudo groupadd devops
sudo usermod -aG devops linuxuser
id linuxuser
getent group devops
```

## 3. Create lab files

```bash
mkdir -p permissions-lab/testdir
cd permissions-lab
touch public.txt private.txt script.sh
```

## 4. Set permissions

```bash
chmod 644 public.txt
chmod 600 private.txt
chmod 755 script.sh
```

Verify:

```bash
ls -l
```

## 5. Create a script

```bash
cat > script.sh <<'EOF'
#!/bin/bash
echo "Backup started"
EOF

chmod 755 script.sh
./script.sh
```

## 6. Create a permission failure

```bash
chmod 644 script.sh
./script.sh
```

Expected: permission denied or equivalent execution failure.

## 7. Diagnose

```bash
whoami
id
ls -l script.sh
ls -ld .
```

## 8. Fix

```bash
chmod 755 script.sh
./script.sh
```

## 9. Ownership experiment

```bash
sudo chown linuxuser:devops private.txt
ls -l private.txt
```

## 10. Capstone-style permission project

Create:

```text
permissions-project/
├── public/
│   └── application.log
├── private/
│   └── secrets.txt
└── scripts/
    └── backup.sh
```

Suggested permissions:

```text
application.log → 644
secrets.txt     → 600
backup.sh       → 755
```

Explain why each choice is appropriate.
