"""
Command runner

"""

import subprocess

def run_command(command):

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except FileNotFoundError:
        print(f"Command not found: {command[0]}")
        return None

    except subprocess.CalledProcessError as error:

        print(f"Command failed with exit code:{error.returncode}")
        print(error.stderr.strip())

        return None


output = run_command(["du", "-h"])

if output is not None:
    print(output)