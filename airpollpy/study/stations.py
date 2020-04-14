import pandas as pd
from pandas import DataFrame
from src import csv_dataset


def get_stations_data(path: str) -> DataFrame:
    df = csv_dataset.get_dataframe(path, 'iso-8859-1')
    return df


def get_worst_stations(path: str) -> DataFrame:
    """
    :param path: path of the data file
    :return: the data set limited to the worst traffic urban station per city
    """

    df = get_stations_data(path)
    df = df[df['type_of_station'] == 'Traffic']
    df = df[df['station_type_of_area'] == 'urban']

    # keep only worse values for criteria
    df = df.loc[df.groupby(["city_name"])["statistic_value (µg/m3)"].idxmax()]

    return df



