# Understand `start`, `stop` and `restart`

Follow below steps:

<img width="1590" height="1828" alt="Image" src="https://github.com/user-attachments/assets/bad01f5a-8e42-4d2d-bae7-168910e8d80f" />



### Important operational habit

Don't restart first.
```bash
First:

status
↓
logs
↓
understand problem
↓
restart if appropriate
```
This is important because restarting a failing service can sometimes temporarily hide the actual problem.

---

# understand `enable` vs `start`

`start` means start the service now.


`enable` means configure it to start automatically according to systemd boot configuration.

Typical workflow:

```bash
enable
+
start

```

<img width="1538" height="1125" alt="Image" src="https://github.com/user-attachments/assets/7e06ec8a-90ba-42ce-8b31-fd43f785c77a" />


which enables and starts it.

You don't need to practice this against a critical service today; understand the concept.
