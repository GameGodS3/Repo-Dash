def search():
    r = requests.get("https://api.github.com/repositories")
    json_data = json.loads(r.text)
    li = random.choice(json_data)
    name_repo = li["name"]
    name_author = li["owner"]["login"]
    
    return name_repo,name_author
    
import json
import requests
import random

search()


