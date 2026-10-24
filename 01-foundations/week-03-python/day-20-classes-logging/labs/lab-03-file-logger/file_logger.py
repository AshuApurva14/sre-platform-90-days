"""
Log to the file

"""

import logging

logging.basicConfig(
    filename="/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-20-classes-logging/labs/lab-03-file-logger/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"

)

logger = logging.getLogger(__name__)

logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

