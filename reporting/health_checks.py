import subprocess
import logging

# Setup basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Helper function to execute a shell command and return output
def execute_command(command):
    try:
        output = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if output.returncode != 0:
            logging.error(f"Command failed with error: {output.stderr.strip()}")
            return None
        return output.stdout.strip()
    except Exception as e:
        logging.error(f"Exception during command execution: {str(e)}")
        return None


# Function to get real-time data for td-agent-bit using top
def get_td_agent_bit_stats():
    command = "top -b -n 1 | grep td-agent-bit"
    output = execute_command(command)
    if output:
        return output
    else:
        logging.warning("No td-agent-bit process found.")
        return None


# Function to parse and display td-agent-bit statistics
def parse_and_display_stats(stats):
    if stats is None:
        logging.info("No statistics to display. Process might not be running.")
    else:
        try:
            # Assuming the output of top is default and splits are based on standard whitespace
            parts = stats.split()
            pid = parts[0]
            cpu_usage = parts[8]
            mem_usage = parts[9]
            time = parts[10]
            logging.info("Successfully retrieved process statistics.")
            print("PID:", pid.decode())
            print("CPU Usage (%):", cpu_usage.decode())
            print("Memory Usage (%):", mem_usage.decode())
            print("Time:", time.decode())
        except IndexError as e:
            logging.error(
                "Error parsing top output, might be due to unexpected format: " + str(e)
            )


def main():
    td_agent_bit_stats = get_td_agent_bit_stats()
    parse_and_display_stats(td_agent_bit_stats)


if __name__ == "__main__":
    main()
