# Lab 03 - `netcat`

**A simple Linux utility which reads and writes data across network connections using TCP or UDP protocol.**

Below are the usecases of this command:



Run:

```bash
nc -h
```

## Creating a raw TCP server

Terminal 1:

```bash
nc -lv 9000
```

Depending upon your version of netcat the output may look like:

```bash
Listening on 0.0.0.0 9000
```

Terminal 2:

```bash
nc localhost 9000
```
Type:

```bash
Hello TCP
```

On terminal 1, you should see:

```bash
Hello TCP
```

<img width="1265" height="222" alt="Image" src="https://github.com/user-attachments/assets/6cd7d34b-b668-4866-ac72-6202b6fb1913" />

<img width="819" height="122" alt="Image" src="https://github.com/user-attachments/assets/8b9597a6-be48-49c0-b2c7-87b14a3fa2a5" />

---

Congratulations:

You have created:

```bash
TCP client
    │
    │ TCP
    ↓
TCP server
```

## Understand what just happened

Terminal 1:

```bash
nc -lv 9000
```

is the server.

It listens:

```bash
0.0.0.0:9000
```

Terminal 2:

```bash
nc localhost 9000
```

is the client.

It establishes:

```bash
client ephemeral port
        ↓
localhost:9000
```

Now data can flow.