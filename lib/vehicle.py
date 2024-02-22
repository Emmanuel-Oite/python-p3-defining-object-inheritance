class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "The vehicle goes vroom vroom!"

    def fill_up_tank(self):
        return "The vehicle fills up its tank."