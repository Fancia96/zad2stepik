
class Employee():
    def __init__(self, last_name, first_name):
        self.__lastname = last_name
        self.__firstname = first_name

    def get_last_name(self):
        return self.__lastname

    def get_first_name(self):
        return self.__firstname

    def change_last_name(self, new_lastname):
        if len(new_lastname) == 0 or str(new_lastname).isdigit():
            raise Exception("name cant be zero length or numbers")
        self.__lastname = new_lastname

    def change_first_name(self, new_firstname):
        if len(new_firstname) == 0 or str(new_firstname).isdigit():
            raise Exception("name cant be zero length or numbers")
        self.__firstname = new_firstname


class ProductionWorker(Employee):

    def __init__(self, last_name, first_name, change_number, pay_hour):
        super().__init__(last_name, first_name)
        self.__change_number = change_number
        self.__pay_hour = pay_hour

    def change_pay_hour(self, pay_hour):
        if pay_hour < 0:
            raise Exception("pay cant be negative")
        if not str(pay_hour).isdigit():
            float(pay_hour)
            self.__pay_hour = float(pay_hour)
            return

        if not str(pay_hour).isnumeric():
            raise Exception("pay hour has to be a number")
        self.__pay_hour = float(pay_hour)

    def get_pay_hour(self):
        return self.__pay_hour

    def change_change_number(self, change_number):
        if str(change_number) != "1" and str(change_number) != "2":
            raise Exception("Shift can be only day or night! 1 or 2")
        else:
            self.__change_number = change_number

    def get_change_number(self):
        return self.__change_number
