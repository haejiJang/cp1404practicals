min_length = 5
max_length = 15
special_character_amount = False
special_character = "!@#$%^&*()_-=+`~,./'[]<>?{}|"

def main():
    '''This function asks the user password and calls valid_password function to evaluate.'''
    print("Please enter a valid password")
    print("Your password must be between 5 and 15 characters, and contain:" )
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if special_character_amount:
        print("\tand 1 or more special characters: ", special_character)
    password=input("=>")
    while not valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)

def valid_password(password):
    '''This function evaluates the validity of password'''
    if len(password) < min_length or len(password) > max_length:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in special_character:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if special_character_amount:
        if count_special == 0:
            return False

    return True


main()