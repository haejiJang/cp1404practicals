'''odd numbers from 1 to 20'''
for i in range(1, 21, 2):
    print(i, end=' ')
print()

'''a'''
for i in range (0, 101, 10):
    print(i, end=' ')
print()

'''b'''
for i in range (20, 0, -1):
    print(i, end=' ')
print()

'''c'''
num_of_stars = int(input("How many stars do you want"))
for i in range (num_of_stars):
    print("*", end=' ')
print()

'''d'''
for i in range (1, num_of_stars + 1):
    print("*" * i)
print()