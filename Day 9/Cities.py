def city_names(city, country="Unknown country"):
    print(city + " is in " + country)
    print ("{0} is in {1}".format(city.title(), country.title()))

city_names("montreal", "canada")
city_names("montreal")

def city_country(city, country):
    return city + ", " + country

print(city_country("Berlin", "Germany"))