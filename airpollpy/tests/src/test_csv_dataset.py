from src import csv_dataset
from src.csv_dataset import concat_two_sets


def test_get_dataframe():
    df = csv_dataset.get_dataframe("../../data/test/csv_test_1.csv")
    assert len(df) == 3
    assert len(df.columns) == 3


def test_get_dataframe_encoding():
    df = csv_dataset.get_dataframe("../../data/test/csv_test_2.csv", 'iso-8859-1')
    assert len(df) == 3
    assert len(df.columns) == 3


def test_concat_two_sets():
    path = "../../data/main/cleaned/o3/London/"
    merged = concat_two_sets(path + 'GB_7_21131_2013_timeseries.csv', path + 'GB_7_21151_2013_timeseries.csv')
    assert len(merged.columns) == 6
    assert len(merged) == 17269


