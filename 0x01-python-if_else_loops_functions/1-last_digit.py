#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if(str(number)[-1]  == 0):
         print(f"Last digit of {number} is 0")

if(number<0):
    if(str(number)[-1] < 6 && str(number)[-1] != 0):
         print(f"Last digit of -{number} is {str(number)[-1]} and is less than 6 and not 0")
    if(str(number)[-1] < 6 && str(number)[-1] != 0):
         print(f"Last digit of -{number} is {str(number)[-1]} and is less than 6 and not 0")
else:
    if(str(number)[-1] > 6 && str(number)[-1] != 0):
         print(f"Last digit of {number} is {str(number)[-1]} and is greater than 6 and not 0")
    if(str(number)[-1] < 6 && str(number)[-1] != 0):
         print(f"Last digit of {number} is {str(number)[-1]} and is greater less 6 and not 0")
