def f(i, N, K):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += a[j]  # bit[j]가 1이면 a[j]가 부분집합에 포함
        if s == K:
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    else:
        bit[i] = 1  # 1이 먼저 들어가든 0이 먼저 들어가든 상관 없음
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)
    return
N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
K = 12
f(0, N, K)