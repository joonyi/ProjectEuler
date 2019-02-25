"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
import time

def isprime(n):
    # make sure n is a positive integer
    n = abs(n)
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# A function to find largest prime factor
def LargestPrimeFactor(n):
    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2

    # n must be odd at this point, thus skip the even numbers and iterate only for odd integers
    # test up to square root because at least one factor less than square root
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n // i # The key is to divide n to get a smaller number and save time

    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        maxPrime = n

    return maxPrime

# n = 13195
# print(LargestPrimeFactor(n))

n = 600851475143
print(LargestPrimeFactor(n))
print("This program took: " + str(time.process_time() * 1000) + "ms.")
