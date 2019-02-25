"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def SumOfMultiples(number):
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum

# Compute sum of multiples 3 and 5 then minus sum of multiples 15
# a_n = a_0 + (n - 1)*d
# sum = n/2 * (a_0 + a_n)
def SumOfMultiples2(number):
    a_0, a_n, d = 3, 999, 3
    sum = (((a_n - a_0)//d + 1) * (a_0 + a_n)) // 2
    a_0, a_n, d = 5, 995, 5
    sum += (((a_n - a_0)//d + 1) * (a_0 + a_n)) // 2
    a_0, a_n, d = 15, 990, 15
    sum -= (((a_n - a_0) // d + 1) * (a_0 + a_n)) // 2

    return sum

number = 1000
print(SumOfMultiples(number))

