"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""
import time
def SumSquareDiff(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1,n+1):
        sum_of_squares += i ** 2
    for i in range(1,n+1):
        square_of_sum += i
    square_of_sum = square_of_sum ** 2
    print(sum_of_squares, square_of_sum)

    return square_of_sum - sum_of_squares


# 1 ... 1^2
# 1+3 ... 2^2
# 1+3+5 ... 3^2
# (n+1)^2 = n^2 + 2n + 1 -> squares are also the sum of odd numbers
def SumSquareDiff2(n):
    square_of_sum = (n * (n+1) // 2) ** 2
    sum_of_squares = 0
    for i in range(1,n*2,2):
        sum_of_squares += i * n
        n -= 1
    return square_of_sum - sum_of_squares

print(SumSquareDiff2(100))
print("This program took: " + str(time.process_time() * 1000) + "ms.")