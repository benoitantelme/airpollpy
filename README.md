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


## Dependencies
- [Pandas](https://pandas.pydata.org/)


## Source:
[European Environment Agency](https://www.eea.europa.eu/) with [creative commons license](https://creativecommons.org/licenses/by/2.5/dk/deed.en_GB)


