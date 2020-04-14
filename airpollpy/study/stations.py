from enum import Enum
from pandas import DataFrame
from src import csv_dataset


FilterMode = Enum('FilterMode', 'max min')


def get_stations_data(path: str) -> DataFrame:
    df = csv_dataset.get_dataframe(path, 'iso-8859-1')
    return df


def get_stations_filtered(df: DataFrame, filter_mode: FilterMode) -> DataFrame:
    """
    :param filter_mode: way to filter the stations
    :param df: stations data frame
    :return: the data set limited to the worst station per city
    """

    if filter_mode == FilterMode.max:
        df = df.loc[df.groupby(["city_name"])["statistic_value (µg/m3)"].idxmax()]
    elif filter_mode == FilterMode.min:
        df = df.loc[df.groupby(["city_name"])["statistic_value (µg/m3)"].idxmin()]
    return df


def get_worst_stations(path: str) -> DataFrame:
    df = get_stations_data(path)
    return get_stations_filtered(df, FilterMode.max)


def get_best_stations(path: str) -> DataFrame:
    df = get_stations_data(path)
    return get_stations_filtered(df, FilterMode.min)


