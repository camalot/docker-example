import re
import json
import random
import requests
import click

@click.command()
@click.option("--verbs", "-v", default=1, help="Number of verbs to generate")
@click.option("--nouns", "-n", default=1, help="Number of nouns to generate")
@click.option("--adjectives", "-a", default=1, help="Number of adjectives to generate")
def get_name(verbs: int = 1, nouns: int = 1, adjectives: int = 1) -> None:
    snouns = load_from_gist("nouns", nouns)
    sadjectives = load_from_gist("adjectives", adjectives)
    sverbs = load_from_gist("verbs", verbs)
    print(f"{' '.join(sadjectives)} {' '.join(snouns)} {' '.join(sverbs)}")


def load_from_gist(type: str, count: int) -> list:
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

if __name__ == '__main__':
    get_name()
