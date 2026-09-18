# HTTP Troubleshooting

When an application is unavailable, I should not immediately restart it.

I should identify where the request is failing.

## Step 1 - Test connectivity

```bash
curl -v https://httpbin.org/get

```

<img width="1711" height="1583" alt="Image" src="https://github.com/user-attachments/assets/faa3df22-a1c2-4913-8aa0-66abe15abd9e" />

## Step 2 - Check HTTP status

Look for:

```bash
200
401
403
404
500
502
503
504

```

## Step 3 - Inspect headers

curl -I https://httpbin.org/get

<img width="1307" height="234" alt="Image" src="https://github.com/user-attachments/assets/2ec8c261-82fe-4151-a753-91d7ab3e5039" />


## Step 4 - Measure response time


```bash
curl -s \
-o /dev/null \
-w "HTTP: %{http_code}\nTime: %{time_total}s\n" \
https://httpbin.org/get

```

<img width="1139" height="189" alt="Image" src="https://github.com/user-attachments/assets/445afb65-b9de-4cd9-9b54-3a767fc873a6" />

