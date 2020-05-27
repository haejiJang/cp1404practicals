"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:
        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, get_fixed_filename(filename))
        os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for index, letter in enumerate(filename):
        previous_letter = filename[index -1 ]
        if previous_letter == "_" and letter.isalnum():
            letter = letter.upper()
        new_name = new_name + letter
        if index < len(filename) - 1:
            next_letter = filename[index + 1]

            if letter.isalnum() and (next_letter.isupper() or next_letter.isdigit()):
                new_name += "_"

    return new_name


main()
