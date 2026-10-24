"""
Log formatting allows you to customize the appearance of log messages. You can specify a format string that defines how the log message should be displayed.

"""

import logging
import subprocess


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)

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
        logger.error("Command not found: %s", {command[0]})
        return None

    except subprocess.CalledProcessError as error:

        logger.error("Command failed with exit code: %d", {error.returncode})
        logger.error("Error output: %s", {error.stderr.strip()})
        return None
    
output = run_command(["hostname"])

if output is not None:
    print(output)