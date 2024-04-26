#!/usr/bin/python3
"""
a python script that reads a github commits
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    headers = {'X-GitHub-Api-Version': '2022-11-28'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for commit in response.json():
            commit_hash = commit['commit']['tree']['sha']
            author_name = commit['commit']['author']['name']
            print(f"{commit_hash}: {author_name}")
    else:
        print("None")
