from data.constants import POLLUTANT
from pandas import DataFrame, concat
from src import csv_dataset

STATISTIC_VALUE = "statistic_value (µg/m3)"


def get_stations_data(path: str) -> DataFrame:
    df = csv_dataset.get_dataframe(path, 'iso-8859-1')
    return df


def get_stations_filtered(df: DataFrame, func) -> DataFrame:
    """
    :param df: stations data frame
    :param func: function to apply to the grouped by series statistic value
    :return: the data set limited to the stations that has been filtered for each city
    """

    return df.loc[df.groupby(["city_name"])[STATISTIC_VALUE].apply(func)]


def get_worst_stations(path: str, pollutant: POLLUTANT) -> DataFrame:
    df = get_stations_filtered(get_stations_data(path), lambda x: x.idxmax())
    df.rename({STATISTIC_VALUE: 'max ' + pollutant.name + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def get_best_stations(path: str, pollutant: POLLUTANT) -> DataFrame:
    df = get_stations_filtered(get_stations_data(path), lambda x: x.idxmin())
    df.rename({STATISTIC_VALUE: 'min ' + pollutant.name + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def get_mean_per_city(path: str, pollutant: POLLUTANT) -> DataFrame:
    df = get_stations_data(path)
    df = df.groupby(["country iso code", "city_name"])[STATISTIC_VALUE].mean().reset_index()
    df.rename({STATISTIC_VALUE: 'mean ' + pollutant.name + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def clean_df(df):
    df.drop(['station_european_code', 'type_of_station', 'station_type_of_area', 'component_caption', 'above_AQG?',
             'country iso code'], axis=1, inplace=True)


def set_index(df):
    df.set_index('city_name', inplace=True)


def create_pollutants_df(pollutant: POLLUTANT, path: str) -> DataFrame:
    worst_df = get_worst_stations(path, pollutant)
    clean_df(worst_df)
    set_index(worst_df)

    best_df = get_best_stations(path, pollutant)
    clean_df(best_df)
    set_index(best_df)

    mean_df = get_mean_per_city(path, pollutant)
    set_index(mean_df)

    return concat([worst_df, mean_df, best_df], axis=1)


