import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
from matplotlib.axes import Axes
from data.constants import POLLUTANT, YEAR, CITY, CITY_NAME, DATE_NAME
from src.emissions import get_dataframe, mean_per_day, mean_per_month, create_pollutant_df, compare_year_to_year


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
    axes = sns.lineplot(x=DATE_NAME, y=f'mean {pollutant.name} (µg/m3)', data=df)
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


def finalize_plot(axes: Axes, title: str, save: bool, name: str):
    axes.set_title(title)
    plt.tight_layout()
    if save:
        axes.get_figure().savefig(name)
    plt.show()
    plt.close()


def plot_pollutant(pollutant: POLLUTANT, save=False):
    df = create_pollutant_df(pollutant, "../../data/main/cleaned/mean/")
    plt.subplots(figsize=(14, 6))
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    axes = sns.lineplot(x=DATE_NAME, y=f'mean {pollutant.name} (µg/m3)', data=df, hue=CITY_NAME)
    finalize_plot(axes, f'{pollutant.name} emissions', save, f'plot_{pollutant.name}.png')


def plot_violin_pollutant(pollutant: POLLUTANT, save=False):
    df = create_pollutant_df(pollutant, "../../data/main/cleaned/mean/")
    plt.subplots(figsize=(14, 6))
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    axes = sns.violinplot(x=CITY_NAME, y=f'mean {pollutant.name} (µg/m3)', data=df, palette='terrain')
    finalize_plot(axes, f'{pollutant.name} emissions', save, f'violin_plot_{pollutant.name}.png')


def plot_pollutant_last_years(pollutant: POLLUTANT, save=False):
    df = create_pollutant_df(pollutant, "../../data/main/cleaned/mean/")
    df = df[df['Date'] > pd.Timestamp(2019, 1, 1, 0).tz_localize(df['Date'].iloc[0].tz)]
    plt.subplots(figsize=(14, 6))
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    axes = sns.lineplot(x=DATE_NAME, y=f'mean {pollutant.name} (µg/m3)', data=df, hue=CITY_NAME)
    finalize_plot(axes, f'{pollutant.name} emissions', save, f'plot_{pollutant.name}_last_year.png')


def compare_19_20(pollutant: POLLUTANT, save=False):
    df = create_pollutant_df(pollutant, "../../data/main/cleaned/mean/")
    df = df[df[DATE_NAME] >= pd.Timestamp(2019, 1, 1, 0).tz_localize(df['Date'].iloc[0].tz)]
    df = df[df[DATE_NAME].dt.month.isin([2, 3, 4])]
    df = compare_year_to_year(df)
    df = df.round(2)
    df.drop(['AirPollutant', 'UnitOfMeasurement'], axis=1, inplace=True)
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='grey', align='center'),
        cells=dict(values=[df['Countrycode'], df['City'], df['Date'], df['Previous year value'],
                           df['Year value'], df['diff'], df['diff %']],
                   fill_color='lightgrey', align='center'))])
    fig.update_layout(title=f'Difference for {pollutant.name} emissions between 2019 and 2020')
    fig.show()


for pol in POLLUTANT:
    compare_19_20(pol)
