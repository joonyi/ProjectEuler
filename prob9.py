"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

x = 1000

for a in range(1, x+1):
    for b in range(1, x+1):
        if a > b:
            continue
        if a + b + (a**2 + b**2)**0.5 == x:
            print("a: " + str(a) + " b: " + str(b) + " c: " + str(int((a**2 + b**2)**0.5)))
            print("Product of abc " + str(a*b*int((a**2 + b**2)**0.5)))