#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    user = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(user, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")
