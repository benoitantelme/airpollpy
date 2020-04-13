from study.stations import get_stations_data


def test_get_stations_data():
    path = "../../data/main/cleaned/others/2013_pm10_monitoring_stations.csv"
    df = get_stations_data(path)
    assert df is not None
