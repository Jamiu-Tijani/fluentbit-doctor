import os
import re
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_conf_file_well_formatted(file_path):
    """
    Checks if a .conf file is well-formatted.
    For simplicity, this function checks:
    - Lines should not start with a whitespace (basic check for incorrect indentation)
    - Section headers should be enclosed in square brackets
    - Key-value pairs should be separated by '='
    """
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            stripped_line = line.strip()
            if stripped_line:  # Ignore empty lines
                # Check for incorrect starting whitespace
                if line[0] in ' \t':
                    logging.error(f"Indentation error in {file_path} on line {line_number}")
                    return False
                # Check for section headers
                if stripped_line.startswith('[') and not stripped_line.endswith(']'):
                    logging.error(f"Malformed section header in {file_path} on line {line_number}")
                    return False
                # Check for key-value pairs
                if '=' in stripped_line:
                    key_value = stripped_line.split('=')
                    if len(key_value) != 2 or not key_value[0].strip() or not key_value[1].strip():
                        logging.error(f"Malformed key-value pair in {file_path} on line {line_number}")
                        return False
    return True

def verify_config_files():
    directories = ["/etc/fluent-bit", "/etc/td-agent-bit"]
    all_files_well_formatted = True

    for directory in directories:
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if filename.endswith('.conf'):
                    file_path = os.path.join(directory, filename)
                    if not is_conf_file_well_formatted(file_path):
                        all_files_well_formatted = False
                        logging.warn(f"File {file_path} has formatting issues.")
        else:
            print(f"Directory {directory} does not exist.")

    if all_files_well_formatted:
        print("All .conf files are well formatted.")
    else:
        print("Some .conf files have formatting issues.")

if __name__ == "__main__":
    logging.info("Verifying .conf files...")
    verify_config_files()
