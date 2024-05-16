import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_fluent_bit_executable():
    """Check if Fluent Bit or td-agent-bit is in the system's PATH."""
    try:
        # Try finding fluent-bit
        result = subprocess.run(
            ["whereis", "fluent-bit"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            if not output.endswith(":"):
                logger.info(f"Fluent Bit executable found: {output}")
                return True

        td_agent_bit_path = "/opt/td-agent-bit/bin/td-agent-bit"
        if os.path.exists(td_agent_bit_path):
            logger.info(f"td-agent-bit executable found: {td_agent_bit_path}")
            return True

        logger.info("Fluent Bit or td-agent-bit executable not found.")
        return False

    except Exception as e:
        logger.error(f"Error checking Fluent Bit or td-agent-bit executable: {e}")
        return False


def check_fluent_bit_version(executable_path=None):
    """Check the version of Fluent Bit or td-agent-bit."""
    try:
        if executable_path:
            command = [executable_path, "--version"]
        else:
            command = ["/opt/td-agent-bit/bin/td-agent-bit", "--version"]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logger.info(f"Fluent Bit version: {result.stdout.strip()}")
            return True
        else:
            logger.info("Unable to determine Fluent Bit or td-agent-bit version.")
            return False
    except Exception as e:
        logger.error(f"Error retrieving Fluent Bit or td-agent-bit version: {e}")
        return False


if __name__ == "__main__":
    logger.info("Verifying Fluent Bit executable...")
    if check_fluent_bit_executable():
        logger.info("Fluent Bit executable verification successful.")
    else:
        logger.info("Fluent Bit executable verification failed.")

    logger.info("Verifying Fluent Bit version...")
    if check_fluent_bit_version():
        logger.info("Fluent Bit version verification successful.")
    else:
        logger.info("Fluent Bit version verification failed.")
