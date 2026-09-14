# Learn redirection

You already used:
```bash
>
```
Example:
```bash
echo "hello" > file.txt
```
This overwrites the file.

And:
```bash
echo "world" >> file.txt
```
This appends.

Now learn:
```bash
2>
```
which redirects standard error.

Example:
```bash
ls /does-not-exist 2> errors.txt
```
Then:
```bash
cat errors.txt
```
For today, understand:
```bash
>   stdout overwrite
>>  stdout append
2>  stderr
```