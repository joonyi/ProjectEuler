"""
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def isprime(n):
    n=int(n)
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def Circular(n, primes):
    s = str(n)
    for i in s:
        if int(i) in [0,2,4,6,8]: # any two or more digits number contain 0,2,4,8 is not circular prime
            return False

    for i in range(len(s)): # rotate left
        s = s[1:] + s[0]
        if int(s) not in primes:
            return False

    return True

def Solution():
    primes = primes_upto(1000000)
    count = 1

    for prime in primes:
        cir = Circular(prime, primes)
        if cir:
            count += 1

    print(count)

Solution()



