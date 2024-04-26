#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""


if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    user = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, password))
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except requests.exceptions.JSONDecodeError:
        print('None')
