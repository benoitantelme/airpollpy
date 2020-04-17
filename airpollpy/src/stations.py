from data.constants import POLLUTANT
from pandas import DataFrame, concat, merge
from src import emissions

STATISTIC_VALUE = "statistic_value (µg/m3)"


def get_stations_data(path: str) -> DataFrame:
    df = emissions.get_dataframe(path, 'iso-8859-1')
    return df


def get_stations_filtered(df: DataFrame, func) -> DataFrame:
    """
    :param df: stations data frame
    :param func: function to apply to the grouped by series statistic value
    :return: the data set limited to the stations that has been filtered for each city
    """

    return df.loc[df.groupby(["city_name"], as_index=False)[STATISTIC_VALUE].apply(func)]


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
    df = df.groupby(["country iso code", "city_name"], as_index=False)[STATISTIC_VALUE].mean()
    df.rename({STATISTIC_VALUE: 'mean ' + pollutant.name + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def clean_df(df):
    df.drop(['station_european_code', 'type_of_station', 'station_type_of_area', 'component_caption', 'above_AQG?',
             'country iso code'], axis=1, inplace=True)


def create_pollutants_df(path: str, pollutant: POLLUTANT) -> DataFrame:
    worst_df = get_worst_stations(path, pollutant)
    clean_df(worst_df)

    best_df = get_best_stations(path, pollutant)
    clean_df(best_df)

    mean_df = get_mean_per_city(path, pollutant)

    res = merge(worst_df, mean_df)
    res = merge(res, best_df)
    res['city_name'] = res['city_name'].str.replace('Helsinki / Helsingfors', 'Helsinki')
    return res


def filter_main_cities(df: DataFrame) -> DataFrame:
    return df[df['city_name'].isin(['Paris', 'London', 'Berlin', 'Madrid', 'Roma', 'Dublin', 'København',
                                    'Thessaloniki', 'Bruxelles', 'Lisboa', 'Luxembourg', 'Oslo', 'Stockholm',
                                    'Wien', 'Sofia', 'Zagreb', 'Praha', 'Tallinn', 'Amsterdam',
                                    'Helsinki', 'Budapest', 'Riga', 'Vilnius', 'Warszawa'])]


def get_best_station(path: str):
    df = get_stations_data(path)
    df = filter_main_cities(df)
    df.drop(['type_of_station', 'station_type_of_area', 'component_caption', 'above_AQG?'], axis=1, inplace=True)

    df['mean'] = df.groupby('city_name')[STATISTIC_VALUE].transform('mean')
    df['diff'] = abs(df['mean'] - df[STATISTIC_VALUE])
    df['diff %'] = df['diff'] * 100 / df['mean']
    return df.loc[df.groupby("city_name")["diff"].idxmin()]

