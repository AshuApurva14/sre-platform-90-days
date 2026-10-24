"""

Command Runner
This module provides a function to run shell commands and log their output. It uses the subprocess module to execute commands and the logging module to log messages.

"""

import logging
import subprocess


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)


logger = logging.getLogger(__name__)

def run_command(command,timeout):

    logger.info("Executing command: %s", command)

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            test=True,
            check=True, 
            timeout=timeout

        )

        logger.info("Commands executed successfully")

        return result.stdout.strip()

    except FileNotFoundError:
        logger.error("Command not found: %s", command[0])
        return None

    except subprocess.CalledProcessError as error:
        logger.error("Comamnd failed with exits code: %s", error.retruncode)
        return None

    except subprocess.TimeoutExpired:
        logger.error("Command timed out after %s seconds", timeout)
        return None