# Max Subdomain Lists — `max_subdomain_lists.sh`

**Bash subdomain wordlist generator + optional URL prober**
Lightweight, portable Bash tool to build common subdomain hostnames and `http(s)` URLs for a target domain. Optionally probes those URLs with `curl` to check which are live.

> 🔒 Use only on domains you own or are authorized to test. Unauthorized scanning may be illegal.

---

## 🚀 Quick summary

`max_subdomain_lists.sh` is a tiny, dependency-light Bash script for quick subdomain enumeration and optional HTTP probing. Perfect for bug bounty recon, pentesters, and security hobbyists who want a simple starting list of candidate subdomains.

**GitHub:** `iamrudhh/max_subdomain_lists`
**Suggested topics:** `bash`, `subdomain-enum`, `recon`, `bug-bounty`, `pentest`, `curl`

---

## 📋 Features

* Pure Bash (Bash 4+) — minimal dependencies.
* Expandable built-in subdomain wordlist (editable).
* Generates `hostnames` and both `https://` & `http://` URLs.
* Optional `--check` probing using `curl` (HEAD then GET fallback).
* Outputs to `subdomain_results.txt` (human-friendly + saved log).
* Fast, small timeout to keep scans efficient.

---

## ⚙️ Requirements

* **Bash 4+**
* **curl** (optional — required only for `--check`)
* Network access for probing

---

## 🔧 Installation

Download the script and make it executable:

```bash
curl -LO https://raw.githubusercontent.com/iamrudhh/max_subdomain_lists/main/max_subdomain_lists.sh
chmod +x max_subdomain_lists.sh
```

(Or clone the repo and use the script directly.)

---

## 💡 Usage

```bash
# Generate hostnames and URLs (no probing)
./max_subdomain_lists.sh example.com

# Generate hostnames/URLs and probe them (requires curl)
./max_subdomain_lists.sh example.com --check

# Script prints usage when no args supplied
./max_subdomain_lists.sh
```

Output is printed to the terminal and saved to `subdomain_results.txt` in the script directory.

---

## 🔎 Example output (truncated)

```
Normalized domain: example.com

Target domain: example.com

Hostnames:
  www.example.com
  mail.example.com
  ftp.example.com
  ...

URLs (https first):
  https://www.example.com
  http://www.example.com
  https://mail.example.com
  http://mail.example.com
  ...

Probing Results:
https://www.example.com                    -> UP   : HTTP 200
http://www.example.com                     -> UP   : HTTP 301
https://mail.example.com                   -> DOWN : failed

[+] Results saved to subdomain_results.txt
```

---

## 🧠 How it works (brief)

1. **normalize\_domain()** — cleans input (removes `http(s)://`, paths, trailing colon) and lowercases it.
2. **build\_hostnames()** — iterates `SUBDOMAIN_RAW` and prepends tokens to the domain.
3. **build\_urls()** — emits `https://` then `http://` for each hostname.
4. **probe\_url()** — uses `curl -I` (HEAD) with short timeout; falls back to GET when needed.
5. **main** — orchestrates and writes output to `subdomain_results.txt`.

---

## ✍️ Customization

* Add/remove words in the `SUBDOMAIN_RAW` heredoc to tune the list.
* Change `OUT_FILE` to a different filename.
* Adjust `-m 4` (curl timeout) to increase/decrease probe timeout.
* Add parallel probing (`xargs -P` or background workers) for speed—be careful to avoid creating too much traffic.

---

## 🔗 Integration ideas

* Pipe hostnames into DNS tools like `massdns`, `amass`, or `assetfinder`.
* Send live hosts to `httprobe`, `gau`, or `waybackurls` for further reconnaissance.
* Add to recon-playbook or CI to auto-generate lists for testing.

---

## ⚖️ Legal & responsible use

Only run this tool against domains you own or have explicit written permission to test. Scanning domains without permission may be illegal and could get you blocked or reported.

---

## 🤝 Contributing

Contributions welcome — fork the repo, edit the `SUBDOMAIN_RAW`, improve probing, add docs or tests, then open a PR. Keep changes small and documented.

---

## 📝 License

Suggested: **MIT License** (or pick whichever you prefer). Add a `LICENSE` file.

---
