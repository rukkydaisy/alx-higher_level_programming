#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:
    a= -(a)
if a > 5:
    print('Last digit of', number, 'is', a, 'and is greater than 5')
elif a == 0:
    print('Last digit of', number, 'is', a, 'and is zero')
elif a < 6 and a != 0:
    print('Last digit of', number, 'is', a, 'and is less than 6 and not zero')

