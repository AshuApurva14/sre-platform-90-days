# Compare SIGTERM and SIGKILL

Run:

```bash
sleep 300 &
PID $!

echo "PID=$PID"

```

Then:

```bash

kill -TERM $PID

```

Verify:

```bash
ps -p <PID>

```

Now repeat:

```bash

sleep 300 &
PID=$!

echo "PID=$PID"
kill -KILL "$PID"

ps -p "$PID"

```

You just observed two different termination mechanisms.


<img width="1055" height="726" alt="Image" src="https://github.com/user-attachments/assets/df347736-889e-47b5-8af7-f787d479db78" />