# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def log_a_message():
    logging.info("Info level debugger in the log_a_message function", extra=other_log_data)


# set the output file and debug level, and
# TODO: use a custom formatting specification

log_str = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
log_date = "%m/%d/%Y %I:%M:%S %p"
other_log_data = {"user": "willc@example.com"}
logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=log_str,
                    datefmt=log_date)
log_a_message()
logging.info("This is an info-level log message", extra=other_log_data)
logging.warning("This is a warning-level message", extra=other_log_data)

