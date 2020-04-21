"""
Hex colours Look Up
Author: Gorilla
Date: 16/04/2020
"""

COLOUR_TO_CODE = {'AliceBlue': '#f0f8ff',
                  'AntiqueWhite': '#faebd7',
                  'black': '#000000',
                  'BlanchedAlmond': '#ffebcd',
                  'blue1': '#0000ff',
                  'BlueViolet': '#8a2be2',
                  'CadetBlue': '#5f9ea0',
                  'Chocolate': '#d2691e',
                  'cyan1': '#00ffff',
                  'DarkGreen': '#006400'
                  }


def main():
    for key in COLOUR_TO_CODE.keys():
        print(key)
    # ask user for input for color
    # print the output = hexadecimal
    color_name = input("Enter a color code: ")
    while color_name != "":
        if color_name in COLOUR_TO_CODE:
            print("The code for {} is {}.".format(color_name, COLOUR_TO_CODE.get(color_name)))
            color_name = input("Enter a color code: ")
        else:
            print("Invalid name")
            color_name = input("Enter a color code: ")


main()
