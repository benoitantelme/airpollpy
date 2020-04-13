import pandas as pd
from pandas import DataFrame
from src import csv_dataset


def get_stations_data(path: str) -> DataFrame:
    df = csv_dataset.get_dataframe(path, 'iso-8859-1')
    return df



