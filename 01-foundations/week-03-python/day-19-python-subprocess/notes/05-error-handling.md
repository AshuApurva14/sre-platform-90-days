# Handling Error when command fail

## But our run_command() has a bug

Consider:
```python
return result.stdout
```

What happens if the command fails?

We're ignoring:

```python
result.returncoderesult.stderr
```

That's poor automation.

For example:

```python
run_command(["cat", "/missing-file"])
```

may return an empty stdout while the real error sits in stderr.

The automation could incorrectly continue.


## Introduce check=True

Python can automatically turn a failed command into an exception.

```python
result = subprocess.run(    
        ["ls", "/does-not-exist"],  
        capture_output=True,   
        text=True,   
        check=True
)
```


Because the command returns non-zero, Python raises:

```python
subprocess.CalledProcessError
```

Now Day 16 becomes relevant again.

```
try:    

except subprocess.CalledProcessError:   

```

## Add timeouts

Now imagine your automation executes:

```
some-command
```

and the command hangs for 30 minutes.

Your Python script also waits.

That's dangerous in CI/CD and monitoring automation.
Use:

```python
subprocess.run(   
         command,  
         capture_output=True,    
         text=True,    
         check=True,    
         timeout=5
)

```


If the process takes more than 5 seconds:

```python
subprocess.TimeoutExpired
```

can be raised.
Handle it:

```python
except subprocess.TimeoutExpired:   
        print("ERROR: Command timed out")    
        
        return None
```

Your command runner is becoming resilient:

```
Command
   ↓
Can executable start?
   ↓
Can command finish?
   ↓
Did it finish in time?
   ↓
Was exit code successful?
   ↓
Capture output
```

That's SRE thinking.