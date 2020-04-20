import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from data.constants import POLLUTANT, UNDERSCORE, SPACE, YEAR, CITY
from src.emissions import get_dataframe, mean_per_day, mean_per_month


def print_mean_per_pol_city_year(city: CITY, pollutant: POLLUTANT, year: YEAR):
    path = "../../data/main/cleaned/mean/" + city.name + UNDERSCORE + pollutant.name + UNDERSCORE + year.name + ".csv"
    df = get_dataframe(path)
    df = mean_per_day(df)
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="mean o3 (µg/m3)", data=df).set_title(city.name + SPACE + pollutant.name +
                                                                   ' emissions ' + year.name)
    plt.show()


def print_mean_per_pol_city(city: CITY, pollutant: POLLUTANT):
    df = pd.DataFrame()
    for path in Path("../../data/main/cleaned/mean/").rglob(f'{city.name}_{pollutant.name}_*.csv'):
        print(path.absolute())
        df_tmp = mean_per_month(get_dataframe(path))
        df = pd.concat([df, df_tmp])
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    plt.figure(figsize=(14, 6))
    sns.lineplot(x="Date", y=f'mean {pollutant.name} (µg/m3)', data=df).set_title(
        f'{city.name} {pollutant.name} emissions')
    plt.show()

    # path = "../../data/main/cleaned/mean/" + city.name + UNDERSCORE + pollutant.name + UNDERSCORE + year.name + ".csv"
    # df = get_dataframe(path)
    # df = mean_per_day(df)
    # sns.set_style("whitegrid", {'grid.linestyle': '-'})
    # plt.figure(figsize=(12, 6))
    # sns.lineplot(x="Date", y="mean o3 (µg/m3)", data=df).set_title(city.name + SPACE + pollutant.name +
    #                                                                ' emissions ' + year.name)
    # plt.show()


# print_mean_per_pol_city_year(CITY.Amsterdam, POLLUTANT.o3, YEAR['2013'])
print_mean_per_pol_city(CITY.Amsterdam, POLLUTANT.o3)
