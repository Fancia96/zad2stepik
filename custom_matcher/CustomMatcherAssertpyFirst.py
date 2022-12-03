from assertpy import add_extension


def can_accelerate(self, this_much):
    speed = self.val.get_speed()

    new_speed = speed + this_much
    if new_speed > self.val.get_max_speed():
        return False
    else:
        return True

add_extension(can_accelerate)