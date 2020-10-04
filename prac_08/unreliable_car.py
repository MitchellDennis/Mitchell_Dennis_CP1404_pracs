
from prac_08.car import Car

import random

class Unreliable_Car(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):

        if self.reliability > random.randint(1, 100):
            super().drive(distance)
        else:
            # print("Car broke down")
            return distance