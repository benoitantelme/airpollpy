import os

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from data.constants import POLLUTANT, UNDERSCORE, SPACE, YEAR, CITY
from src.emissions import get_dataframe, mean_per_day, mean_per_month


def plot_mean_per_pol_city_year(city: CITY, pollutant: POLLUTANT, year: YEAR):
    df = get_dataframe(f'../../data/main/cleaned/mean/{city.name}_{pollutant.name}_{year.name}.csv')
    df = mean_per_day(df)
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y=f"mean {pollutant.name} (µg/m3)", data=df).set_title(
        f'{city.name} {pollutant.name} emissions {year.name}')
    plt.show()


def plot_mean_per_pol_city(city: CITY, pollutant: POLLUTANT, save=False):
    df = pd.DataFrame()
    for path in Path("../../data/main/cleaned/mean/").rglob(f'{city.name}_{pollutant.name}_*.csv'):
        print(path.absolute())
        df_tmp = mean_per_month(get_dataframe(path))
        df = pd.concat([df, df_tmp])

    fig, axes = plt.subplots(figsize=(14, 6))
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    axes = sns.lineplot(x="Date", y=f'mean {pollutant.name} (µg/m3)', data=df)
    axes.set_title(f'{city.name} {pollutant.name} emissions')
    # plt.xticks(rotation=40, ha='right')
    plt.tight_layout()
    plt.show()
    if save:
        axes.get_figure().savefig(f'{city.name}_plot_{pollutant.name}.png')
    plt.close()


def plot_all_best_stations(save: bool):
    for city in CITY:
        for pol in POLLUTANT:
            plot_mean_per_pol_city(city, pol, save)


def plot_pollutant(pollutant: POLLUTANT, save=False):
    df = pd.DataFrame()
    for city in CITY:
        city_df = pd.DataFrame()
        for path in Path("../../data/main/cleaned/mean/").rglob(f'{city.name}_{pollutant.name}_*.csv'):
            print(path.absolute())
            df_tmp = mean_per_month(get_dataframe(path))
            city_df = pd.concat([city_df, df_tmp])
        city_df['city'] = city.name
        df = pd.concat([df, city_df])

    fig, axes = plt.subplots(figsize=(14, 6))
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    axes = sns.lineplot(x="Date", y=f'mean {pollutant.name} (µg/m3)', data=df, hue='city')
    axes.set_title(f'{pollutant.name} emissions')
    plt.tight_layout()
    # plt.show()
    if save:
        axes.get_figure().savefig(f'plot_{pollutant.name}.png')
    plt.close()


# print_mean_per_pol_city_year(CITY.Amsterdam, POLLUTANT.o3, YEAR['2013'])
# plot_mean_per_pol_city(CITY.Madrid, POLLUTANT.pm25, False)
# plot_all_best_stations(True)

for pol in POLLUTANT:
    plot_pollutant(pol, True)
# plot_pollutant(POLLUTANT.pm25, True)

#
# for ext in ('*2013*.csv', '*2014*.csv'):
#     for path in Path(f'../../data/main/cleaned/mean').rglob(ext):
#         os.remove(path)




