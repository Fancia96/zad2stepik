
class Car():
    def __init__(self, make, year_model, max_speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__reverse_gear = False
        self.__max_speed = max_speed

    def accelerateManually(self, how_much):
        new_speed = self.__speed + how_much
        if new_speed > self.__max_speed:
            raise Exception("You cant go that fast with this car!")
        else:
            self.__speed += 5

    def accelerate(self):
        self.accelerateManually(5)

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
