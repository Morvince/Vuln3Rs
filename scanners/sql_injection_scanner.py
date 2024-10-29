import requests
from config import SQL_PAYLOADS_FILE, REQUEST_TIMEOUT, USER_AGENT

# chargement des payloads par fichier
def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def scan_sql_injection(url):
    payloads = load_payloads(SQL_PAYLOADS_FILE)
    headers = {"User-Agent": USER_AGENT}
    
    print(f"[*] Testing SQL Injection on {url}")
    
    vulnerable = False
    for payload in payloads:
        full_url = f"{url}?id={payload}"
        try:
            response = requests.get(full_url, headers=headers, timeout=REQUEST_TIMEOUT)
            
            # recherche des "probables" erreurs sql
            if "error" in response.text or "syntax" in response.text:
                print(f"[!] SQL Injection vulnerability detected with payload: {payload}")
                vulnerable = True
            else:
                print(f"[-] No vulnerability detected with payload: {payload}")
        
        except requests.exceptions.RequestException as e:
            print(f"[!] Error during request: {e}")
    
    if not vulnerable:
        print("[*] SQL Injection scan complete, no vulnerabilities found.")
