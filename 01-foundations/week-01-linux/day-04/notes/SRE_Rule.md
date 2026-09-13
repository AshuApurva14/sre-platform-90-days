# The important SRE Rule: graceful vs forceful

Think about an application such as a Web server.

You generally don't want:

```bash
SIGKILL
 ↓
connections immediately disappear

```

You would prefer:

```bash
SIGTERM
 ↓
application receives shutdown request
 ↓
cleanup
 ↓
close connections
 ↓
exit
```

That is why Kubernetes also has graceful termination behavior when pods are terminated. This connection is worth remembering for later.