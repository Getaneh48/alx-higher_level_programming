#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request as request
import sys

if __name__ == '__main__':
    """
    entry point
    """
    with request.urlopen(sys.argv[1]) as resp:
        print(resp.getheader('X-Request-Id'))
