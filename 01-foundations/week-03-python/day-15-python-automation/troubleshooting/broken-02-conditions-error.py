"""
Task

Run it.

You may notice that:

95

doesn't produce the expected result.

Why?

Because Python checks conditions from top to bottom.

Fix the ordering.

Expected logic:

>= 90 → CRITICAL
>= 80 → WARNING
< 80  → OK


"""


cpu = 95

if cpu >= 80:
    print("OK")

elif cpu >= 90:
    print("CRITICAL")

else:
    print("NORMAL")


