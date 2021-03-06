import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path
from data.constants import POLLUTANT, YEAR, CITY, CITY_NAME, DATE_NAME, PREVIOUS_YEAR_VALUE, YEAR_VALUE


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
    for path in Path(f'../../data/main/cleaned/{pollutant.name}').rglob('*.csv'):
        df = pd.read_csv(path)
        df.drop_duplicates(inplace=True)
        df.to_csv(path, index=False)


def concat_two_sets(path1: str, path2: str) -> DataFrame:
    df1 = get_dataframe(path1)
    df2 = get_dataframe(path2)

    return pd.concat([df1, df2])


def concat_sets(dir_path: str, year: YEAR) -> DataFrame:
    df = DataFrame()
    for path in Path(dir_path).rglob(f'*{year.name}*.csv'):
        df = pd.concat([df, get_dataframe(path)])
    return df


def get_mean_frame(df: DataFrame, pollutant: POLLUTANT) -> DataFrame:
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", "DatetimeBegin"],
                    as_index=False)["Concentration"].mean()
    df.rename({"Concentration": f'mean {pollutant.name} (µg/m3)'}, axis=1, inplace=True)
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
                    df.to_csv(f"../../data/main/cleaned/mean/{city.name}_{pollutant.name}_{year.name}.csv",
                              index=False)


def set_date(df: DataFrame) -> DataFrame:
    df['DatetimeBegin'] = pd.to_datetime(df['DatetimeBegin'])
    df[DATE_NAME] = df['DatetimeBegin'].apply(lambda x: x.normalize())
    df.drop('DatetimeBegin', axis=1, inplace=True)
    return df


def mean_per_day(df: DataFrame) -> DataFrame:
    measure_name = df.columns.values[-1]

    df = set_date(df)
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", DATE_NAME],
                    as_index=False)[measure_name].mean().round(2)
    return df


def mean_per_month(df: DataFrame) -> DataFrame:
    measure_name = df.columns.values[-1]

    df = set_date(df)
    df[DATE_NAME] = df['Date'].apply(lambda x: x.replace(day=1))
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", DATE_NAME],
                    as_index=False)[measure_name].mean().round(2)
    return df


def create_pollutant_df(pollutant: POLLUTANT, main_path: str) -> DataFrame:
    df = pd.DataFrame()
    for city in CITY:
        city_df = pd.DataFrame()
        for path in Path(main_path).rglob(f'{city.name}_{pollutant.name}_*.csv'):
            print(path.absolute())
            df_tmp = mean_per_month(get_dataframe(path))
            city_df = pd.concat([city_df, df_tmp])
        city_df[CITY_NAME] = city.name
        df = pd.concat([df, city_df])
    return df


def compare_year_to_year(df: DataFrame) -> DataFrame:
    measure_name = df.columns.values[-2]

    # create date info and clean
    df['Year'] = df[DATE_NAME].apply(lambda x: x.year)
    df['DM'] = df[DATE_NAME].apply(lambda x: f'{x.day}-{x.month}')
    first_year = df['Year'].iloc[0]
    df.reset_index(drop=True, inplace=True)

    # copy first year measurement
    df[PREVIOUS_YEAR_VALUE] = df[df['Year'] == first_year][measure_name]
    df[PREVIOUS_YEAR_VALUE] = df.groupby([CITY_NAME, 'DM'], as_index=False)[PREVIOUS_YEAR_VALUE].transform('sum')

    # calculate the diff on second year
    df = df[df['Year'] != first_year]
    df[YEAR_VALUE] = df[measure_name]
    df['diff'] = df[YEAR_VALUE] - df[PREVIOUS_YEAR_VALUE]
    df['diff %'] = df['diff'] * 100 / df[PREVIOUS_YEAR_VALUE]

    # cleanup
    df.drop(measure_name, axis=1, inplace=True)
    df.drop('DM', axis=1, inplace=True)
    df.drop('Year', axis=1, inplace=True)

    return df


