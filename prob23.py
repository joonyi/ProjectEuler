import time
def d(n):
    pair = [1]
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            if i not in pair:
                pair.append(i)
            if n//i not in pair:
                pair.append(n//i)

    return sum(pair)

def NonAbundantSum(n):
    total = sum([i for i in range(1, (n + 1))])
    abunNum = [i for i in range(1, n) if d(i) > i]
    abunSums = [0] * (n+1)
    for i in abunNum:
        for j in abunNum:
            add = i + j
            if  add <= n and abunSums[add] == 0:
                abunSums[add] = add

    return total - sum(abunSums)

print(NonAbundantSum(28123))
print("This program took: " + str(time.process_time() * 1000) + "ms.")