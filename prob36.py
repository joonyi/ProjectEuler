"""
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def Solution(limit):
    nums = list(range(limit))
    palins = []
    for n in nums:
        tmp = n
        palin = 0
        while tmp > 0:
            palin = (palin * 10) + (tmp % 10)
            tmp //= 10

        s = bin(n)[2:]
        t = s[::-1]
        if t == s and palin == n:
            palins.append(palin)

    return sum(palins), palins

print(Solution(1000000))

