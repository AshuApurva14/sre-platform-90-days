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

## Step 1 - Solution

<img width="1321" height="404" alt="Image" src="https://github.com/user-attachments/assets/04567c2f-264f-4402-b085-e1986d6a61ab" />

If the user already exists, do not recreate it; continue with the existing account.

## 2. Create the group

```bash
sudo groupadd devops
sudo usermod -aG devops linuxuser
id linuxuser
getent group devops
```
## Step 2 - Solution

<img width="1319" height="318" alt="Image" src="https://github.com/user-attachments/assets/214530f9-6b09-42d3-a529-ba51707d3283" />

## 3. Create lab files

```bash
mkdir -p permissions-lab/testdir
cd permissions-lab
touch public.txt private.txt script.sh
```
## Step 3 - Solution

<img width="1279" height="346" alt="Image" src="https://github.com/user-attachments/assets/2d02c156-cc70-429e-a95d-de68ce0adba7" />


## 4. Set permissions

```bash
chmod 644 public.txt
chmod 600 private.txt
chmod 755 script.sh
```

## Step 3 - Solution

<img width="1205" height="516" alt="Image" src="https://github.com/user-attachments/assets/db817ac3-35da-4d70-9558-41348bfb89d9" />


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


## Ste 5 - Solution

<img width="1216" height="385" alt="Image" src="https://github.com/user-attachments/assets/4c02e0d2-73e2-416a-9b0d-1248135fb761" />


## 6. Create a permission failure

```bash
chmod 644 script.sh
./script.sh
```

Expected: permission denied or equivalent execution failure.

##  Step 6 - Solution

<img width="1139" height="273" alt="Image" src="https://github.com/user-attachments/assets/b72aee11-fc4a-4691-8920-b0ed458d157e" />

## 7. Diagnose

```bash
whoami
id
ls -l script.sh
ls -ld .
```

## Step 7 - Solution

<img width="2317" height="364" alt="Image" src="https://github.com/user-attachments/assets/34f103a7-912d-48c9-932b-cfc0a24d609a" />

## 8. Fix

```bash
chmod 755 script.sh
./script.sh
```

## Step 8 - Solution

<img width="1335" height="236" alt="Image" src="https://github.com/user-attachments/assets/731632ed-3464-4c34-8175-eaefa53cf079" />

## 9. Ownership experiment

```bash
sudo chown linuxuser:devops private.txt
ls -l private.txt
```

# Step 9 - Solution

<img width="1494" height="206" alt="Image" src="https://github.com/user-attachments/assets/492f61e6-43b8-4f65-9c35-45869d8d5bdb" />

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



## Step 10 - Solution

<img width="2289" height="694" alt="Image" src="https://github.com/user-attachments/assets/7e5fbbcb-b6ff-4282-8d5d-477dd6ba3ae2" />