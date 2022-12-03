from hamcrest.core.base_matcher import BaseMatcher

from Car import Car


class IsGivenACar(BaseMatcher):
    def __init__(self):
        pass

    def _matches(self, car: Car):
        speed = car.get_speed()

        if speed == 0:
            return True
        else:
            return False

    def describe_to(self, description):
        description.append_text('car is not on brake ')

def is_on_brake():
    return IsGivenACar()
