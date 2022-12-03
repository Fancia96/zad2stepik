import unittest
from assertpy import assert_that

from Car import Car


class CarWithAssertpyTest(unittest.TestCase):

    def setUp(self):
        self.temp = Car("kia", 2005, 15)

    def testInstance(self):
        assert_that(self.temp).is_instance_of(Car)

    def test_Car_speed_up_once(self):
        self.temp.accelerate()
        assert_that(5).is_equal_to(self.temp.get_speed())

    def test_Car_speed_up_twice(self):
        self.temp.accelerate()
        self.temp.accelerate()
        assert_that(10).is_close_to(self.temp.get_speed(), 0)

    def test_Car_speed_and_brake(self):
        self.temp.accelerate()
        self.temp.brake()
        assert_that(0).is_equal_to(self.temp.get_speed())

    def test_Car_check_make(self):
        assert_that("kia").is_equal_to(self.temp.get_make())

    def test_Car_check_make_give_wrong(self):
        assert_that("kiaa").is_not_equal_to(self.temp.get_make())

    def test_Car_check_year_model(self):
        assert_that(2005).is_greater_than_or_equal_to(self.temp.get_year_model())

    def test_Car_check_year_model_give_wrong(self):
        assert_that(2006).is_not_same_as(self.temp.get_year_model())

    def test_brake_without_change_gear_Exceptions(self):
        assert_that(self.temp.brake).raises(Exception)

    def test_brake_with_changing_gear(self):
        self.temp.set_reverse_gear()
        self.temp.brake()
        assert_that(-5, self.temp.get_speed())

    def test_change_reverese_gear_with_some_speed(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.temp.set_reverse_gear()
        assert_that(self.temp.get_speed()).is_close_to(0, 0)

    def test_set_normal_gear_with_some_speed(self):
        self.temp.accelerate()
        self.temp.accelerate()
        self.temp.set_normal_gear()
        assert_that(self.temp.get_speed()).is_close_to(10, 0)

    def test_set_normal_gear_with_minus_speed(self):
        self.temp.set_reverse_gear()
        self.temp.brake()
        self.temp.set_normal_gear()
        assert_that(self.temp.get_speed()).is_between(0, 0)

    def test_reaching_max_speed(self):
        for i in range (3):
            self.temp.accelerate()

        assert_that(self.temp.get_speed()).is_greater_than_or_equal_to(15)

    def test_going_above_max_speed(self):
        for i in range (3):
            self.temp.accelerate()

        assert_that(self.temp.accelerate).raises(Exception)

    def test_set_normal_gear_with_some_speed_float(self):
        self.temp.accelerateManually(5.6)
        self.temp.accelerateManually(2.2)

        assert_that(self.temp.get_speed()).is_greater_than_or_equal_to(7.8)

    def tearDown(self):
        self.temp = None