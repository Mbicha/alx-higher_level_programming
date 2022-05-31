#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = repr(number)
last_digit_str = number_str(-1)
last_digit = int(last_digit_str)
if last_digit > 5:
	print(f"Last digit of {number_str} is {last_digit} and isgreater than 5")
elif last_digit == 0:
	print(f"Last digit of {number_str} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
	print(f"Last digit of {number_str} is {last_digit} and is less than and not 0")

