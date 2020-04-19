import seaborn as sns
import matplotlib.pyplot as plt

from data.constants import POLLUTANT, UNDERSCORE, SPACE, YEAR, CITY
from src.emissions import get_dataframe, mean_per_day


def print_mean_per_pol_city_year(city: CITY, pollutant: POLLUTANT, year: YEAR):
    path = "../../data/main/cleaned/mean/" + city.name + UNDERSCORE + pollutant.name + UNDERSCORE + year.name + ".csv"
    df = get_dataframe(path)
    df = mean_per_day(df)
    sns.set_style("whitegrid", {'grid.linestyle': '-'})
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="mean o3 (µg/m3)", data=df).set_title(city.name + SPACE + pollutant.name +
                                                                   ' emissions ' + year.name)
    plt.show()


print_mean_per_pol_city_year(CITY.Amsterdam, POLLUTANT.o3, YEAR['2013'])

