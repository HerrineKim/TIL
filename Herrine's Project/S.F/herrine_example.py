import random

matrix = [[0] * 52 for _ in range(52)]
alist = []

for i in range(52):
    for j in range(52):
        x = random.randrange(0, 100)
        while x in alist:
            x = 0
        matrix[i][j] = x
        if x != 0:
            alist.append(x)

for a in range(len(matrix)):
    for b in range(len(matrix[a])):
        print(matrix[a][b], end=" ")
    print()
