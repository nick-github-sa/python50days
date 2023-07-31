import os
import socket
import subprocess


# Define the target company domain
company_domain = "mitto.ch"

# Define the output file paths
domain_file = "domains.txt"
ip_file = "ips.txt"
nmap_file = "nmap_scan.txt"

# Enumerate domains and subdomains
subdomains = set()
for i in range(1, 10):
    cmd = f"curl -s 'https://crt.sh/?q=%25.{company_domain}&output=json' | jq -r '.[].name_value' | sed 's/\*\.//g' | grep -oE '([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9])\.{company_domain}' | sort -u"
    output = subprocess.check_output(cmd, shell=True).decode().strip()
    subdomains.update(output.splitlines())
    
# Write domains and subdomains to file
with open(domain_file, "w") as f:
    for subdomain in sorted(subdomains):
        f.write(subdomain + "\n")

# Retrieve IP addresses for each domain and subdomain
ip_addresses = {}
for subdomain in subdomains:
    try:
        ip_addresses[subdomain] = socket.gethostbyname(subdomain)
    except:
        pass

# Write IP addresses to file
with open(ip_file, "w") as f:
    for subdomain, ip_address in ip_addresses.items():
        f.write(f"{subdomain},{ip_address}\n")

