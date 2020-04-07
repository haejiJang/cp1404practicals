try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Do not enter 0. Please put integer numbers only.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

'''
When will a ValueError occur?
    => When I try to put numbers that are not integers.
When will a ZeroDivisionError occur?
   =>  When I try to put 0 for denominator
Could you change the code to avoid the possibility of a ZeroDivisionError?
    => Yes.
'''