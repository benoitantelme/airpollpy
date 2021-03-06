# airpollpy
Project around air pollution in Python


## What is it?
The goal of the project is to retrieve and analyze data from the European Environment Agency.
Initially inspired by this [article](https://www.eea.europa.eu/themes/air/air-quality-and-covid19/air-quality-and-covid19).


## Pollutants
I decided to focus on:
- [O3](https://www.londonair.org.uk/LondonAir/guide/WhatIsO3.aspx)
- [NO2](https://www.londonair.org.uk/LondonAir/guide/WhatIsNO2.aspx)
- [PM10](https://uk-air.defra.gov.uk/air-pollution/daqi?view=more-info&pollutant=pm10#pollutant)
- [PM2.5](https://uk-air.defra.gov.uk/air-pollution/daqi?view=more-info&pollutant=pm25#pollutant)


## Getting the data
I started retrieving the data for London using the [Bloomsbury monitoring station](https://uk-air.defra.gov.uk/networks/site-info?site_id=CLL2)
which code corresponds to GB0566A in the csv files.
A potential amelioration would be to take the data from all stations for this city and use a mean. However that is **a lot** of data.


## Stations
Comparison of all station data available from a 2013 data set to check the min, mean and max for a city in order to study 
and visualize those numbers before using the main data sets. Potentially it could be doable to select a **best** station 
for a city and pollutant instead of using the full data set.

Vizualisation of the worst, the best and a mean of all measures per cities and pollutant:
![European cities NO2 emissions in 2013](data/plot/stations/stations_plot_no2.png)
![European cities PM10 emissions in 2013](data/plot/stations/stations_plot_pm10.png)
![European cities PM2.5 emissions in 2013](data/plot/stations/stations_plot_pm25.png)
![European cities O3 emissions in 2013](data/plot/stations/stations_plot_o3.png)


Best, as in closest to the mean or unique station in a city per pollutant:
![Best stations NO2 for each city in 2013](data/plot/stations/best_stations_2013_no2.png)
![Best stations PM10 for each city in 2013](data/plot/stations/best_stations_2013_pm10.png)
![Best stations PM25 for each city in 2013](data/plot/stations/best_stations_2013_pm25.png)
![Best stations O3 for each city in 2013](data/plot/stations/best_stations_2013_o3.png)


Best station for each pollutant an city:

| City  | NO2  | O3  | PM10  | PM2.5  |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Amsterdam  | NL00012  | NL00003  | NL00020  | NL00007  |
| Berin  | DEBE065  | DEBE010  | DEBE067  | DEBE068  |
| Budapest  | HU0045A  | HU0022A  | HU0045A  | N/A  |
| Dublin  | IE0105A  | IE0127A  | IE0036A  | IE0028A  |
| København  | DK0030A  | DK0034A  | DK0034A  | DK0034A  |
| Lisboa  | PT03072  | PT03071  | PT03071  | PT03071  |
| London  | GB0637A  | GB0743A  | GB0636A  | GB0636A  |
| Luxembourg  | N/A  | LU0101A  | LU0100A  | N/A  |
| Madrid  | ES1532A  | ES1945A  | ES1937A  | ES1937A  |
| Oslo  | NO0071A  | NO0088A  | NO0057A  | NO0083A  |
| Paris  | FR04131  | FR04143  | FR04131  | FR04143  |
| Praha  | CZ0AKAL  | CZ0ARIE  | CZ0ASUC  | CZ0ALIB  |
| Riga  | LV00RP5  | LV0RKE2  | LV0RKR9  | LV0RKR9  |
| Roma  | IT1836A  | IT2012A  | IT1906A  | IT0957A  |
| Sofia  | BG0050A  | BG0040A  | BG0073A  | BG0050A  |
| Stockholm  | SE0087A  | SE0022A  | SE0027A  | SE0087A  |
| Tallinn  | EE0018A  | EE0018A  | EE0018A  | EE0018A  |
| Thessaloniki  | GR0018A  | GR0018A  | GR0018A  | content  |
| Vilnius  | LT00001  | LT00003  | LT00001  | LT00003  |
| Warszawa  | PL0592A  | PL0141A  | PL0141A  | PL0141A  |
| Wien  | AT9STAD  | AT90LAA  | AT90TAB  | AT90AKC  |
| Zagreb  | HR0007A  | HR0009A  | HR0009A  | N/A  |


## Creating a mean data set per city and pollutant
An issue with the **best station** method: some stations from 2013 don't provide data later. 
Also, a different station could be closer to the mean in later years.
I decided to use the whole data set available and work on it to build a mean for each city and timestamp.
The data in *data/main/cleaned* is available per pollutant, city and then a file per station and year.
The goal is going to be to merge every stations value and average it to a mean for the whhole city concerned.


## Visualization of the pollutants emissions data
After looking at the curve, some data are missing for 2014 in Paris and the amount of data is huge and hard to plot. 
So I decided to focus on data from 2015 first and remove the older data.

Looking at the whole data set from 2015 to 2020 included:
![NO2 Violin Plot](data/plot/emissions/main/violin_plot_no2.png)
![O3 Violin Plot](data/plot/emissions/main/violin_plot_o3.png)
![PM10 Violin Plot](data/plot/emissions/main/violin_plot_pm10.png)
![PM25 Violin Plot](data/plot/emissions/main/violin_plot_pm25.png)

Looking at the evolution throughout the years:
![NO2 Plot](data/plot/emissions/main/plot_no2.png)
![O3 Plot](data/plot/emissions/main/plot_o3.png)
![PM10 Plot](data/plot/emissions/main/plot_pm10.png)
![PM25 Plot](data/plot/emissions/main/plot_pm25.png)
There is still missing data for Paris pm2.5 emissions during 2019.
We can see that the NO2 emissions are lower during the 2020 covid-19 lockdown, while pm2.5 and pm10 seems for some cities only to be lower.


## Recent data and covid crisis
Only looking at 2019 up to now:
![NO2 Plot](data/plot/emissions/main/plot_no2_last_year.png)
![PM10 Plot](data/plot/emissions/main/plot_pm10_last_year.png)
![PM25 Plot](data/plot/emissions/main/plot_pm25_last_year.png)
We can see that, as mentioned in the EEA article, the NO2 diminution explained by traffic reduction is clear.
While other pollutants reduction is not necessarily evident.

Tables with difference between 2020 and 2019 for February, March and April:
![NO2 Plot](data/plot/emissions/main/no2_diff_19_20.png)
![PM10 Plot](data/plot/emissions/main/pm10_diff_19_20.png)
![PM25 Plot](data/plot/emissions/main/pm25_diff_19_20.png)

For NO2 the difference is evident. It is noticeable as well for PM10 and for PM2.5 we are missing some data for Paris and 
the conclusion is harder to reach with this set of data.

## Dependencies
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)


## Source:
[European Environment Agency](https://www.eea.europa.eu/) with [creative commons license](https://creativecommons.org/licenses/by/2.5/dk/deed.en_GB)


