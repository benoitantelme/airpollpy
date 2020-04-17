import pandas as pd
from pandas import DataFrame
import os
from pathlib import Path


def get_dataframe(path: str, encoding=None) -> DataFrame:
    if not encoding:
        encoding = 'UTF-8'
    return pd.read_csv(path, encoding=encoding)


def clean_pm10_timeseries(path: str) -> DataFrame:
    df = pd.read_csv(path)

    df.drop(['Namespace', 'AirQualityNetwork', 'AirQualityStationEoICode', 'SamplingPoint', 'SamplingProcess', 'AirPollutantCode',
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


def merge_two_sets(path1: str, path2: str) -> DataFrame:
    df1 = get_dataframe(path1)
    df2 = get_dataframe(path2)

    merged = pd.concat([df1, df2])
    # merged = pd.merge(df1, df2)
    return merged




