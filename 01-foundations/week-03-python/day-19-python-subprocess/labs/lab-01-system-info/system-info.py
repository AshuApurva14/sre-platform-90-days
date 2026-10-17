"""
Lab 1 - System Information Collector
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

    except subprocess.CalledProcessError as error:
        print(f"Command Failed: {error.stderr}")

        return None

def main():
    hostname = run_command(["hostname"])
    uptime = run_command(["uptime"])
    disk = run_command(["df", "-h"])


    print("HOSTNAME")
    print(hostname)

    print("UPTIME")
    print(uptime)

    print("DISK")
    print(disk)


if __name__ == "__main__":
    main()