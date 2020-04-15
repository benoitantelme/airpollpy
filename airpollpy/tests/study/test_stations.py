from src.stations import get_stations_data, clean_df
from src.stations import get_worst_stations
from src.stations import get_best_stations
from src.stations import get_mean_per_city

path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"


def test_get_stations_data():
    path = path1 + 'pm10' + path2
    df = get_stations_data(path)
    assert df is not None


def get_worst_stations_helper(pollutant: str, cities: int):
    path = path1 + pollutant + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path, pollutant)
    assert df is not None
    assert len(df) < size
    # number of worst station/city for a pollutant
    assert len(df) == cities


def test_get_worst_pm10_stations():
    get_worst_stations_helper('pm10', 525)


def test_get_worst_pm25_stations():
    get_worst_stations_helper('pm25', 344)


def test_get_worst_no2_stations():
    get_worst_stations_helper('no2', 557)


def test_get_worst_o3_stations():
    get_worst_stations_helper('o3', 471)


def test_get_best_no2_stations():
    path = path1 + 'no2' + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_best_stations(path, 'no2')
    assert df is not None
    assert len(df) < size
    # number of best station/city for 'no2'
    assert len(df) == 557


def test_get_mean_per_city():
    path = path1 + 'pm10' + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_mean_per_city(path, 'pm10')
    assert df is not None
    assert len(df) < size
    # number of best station/city for 'no2'
    assert len(df) == 525
    assert len(df.columns) == 3


def test_clean_df():
    path = path1 + 'pm10' + path2
    df = get_stations_data(path)
    assert df is not None
    assert len(df.columns) == 8
    clean_df(df)
    assert len(df.columns) == 2



