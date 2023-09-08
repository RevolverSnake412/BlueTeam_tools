#!/usr/bin/python3
import sys, subprocess, os
from datetime import datetime

# Check if target is present
if len(sys.argv) != 2:
    print("Usage: ./nmap_open_ports.py <target>")
    exit(1)
else:
    target = sys.argv[1]

# Convert current date to hex for shorter text file
current_date = hex(int(datetime.now().strftime("%m%d%H%M%S")))
# Build file format
output_file = f"nmap_{current_date}.txt"

# Executing part
print(f"Running Nmap...")
# Run nmap and save result in text file
try:
    with open(output_file, 'w') as file:
        subprocess.run(['nmap', target], stdout=file, stderr=subprocess.PIPE, text=True)
    print(f"Nmap results saved to {output_file}")

    # Parse the Nmap output to extract open ports
    open_ports = []
    with open(output_file, 'r') as nmap_output_file:
        for line in nmap_output_file:
            if "open" in line:
                parts = line.split()
                port = parts[0].split('/')[0]
                open_ports.append(port)

    # Format and print the open ports
    if open_ports:
        open_ports_str = ', '.join(open_ports)
        print(f"<PORTS OPEN: {open_ports_str}>")
    else:
        print("No open ports found.")

# Exit if nmap is not found on system
except FileNotFoundError:
    print("nmap command not found")
