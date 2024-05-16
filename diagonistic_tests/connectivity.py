import subprocess


def nslookup(hostname):
    try:
        # Running the nslookup command
        result = subprocess.run(["nslookup", hostname], capture_output=True, text=True)
        if result.returncode != 0:
            print("nslookup failed:", result.stderr)
            return None

        # Parsing the output to find the IP address
        output = result.stdout.split("\n")
        ip = []
        for line in output:
            if "Address" in line or "Server" in line:
                return line.split("\t")[-1]
    except Exception as e:
        print("An error occurred in nslookup:", e)
    return None


def check_telnet(ip, port):
    try:
        # Forming the telnet command as a string
        command = f"telnet {ip} {port}"
        # Running telnet using subprocess
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=10
        )
        # Check if Telnet connection was successful
        if result.returncode == 0:
            print(f"Successfully connected to {ip} on port {port}")
            return True
        else:
            print(f"Failed to connect to {ip} on port {port}: {result.stderr}")
    except subprocess.TimeoutExpired:
        print(f"Connection to {ip} on port {port} timed out.")
    except Exception as e:
        print(f"An error occurred while trying to connect via telnet: {e}")
    return False


hostname = "private.tcp.obsroute.uw2.dev.adskeng.net"
port = 9995

ip_address = nslookup(hostname)
if ip_address:
    print(f"IP Address found: {ip_address}")
    active = check_telnet(ip_address, port)
    if active:
        print(f"Service is active on {hostname}:{port}")
    else:
        print(f"Service is not active on {hostname}:{port}")
else:
    print(f"No IP address found for {hostname}")
