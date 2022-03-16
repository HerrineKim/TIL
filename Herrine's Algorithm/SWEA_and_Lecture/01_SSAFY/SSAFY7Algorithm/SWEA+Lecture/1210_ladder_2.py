T = 10
for t in range(1, T+1):
    x = int(input())
    lad = [[0 for _ in range(102)] for _ in range(100)]
    for i in range(100):
        lad[i][1:-1] = map(int, input().split())

    print(lad)