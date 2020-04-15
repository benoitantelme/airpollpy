from src.stations import create_pollutants_df, filter_main_cities, get_best_station, STATISTIC_VALUE
from data.constants import POLLUTANT
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"


def plot_european_cities_pollutant(pollutant: POLLUTANT, save=False):
    pollutant_df = create_pollutants_df(path1 + pollutant.name + path2, pollutant)
    print(pollutant_df.head())

    main_cities_df = filter_main_cities(pollutant_df)

    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    p = main_cities_df.plot.bar(x='city_name', figsize=(12, 6),
                                title='European cities ' + pollutant.name + ' emissions in 2013')
    if save:
        p.get_figure().savefig('stations_plot_' + pollutant.name + '.png')
    plt.show()


def plot_all_cities_pollutant():
    for pol in POLLUTANT:
        plot_european_cities_pollutant(pol)


def plot_best_stations_tables(pollutant: POLLUTANT, save=False):
    path = path1 + pollutant.name + path2
    df = get_best_station(path)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='grey', align='center'),
        cells=dict(values=[df['country iso code'], df['city_name'], df['station_european_code'], df[STATISTIC_VALUE],
                           df['mean'], df['diff'], df['diff %']],
                   fill_color='lightgrey', align='center'))])
    fig.update_layout(title='Best stations for ' + pollutant.name + ' emissions in 2013')
    fig.show()
    if save:
        fig.write_image('stations_plot_' + pollutant.name + '.png')


def plot_all_best_stations():
    for pol in POLLUTANT:
        plot_best_stations_tables(pol, False)


plot_all_best_stations()
