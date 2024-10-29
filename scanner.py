#!/usr/bin/env python3

import argparse
from scanners.sql_injection_scanner import sql_injection_scanner
from scanners.xss_scanner import xss_scanner
from scanners.csrf_scanner import csrf_scanner
from scanners.header_scanner import header_scanner

def main():
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")

    parser.add_argument('--sqli', action='store_true', help="Scanner pour les injections SQL")
    parser.add_argument('--xss', action='store_true', help="Scanner pour les failles XSS")
    parser.add_argument('--csrf', action='store_true', help="Scanner pour les failles CSRF")
    parser.add_argument('--headers', action='store_true', help="Scanner pour les en-têtes HTTP")
    parser.add_argument('--all', action='store_true', help="Lancer tous les scanners")
    parser.add_argument('url', type=str, help="URL cible à scanner")
    
    args = parser.parse_args()
    url = args.url

    # option de scan SQLi
    if args.sqli:
        sql_injection_scanner(url)

    # option de scan XSS
    if args.xss:
        xss_scanner(url)

    # option de scan CSRF
    if args.csrf:
        csrf_scanner(url)

    # option de scan des headers
    if args.headers:
        header_scanner(url)

    # Si l'option "all" est activée, exécuter tous les scanners
    if args.all:
        print("[*] Lancement de tous les scanners...")
        sql_injection_scanner(url)
        xss_scanner(url)
        csrf_scanner(url)
        header_scanner(url)

if __name__ == "__main__":
    main()