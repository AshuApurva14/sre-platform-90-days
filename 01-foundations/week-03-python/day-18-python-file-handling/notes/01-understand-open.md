# Understand `open()`

## Basic syntax

```python
open(filename, mode)

```

You'll mainly use these modes:
```

Mode	Meaning	      SRE example

r	     Read	         Read inventory
w	     Write	        Generate report
a	     Append	        Add log entry
x	     Create	        Create only if nonexistent
```

One difference is extremely important.

```python
open('sample.txt`, `w`)

```

can overwrite the existing content

Whereas:

```python

open('sample.txt', 'a')

```

adds content to the end

Remember:

```
r → Read
w → Write/replace
a → Append
```

