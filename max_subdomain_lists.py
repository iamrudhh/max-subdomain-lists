
# subdomain_url_builder.py
# Python 3.8+
# Optional dependency (for probing): pip install requests

from urllib.parse import urlparse
import requests   # optional: used only if --check is used
import sys

SUBDOMAIN_RAW = """www
mail
ftp
test
dev
staging
api
blog
shop
support
secure
ns1
ns2
vpn
portal
beta
"""

def normalize_domain(user_input: str) -> str:
    """Return domain part only (strip scheme and path)."""
    parsed = urlparse(user_input if "://" in user_input else "http://" + user_input)
    host = parsed.netloc or parsed.path
    if host.endswith(":"):
        host = host[:-1]
    return host.strip().lower()

def load_subdomains_from_string(raw: str):
    """Turn the multiline subdomain block into a clean list."""
    lines = [l.strip().lower() for l in raw.splitlines() if l.strip()]
    return list(dict.fromkeys(lines))  # remove duplicates, keep order

def build_hostnames(domain: str, subdomains: list[str]) -> list[str]:
    """Build hostnames like 'api.example.com'."""
    hostnames = []
    for s in subdomains:
        hostname = domain if s == "@" else f"{s}.{domain}"
        hostnames.append(hostname)
    return hostnames

def build_urls(hostnames: list[str], schemes=("https", "http")) -> list[str]:
    """Prepend scheme to create URLs."""
    return [f"{scheme}://{host}" for host in hostnames for scheme in schemes]

def probe_url(url: str, timeout: float = 4.0) -> tuple[bool, str]:
    """Send HEAD request (fallback to GET)."""
    try:
        resp = requests.head(url, allow_redirects=True, timeout=timeout)
        if resp.status_code == 405:
            resp = requests.get(url, allow_redirects=True, timeout=timeout)
        return True, f"HTTP {resp.status_code}"
    except requests.exceptions.RequestException as e:
        return False, str(e)

def main(domain_input: str, check: bool = False):
    domain = normalize_domain(domain_input)
    print(f"Normalized domain: {domain}\n")

    subs = load_subdomains_from_string(SUBDOMAIN_RAW)
    print(f"Loaded {len(subs)} subdomains\n")

    hostnames = build_hostnames(domain, subs)
    urls = build_urls(hostnames)

    # Collect results
    results = []
    results.append(f"Target domain: {domain}\n")
    results.append("Hostnames:")
    results.extend([f"  {h}" for h in hostnames])
    results.append("\nURLs (https first):")
    results.extend([f"  {u}" for u in urls])

    # Print to console
    print("\n".join(results), "\n")

    # If probing enabled
    if check:
        print("Probing URLs (requires 'requests')...\n")
        results.append("\nProbing Results:")
        for u in urls:
            up, info = probe_url(u)
            status = "UP" if up else "DOWN"
            line = f"{u:40} -> {status:4} : {info}"
            print(line)
            results.append(line)

    # Save everything to file
    out_file = "subdomain_results.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(results))

    print(f"\n[+] Results saved to {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python subdomain_url_builder.py <domain> [--check]")
        sys.exit(1)
    domain_arg = sys.argv[1]
    do_check = "--check" in sys.argv
    main(domain_arg, check=do_check)
