"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import time

# This solution better
def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes

def is_prime(n):
    """Checks if a number and returns True or False depending on the result."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

def primes2(n):
    current_number = 3
    total_primes = 1
    while True:
        if is_prime(current_number):
            total_primes += 1
        if total_primes == 10001:
            return current_number
        current_number += 2


print(primes2(11))
print("This program took: " + str(time.process_time() * 1000) + "ms.")