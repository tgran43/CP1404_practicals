from prac_08.silver_service_taxi import SilverServiceTaxi

car = SilverServiceTaxi("Hummer", 200, 2)
print(car)
car.drive(18)
print("${:.2f}".format(car.get_fare()))