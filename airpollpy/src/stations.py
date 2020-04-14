from enum import Enum
from pandas import DataFrame
from src import csv_dataset

FilterMode = Enum('FilterMode', 'max min')


def get_stations_data(path: str) -> DataFrame:
    df = csv_dataset.get_dataframe(path, 'iso-8859-1')
    return df


def get_stations_filtered(df: DataFrame, func, filter_mode: str, pollutant: str) -> DataFrame:
    """
    :param df: stations data frame
    :param func: function to apply to the grouped by series statistic value
    :param pollutant: the pollutant concerned
    :param filter_mode: way to filter the stations
    :return: the data set limited to the station that has been filtered per city
    """

    df = df.loc[df.groupby(["city_name"])["statistic_value (µg/m3)"].apply(func)]
    df.rename({'statistic_value (µg/m3)': filter_mode.name + ' ' + pollutant + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def get_worst_stations(path: str, pollutant: str) -> DataFrame:
    df = get_stations_data(path)
    return get_stations_filtered(df, lambda x: x.idxmax(), FilterMode.max, pollutant)


def get_best_stations(path: str, pollutant: str) -> DataFrame:
    df = get_stations_data(path)
    return get_stations_filtered(df, lambda x: x.idxmin(), FilterMode.min, pollutant)


def get_mean_per_city(path: str, pollutant: str) -> DataFrame:
    df = get_stations_data(path)
    df = df.groupby(["country iso code", "city_name"])["statistic_value (µg/m3)"].mean().to_frame()
    df.rename({'statistic_value (µg/m3)': 'mean ' + pollutant + ' (µg/m3)'}, axis=1, inplace=True)
    return df

