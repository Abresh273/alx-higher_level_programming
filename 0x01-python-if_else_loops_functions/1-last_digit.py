#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if(str(number)[-1] == 0):
    print(f"Last digit of {number} is 0 and is 0")
if(number < 0 && str(number)[-1] < 6):
    print(f"ast digit of {number} is -{str(number)[-1]} and is less than 6 and not 0")
if(number > 0 && str(number)[-1] > 5):
    print(f"ast digit of {number} is {str(number)[-1]} and is greater than 5 and not 0")   
if(number > 0 && str(number)[-1] < 5):
    print(f"ast digit of {number} is {str(number)[-1]} and is less than 5 and not 0")  
