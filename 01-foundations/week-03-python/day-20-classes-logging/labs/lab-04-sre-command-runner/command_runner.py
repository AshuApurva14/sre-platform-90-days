"""
Command Runner module for executing shell commands and logging their output.
"""

import logging
import subprocess

logger = logging.getLogger(__name__)

class CommandRunner:

    def __init__(self, timeout=5):
        self.timeout = timeout

    def run(self, command):
        logger.info("Executing command %s", command)

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                timeout=self.timeout
            )

            logger.info("Command executed successfully")

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            logger.error(
                "Comamnd timed out after %s seconds",
                self.timeout
            )

            return None