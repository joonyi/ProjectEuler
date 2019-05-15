"""
Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
import math
def n_fractinal(n, digit, total):
    n = digit - n
    total //= 10**n
    return total % 10

def Solution(limit):
    nums = list(range(10,100))
    total = 0
    i = 1
    j = 0
    digit = -1
    for num in nums:
        if num % 10 == 0:
            i *= 10
            j += 1
        digit += j
        total = (total*i) + num
    return digit,total
    # part = 0
    # for k in [1,10,100]:
    #     part = n_fractinal(10000, digit, total)
    #
    # return part

print(Solution(100))