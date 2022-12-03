import unittest
from hamcrest import *

from Car import Car
from custom_matcher.CustomMatcherHamcrestFirst import can_accelerate
from custom_matcher.CustomMatcherHamcrestSecond import is_on_brake


class CarHamcrestWithCustomMatchers(unittest.TestCase):

    def setUp(self):
        self.temp = Car("kia", 2005, 5)

    def testInstance(self):
        assert_that(self.temp, instance_of(Car))

    def firstCustomTest(self):
        assert_that(self.temp, can_accelerate())

    def secondCustomTest(self):
        assert_that(self.temp, is_on_brake())

    def tearDown(self):
        self.temp = None
