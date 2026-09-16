# Incident 1 - Application is down

This is your main Day 7 lab.

We'll create a tiny application using Python's built-in HTTP server.

Go to:
```bash
cd ~/sre-90-days/week-01/day-07
```
Create a test directory:
```bash
mkdir -p web-app
echo "Week 1 SRE Lab Application" > web-app/index.html
```
Start the application:
```bash
cd web-app
python3 -m http.server 8080 > ../troubleshooting/app.log 2>&1 &
```
Find the PID:
```bash
pgrep -f "http.server 8080"
```
Suppose it gives:
```bash
12345
```

---

## Verify the application

Test HTTP:
```bash
curl http://localhost:8080
```

You should see:
```
Week 1 SRE Lab Application
```

Now verify the process:

```bash
ps -p 12345 -f
```

Replace 12345 with your real PID.

Now verify the port:
```bash
ss -lntp | grep 8080
```

You should see something listening on port 8080.

You have now verified:
```bash
Application
    ↓
Process
    ↓
PID
    ↓
Port
    ↓
HTTP response

```

<img width="1629" height="785" alt="Image" src="https://github.com/user-attachments/assets/68c99e5c-c55b-4cf2-9f21-ad44dff79d75" />

---

## Break the application

Now stop it:
```bash
kill 12345
```
Again, use your real PID.

Check:
```bash
curl http://localhost:8080
```
It should fail.

Excellent.

You've created the incident:
```bash
Application is unavailable.
```

<img width="1244" height="127" alt="Image" src="https://github.com/user-attachments/assets/83f9754a-7767-4452-b3e6-421aa0635d07" />

---

## Troubleshoot without immediately restarting

Pretend you're an on-call engineer.

Step 1 — Is the process running?
pgrep -f "http.server 8080"

No result?

Good.

Step 2 — Is port 8080 listening?
ss -lntp | grep 8080

No result?

Good.

Step 3 — Check the application log
cat ~/sre-90-days/week-01/day-07/troubleshooting/app.log
Step 4 — Determine the recovery action

The process is gone, so you need to restart it.

## Recover the application

Start it again:
```bash
cd ~/sre-90-days/week-01/day-07/web-app

python3 -m http.server 8080 \
    > ../troubleshooting/app.log 2>&1 &
```
Find PID:
```bash
pgrep -f "http.server 8080"
```
Verify:
```bash
curl http://localhost:8080
```
Then:
```bash
ss -lntp | grep 8080
```
And:
```bash
ps -p <PID> -f
```
Your recovery is now proven by evidence, not by assuming that the process started.

<img width="1667" height="521" alt="Image" src="https://github.com/user-attachments/assets/33b00258-d40c-4f94-8388-c93399b14383" />

---

