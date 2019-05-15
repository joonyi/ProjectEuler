def printSpiral(n):
    for i in range(n):
        for j in range(n):
            # Finds minimum of four inputs
            x = min(min(i, j), min(n - 1 - i, n - 1 - j))
            # For upper right half
            if (i <= j):
                print((n - 2 * x) * (n - 2 * x) -
                      (i - x) - (j - x), end="\t")
            # For lower left half
            else:
                print(((n - 2 * x - 2) *
                       (n - 2 * x - 2) +
                       (i - x) + (j - x)), end="\t")
        print()

printSpiral(7)

# center = 1
# a = (9, 25, 49, 81, 121, ...) = 4n^2 + 4n + 1
# b = (5, 17, 37, 65, 101, ...) = 4n^2 + 1
# c = (3, 13, 31, 57, 91, ...) = 4n^2 - 2n + 1
# d = (7, 21, 43, 73, 111, ...) = 4n^2 + 2n + 1
# Sum = a + b + c + d
#     = 1 + S(16n^2) + S(4n) + S(4) where S is sum from 1 to N
#     = 1 + 8*(1/3)*n*(n+1)*(2n+1) + 2n(n+1) + 4n
def UsingFormula(n):
    return 1 + (2/3)*n*(8*n**2 + 15*n + 13)

print(UsingFormula((1001-1)//2))

size = 3
total = 1
num = 1
i = 2
while size <= 1001:
    for _ in range(4):
        num += i
        total += num
    i += 2
    size += 2

print(total)