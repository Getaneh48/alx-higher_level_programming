#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 2:
        search = sys.argv[1]
        data = {'q': search}
    else:
        data = {'q': ''}
    resp = requests.post(url, data=data)
    result = resp.json()
    if resp.headers.get('Content-Type') == 'application/json':
        if len(result) == 0:
            print("No result")
        else:
            print(f"[{result['id']}] {result['name']}")
    else:
        print("No result")
