#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request as request

if __name__ == '__main__':
    """
    entry point
    """
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf8')}")
