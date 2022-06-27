def f(i, j, k):
    print(i, j, k)


N = 10
R = 3
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            f(i, j, k)
