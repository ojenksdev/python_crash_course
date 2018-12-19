
def city_country(city, country, population=''):
    """returns a city and name in a string"""
    if population:
        city = city + ', ' + country + ' - ' + str(population)
    else:
        city = city + ', ' + country
    return city.title()

