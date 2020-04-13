from src import csv_dataset


def test_get_dataframe():
    df = csv_dataset.get_dataframe("../../data/test/csv_test_1.csv")
    assert len(df) == 3
    assert len(df.columns) == 3


def test_get_dataframe_encoding():
    df = csv_dataset.get_dataframe("../../data/test/csv_test_2.csv", 'iso-8859-1')
    assert len(df) == 3
    assert len(df.columns) == 3


def test_clean_pm10_timeseries():
    path = "../../data/main/original/PM10/London/GB_5_22642_2020_timeseries.csv"
    df = csv_dataset.get_dataframe(path)
    assert len(df.columns) == 17

    rows = len(df)
    df = csv_dataset.clean_pm10_timeseries(path)
    assert len(df.columns) == 8
    assert len(df) < rows

