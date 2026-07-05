import json


def load_json(path):

    records = []

    with open(path, "r") as f:

        for line in f:
            records.append(json.loads(line))

    return records