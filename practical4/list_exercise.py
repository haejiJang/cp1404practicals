def basic_list_operations():
    '''This function shows basic list operation'''
    numbers = []
    for i in range (5):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is ", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is ", min(numbers))
    print("The largest number is ", max(numbers))
    print("The average of the numbers is ", sum(numbers)/len(numbers))

basic_list_operations()

def woefully_inadequate_security_checker():
    '''This function evaluates username's accessibility'''
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = str(input("What is your name?"))
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

woefully_inadequate_security_checker()
