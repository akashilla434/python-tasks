import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
city_Series=pd.Series(cities)
print(city_Series)
data=["Delhi", "Chennai", "Bangalore"]
my_cities_Series=pd.Series(cities,index=my_cities)
print(my_cities_Series)
print(data_Series.isnull())
print(data_Series[data_Series.isnull()])
