import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45

def main():
    '''This function displays quick picks program'''
    number_of_picks = int(input("How many quick picks?"))

    for i in range(number_of_picks):
        quick_pick = []
        for l in range(NUMBER_PER_LINE):
            number = random.randint(MIN,MAX)
            while number in quick_pick:
                number = random.randint(MIN,MAX)
            quick_pick.append(number)
        quick_pick.sort
        print(" ".join("{:2}".format(number) for number in quick_pick))
main()