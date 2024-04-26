#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == '__main__':
    """
    entry point
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            result = resp.read()
            print(result.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
