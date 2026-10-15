"""
Error logger 

"""

from datetime import datetime

def log_error(message):
    timestamp = datetime.now()


    log_entry = f"{timestamp} ERROR {message}\n"

    with open("/workspaces/sre-platform-90-days/01-foundations/week-03-python/day-18-python-file-handling/labs/lab-03-error-log/errors.log", "a") as file:
        file.write(log_entry)


log_error("Database connection failed")
log_error("API health check failed")


