from src.stations import create_pollutants_df
from data.constants import POLLUTANT
import seaborn as sns
import matplotlib.pyplot as plt

path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"


def plot_european_cities_pollutant(pollutant: POLLUTANT, save=False):
    path = path1 + pollutant.name + path2

    pollutant_df = create_pollutants_df(pollutant, path)
    print(pollutant_df.head())

    main_cities_df = pollutant_df[
        pollutant_df['city_name'].isin(['Paris', 'London', 'Berlin', 'Madrid', 'Roma', 'Dublin', 'København',
                                        'Thessaloniki', 'Bruxelles', 'Lisboa', 'Luxembourg', 'Oslo', 'Stockholm',
                                        'Wien', 'Sofia', 'Zagreb', 'Praha', 'Tallinn', 'Amsterdam',
                                        'Helsinki', 'Budapest', 'Riga', 'Vilnius', 'Warszawa'])]

    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    p = main_cities_df.plot.bar(x='city_name', figsize=(12, 6), title='European cities ' + pollutant.name + ' emissions in 2013')
    if save:
        p.get_figure().savefig('stations_plot_' + pollutant.name + '.png')
    plt.show()


for pol in POLLUTANT:
    plot_european_cities_pollutant(pol)

