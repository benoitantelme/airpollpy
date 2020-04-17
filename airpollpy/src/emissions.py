import pandas as pd
from pandas import DataFrame
from pathlib import Path

from data.constants import POLLUTANT


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


def concat_sets(dir_path: str, year: str) -> DataFrame:
    df = DataFrame()
    for path in Path(dir_path).rglob('*' + year + '*.csv'):
        df = pd.concat([df, get_dataframe(path)])
    return df


def get_mean_frame(df: DataFrame, pollutant: POLLUTANT) -> DataFrame:
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", "DatetimeBegin"],
                    as_index=False)["Concentration"].mean()
    df.rename({"Concentration": 'mean ' + pollutant.name + ' (µg/m3)'}, axis=1, inplace=True)
    return df


