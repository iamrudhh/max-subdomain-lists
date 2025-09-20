Here’s a clean and professional **GitHub README** for your `max-subdomain-lists` tool based on your Python script:

````markdown
# Max Subdomain Lists 🕵️‍♂️

**Max Subdomain Lists** is a simple Python tool to generate common subdomains and URLs for any domain. It is designed for **bug bounty hunters, penetration testers, and security enthusiasts** who want to quickly enumerate subdomains and optionally check their availability.

---

## 📦 Features

- Generates common subdomains for a target domain.
- Builds full URLs with both `https` and `http` schemes.
- Optionally probes URLs to check if they are live (requires `requests` library).
- Saves results to a file `subdomain_results.txt`.
- Simple, beginner-friendly, and fully Python-based.

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/iamrudhh/max-subdomain-lists.git
cd max-subdomain-lists
````

2. (Optional) Install `requests` if you want to check live URLs:

```bash
pip install requests
```

---

## 🛠 Usage

```bash
python subdomain_url_builder.py <domain> [--check]
```

* `<domain>` → The target domain (e.g., `example.com`).
* `--check` → Optional flag to probe the URLs and see if they are live.

### Examples

Generate URLs for `example.com` without checking:

```bash
python subdomain_url_builder.py example.com
```

Generate and probe URLs for `example.com`:

```bash
python subdomain_url_builder.py example.com --check
```

---

## 📂 Output

The tool will:

1. Print normalized domain, hostnames, and URLs in the console.
2. If `--check` is used, it will display which URLs are **UP** or **DOWN**.
3. Save all results to a file named `subdomain_results.txt`.

Example output snippet:

```
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
```

---

## 🔧 How It Works

1. **Domain normalization** – Strips scheme and path from the user input.
2. **Subdomain generation** – Combines the target domain with a predefined list of common subdomains.
3. **URL building** – Prepends `https` and `http` schemes to each hostname.
4. **Optional probing** – Sends HTTP HEAD requests to check if the URLs are accessible.
5. **Results** – Prints and saves all results to `subdomain_results.txt`.

---

## ⚡ Performance

* Lightweight and fast for small to medium lists of subdomains.
* The optional probing uses simple HTTP requests with a short timeout, making it efficient for quick checks.
* Can be easily extended by adding more subdomains to the `SUBDOMAIN_RAW` list.

---

## 👤 Author

**Anirudh (GitHub: [iamrudhh](https://github.com/iamrudhh))**

---

## ⚠️ Disclaimer

This tool is meant for **educational purposes** and **authorized security testing only**. Do not use it on domains you do not own or have permission to test.

```

---

If you want, I can also **make a more visual version** with **badges, emojis, and usage screenshots** to make it GitHub-ready and more attractive.  

Do you want me to do that?
```
