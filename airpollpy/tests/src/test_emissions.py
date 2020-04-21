from pathlib import Path
from data.constants import POLLUTANT, YEAR
from src import emissions
from src.emissions import concat_two_sets, concat_sets, get_mean_frame, get_dataframe, mean_per_day, mean_per_month, \
    create_pollutant_df
from datetime import datetime


def test_get_dataframe():
    df = emissions.get_dataframe("../../data/test/csv_test_1.csv")
    assert len(df) == 3
    assert len(df.columns) == 3


def test_get_dataframe_encoding():
    df = emissions.get_dataframe("../../data/test/csv_test_2.csv", 'iso-8859-1')
    assert len(df) == 3
    assert len(df.columns) == 3


def test_concat_two_sets():
    path = "../../data/main/cleaned/o3/London/"
    merged = concat_two_sets(f'{path}GB_7_21131_2015_timeseries.csv', f'{path}GB_7_21131_2015_timeseries.csv')
    assert len(merged.columns) == 6
    assert len(merged) == 17444


def test_concat_sets():
    path = "../../data/main/cleaned/o3/Amsterdam/"
    concat = concat_sets(path, YEAR['2015'])
    assert len(concat.columns) == 6
    assert len(concat) == 34224


def test_get_mean_frame():
    path = "../../data/main/cleaned/o3/Amsterdam/"
    year = YEAR['2015']
    df = concat_sets(path, year)
    df = get_mean_frame(df, POLLUTANT.o3)
    mean = df.iloc[0]['mean o3 (µg/m3)']

    total = 0
    nbr = 0
    for path in Path(path).rglob('*' + year.name + '*.csv'):
        df2 = get_dataframe(path)
        total += df2[df2['DatetimeBegin'] == '2015-01-01 00:00:00 +01:00']["Concentration"].item()
        nbr += 1
    assert mean == (total/nbr)


first_day = datetime.strptime('2015-01-01', '%Y-%m-%d').date()


def test_mean_per_day():
    df = get_dataframe("../../data/main/cleaned/mean/Amsterdam_o3_2015.csv")
    measure_name = df.columns.values[-1]
    expected_mean = df[df['DatetimeBegin'].str.contains('2015-01-01')][measure_name].sum()/24

    df = mean_per_day(df)
    assert expected_mean.round(2) == df[df["Date"] == first_day][measure_name].item()


def test_mean_per_month():
    df = get_dataframe("../../data/main/cleaned/mean/Amsterdam_o3_2015.csv")
    measure_name = df.columns.values[-1]
    expected_mean = df[df['DatetimeBegin'].str.contains('2015-01')][measure_name].sum() / (24*31)

    df = mean_per_month(df)
    assert expected_mean.round(2) == df[df["Date"] == first_day][measure_name].item()


def test_create_pollutant_df():
    df = create_pollutant_df(POLLUTANT.o3, "../../data/test/mean/")
    assert len(df.columns) == 6
    assert len(df) == 48

