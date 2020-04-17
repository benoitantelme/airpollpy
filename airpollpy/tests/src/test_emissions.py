from pathlib import Path

from data.constants import POLLUTANT
from src import emissions
from src.emissions import concat_two_sets, concat_sets, get_mean_frame, get_dataframe


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
    merged = concat_two_sets(path + 'GB_7_21131_2013_timeseries.csv', path + 'GB_7_21151_2013_timeseries.csv')
    assert len(merged.columns) == 6
    assert len(merged) == 17269


def test_concat_sets():
    path = "../../data/main/cleaned/o3/Amsterdam/"
    concat = concat_sets(path, '2013')
    assert len(concat.columns) == 6
    assert len(concat) == 34277


def test_get_mean_frame():
    path = "../../data/main/cleaned/o3/Amsterdam/"
    df = concat_sets(path, '2013')
    df = get_mean_frame(df, POLLUTANT.o3)
    mean = df.iloc[0]['mean o3 (µg/m3)']

    total = 0
    nbr = 0
    for path in Path(path).rglob('*2013*.csv'):
        df2 = get_dataframe(path)
        total += df2[df2['DatetimeBegin'] == '2013-01-01 00:00:00 +01:00']["Concentration"].item()
        nbr += 1
    assert mean == (total/nbr)







