import unittest

class FizzBuzz:
    def game(self, num):
        if ((num % 15) == 0):
            return "FizzBuzz"
        if ((num % 3) == 0):
            return "Buzz"
        if ((num % 5) == 0):
            return "Fizz"
        else:
            raise Exception("Error in FizzBuzz")

class FizzBuzzTest(unittest.TestCase):

    def setUp(self):
        self.temp = FizzBuzz()

    def test_Fizz_Buzz_positive_30(self):
        self.assertEqual("FizzBuzz", self.temp.game(30))

    def test_Fizz_positive_25(self):
        self.assertEqual("Fizz", self.temp.game(25))

    def test_Buzz_positive_9(self):
        self.assertEqual("Buzz", self.temp.game(9))

    def test_Buzz_positive_minus9(self):
        self.assertEqual("Buzz", self.temp.game(-9))

    def test_Fizz_Buzz_positive_minus30(self):
        self.assertEqual("FizzBuzz", self.temp.game(-30))

    def test_Fizz_positive_minus25(self):
        self.assertEqual("Fizz", self.temp.game(-25))

    def test_Fizz_Buzz_negative_31(self):
        self.assertRaises(Exception, self.temp.game, 31)

    def test_Fizz_Buzz_negative_26(self):
        self.assertRaises(Exception, self.temp.game, 26)

    def test_Fizz_Buzz_negative_11(self):
        self.assertRaises(Exception, self.temp.game, 11)

    def test_Fizz_Buzz_negative_minus31(self):
        self.assertRaises(Exception, self.temp.game, -31)

    def test_Fizz_Buzz_negative_minus26(self):
        self.assertRaises(Exception, self.temp.game, -26)

    def test_Fizz_Buzz_negative_minus11(self):
        self.assertRaises(Exception, self.temp.game, -11)

    def test_Fizz_Buzz_Exceptions(self):
        self.assertRaises(Exception, self.temp.game, 7)

    def tearDown(self):
        self.temp = None

