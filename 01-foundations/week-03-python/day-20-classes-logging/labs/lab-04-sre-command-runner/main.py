"""
Main config

"""
from command_runner import CommandRunner
from logging_config import configure_logging

def main():

    configure_logging()

    runner = CommandRunner(timeout=5)
    hostname = runner.run(["hostname"])

    if hostname is not None:
        print(f"Hostname: {hostname}")

if __name__ == "__main__":
    main()

