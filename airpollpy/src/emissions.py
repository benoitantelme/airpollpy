import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path

from data.constants import POLLUTANT, YEAR, CITY, UNDERSCORE, SPACE, HYPHEN


def get_dataframe(path: str, encoding=None) -> DataFrame:
    if not encoding:
        encoding = 'UTF-8'
    return pd.read_csv(path, encoding=encoding)


def clean_pm10_timeseries(path: str) -> DataFrame:
    df = pd.read_csv(path)

    df.drop(['Namespace', 'AirQualityNetwork', 'AirQualityStationEoICode', 'SamplingPoint', 'SamplingProcess',
             'AirPollutantCode',
             'DatetimeEnd', 'Verification', 'Sample', 'AveragingTime'], axis=1, inplace=True)

    # clean invalid rows
    df = df[df['Validity'] != -1]
    df.drop('Validity', axis=1, inplace=True)

    return df


def clean_and_export_data(path: str):
    for path in Path('../../data/main/original').rglob('*.csv'):
        print(path.absolute())
        df = clean_pm10_timeseries(path.absolute())
        new_path = str(path.absolute()).replace('original', 'cleaned')
        df.to_csv(new_path, index=False)
        print(new_path)


def remove_cs_index():
    for path in Path('../../data/main/cleaned/pm25').rglob('*.csv'):
        df = pd.read_csv(path)
        df.drop(['Unnamed: 0'], axis=1, inplace=True)
        df.to_csv(path, index=False)


def remove_duplicates(pollutant: POLLUTANT):
    # shouldn't be there but found out the original files actually had lots of duplicates
    for path in Path('../../data/main/cleaned/' + pollutant.name).rglob('*.csv'):
        df = pd.read_csv(path)
        df.drop_duplicates(inplace=True)
        df.to_csv(path, index=False)


def concat_two_sets(path1: str, path2: str) -> DataFrame:
    df1 = get_dataframe(path1)
    df2 = get_dataframe(path2)

    return pd.concat([df1, df2])


def concat_sets(dir_path: str, year: YEAR) -> DataFrame:
    df = DataFrame()
    for path in Path(dir_path).rglob('*' + year.name + '*.csv'):
        df = pd.concat([df, get_dataframe(path)])
    return df


def get_mean_frame(df: DataFrame, pollutant: POLLUTANT) -> DataFrame:
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", "DatetimeBegin"],
                    as_index=False)["Concentration"].mean()
    df.rename({"Concentration": 'mean ' + pollutant.name + ' (µg/m3)'}, axis=1, inplace=True)
    return df


def create_mean_sets() -> DataFrame:
    path = "../../data/main/cleaned/"
    for pollutant in POLLUTANT:
        for city in CITY:
            tmp_path = path + pollutant.name + os.path.sep + city.name + os.path.sep
            for year in YEAR:
                df = concat_sets(tmp_path, year)
                if not df.empty:
                    df = get_mean_frame(df, pollutant)
                    df.to_csv("../../data/main/cleaned/mean/" + city.name + UNDERSCORE + pollutant.name +
                              UNDERSCORE + year.name + '.csv',
                              index=False)


def set_date(df: DataFrame) -> DataFrame:
    df['DatetimeBegin'] = df['DatetimeBegin'].apply(lambda x: pd.to_datetime(x))
    df['Date'] = df['DatetimeBegin'].apply(lambda x: x.date())
    df.drop('DatetimeBegin', axis=1, inplace=True)
    return df


def mean_per_day(df: DataFrame) -> DataFrame:
    measure_name = df.columns.values[-1]

    df = set_date(df)
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", "Date"],
                    as_index=False)[measure_name].mean().round(2)
    return df


def mean_per_month(df: DataFrame) -> DataFrame:
    measure_name = df.columns.values[-1]

    df = set_date(df)
    df['Date'] = df['Date'].apply(lambda x: str(x.year) + HYPHEN + x.strftime('%m'))
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", "Date"],
                    as_index=False)[measure_name].mean().round(2)
    return df
