from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        super().__init__(wheel_size, wheel_number)

    def honk(self):
        print("Honk! Honk!")

    def go(self):
        return "The car goes vroom vroom!"

    def fill_up_tank(self):
        return "The car fills up its tank."
