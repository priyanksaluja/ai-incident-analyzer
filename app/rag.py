import json

def load_incidents():
    with open("app/data/incidents.json") as f:
        return json.load(f)
    