## Lab 05 - `TCP troubleshooting`

Start the server again:

```bash
python3 -m http.server 8080
```
Check:

```bash
ss -lntp | grep 8080
```
Then:

```bash
nc -vz localhost 8080
```
Expected:

```bash
succeeded!
```

Then:

```bash
curl -I http://localhost:8080
```

You should see HTTP Headers.

<img width="1321" height="182" alt="Image" src="https://github.com/user-attachments/assets/3fcd420b-8cda-42ac-b3c7-63ac7602b9d0" />

<img width="925" height="384" alt="Image" src="https://github.com/user-attachments/assets/4e4ffd70-4b0d-4372-855c-f1548ded957c" />

---


You have now tested there layers:

```bash
ss
 ↓
Is something listening?

nc
 ↓
Can I establish TCP?

curl
 ↓
Can HTTP work?
```
That's a very useful mental model.