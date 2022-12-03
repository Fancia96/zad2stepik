import math
import unittest


def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier - 0.6) / multiplier

class Planets():
    def calculateYears(seconds, planet):

        if seconds < 0:
            raise Exception("life seconds cant be on a minus value")

        planets = [
            Planet(0.2408467, "Merkury"),
            Planet(0.61519726, "Wenus"),
            Planet(1, "Ziemia"),
            Planet(1.8808158, "Mars"),
            Planet(11.862615, "Jowisz"),
            Planet(29.447498, "Saturn"),
            Planet(84.016846, "Uran"),
            Planet(164.79132, "Neptun")]

        for i in range(len(planets)):
            if planets[i].get_name() == planet:
                try:
                    float(seconds)
                except:
                    raise Exception("cant convert strin to float")
                bd = round_half_down(float(seconds) / float(planets[i].get_rotation()),2)
                # seconds.divide(planets[i].seconds, 3, RoundingMode.HALF_DOWN).toString()).setScale(2, RoundingMode.HALF_DOWN);
                return bd

        return None

class Planet:
    def __init__(self, rotation, name):

        strung = str(rotation * 31556926)
        if strung.__contains__("."):
            strung = strung.split("\\.")[0]

        self.__rotation = float(strung)
        self.__name = name

    def get_rotation(self):
        return self.__rotation

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    temp = Planets
    print(temp.calculateYears(1000000000, "Ziemia"))

class PlanetsTest(unittest.TestCase):

    def setUp(self):
        self.temp = Planets

    def test_right_output_for_Merkury(self):
        self.assertEqual(280.88, self.temp.calculateYears(2134835688, "Merkury"))

    def test_right_output_for_Wenus(self):
        self.assertEqual(280.88, self.temp.calculateYears(2134835688, "Merkury"))

    def test_right_output_for_Ziemia(self):
        self.assertEqual(31.69, self.temp.calculateYears(1000000000, "Ziemia"))

    def test_right_output_for_Mars(self):
        self.assertEqual(16.85, self.temp.calculateYears(1000000000, "Mars"))

    def test_right_output_for_Jowisz(self):
        self.assertEqual(2.67, self.temp.calculateYears(1000000000, "Jowisz"))

    def test_right_output_for_Saturn(self):
        self.assertEqual(107.61, self.temp.calculateYears(100000000000, "Saturn"))

    def test_right_output_for_Uran(self):
        self.assertEqual(37.72, self.temp.calculateYears(100000000000, "Uran"))

    def test_right_output_for_Neptun(self):
        self.assertEqual(19.23, self.temp.calculateYears(100000000000, "Neptun"))

    def test_null_person_life_seconds_get_exception(self):
        self.assertRaises(Exception, self.temp.calculateYears, None, "Ziemia")

    def test_float_number_life_seconds_value(self):
        self.assertEqual(31.69, self.temp.calculateYears(1000000000.9999999, "Ziemia"))

    def test_zero_length_planet_value(self):
        self.assertEqual(None, self.temp.calculateYears(1000000000, ""))

    def test_minus_person_life_seconds_value(self):
        self.assertRaises(Exception, self.temp.calculateYears, -1000000000, "Ziemia")

    def test_text_as_person_life_seconds_value(self):
        self.assertRaises(Exception, self.temp.calculateYears, "asc", "Ziemia")

    def test_number_as_planet_name(self):
        self.assertEqual(None, self.temp.calculateYears(1000000000, 123))

    def test_minus_number_as_planet_name(self):
        self.assertEqual(None, self.temp.calculateYears(1000000000, -123))

    def test_None_as_planet_name(self):
        self.assertEqual(None, self.temp.calculateYears(1000000000, None))

    def tearDown(self):
        self.temp = None

