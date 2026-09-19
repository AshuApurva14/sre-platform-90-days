# HTTP Troubleshooting

## Measure API Performance

## Basic Test

```bash
curl -v URL
```

Useful for seeing request and response details.

## Status Code

```bash
curl -I URL
```

Useful for quickly inspecting response headers/status.

## Response Time

```bash
curl -s \
-o /dev/null \
-w "HTTP Code: %{http_code}\nTime: %{time_total}s\n" \
URL

```

Useful for measuring basic request latency.


<img width="1541" height="330" alt="Image" src="https://github.com/user-attachments/assets/e971cddf-463b-42c2-8efa-516c537d6f57" />

---



