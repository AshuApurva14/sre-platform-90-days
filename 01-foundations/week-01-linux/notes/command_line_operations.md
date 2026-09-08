# Foundational Commands

<img width="1466" height="854" alt="Image" src="https://github.com/user-attachments/assets/7ec56796-de9d-4770-966f-a825423d2ec4" />

## Restarting and Shutting down system

### Shutdown

```bash
shutdown -h
```

### Rebbot

```bash
shutdown -r
```

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

`-` : Changes to previous working directory

---

## Learn `ls`

### List content

`ls` - List files and irectory

```bash
ls 
ls -l
ls -la

```

### Learn `>` and  `>>` (Redirection symbol)

`>` - overwrite to existing file

`>>` - append to existing file

```bash
echo "My file" > notes.txt
echo "My file2" >> notes.txt

```


### Learn `cp` command

`cp` - Copy file content and directory


### Learn `mv`

`mv` - Move file and directory

### Learn `rm`

`rm` - Remove files and directory

### Learn `less` 

`less` - View first 20 lines of file

---

## Hard Links

The `ln` utility is used to create hard links. Unlike a standard copy, a hard link acts as an additional name for the exact same data on the disk.

```bash
ln file 1 file 2
```
- Data Preservavtion


`inode number:` a unique identifier for the data on the disk, you can verify this by viewing the inode numbers with ls -li:

```bash
ls -li file 1 file2

```

### Soft (Symbolic) Links

Soft links, often called "symlinks", are created with the -s option, as in:

```bash
ln -s file 1 file2

```

When you inspect a symbolic link with ls -li, you will notice it has its own unique inode number and a distinct file type indicator (an l at the start of the permissions string, along with a -> pointing to the target). Unlike a hard link, a symbolic link does not share the original file's data; it acts as a "pointer" or shortcut to the original file path.

Points to considr before symlinks:

- Cross-Filesystem Support

- Minimal Overhead

- Flexibility : 
    A symlink can be updated to point to a new location without affecting the source file, which makes it a convenient way to create a short, stable name for a long or frequently changing path.


- Watch for Dangling Links

---

## Working with Files 

### Viewing files

- `cat` - Used for viewing shorter files.
- `tac` - Used for look file backward, starting from last line.
- `less` - It is used to view larger files, it provides scroll back feature and search/ navigate options as well.
- `tail` - Used to view last 10 lines of a file
- `head` - The opposite of tail, it is used to view first 10 lines of the file.


### Moving, renaming and removing files

- `mv` - Rename or Move files 
- `rm` - Remove a file
- `rm -i` - Interactively remove a file (prompts before each)
- `rm -f` - Forcefully remove a file (no prompts)

### Creating , renaming and removing directories

- `mkdir` - create a directory
- `rmdir` - Remove a directory
- `rm -r` 
- `mkdir -p`
- `mv` 
- `rmdir -r`
- `rm -rf`

