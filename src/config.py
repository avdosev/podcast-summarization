import json

def read_config(path='config.json'):
    with open(path) as f:
        return json.load(f)
