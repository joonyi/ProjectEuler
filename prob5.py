"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# from math import gcd
from functools import reduce
def gcd(a,b):
    # Euclid's algorithm
    while b:
        a, b = b, a%b
    return a
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    res = a*b//gcd(a,b)
    return res

def SmallestMultiple():
    return reduce(lcm, range(1,20+1))

print(SmallestMultiple())


"""
Compute the prime factorization of each number from 1 to 20, and 
multiply the greatest power of each prime together:

20 = 2^2 * 5
19 = 19
18 = 2 * 3^2
17 = 17
16 = 2^4
15 = 3 * 5
14 = 2 * 7
13 = 13
11 = 11

All others are included in the previous numbers.

ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560
"""