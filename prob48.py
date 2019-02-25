"""
Self powers
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
"""
import time
a = 1
b = 1
add = 0
while a <= 1000 and b <= 1000:
    add += a ** b
    a += 1
    b += 1

remain = add % 10000000000
print(add, "\n", remain)
print("This program took: " + str(time.process_time() * 1000) + "ms.")
