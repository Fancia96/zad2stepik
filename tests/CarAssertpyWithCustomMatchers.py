import unittest
from assertpy import assert_that

from Car import Car

class CarAssertpyWithCustomMatchers(unittest.TestCase):

    def setUp(self):
        self.temp = Car("kia", 2005, 15)

    def testInstance(self):
        assert_that(self.temp).is_instance_of(Car)

    def firstCustomTest(self):
        self.temp.accelerate()
        assert_that(self.temp).can_accelerate(5)

    def secondCustomTest(self):
        assert_that(self.temp).is_on_brake()


    def tearDown(self):
        self.temp = None