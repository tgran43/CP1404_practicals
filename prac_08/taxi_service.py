from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")
action = input("q)uit, c)hoose taxi, d)rive").lower()
bill = 0.0
while action != 'q':
    if action == "c":
        print("Taxis available:")
        for i, taxi in enumerate(taxis):
            print("{} - {}".format(i, taxi))
        selected_taxi = taxis[int(input("Choose taxi: "))]
    elif action == "d":
        selected_taxi.start_fare()
        selected_taxi.drive(int(input("Drive how far? ")))
        bill += selected_taxi.get_fare()
        print("Your {} trip cost you ${:.2f}".format(selected_taxi.name, selected_taxi.get_fare()))
    print("Bill to date = ${:.2f}".format(bill))
    action = input("q)uit, c)hoose taxi, d)rive").lower()
print("Total trip cost: ${:.2f}".format(bill))
for i, taxi in enumerate(taxis):
    print("{} - {}".format(i, taxi))
