import logging

# Create a custom logger
logger = logging.getLogger("fluent-bit-doctor")
logger.setLevel(logging.DEBUG)  # Set the minimum log level to DEBUG

# Define a custom formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Add formatter to the handler
ch.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(ch)
