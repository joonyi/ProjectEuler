from itertools import permutations

def perm1(n):
    a = list(range(n))
    def sub(i):
        if i == n - 1:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                yield from sub(i + 1)
                a[i], a[k] = a[k], a[i]
    yield from sub(0)

def perm2(n):
    a = list(range(n))
    def sub(i):
        if i == n - 1:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                yield from sub(i + 1)
            x = a[i] # produce lexicographic order
            for k in range(i + 1, n):
                a[k - 1] = a[k]
            a[n - 1] = x
    yield from sub(0)


def nextperm(a):
    n = len(a)
    i = n - 1
    while i > 0 and a[i - 1] > a[i]:
        i -= 1
    j = i
    k = n - 1
    while j < k:
        a[j], a[k] = a[k], a[j] #swap back
        j += 1
        k -= 1
    if i == 0:
        return False
    else:
        j = i
        while a[j] < a[i - 1]:
            j += 1
        a[i - 1], a[j] = a[j], a[i - 1]
        return True

def perm3(n):
    if type(n) is int:
        if n < 1:
            return []
        a = list(range(n))
    else:
        a = sorted(n)
    u = [tuple(a)]
    while nextperm(a):
        u.append(tuple(a))
    return u

def perm4(n):
    xs = list(range(n))
    ac = [[]]
    for x in xs:
        ac_new = []
        for ts in ac:
            for n in range(0,ts.__len__()+1):
                new_ts = ts[:]  #(shallow) copy of ts
                new_ts.insert(n,x)
                ac_new.append(new_ts)
        ac=ac_new
    return ac

def Permutation(n):
    perm = list(permutations([i for i in range(3)]))

    return perm #,perm[n-1]

print(Permutation(3))
print(list(perm3(4)))