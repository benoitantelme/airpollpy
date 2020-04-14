from enum import Enum
from pandas import DataFrame
from src import csv_dataset


FilterMode = Enum('FilterMode', 'max min')


def get_stations_data(path: str) -> DataFrame:
    df = csv_dataset.get_dataframe(path, 'iso-8859-1')
    return df


def get_stations_filtered(df: DataFrame, filter_mode: FilterMode, pollutant: str) -> DataFrame:
    """
    :param pollutant: the pollutant concerned
    :param filter_mode: way to filter the stations
    :param df: stations data frame
    :return: the data set limited to the worst station per city
    """

    if filter_mode == FilterMode.max:
        df = df.loc[df.groupby("city_name")["statistic_value (µg/m3)"].idxmax()]
    elif filter_mode == FilterMode.min:
        df = df.loc[df.groupby("city_name")["statistic_value (µg/m3)"].idxmin()]
    else:
        raise ValueError(filter_mode + ' is not an expected value')

    df.rename({'statistic_value (µg/m3)': filter_mode.name + ' ' + pollutant + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def get_worst_stations(path: str, pollutant: str) -> DataFrame:
    df = get_stations_data(path)
    return get_stations_filtered(df, FilterMode.max, pollutant)


def get_best_stations(path: str, pollutant: str) -> DataFrame:
    df = get_stations_data(path)
    return get_stations_filtered(df, FilterMode.min, pollutant)


def get_mean_per_city(path: str, pollutant: str) -> DataFrame:
    df = get_stations_data(path)
    df = df.groupby("city_name")["statistic_value (µg/m3)"].mean().to_frame()
    df.rename({'statistic_value (µg/m3)': 'mean ' + pollutant + ' (µg/m3)'}, axis=1, inplace=True)
    return df

