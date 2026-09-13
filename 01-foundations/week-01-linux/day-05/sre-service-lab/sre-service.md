## Deliberately create a controlled service problem

This is your main recovery lab.

Rather than breaking a production service, create a tiny custom service in a VM/Linux environment where systemd is available.

Create a simple script
```bash
mkdir -p ~/sre-service-lab
nano ~/sre-service-lab/hello-service.sh
```
Use:
```bash
#!/bin/bash

while true
do
    echo "Service is running"
    sleep 10
done
```
Make it executable:
```bash
chmod 755 ~/sre-service-lab/hello-service.sh
```
Now create a systemd unit.

If you're working on a Linux VM or host with systemd:
```bash
sudo nano /etc/systemd/system/sre-demo.service
```
Use:
```bash
[Unit]
Description=SRE Learning Demo Service
After=network.target

[Service]
Type=simple
ExecStart=/home/YOUR_USER/sre-service-lab/hello-service.sh
Restart=on-failure
User=YOUR_USER

[Install]
WantedBy=multi-user.target
```
Replace YOUR_USER with your Linux username.

Then:
```bash
sudo systemctl daemon-reload
```
This tells systemd:

Re-read the unit files.

## Start your demo service

Run:
```bash
sudo systemctl start sre-demo
```
Check:
```bash
systemctl status sre-demo
```
You should see:
```bash
Active: active (running)
Main PID: ...
```
Now:
```bash
ps -p <MAIN_PID> -f
```
You've built the complete relationship:
```bash
sre-demo.service
       ↓
Main PID
       ↓
hello-service.sh

```

<img width="1410" height="785" alt="Image" src="https://github.com/user-attachments/assets/d4749075-1924-476d-9c90-960e5484790e" />

---

## Read your service logs

Because this service writes to standard output, systemd/journald can capture its output.

Run:

journalctl -u sre-demo -n 20

Then:

journalctl -u sre-demo -f

You should see:

Service is running
Service is running
...

Press:

Ctrl+C

<img width="913" height="929" alt="Image" src="https://github.com/user-attachments/assets/6d611d18-ec69-44af-ba0a-0fd0965c0fb2" />

---

## Create a service failure

Now intentionally break the service.

Edit the unit:
```bash
sudo nano /etc/systemd/system/sre-demo.service
```
Change:
```bash
ExecStart=/home/YOUR_USER/sre-service-lab/does-not-exist.sh
```
Reload:
```bash
sudo systemctl daemon-reload
```
Now:
```bash
sudo systemctl restart sre-demo
```
Check:
```bash
systemctl status sre-demo
```
It should fail.

This is exactly what we want.

You've created an operational incident.

<img width="1193" height="575" alt="Image" src="https://github.com/user-attachments/assets/a125839c-8158-4afb-9cbd-086d9ad39245" />

---

Investigate the failure

Do not fix it yet.

First:

systemctl status sre-demo

Then:

journalctl -u sre-demo -n 50

Then look at the error.

You should find that ExecStart points to something that doesn't exist.

This teaches the most important Day 5 pattern:

Service failed
      ↓
status
      ↓
logs
      ↓
identify error
      ↓
fix configuration
      ↓
reload
      ↓
restart
      ↓
verify
Step 23 — Fix the service

Restore the correct path:

ExecStart=/home/YOUR_USER/sre-service-lab/hello-service.sh

Then:

sudo systemctl daemon-reload

Restart:

sudo systemctl restart sre-demo

Verify:

systemctl status sre-demo

Then:

journalctl -u sre-demo -n 20

Finally:

ps -p <MAIN_PID> -f

You've now completed a realistic mini-incident.

<img width="1566" height="1403" alt="Image" src="https://github.com/user-attachments/assets/1899d76f-ff5c-40f6-8c6f-6f6b2df21dee" />

---

Understand daemon-reload

Remember this:

sudo systemctl daemon-reload

does not restart your service.

It tells systemd:

Re-read the service/unit configuration files.

Then you separately do:

sudo systemctl restart sre-demo

So:

Changed unit file
      ↓
daemon-reload
      ↓
restart/reload service as appropriate

This distinction is important.

Step 25 — Understand enablement

Once the service works:

sudo systemctl enable sre-demo

Check:

systemctl is-enabled sre-demo

Now you understand:

start
 ↓
running now

enable
 ↓
configured for automatic startup

You can stop/disable it afterward if you don't want it persisting:

sudo systemctl disable sre-demo
sudo systemctl stop sre-demo

<img width="1333" height="379" alt="Image" src="https://github.com/user-attachments/assets/a6da9198-edf0-4fe8-9f76-23070e6262d9" />

