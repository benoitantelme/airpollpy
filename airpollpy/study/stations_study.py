from src.stations import create_pollutants_df
from data.constants import POLLUTANT
import seaborn as sns
import matplotlib.pyplot as plt

path1 = "../../data/main/cleaned/others/2013_"
path2 = "_monitoring_stations.csv"
pollutant = POLLUTANT.pm10
path = path1 + pollutant.name + path2

pollutant_df = create_pollutants_df(pollutant, path)
print(pollutant_df.head())

main_cities_df = pollutant_df[
    pollutant_df['city_name'].isin(['Paris', 'London', 'Berlin', 'Madrid', 'Roma', 'Dublin', 'København',
                                    'Thessaloniki', 'Bruxelles', 'Lisboa', 'Luxembourg', 'Oslo', 'Stockholm',
                                    'Wien', 'Sofia', 'Zagreb', 'Praha', 'Tallinn', 'Amsterdam',
                                    'Helsinki / Helsingfors', 'Budapest', 'Riga', 'Vilnius', 'Warszawa'])]

sns.set_style("whitegrid", {'grid.linestyle': '-'})
fig = main_cities_df.plot.bar(x='city_name', figsize=(14, 8)).get_figure()
# fig.savefig('stations_plot.png')
plt.show()
