import pandas as pd


def get_dataset(path: str):
    return pd.read_csv(path)


