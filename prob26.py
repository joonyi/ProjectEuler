"""
0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""

# Unsolved
a = 1
b = 7
digits = 8
for i in range(digits):
    n = a/b
    print(str(a)+'/'+str(b)+'='+str(n))
    a = (a % b) * 10
    # print(n)

def cycle(b):
    a = 1
    t = 0
    while True:
        a = a * 10 % b
        t += 1
        if a == 1:
            break
    return t

