import os

PAYLOADS_DIR = os.path.join("payloads")

SQL_PAYLOADS_FILE = os.path.join(PAYLOADS_DIR, "sql_payloads.txt")
XSS_PAYLOADS_FILE = os.path.join(PAYLOADS_DIR, "xss_payloads.txt")
HEADERS_CONFIG_FILE = os.path.join(PAYLOADS_DIR, "headers_config.txt")
CSRF_TOKENS_FILE = os.path.join(PAYLOADS_DIR, "csrf_tokens.txt")

REQUEST_TIMEOUT = 10  # Timeout des requêtes (s)
USER_AGENT = "Vuln3Rs/1.0"

def check_payload_files():
    files = [SQL_PAYLOADS_FILE, XSS_PAYLOADS_FILE, HEADERS_CONFIG_FILE, CSRF_TOKENS_FILE]
    missing_files = [f for f in files if not os.path.exists(f)]
    if missing_files:
        print(f"[!] Warning: The following payload files are missing: {', '.join(missing_files)}")
    else:
        print("[*] All payload files are present.")

check_payload_files()