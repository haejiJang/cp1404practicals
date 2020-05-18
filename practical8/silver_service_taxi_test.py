from practical8.silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi class."""
    my_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(my_taxi.get_fare())

main()