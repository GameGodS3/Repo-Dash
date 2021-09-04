import json
import random
import requests


def search():
    r = requests.get("https://api.github.com/repositories")
    json_data = json.loads(r.text)
    repo_name_li = []
    repo_author_li = []
    for i in range(3):
        li = random.choice(json_data)
        name_repo = li["name"]
        name_author = li["owner"]["login"]

        repo_name_li.append(name_repo)
        repo_author_li.append(name_author)

    return repo_name_li, repo_author_li
