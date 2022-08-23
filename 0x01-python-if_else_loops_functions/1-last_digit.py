#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
lst = n % 10 if n > 0 else -n % 10
if n < 0:
    lst *= -1
if lst == 0:
    print(f"Last digit of {n} is {lst} and is 0")
elif lst < 6:
    print(f"Last digit of {n} is {lst} and is less than 6 and not 0")
else:
    print(f"Last digit of {n} is {lst} and is greater than 5")
