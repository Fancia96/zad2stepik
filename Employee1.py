import unittest


class Employee():
    def __init__(self, last_name, first_name):
        self.__lastname = last_name
        self.__firstname = first_name

    def get_last_name(self):
        return self.__lastname

    def get_first_name(self):
        return self.__firstname

    def change_last_name(self, new_lastname):
        if len(new_lastname) == 0 or str(new_lastname).isdigit():
            raise Exception("name cant be zero length or numbers")
        self.__lastname = new_lastname

    def change_first_name(self, new_firstname):
        if len(new_firstname) == 0 or str(new_firstname).isdigit():
            raise Exception("name cant be zero length or numbers")
        self.__firstname = new_firstname


class ProductionWorker(Employee):

    def __init__(self, last_name, first_name, change_number, pay_hour):
        super().__init__(last_name, first_name)
        self.__change_number = change_number
        self.__pay_hour = pay_hour

    def change_pay_hour(self, pay_hour):
        if pay_hour < 0:
            raise Exception("pay cant be negative")
        if not str(pay_hour).isdigit():
            float(pay_hour)
            self.__pay_hour = float(pay_hour)
            return

        if not str(pay_hour).isnumeric():
            raise Exception("pay hour has to be a number")
        self.__pay_hour = float(pay_hour)

    def get_pay_hour(self):
        return self.__pay_hour

    def change_change_number(self, change_number):
        if str(change_number) != "1" and str(change_number) != "2":
            raise Exception("Shift can be only day or night! 1 or 2")
        else:
            self.__change_number = change_number

    def get_change_number(self):
        return self.__change_number


class ProductionWorkerTest(unittest.TestCase):

    def setUp(self):
        self.temp = ProductionWorker("viallet", "guillaume", 2, 5)

    def test_change_lastname_positive(self):
        self.temp.change_last_name("Bojanowski")
        self.assertEqual("Bojanowski", self.temp.get_last_name())

    def test_change_lastname_throw_exception(self):
        self.assertRaises(Exception, self.temp.change_last_name, "")

    def test_change_lastname_throw_exception_number(self):
        self.assertRaises(Exception, self.temp.change_last_name, 123)

    def test_change_lastname_throw_exception_minus_number(self):
        self.assertRaises(Exception, self.temp.change_last_name, -123)

    def test_change_firstname_positive(self):
        self.temp.change_first_name("Wilhelm")
        self.assertEqual("Wilhelm", self.temp.get_first_name())

    def test_change_firstname_throw_exception(self):
        self.assertRaises(Exception, self.temp.change_first_name, "")

    def test_change_firstname_throw_exception_number(self):
        self.assertRaises(Exception, self.temp.change_first_name, 123)

    def test_change_firstname_throw_exception_minus_number(self):
        self.assertRaises(Exception, self.temp.change_first_name, -123)

    def test_change_pay_hour_positive_round_number(self):
        self.temp.change_pay_hour(6)
        self.assertEqual(6, self.temp.get_pay_hour())

    def test_change_pay_hour_positive_float_number(self):
        self.temp.change_pay_hour(6.5)
        self.assertEqual(6.5, self.temp.get_pay_hour())

    def test_change_pay_hour_exception_non_numeric(self):
        self.assertRaises(Exception, self.temp.change_pay_hour, "abc123")

    def test_change_pay_hour_exception_negative_number(self):
        self.assertRaises(Exception, self.temp.change_pay_hour, -1)

    def test_change_number_positive(self):
        self.temp.change_change_number(1)
        self.assertEqual(1, self.temp.get_change_number())

    def test_change_number_exception_minus_number(self):
        self.assertRaises(Exception, self.temp.change_change_number, -1)

    def test_change_number_exception_wrong_number(self):
        self.assertRaises(Exception, self.temp.change_change_number, 3)

    def test_change_number_exception_non_number_value(self):
        self.assertRaises(Exception, self.temp.change_change_number, "abc")

    def tearDown(self):
        self.temp = None
