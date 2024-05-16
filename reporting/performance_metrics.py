import subprocess
import yaml
import logging
from datetime import datetime
import time

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def test_fluent_bit_latency():
    # Read configuration from YAML file
    with open("reporting/config.yml", "r") as file:
        config = yaml.safe_load(file)

    # Prepare the tcpdump command
    tcpdump_cmd = f"sudo tcpdump -i {config['interface']} host {config['splunk_ip']} and port {config['splunk_port']} -w {config['output_file']}"
    logging.info("Starting tcpdump...")

    try:
        # Start tcpdump
        tcpdump_process = subprocess.Popen(
            tcpdump_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        logging.info(f"tcpdump started with PID: {tcpdump_process.pid}")

        # Append a random text to the test log file
        with open(config["log_file"], "a") as log_file:
            log_file.write(f"Random log entry {datetime.now()}\n")

        # Wait for the specified duration in seconds
        time.sleep(config["duration"])

        # Terminate the tcpdump process
        tcpdump_process.terminate()
        try:
            tcpdump_process.wait(timeout=60)  # Wait for process to terminate
        except subprocess.TimeoutExpired:
            tcpdump_process.kill()  # Force kill if not terminated after timeout
            # logging.error("tcpdump did not terminate gracefully and was killed.")

        logging.info("tcpdump stopped.")

        # Analyze the capture
        analysis_cmd = f"sudo tcpdump -nn -r {config['output_file']} 2>/dev/null | awk '{{print $1}}'"
        first_packet_time = (
            subprocess.check_output(analysis_cmd + " | head -1", shell=True)
            .decode()
            .strip()
        )
        last_packet_time = (
            subprocess.check_output(analysis_cmd + " | tail -1", shell=True)
            .decode()
            .strip()
        )
        if len(first_packet_time) < 2:
            exit("Couldn't capture packet at this time . Try again")
        # Convert timestamps to seconds
        FMT = "%H:%M:%S.%f"
        start_seconds = datetime.strptime(first_packet_time, FMT)
        end_seconds = datetime.strptime(last_packet_time, FMT)
        latency = (end_seconds - start_seconds).total_seconds()

        logging.info(f"Latency: {latency} seconds")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    test_fluent_bit_latency()
