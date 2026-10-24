"""
Basic logging example

"""

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("CPU usage is high")
logging.error("Database connection failed")

