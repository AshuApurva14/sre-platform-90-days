"""

commands.py
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

        return result.stdout

    except FileNotFoundError:

        print(f"ERROR: Command not found: {command[0]}")

        return None


    except subprocess.CalledProcessError as error:

        print(
            f"ERROR: Command failed with:"
            f"exit code: {error.returncode}"  )

        if error.stderr:
            print(result.stderr.strip())

        return None

    except subprocess.TimeoutExpired:

        print(f"ERROR: command time out: {command}")
        return None