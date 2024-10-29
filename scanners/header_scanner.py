import requests
from config import HEADERS_CONFIG_FILE, REQUEST_TIMEOUT, USER_AGENT

def load_headers_config(file_path):
    headers_config = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            header, *expected_value = line.strip().split(':')
            headers_config.append((header.strip(), expected_value[0].strip() if expected_value else None))
    return headers_config

def scan_headers(url):
    print(f"[*] Testing HTTP headers on {url}")
    
    headers_config = load_headers_config(HEADERS_CONFIG_FILE) 
    headers = {"User-Agent": USER_AGENT}
    
    try:
        response = requests.head(url, headers=headers, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.RequestException as e:
        print(f"[!] Error during request: {e}")
        return

    for header, expected_value in headers_config:
        if header in response.headers:
            actual_value = response.headers[header]
            if expected_value:
                if actual_value == expected_value:
                    print(f"[+] {header} is correctly set to '{expected_value}'.")
                else:
                    print(f"[!] {header} is present but has an unexpected value '{actual_value}'. Expected: '{expected_value}'.")
            else:
                print(f"[+] {header} is present.")
        else:
            print(f"[-] {header} is missing.")
    
    print("[*] Header scan complete.")
