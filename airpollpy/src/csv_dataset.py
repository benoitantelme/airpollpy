import pandas as pd
from pandas import DataFrame


def get_dataframe(path: str) -> DataFrame:
    return pd.read_csv(path)


def clean_pm10_timeseries(path: str) -> DataFrame:
    df = pd.read_csv(path)

    df.drop(['Namespace', 'AirQualityNetwork', 'AirQualityStationEoICode', 'SamplingPoint', 'SamplingProcess', 'AirPollutantCode',
             'DatetimeEnd', 'Verification'], axis=1, inplace=True)

    # clean invalid rows
    df = df[df['Validity'] != -1]

    return df


