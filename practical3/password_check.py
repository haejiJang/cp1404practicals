minimum_length = 6

def main():
    password = get_password()
    print("*" * len(password))

def get_password():
    '''This function gets the password from the user'''
    password = input("Enter the password. Minimum length is {}.".format(minimum_length))
    while len(password) < 6:
        password = input("The minimum length of password is {}.".format(minimum_length))

    return password

main()