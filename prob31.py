"""
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
def count(coins, n):
    # Dynamic programming bottom up
    table = [0 for _ in range(n+1)]

    # Base case is 1 bcs we want to add 1 when target == coin
    table[0] = 1

    # Pick one coin at a time, and compute if I have only that one coin
    # how many possible ways to sum up to target
    for coin in coins:
        for j in range(coin, n+1):
            table[j] += table[j - coin]

    return table[n]


coins = [1, 2, 5]
n = 5
print(count(coins, n))


