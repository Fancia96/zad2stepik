import unittest
from hamcrest import *

from Employee import Employee, ProductionWorker


class EmployeeWithPyHamcrest(unittest.TestCase):

    def setUp(self):
        self.temp = ProductionWorker("viallet", "guillaume", 2, 5)

    def test_change_lastname_positive(self):
        self.temp.change_last_name("Zielony")
        assert_that("Zielony", is_(self.temp.get_last_name()))

    def test_change_lastname_throw_exception(self):

        assert_that(
        calling(self.temp.change_last_name).with_args(""),
        raises(Exception))

    def test_change_lastname_throw_exception_number(self):

        assert_that(
            calling(self.temp.change_last_name).with_args(123),
            raises(Exception))

    def test_change_lastname_throw_exception_minus_number(self):
        assert_that(
            calling(self.temp.change_last_name).with_args(-123),
            raises(Exception))

    def test_change_firstname_positive(self):
        self.temp.change_first_name("Wilhelm")
        assert_that("Wilhelm", is_(self.temp.get_first_name()))

    def test_change_firstname_throw_exception(self):
        assert_that(
            calling(self.temp.change_first_name).with_args(""),
            raises(Exception))

    def test_change_firstname_throw_exception_number(self):
        assert_that(
            calling(self.temp.change_first_name).with_args(123),
            raises(Exception))

    def test_change_firstname_throw_exception_minus_number(self):
        assert_that(
            calling(self.temp.change_first_name).with_args(-123),
            raises(Exception))

    def test_change_pay_hour_positive_round_number(self):
        self.temp.change_pay_hour(6)
        assert_that(self.temp.get_pay_hour(), is_(6))

    def test_change_pay_hour_positive_float_number(self):
        self.temp.change_pay_hour(6.5)
        assert_that(self.temp.get_pay_hour(), is_(6.5))

    def test_change_pay_hour_exception_non_numeric(self):
        assert_that(
            calling(self.temp.change_pay_hour).with_args("abc123"),
            raises(Exception))

    def test_change_pay_hour_exception_negative_number(self):
        assert_that(
            calling(self.temp.change_pay_hour).with_args(-1),
            raises(Exception))

    def test_change_number_positive(self):
        self.temp.change_change_number(1)
        assert_that(self.temp.get_change_number(), is_(1))

    def test_change_number_exception_minus_number(self):
        assert_that(
            calling(self.temp.change_change_number).with_args(-1),
            raises(Exception))

    def test_change_number_exception_wrong_number(self):
        assert_that(
            calling(self.temp.change_change_number).with_args(3),
            raises(Exception))

    def test_change_number_exception_non_number_value(self):
        assert_that(
            calling(self.temp.change_change_number).with_args("abc"),
            raises(Exception))

    def tearDown(self):
        self.temp = None
