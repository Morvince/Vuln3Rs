import requests
from config import XSS_PAYLOADS_FILE, REQUEST_TIMEOUT, USER_AGENT 

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def scan_xss(url):
    payloads = load_payloads(XSS_PAYLOADS_FILE)
    headers = {"User-Agent": USER_AGENT}
    
    print(f"[*] Testing XSS on {url}")
    
    vulnerable = False
    for payload in payloads:
        full_url = f"{url}?q={payload}"  # le param q est supposément vulnérable
        try:
            response = requests.get(full_url, headers=headers, timeout=REQUEST_TIMEOUT)
            
            # Si le script est exécuté dans la page alors => vulnérable
            if payload in response.text:
                print(f"[!] XSS vulnerability detected with payload: {payload}")
                vulnerable = True
            else:
                print(f"[-] No XSS vulnerability detected with payload: {payload}")
        
        except requests.exceptions.RequestException as e:
            print(f"[!] Error during request: {e}")
    
    if not vulnerable:
        print("[*] XSS scan complete, no vulnerabilities found.")
