"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My car")
    my_car.drive(30)
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo)
    print("odo =", limo.odometer)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()
