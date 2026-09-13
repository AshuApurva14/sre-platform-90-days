# Learn `bg`, `fg` and `ctrl+z`

## `Ctrl + Z`

`Ctrl+z` is used to stop the process runn

Run :

```bash
sleep 300

```

Press:

```bash

Ctrl + Z
```

Now:

```bash
jobs
```

You will see the stopped job.

This gives you practical connection:

```bash
Ctrl+Z
   ↓
process/job stopped

```

---


## `bg`

Continue that stopped job in the background:

```bash

bg %1
```

Then:

```bash
jobs
```

It should be running now in background.

Mental model:

```bash
stopped job
    ↓
bg
    ↓
running in background

```

## `fg`

Start another process:

```bash

sleep 300 &

```

Then:

```bash
jobs
```

Bring into the foreground:

```bash

fg %1

```

then stop with:

```bash
Ctrl+C

```

Mental model:

```bash
bg → continue in background
fg → move job to foreground
```

