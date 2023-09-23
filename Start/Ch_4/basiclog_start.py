# demonstrate the logging api in Python

# TODO: use the built-in logging module
import datetime
import logging 

# logging.critical(f"Started logging at {datetime.datetime.now()}") # if you include a report before setting basicConfig python sets the default config and setting again does not work

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w") # basicConfig can only be set once in a program
logging.critical(f"Started logging at {datetime.datetime.now()}") 
# TODO: Try out each of the log levels
logging.debug("Debug-level message: Diagnostic information useful for debugging")
logging.info("Info-level message: General information about program execution results")
logging.warning("Warning-level message: Something unexpected or an approaching problem")
logging.error("Error-level message: Unable to perform a specific operation due to a problem")
logging.critical("Critical-level message: Program may be unable to continue due to a serious error")

# TODO: Output formatted strings to the log

logging.critical(f"Logging stopped at {datetime.datetime.now()}")