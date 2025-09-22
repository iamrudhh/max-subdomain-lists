Max Subdomain Lists — Bash Subdomain Enumeration Tool

Max Subdomain Lists is a lightweight Bash-based subdomain enumeration script that generates common subdomains for a given domain, builds corresponding URLs with both HTTP and HTTPS schemes, and optionally probes them using curl to check if they are live.

This tool is designed for bug bounty hunters, penetration testers, and cybersecurity professionals who need a simple and fast way to perform subdomain discovery and URL validation without relying on heavy external dependencies.

Features

🔹 Generate a predefined list of common subdomains for a target domain.

🔹 Build full URLs with both https:// and http://.

🔹 Optional probing mode using curl (HEAD with fallback to GET).

🔹 Normalize user input by removing schemes and paths.

🔹 Save all results to subdomain_results.txt for later use.

🔹 Single file, lightweight Bash script — no Python or external tools required.

Requirements

Bash 4+

curl (only required if using the probing feature --check)

Installation

Clone the repository and make the script executable:

git clone https://github.com/iamrudhh/max-subdomain-lists.git
cd max-subdomain-lists
chmod +x subdomain_url_builder.sh

Usage
Basic enumeration (generate hostnames & URLs only):
./subdomain_url_builder.sh example.com

With probing (check if URLs are live):
./subdomain_url_builder.sh example.com --check

Arguments:

<domain> → The target domain (e.g., example.com or https://example.com/path).

--check → Optional flag that probes each generated URL using curl.

Example Output
Target domain: example.com

Hostnames:
  www.example.com
  mail.example.com
  ftp.example.com
  ...

URLs (https first):
  https://www.example.com
  http://www.example.com
  ...

Probing Results:
https://www.example.com           -> UP   : HTTP 200
http://www.example.com            -> UP   : HTTP 200


All results are saved automatically to subdomain_results.txt.

How It Works

Domain Normalization → Removes schemes (http://, https://) and paths from the input.

Subdomain Generation → Combines the domain with a built-in wordlist of common subdomains.

URL Construction → Creates full URLs for each subdomain with https:// and http://.

Optional Probing → Uses curl to send a HEAD request (fallback to GET if necessary).

Result Saving → Displays results in the console and writes them to subdomain_results.txt.

Performance

Optimized for fast subdomain discovery with a small to medium wordlist.

Probing mode uses a 4-second timeout for quick availability checks.

Easily extendable: add more entries to the SUBDOMAIN_RAW list inside the script.

For faster large-scale probing, combine the tool with xargs -P or GNU parallel.

Author

Anirudh
GitHub: iamrudhh

Disclaimer

This script is intended for educational use and authorized security testing only.
Do not use it on domains you do not own or lack explicit permission to test.
The author assumes no responsibility for misuse.
