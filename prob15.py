"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import time
n = 2+1
A = [[0 for _ in range(n)] for _ in range(n)]

for i in range(len(A)):
    A[0][i] = 1
for j in range(len(A[0])):
    A[j][0] = 1

for i in range(1, len(A)):
    for j in range(1, len(A[0])):
        A[i][j] = A[i-1][j] + A[i][j-1]

print(A)
print(A[-1][-1])
print("This program took: " + str(time.process_time() * 1000) + "ms.")

