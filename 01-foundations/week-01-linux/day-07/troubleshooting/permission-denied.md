# Incident -2 Permission denied

Create:
```bash
mkdir -p permission-lab
echo "Sensitive information" > permission-lab/secret.txt
```
Set restrictive permissions:
```bash
chmod 600 permission-lab/secret.txt
```
Check:
```bash
ls -l permission-lab/secret.txt
```
You should see something similar to:
```bash
ls -l permission-lab/secret.txt
```
You should see something similar to:
```bash
-rw-------
```
---

## Create the permission problem

If you have your linuxuser lab account, change ownership:
```bash
sudo chown linuxuser:linuxuser permission-lab/secret.txt
```
Then:
```bash
ls -l permission-lab/secret.txt
```
Try:
```bash
cat permission-lab/secret.txt
```
Depending on which user you're currently using, you may get:
```bash
Permission denied
```
Now troubleshoot.

<img width="1708" height="628" alt="Image" src="https://github.com/user-attachments/assets/ffc5f764-c956-4f1a-a660-da73ea332584" />

---

## Permission troubleshooting sequence

Run:
```bash
whoami
```
Then:
```bash
id
```
Then:
```bash
ls -l permission-lab/secret.txt
```
And:
```bash
ls -ld permission-lab
```
Ask:
```bash
Am I the owner?
Am I in the file's group?
What permissions does my access category have?
```
Then apply the minimum required fix.

Don't use:
```bash
chmod 777
```
just to make the error disappear.

This is exactly the troubleshooting mindset you want to take into Kubernetes and production systems.

<img width="2306" height="539" alt="Image" src="https://github.com/user-attachments/assets/0dd7913d-5fe6-4aba-9dad-dea3a35d083f" />

