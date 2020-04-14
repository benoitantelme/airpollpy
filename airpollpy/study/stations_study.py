from src.stations import get_worst_stations, get_mean_per_city, get_best_stations, STATISTIC_VALUE
import pandas as pd


def clean_df(df):
    df.drop(['station_european_code', 'type_of_station', 'station_type_of_area', 'component_caption', 'above_AQG?',
             'country iso code'], axis=1, inplace=True)


def set_index(df):
    df.set_index('city_name', inplace=True)


path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"

pollutant = 'pm10'
path = path1 + pollutant + path2

worst_df = get_worst_stations(path, pollutant)
clean_df(worst_df)
set_index(worst_df)

best_df = get_best_stations(path, pollutant)
clean_df(best_df)
set_index(best_df)

mean_df = get_mean_per_city(path, pollutant)
set_index(mean_df)

pollutant_df = pd.concat([worst_df, mean_df, best_df], axis=1)
print(pollutant_df.head())

# df1 = df[['a','d']]
