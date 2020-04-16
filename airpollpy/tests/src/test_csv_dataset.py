from src import csv_dataset


def test_get_dataframe():
    df = csv_dataset.get_dataframe("../../data/test/csv_test_1.csv")
    assert len(df) == 3
    assert len(df.columns) == 3


def test_get_dataframe_encoding():
    df = csv_dataset.get_dataframe("../../data/test/csv_test_2.csv", 'iso-8859-1')
    assert len(df) == 3
    assert len(df.columns) == 3


