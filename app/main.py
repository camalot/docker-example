import re
import json
import random
import requests

def main():
    nouns = load_from_gist("nouns", 1)
    adjectives = load_from_gist("adjectives", 1)
    verbs = load_from_gist("verbs", 1)
    print(f"{' '.join(adjectives)} {' '.join(nouns)} {' '.join(verbs)}")


def load_from_gist(type, count):
    types = [ "adjectives", "nouns", "verbs" ]
    if type not in types:
        type = "nouns"
    if count <= 0:
        count = 1
    elif count > 10:
        count = 10
    data = requests.get(f"https://gist.githubusercontent.com/camalot/8d2af3796ac86083e873995eab98190d/raw/b39de3a6ba03205380caf5d58e0cae8a869ac36d/{type}.js").text
    data = re.sub(r"(var\s(adjectives|nouns|verbs)\s=\s)|;$","", data)
    jdata = json.loads(data)
    return random.sample(jdata, count)

if __name__ == "__main__":
    main()
