"""
Logging configuration for the SRE Command Runner application.

"""

import logging


def configure_logging():

    logging.basicConfig(
        filename="/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-20-classes-logging/labs/lab-04-sre-command-runner/logs/app.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s"
    )

