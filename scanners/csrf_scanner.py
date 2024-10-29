import requests
from bs4 import BeautifulSoup
from config import CSRF_TOKENS_FILE, REQUEST_TIMEOUT, USER_AGENT

def load_csrf_token_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def scan_csrf(url):
    print(f"[*] Testing for CSRF protection on {url}")
    
    csrf_token_names = load_csrf_token_names(CSRF_TOKENS_FILE)
    headers = {"User-Agent": USER_AGENT}
    
    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.RequestException as e:
        print(f"[!] Error during request: {e}")
        return
    
    # Parse pour identifier les formulaires
    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")
    
    if not forms:
        print("[-] No forms found on the page.")
        return
    
    for index, form in enumerate(forms, start=1):
        has_csrf_token = False
        # lookup d'un champ correspondant à un nom de token CSRF
        for input_tag in form.find_all("input"):
            if input_tag.get("name") in csrf_token_names:
                print(f"[+] Form {index} contains a CSRF token field: {input_tag.get('name')}")
                has_csrf_token = True
                break
        
        if not has_csrf_token:
            print(f"[-] Form {index} is missing a CSRF token field.")
    
    print("[*] CSRF scan complete.")
