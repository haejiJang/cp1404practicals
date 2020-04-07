import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

'''
16
3
4.323922084022535
'''

'''
10
7
4.203271660713382
'''

'''
19
5
3.752464875044672
'''


'''What did you see on line 1? 
    I saw integer numbers.
What was the smallest number you could have seen, what was the largest?
    The smallest was 5 and the biggest was 20.

What did you see on line 2?
    I saw odd numbers.
What was the smallest number you could have seen, what was the largest?
    The smallest was 3 and the largest was 9.
Could line 2 have produced a 4?
    No. It only produced only odd numbers
    

What did you see on line 3?
    I saw numbers with a lot of decimals.
What was the smallest number you could have seen, what was the largest?
    The smallest was 2.54~~~~. The largest was 5.48~~~~.
Write code, not a comment, to produce a random number between 1 and 100 inclusive.'''

print(random.randint(1,1))