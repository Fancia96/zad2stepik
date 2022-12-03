import unittest


class Car1():
    def __init__(self, make, year_model, max_speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__reverse_gear = False
        self.__max_speed = max_speed

    def accelerate(self):
        new_speed = self.__speed + 5
        if new_speed > self.__max_speed:
            raise Exception("You cant go that fast with this car!")
        else:
            self.__speed += 5

    def set_reverse_gear(self):
        self.__reverse_gear = True
        self.__speed = 0

    def set_normal_gear(self):
        self.__reverse_gear = False
        if self.get_speed() < 0:
            self.__speed = 0

    def brake(self):
        new_speed = self.__speed - 5
        if new_speed < 0 and self.__reverse_gear:
            self.__speed -= 5
        elif new_speed < 0 and not self.__reverse_gear:
            raise Exception("You have to change gear!")
        else:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_max_speed(self):
        return self.__max_speed


class CarTest(unittest.TestCase):

    def setUp(self):
        self.temp = Car("opel", 1996, 100)

    def test_Car_speed_up_once(self):
        self.temp.accelerate()
        self.assertEqual(5, self.temp.get_speed())

    def test_Car_speed_up_twice(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.assertEqual(10, self.temp.get_speed())

    def test_Car_speed_and_brake(self):
        self.temp.accelerate()
        self.temp.brake()
        self.assertEqual(0, self.temp.get_speed())

    def test_Car_check_make(self):
        self.assertEqual("opel", self.temp.get_make())

    def test_Car_check_make_give_wrong(self):
        self.assertNotEqual("opell", self.temp.get_make())

    def test_Car_check_year_model(self):
        self.assertEqual(1996, self.temp.get_year_model())

    def test_Car_check_year_model_give_wrong(self):
        self.assertNotEqual(1997, self.temp.get_year_model())

    def test_brake_without_change_gear_Exceptions(self):
        self.assertRaises(Exception, self.temp.brake)

    def test_brake_with_changing_gear(self):
        self.temp.set_reverse_gear()
        self.temp.brake()
        self.assertEqual(-5, self.temp.get_speed())

    def test_change_reverese_gear_with_some_speed(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.temp.set_reverse_gear()
        self.assertEqual(0, self.temp.get_speed())

    def test_set_normal_gear_with_some_speed(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.temp.set_normal_gear()
        self.assertEqual(10, self.temp.get_speed())

    def test_set_normal_gear_with_minus_speed(self):
        self.temp.set_reverse_gear()
        self.temp.brake()
        self.temp.set_normal_gear()
        self.assertEqual(0, self.temp.get_speed())

    def test_reaching_max_speed(self):
        for i in range (20):
            self.temp.accelerate()

        self.assertEqual(100, self.temp.get_speed())

    def test_going_above_max_speed(self):
        for i in range (20):
            self.temp.accelerate()

        self.assertRaises(Exception, self.temp.accelerate)

    def tearDown(self):
        self.temp = None

class CarTest2(unittest.TestCase):

    def setUp(self):
        self.temp = Car("kia", 2005, 15)

    def test_Car_speed_up_once(self):
        self.temp.accelerate()
        self.assertEqual(5, self.temp.get_speed())

    def test_Car_speed_up_twice(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.assertEqual(10, self.temp.get_speed())

    def test_Car_speed_and_brake(self):
        self.temp.accelerate()
        self.temp.brake()
        self.assertEqual(0, self.temp.get_speed())

    def test_Car_check_make(self):
        self.assertEqual("kia", self.temp.get_make())

    def test_Car_check_make_give_wrong(self):
        self.assertNotEqual("kiaa", self.temp.get_make())

    def test_Car_check_year_model(self):
        self.assertEqual(2005, self.temp.get_year_model())

    def test_Car_check_year_model_give_wrong(self):
        self.assertNotEqual(2006, self.temp.get_year_model())

    def test_brake_without_change_gear_Exceptions(self):
        self.assertRaises(Exception, self.temp.brake)

    def test_brake_with_changing_gear(self):
        self.temp.set_reverse_gear()
        self.temp.brake()
        self.assertEqual(-5, self.temp.get_speed())

    def test_change_reverese_gear_with_some_speed(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.temp.set_reverse_gear()
        self.assertEqual(0, self.temp.get_speed())

    def test_set_normal_gear_with_some_speed(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.temp.set_normal_gear()
        self.assertEqual(10, self.temp.get_speed())

    def test_set_normal_gear_with_minus_speed(self):
        self.temp.set_reverse_gear()
        self.temp.brake()
        self.temp.set_normal_gear()
        self.assertEqual(0, self.temp.get_speed())

    def test_reaching_max_speed(self):
        for i in range (3):
            self.temp.accelerate()

        self.assertEqual(15, self.temp.get_speed())

    def test_going_above_max_speed(self):
        for i in range (3):
            self.temp.accelerate()

        self.assertRaises(Exception, self.temp.accelerate)

    def tearDown(self):
        self.temp = None
