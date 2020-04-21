def main():
    '''This function is to make a dictionary of names and email addresses'''
    email_and_name = {}
    address = input("Email: ")
    while address != "":
        name = user_name(address)
        confirmation = input("Is your name {}? (Y/n)".format(name))
        if confirmation.upper != "Y" or confirmation != "":
            name = input("Name: ")
        email_and_name[address] = name
        address = input("Email: ")

    for address, name in email_and_name.items():
        print("{} ({})".format(name, address))

def user_name(address):
    '''Get user's name from the email address'''
    no_atmark = address.split('@')[0]
    no_dot = no_atmark.split('.')
    name = " ".join(no_dot).title()
    return name

main()
