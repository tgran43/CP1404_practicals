from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return str("{}, reliability={}".format(super().__str__(), self.reliability))

    def drive(self, distance):
        if random.random() * 100 < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0
