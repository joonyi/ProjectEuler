"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
def SumPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

    total = 0
    for i, elem in enumerate(primes):
        if elem:
            total += i

    return total, sum(primes)

n = 2000000
print(SumPrimes(n))
print("This program took: " + str(time.process_time() * 1000) + "ms.")