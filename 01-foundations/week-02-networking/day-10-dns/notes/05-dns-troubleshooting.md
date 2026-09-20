## DNS Troubleshooting Checklist

1. Does the hostname resolve?
2. What IP address does it resolve to?
3. Which DNS server answered?
4. Is the answer expected?
5. Is there a CNAME?
6. What is the TTL?
7. Does another resolver return the same answer?



```bash
Application URL not working
          |
          v
     DNS lookup
          |
      +---+---+
      |       |
    FAIL    SUCCESS
      |       |
   DNS issue  |
              v
          TCP connection
              |
              v
             TLS
              |
              v
             HTTP
              |
              v
         Application
```

## Resolver Comparison

Resolver 1:

```bash
8.8.8.8
```

Resolver 2:

```bash
1.1.1.1
```

Purpose:

Compare DNS answers when investigating resolver or propagation-related problems.

<img width="1464" height="285" alt="Image" src="https://github.com/user-attachments/assets/1aaf5a5a-3ec5-4f6f-bfd0-043c7657ee96" />

The exact IP answers may differ or change. Record what you actually observe rather than copying an expected answer.

---

