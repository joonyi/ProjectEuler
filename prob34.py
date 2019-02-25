
def factorial(n):
    fac = 1
    while n > 0:
        fac *= n
        n -= 1
    return fac

def CuriousNum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += factorial(digit)
        n //= 10

    return sum

n = [i for i in range(3,100000) if CuriousNum(i) == i]
print(n, sum(n))