# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        print(f'name: {self.name}, lat: {self.lat}, lon: {self.lon}')


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('/Users/ryanboris/Documents/Lambda/Sprint-Challenge--Intro-Python/src/cityreader/cities.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == 'city' or row[3] == 'lat' or row[4] == 'lon':
                continue
            cities.append(City(row[0], float(row[3]), float(row[4])))
    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print((c.name, c.lat, c.lon))

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

lat1 = float(input('Please enter the first latitude coordinate.'))
lon1 = float(input('Please enter the first longitude coordinate.'))
lat2 = float(input('Please enter the second latitude coordinate.'))
lon2 = float(input('Please enter the second longitude coordinate.'))


def cityreader_stretch(lat1, lon1, lat2, lon2, cities):
    within = []
    if lat1 > lat2:
        normalized_lat1 = lat2
        normalized_lat2 = lat1
    else:
        normalized_lat1 = lat1
        normalized_lat2 = lat2

    if lon1 > lon2:
        normalized_lon1 = lon2
        normalized_lon2 = lon1
    else:
        normalized_lon1 = lon1
        normalized_lon2 = lon2

    for city in cities:
        if normalized_lat1 <= city.lat <= normalized_lat2 and normalized_lon1 <= city.lon <= normalized_lon2:
            within.append(city)

    return within
