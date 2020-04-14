from study.stations import get_stations_data
from study.stations import get_worst_stations

path = "../../data/main/cleaned/others/2013_pm10_monitoring_stations.csv"


def test_get_stations_data():
    df = get_stations_data(path)
    assert df is not None


def test_get_worst_stations():
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path)
    assert df is not None
    assert len(df) < size
    # number of ''traffic urban'' cities
    assert len(df) == 317


