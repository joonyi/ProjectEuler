"""
Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23
"""

triangle = [[3],
       [7, 4],
       [2, 4, 6],
       [8, 5, 9, 3]]

# triangle = [
# [75],
# [95,64],
# [17,47,82],
# [18,35,87,10],
# [20,4,82,47,65],
# [19,1,23,75,3,34],
# [88,2,77,73,7,63,67],
# [99,65,4,28,6,16,70,92],
# [41,41,26,56,83,40,80,70,33],
# [41,48,72,33,47,32,37,16,94,29],
# [53,71,44,65,25,43,91,52,97,51,14],
# [70,11,33,28,77,73,17,78,39,68,17,57],
# [91,71,52,38,17,14,91,43,58,50,27,29,48],
# [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
# [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23],
# ]
def MaxPathSum(triangle):
    if not triangle:
        return
    res = list(triangle[-1])
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            res[j] = max(res[j], res[j+1]) + triangle[i][j]
    return res[0]

def MaxPathSum2(triangle):
    if not triangle:
        return
    res = [[0 for i in range(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                res[i][j] = res[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                res[i][j] = res[i-1][j-1] + triangle[i][j]
            else:
                res[i][j] = max(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
    return max(res[-1])

print(MaxPathSum(triangle))