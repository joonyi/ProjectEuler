"""
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

def Fibonacci(limit):
    fib = [1,2]
    i = 0
    sum_even = 2
    while fib[i] + fib[i+1] < limit:
        fib.append(fib[i] + fib[i+1])
        i += 1
        if fib[-1] % 2 == 0:
            sum_even += fib[-1]

    return sum_even

print(Fibonacci(4000000))