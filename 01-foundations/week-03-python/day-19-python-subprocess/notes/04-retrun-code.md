# Return codes — critical SRE concept

Every process returns an exit code.

Conventionally:

```
0       → success
non-zero → failure
```

Try:

```python
import subprocess

result = subprocess.run(    
    ["ls", "/tmp"],   
     capture_output=True,    
     text=True
)

print("Return code:", result.returncode)

```


You should normally see:

```
Return code: 0
```

Now intentionally break it:

```python
result = subprocess.run(   
     ["ls", "/does-not-exist"],    
     capture_output=True,   
     text=True)
```


Inspect:

```python
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("RETURN CODE:", result.returncode)
```

You'll likely get a non-zero return code.

This concept appears everywhere in DevOps:

```
GitHub Actions
Jenkins
Bash
Docker
Terraform
kubectl
Ansible
Python automation
       ↓
Exit code
```

A failed command's exit code is one mechanism CI/CD systems use to know a step failed.