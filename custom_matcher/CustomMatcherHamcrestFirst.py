from hamcrest.core.base_matcher import BaseMatcher

from Car import Car


class IsGivenACar(BaseMatcher):
    def __init__(self):
        pass

    def _matches(self, car: Car):
        speed = car.get_speed()

        if speed == car.get_max_speed():
            return False
        else:
            return True

    def describe_to(self, description):
        description.append_text('cannot go FASTER ')

def can_accelerate():
    return IsGivenACar()
