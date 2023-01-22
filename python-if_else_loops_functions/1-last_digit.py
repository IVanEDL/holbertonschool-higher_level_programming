#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    module = -(-number % 10)
else:
    module = number % 10
if module > 5:
    print(f"Last digit of {number} is {module} and is greater than 5")
elif module == 0:
    print(f"Last digit of {number} is {module} and is 0")
else:
    print(f"Last digit of {number} is {module} and is less than 6 and not 0")
