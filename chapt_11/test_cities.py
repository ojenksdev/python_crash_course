import unittest

from cities import city_country

class CityNameTestCase(unittest.TestCase):
    """Testing for the city name"""

    def test_city_country(self):
        """Does the city print out properly?"""
        city_name = city_country('paris', 'france')
        self.assertEqual(city_name, 'Paris, France')

    def test_city_country_population(self):
        """Making sure the optional population parameter works"""
        city_name = city_country('paris', 'france', 8243000)
        self.assertEqual(city_name, 'Paris, France - 8243000')

unittest.main()
