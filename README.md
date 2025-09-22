Max Subdomain Lists — Bash Edition 🕵️‍♂️🔧

A small, focused Bash port of the original Python tool that generates common subdomains and builds URLs (https/http) for a target domain — with an optional probing mode that checks whether those URLs are live. Designed for bug bounty hunters, pentesters, and security enthusiasts who want a fast, simple utility without Python.

📦 Features

Builds common subdomain hostnames (e.g. api.example.com, mail.example.com).

Produces URLs for both https:// and http:// (https first).

Optional probing of URLs using curl (HEAD, fallback to GET).

Saves all output to subdomain_results.txt.

Lightweight, single-file Bash script — easy to read and extend.

⚙️ Requirements

Bash 4+ (tested with Bash 4.x/5.x)

curl — optional but required for the --check probing flag

📥 Installation

Clone your repo (or copy the script) and make it executable:

git clone https://github.com/iamrudhh/max-subdomain-lists.git
cd max-subdomain-lists
chmod +x subdomain_url_builder.sh

🛠 Usage
# Basic: build hostnames & URLs only
./subdomain_url_builder.sh example.com

# With probing (requires curl)
./subdomain_url_builder.sh example.com --check


Arguments:

<domain> → Target domain (e.g. example.com or https://example.com/path — the script normalizes it).

--check → Optional flag: probe the generated URLs to see if they respond.

🔍 What the script does

Normalize domain — strips scheme (http(s)://) and path, lowercases the host.

Load subdomain list — uses the built-in SUBDOMAIN_RAW block (easy to extend).

Build hostnames — joins each subdomain with the target domain.

Build URLs — prepends https:// and http:// to each hostname (https first).

Optional probing — curl -I (HEAD) with a short timeout (fallback to GET on 405) to detect live hosts.

Save & print — prints results to console and saves everything to subdomain_results.txt.

📂 Output

All results are written to subdomain_results.txt in the current directory.

Example console snippet:

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
...

⚡ Performance & Tuning

The script is intentionally simple and single-threaded for readability and easy deployment.

Probing uses a small timeout (4s by default) for quick checks.

If you need faster probing at scale, you can:

Pipe the URL list into xargs -P to run parallel curl checks, or

Use GNU parallel to probe concurrently.

To extend the wordlist, add subdomain entries to the SUBDOMAIN_RAW block in the script.

👤 Author

Anirudh — GitHub: iamrudhh

⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not use it on domains you do not own or do not have explicit permission to test. The author is not responsible for misuse.
