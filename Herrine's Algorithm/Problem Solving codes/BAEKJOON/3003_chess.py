criteria = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))
res = [0 for _ in range(len(pieces))]

for i in range(len(pieces)):
    res[i] += (criteria[i] - pieces[i])

for j in range(len(res)):
    print(res[j], end=' ')