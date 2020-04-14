from study.stations import get_stations_data
from study.stations import get_worst_stations

path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"


def test_get_stations_data():
    path = path1 + 'pm10' + path2
    df = get_stations_data(path)
    assert df is not None


def test_get_worst_pm10_stations():
    path = path1 + 'pm10' + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path)
    assert df is not None
    assert len(df) < size
    # number of ''traffic urban'' cities for pm10
    assert len(df) == 317


def test_get_worst_pm25_stations():
    path = path1 + 'pm25' + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path)
    assert df is not None
    assert len(df) < size
    # number of ''traffic urban'' cities for pm25
    assert len(df) == 135


def test_get_worst_no2_stations():
    path = path1 + 'no2' + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path)
    assert df is not None
    assert len(df) < size
    # number of ''traffic urban'' cities for no2
    assert len(df) == 343


def test_get_worst_o3_stations():
    path = path1 + 'o3' + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path)
    assert df is not None
    assert len(df) < size
    # number of ''traffic urban'' cities for o3
    assert len(df) == 98
