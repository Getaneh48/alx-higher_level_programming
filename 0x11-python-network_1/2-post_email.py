#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys

if __name__ == '__main__':
    """
    entry point
    """
    url = sys.argv[1]
    email = sys.agv[2]
    data = {'email': email}
    post_data = urlib.parse.urlencode(data)
    post_data = post_data.encode('utf8')
    req = urllib.request.Request(url, post_data)

    with urllib.request.urlopen(req) as resp:
        result = resp.read()
        print(result.decode("utf8"))
