"""
Log levels are used to indicate the severity of a log message. The standard log levels in Python's logging module are:
- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.
"""

import logging


logging.basicConfig(level=logging.DEBUG)
logging.debug("Executing command")
logging.info("Health check started")
logging.warning("CPU usage above 80%")
logging.error("kubectl command failed")
logging.critical("Unable to monitor production cluster")


"""
Instead of using the basicConfig method, you can also create a logger object and set its level. This allows for more flexibility in configuring loggers, handlers, and formatters.  
"""

logger = logging.getLogger(__name__)
logger.info("Application started")
logger.warning("CPU usage high")
logger.error("Command failed")