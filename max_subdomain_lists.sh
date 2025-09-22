#!/usr/bin/env bash
# subdomain_url_builder.sh
# Bash 4+
# Optional probing requires: curl

set -euo pipefail

# --- Subdomain wordlist (expandable) ---
SUBDOMAIN_RAW=$(cat <<'EOF'
www
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
EOF
)

OUT_FILE="subdomain_results.txt"

normalize_domain() {
    local input="$1"
    # Strip scheme if present
    input="${input#http://}"
    input="${input#https://}"
    # Strip path
    input="${input%%/*}"
    # Strip trailing colon (if user gave domain:)
    input="${input%%:}"
    echo "${input,,}"   # lowercase
}

build_hostnames() {
    local domain="$1"
    while read -r sub; do
        [[ -z "$sub" ]] && continue
        if [[ "$sub" == "@" ]]; then
            echo "$domain"
        else
            echo "$sub.$domain"
        fi
    done <<< "$SUBDOMAIN_RAW"
}

build_urls() {
    local hostnames="$1"
    while read -r host; do
        [[ -z "$host" ]] && continue
        echo "https://$host"
        echo "http://$host"
    done <<< "$hostnames"
}

probe_url() {
    local url="$1"
    # Use curl with HEAD first, fallback to GET
    local code
    code=$(curl -o /dev/null -s -w "%{http_code}" -m 4 -I "$url" || true)
    if [[ "$code" == "405" || "$code" == "" ]]; then
        code=$(curl -o /dev/null -s -w "%{http_code}" -m 4 "$url" || true)
    fi
    if [[ -n "$code" && "$code" -gt 0 ]]; then
        echo "UP   : HTTP $code"
    else
        echo "DOWN : failed"
    fi
}

main() {
    if [[ $# -lt 1 ]]; then
        echo "Usage: $0 <domain> [--check]"
        exit 1
    fi

    local domain_input="$1"
    local check="${2:-}"
    local domain
    domain=$(normalize_domain "$domain_input")

    echo "Normalized domain: $domain"
    echo

    # Build hostnames and URLs
    hostnames=$(build_hostnames "$domain")
    urls=$(build_urls "$hostnames")

    {
        echo "Target domain: $domain"
        echo
        echo "Hostnames:"
        echo "$hostnames" | sed 's/^/  /'
        echo
        echo "URLs (https first):"
        echo "$urls" | sed 's/^/  /'
    } | tee "$OUT_FILE"

    # Optional probing
    if [[ "$check" == "--check" ]]; then
        echo
        echo "Probing URLs..."
        {
            echo
            echo "Probing Results:"
            while read -r u; do
                result=$(probe_url "$u")
                printf "%-40s -> %s\n" "$u" "$result"
            done <<< "$urls"
        } | tee -a "$OUT_FILE"
    fi

    echo
    echo "[+] Results saved to $OUT_FILE"
}

main "$@"
