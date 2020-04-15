from data.constants import POLLUTANT
from src.stations import get_stations_data, clean_df, create_pollutants_df, filter_main_cities, get_best_station
from src.stations import get_worst_stations
from src.stations import get_best_stations
from src.stations import get_mean_per_city

path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"


def test_get_stations_data():
    path = path1 + POLLUTANT.pm10.name + path2
    df = get_stations_data(path)
    assert df is not None


def get_worst_stations_helper(pollutant: POLLUTANT, cities: int):
    path = path1 + pollutant.name + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_worst_stations(path, pollutant)
    assert df is not None
    assert len(df) < size
    # number of worst station/city for a pollutant
    assert len(df) == cities


def test_get_worst_pm10_stations():
    get_worst_stations_helper(POLLUTANT.pm10, 525)


def test_get_worst_pm25_stations():
    get_worst_stations_helper(POLLUTANT.pm25, 344)


def test_get_worst_no2_stations():
    get_worst_stations_helper(POLLUTANT.no2, 557)


def test_get_worst_o3_stations():
    get_worst_stations_helper(POLLUTANT.o3, 471)


def test_get_best_no2_stations():
    path = path1 + POLLUTANT.no2.name + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_best_stations(path, POLLUTANT.no2)
    assert df is not None
    assert len(df) < size
    # number of best station/city for 'no2'
    assert len(df) == 557


def test_get_mean_per_city():
    path = path1 + POLLUTANT.pm10.name + path2
    df = get_stations_data(path)
    size = len(df)

    df = get_mean_per_city(path, POLLUTANT.pm10)
    assert df is not None
    assert len(df) < size
    # number of best station/city for 'no2'
    assert len(df) == 525
    assert len(df.columns) == 3


def test_clean_df():
    path = path1 + POLLUTANT.pm10.name + path2
    df = get_stations_data(path)
    assert df is not None
    assert len(df.columns) == 8
    clean_df(df)
    assert len(df.columns) == 2


def test_create_pollutants_df():
    pollutant = POLLUTANT.pm10
    path = path1 + pollutant.name + path2
    df = create_pollutants_df(path, pollutant)
    assert df is not None
    assert len(df.columns) == 5


def test_filter_main_cities():
    path = path1 + POLLUTANT.pm10.name + path2
    df = filter_main_cities(get_stations_data(path))
    assert df is not None
    assert len(df) == 121


def test_get_best_station():
    path = path1 + POLLUTANT.pm10.name + path2
    df = get_best_station(path)
    assert df is not None
    assert len(df) == 22

