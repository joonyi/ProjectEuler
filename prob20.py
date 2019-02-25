"""
Factorial digit sum
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n):
    fac = 1
    while n > 0:
        fac *= n
        n -= 1
    return fac

def facDigitSum(n):
    digit = factorial(n)
    total = 0
    while digit > 0:
        total += digit % 10
        digit //= 10

    return total

def facDigitSum2(n):
    total = sum([int(x) for x in str(factorial(n))])
    return total

print(facDigitSum(100))