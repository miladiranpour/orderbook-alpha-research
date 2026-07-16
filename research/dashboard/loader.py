import pickle
from pathlib import Path


def load_result(path):
    with Path(path).open("rb") as file:
        return pickle.load(file)
