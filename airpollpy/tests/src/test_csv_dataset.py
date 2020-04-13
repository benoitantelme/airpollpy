from src import csv_dataset


def test_test():
    assert True


def test_get_dataset():
    ds = csv_dataset.get_dataset("../../data/test/csv_test_1.csv")
    assert len(ds) == 3
    assert len(ds.columns) == 3
