# Day 8 troubleshooting flow

User says:

```bash
"Application is down"
        |
        v
curl -v URL
        |
        v
Can I connect?
     /       \
   NO         YES
   |           |
TCP/DNS/      HTTP response
port issue       |
                 v
             Status code?
            /     |      \
          4xx    5xx     2xx
           |      |       |
       Request   Server   Request
       issue     issue    works
```
Your troubleshooting mindset should always be:

- Identify the layer first.
- Fix second.