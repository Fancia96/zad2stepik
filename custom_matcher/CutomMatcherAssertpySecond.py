from assertpy import add_extension

from Car import Car

def is_on_brake(self):
    speed = self.val.get_speed()

    if speed == 0:
        return True
    else:
        return False
add_extension(is_on_brake)