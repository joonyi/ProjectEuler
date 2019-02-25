"""
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

num = 2 ** 1000
total = 0
while num > 0:
    total += num % 10
    num = num // 10

print(total)