# airpollpy
Project around air pollution in Python

## What is it?
The initial goal of the project is to retrieve data (method to be decided) from the European Environment Agency.
Then start cleaning the data sets and using them for visualization. 
And potentially something more elaborate later that would require more data to start thinking about correlation and models.


## Data info
I started retrieving the data for London using the [Bloomsbury monitoring station](https://uk-air.defra.gov.uk/networks/site-info?site_id=CLL2)
which code corresponds to GB0566A in the csv files.
Potential amelioration would be to take the data from all stations for this city and use a mean.
Still have to find a proper way to retrieve all the data and decide how to store them (original and/or cleaned set?).


## Stations
Using stations data from 2013 to check the min, mean and max for a city in order to study and visualize those numbers before using the main data sets.
![European cities NO2 emissions in 2013](data/plot/stations/stations_plot_no2.png)

![European cities PM10 emissions in 2013](data/plot/stations/stations_plot_pm10.png)

![European cities PM2.5 emissions in 2013](data/plot/stations/stations_plot_pm25.png)

![European cities O3 emissions in 2013](data/plot/stations/stations_plot_o3.png)


Best, as in closest to the mean or unique station in the city per pollutant:
![Best stations NO2 for each city in 2013](data/plot/stations/best_stations_2013_no2.png)

![Best stations PM10 for each city in 2013](data/plot/stations/best_stations_2013_pm10.png)

![Best stations PM25 for each city in 2013](data/plot/stations/best_stations_2013_pm25.png)

![Best stations O3 for each city in 2013](data/plot/stations/best_stations_2013_o3.png)


Stations used for each pollutant:

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


## Dependencies
- [Pandas](https://pandas.pydata.org/)


## Source:
[European Environment Agency](https://www.eea.europa.eu/) with [creative commons license](https://creativecommons.org/licenses/by/2.5/dk/deed.en_GB)


