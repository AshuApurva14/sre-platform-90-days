## File system in Linux

### Root Directory

It is a logical structure that stores and access files within that space.

- `/` - The root of entire filesystem tree.
- `/home` - Personal directory for each non-root user.
- `/tmp` - Temporary files
- `etc` - System-wide configurations files
- `var` - Variable data which changes during normal operations such as files like (`/var/logs`).


```
/
├── home
├── etc
├── tmp
├── usr
└── var

```
---

### Current Directory
1. 
```
$pwd

```

---

### Absolute Path and Rleative Path

### Absolute Path

An Absolute path starts from `/`.

Example:
```bash
/tmp
```

```bash
/home/user1
```

### Relative Path

A relative path starts from where you are currently standing.

For Example:

```bash
cd /tmp
mkdir sre
cd sre
pwd

```
Now:

```bash
cd ..
```
You moved one directory upward.

Check:

```bash
pwd
```

Then:

```bash
cd .
pwd
```

Relative path shortcuts:

`.` : means current working directory

`..` : means parent directory

`~` : Home directory

---

### 

Your rule from today

When you don't know a command:

```bash
1. man
2. --help
3. official documentation
4. search/web
```



