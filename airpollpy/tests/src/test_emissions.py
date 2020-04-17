from data.constants import POLLUTANT
from src import emissions
from src.emissions import concat_two_sets, concat_sets, get_mean_frame


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
    assert len(concat) == 68554


def test_get_mean_frame():
    path = "../../data/main/cleaned/o3/Amsterdam/"
    df = concat_sets(path, '2013')
    df = get_mean_frame(df, POLLUTANT.o3)
    print()





