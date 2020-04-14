from study.stations import get_stations_data
from study.stations import get_worst_stations

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

    df = get_worst_stations(path)
    assert df is not None
    assert len(df) < size
    # number of ''traffic urban'' cities for a pollutant
    assert len(df) == cities


def test_get_worst_pm10_stations():
    get_worst_stations_helper('pm10', 317)


def test_get_worst_pm25_stations():
    get_worst_stations_helper('pm25', 135)


def test_get_worst_no2_stations():
    get_worst_stations_helper('no2', 343)


def test_get_worst_o3_stations():
    get_worst_stations_helper('o3', 98)

