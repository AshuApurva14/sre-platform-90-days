# Learn `variables`

Create:
```bash
nano labs/variables.sh
```

Use:

```bash
#!/bin/bash

NAME="Ashutosh"
TOPIC="Linux"

echo "Name: $NAME"
echo "Topic: $TOPIC"
```

Run:
```bash
chmod 755 labs/variables.sh
./labs/variables.sh
```

Understand:

```bash
NAME="Ashutosh"
```
creates a variable.

And:
```bash
$NAME
```
reads its value.

## Important Bash rule

Don't put spaces around =.

Correct:
```bash
NAME="Ashutosh"

Incorrect:

NAME = "Ashutosh"
```

<img width="1391" height="789" alt="Image" src="https://github.com/user-attachments/assets/2bcd8343-671d-4fe4-93fe-adc1c7270763" />