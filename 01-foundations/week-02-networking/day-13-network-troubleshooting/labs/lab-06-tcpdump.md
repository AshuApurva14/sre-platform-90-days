# Lab 6 — tcpdump

Terminal 1:

```python
python3 -m http.server 8080
```

Terminal 2:

```bash
sudo tcpdump -i any port 8080
```

Terminal 3:

```bash
curl http://localhost:8080
```

Look at the packets.

You don't need to understand every field.

Your goal is simply to connect:

```
curl
 ↓
TCP connection
 ↓
packets
 ↓
server
```