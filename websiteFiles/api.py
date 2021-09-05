import json
import random
import requests


def search():
    r = requests.get("https://api.github.com/repositories")
    json_data = json.loads(r.text)
    repo_list = []
    for i in range(3):
        li = random.choice(json_data)
        name_repo = li["name"]
        name_author = li["owner"]["login"]

        repo_list.append({"name": name_repo, "author": name_author})
    return repo_list
