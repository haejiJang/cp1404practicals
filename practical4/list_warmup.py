#Create a Python file called lists_warmup.py and enter the following line:

#numbers = [3, 1, 4, 1, 5, 9, 2]

#What values do the following expressions have?
#Without running the code, write down your answers to these questions (on paper, or in your Python file as a comment), then use Python to see if you were correct.

#numbers[0]
#numbers[-1]
#numbers[3]
#numbers[:-1]
#numbers[3:4]
#5 in numbers
#7 in numbers
#"3" in numbers
#numbers + [6, 5, 3]

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0]) #3
print(numbers[-1]) #2
print(numbers[3]) #1
print(numbers[:-1]) #3, 1, 4, 1, 5, 9
print(numbers[3:4]) #1
print(5 in numbers) #True
print(7 in numbers) #False
print("3" in numbers) #False
print(numbers + [6,5,3]) #[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]