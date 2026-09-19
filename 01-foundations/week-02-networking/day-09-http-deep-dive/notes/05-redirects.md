# HTTP redirects

Understand:

```bash
301
302
307
308
```

Run:

```bash
curl -I http://httpbin.org/redirect/1
```

You may see a `redirect response.`

Now:

```bash
curl -I https://httpbin.org/redirect/1
```

Then `follow redirects:`

```bash
curl -L https://httpbin.org/redirect/1
```

The important curl option:

```bash
-L
```

means:

```bash
Follow redirects.
```

<img width="1359" height="764" alt="Image" src="https://github.com/user-attachments/assets/1a52f062-d4aa-4f38-b397-a51ee943cf1e" />

---

## Why redirects matter to DevOps

Imagine:

```bash
http://myapp.com
       |
       | 301
       v
https://myapp.com
```

Or:

```bash
old.example.com
       |
       | 301
       v
new.example.com
```

Troubleshooting redirects is important because incorrect redirect configuration can cause:

```bash
Redirect loops
Unexpected HTTP → HTTPS behavior
Wrong hostname
Authentication problems
```

