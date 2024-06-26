#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    """
    entry point
    """
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys

    email = sys.argv[2]
    url = sys.argv[1]
    data = {'email': email}

    with urlopen(url, urlencode(data).encode('utf-8')) as resp:
        print(resp.read().decode('utf-8'))
