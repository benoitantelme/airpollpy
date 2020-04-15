from src.stations import get_worst_stations, get_mean_per_city, get_best_stations, clean_df, set_index, \
    create_pollutants_df
from data.constants import POLLUTANT
import pandas as pd


path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"
pollutant = POLLUTANT.pm10
path = path1 + pollutant.name + path2

pollutant_df = create_pollutants_df(pollutant, path)
print(pollutant_df.head())


