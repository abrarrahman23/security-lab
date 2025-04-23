# log_parser.py
# Script to extract IP addresses from failed login attempts

with open("auth.log", "r") as f:
    with open("failed_logins.txt", "w") as output_file:
        for line in f:
            if "Failed password" in line:
                parts = line.split()
                ip_address = parts[-4]  # Last 4th element is the IP address
                output_file.write(f"Failed login attempt from IP: {ip_address}\n")
                print(f"Failed login attempt from IP: {ip_address}")
