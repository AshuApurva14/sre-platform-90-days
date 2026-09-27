# tcpdump

- tcpdump lets me observe packets traveling through a network interface.
- Allow list interfaces.
- Allow capture traffic over specific port and from/to a host.

List interface:

```
tcpdump -D 
```

Capture traffic:

```
sudo tcpdump -i any
```

Capture port 443:

```
sudo tcpdump -i any port 443
```

Capture packets from/to a host:

```bash
sudo tcpdump -i any host 8.8.8.8
```