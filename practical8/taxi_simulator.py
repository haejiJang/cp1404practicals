from practical8.car import Car
from practical8.taxi import Taxi
from practical8.silver_service_taxi import SilverServiceTaxi


def main():
    """Write a taxi simulator program that uses your Taxi and SilverServiceTaxi
       classes. Each time, until they quit:
       The user should be presented with a list of available taxis and get to
       choose one. Then they should say how far they want to drive.
       At the end of each trip, show them the price and add it to their bill.
       """
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            while True:
                try:
                    taxi_choice = int(input("Choose taxi: "))
                    if taxi_choice < 0 or taxi_choice > 2:
                        print("Invalid taxi choice")
                        display_taxis(taxis)
                    else:
                        break
                except ValueError:
                    print("Invalid taxi choice")
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d" and current_taxi != None:
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            total_cost += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()