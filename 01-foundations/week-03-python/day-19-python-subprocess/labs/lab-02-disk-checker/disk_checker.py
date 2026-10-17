"""
Check disk

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

    except subprocess.CalledProcessError as error:

        print(f"Command failed: {error}")
        print(f"Return code: {error.returncode}")
        print(f"Error: {error.stderr}")

        return None


output = run_command(["df", "-h"])

if output is not None:
    print("================== Disk usage info ===================\n")
    print(output)