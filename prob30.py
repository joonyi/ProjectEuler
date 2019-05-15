"""
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers
of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""
# A max number with d digits is n = d*9^5 and it must be bounded by number-length interval
# 10^(d-1) < d*9^5 < 10^d

fifth = []
larger = []
for i in range(10,354294+1):
    total = 0
    n = i
    while n > 0:
        tmp = n % 10
        total += tmp**5
        n //= 10
    if total == i:
        fifth.append(i)
    elif total < i:
        larger.append(i)

# print(fifth)
print(larger[:100])