from src.stations import create_pollutants_df, filter_main_cities, get_best_station
from data.constants import POLLUTANT
import seaborn as sns
import matplotlib.pyplot as plt

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


def plot_all():
    for pol in POLLUTANT:
        plot_european_cities_pollutant(pol)


path = path1 + POLLUTANT.no2.name + path2
df = get_best_station(path)
print()



