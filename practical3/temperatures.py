MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""



def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("Fahrenheit : "))
            celsius = fahrenheit_convert_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_convert_to_fahrenheit(celsius):
    '''This function converts celsius to fahrenheit'''
    return celsius * 9.0 / 5 + 32

def fahrenheit_convert_to_celsius(fahrenheit):
    '''This function converts fahrenheit to celsius'''
    return  5 / 9 * (fahrenheit - 32)

main()