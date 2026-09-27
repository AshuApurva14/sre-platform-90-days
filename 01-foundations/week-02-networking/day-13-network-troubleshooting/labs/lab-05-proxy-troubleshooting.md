# Proxy Investigation

Run:

```bash
env | grep -i proxy
```

Then:

```bash
curl -v https://example.com
```

Look at whether curl is connecting directly or through a proxy.

Don't change your corporate proxy configuration unless you know the environment requirements.