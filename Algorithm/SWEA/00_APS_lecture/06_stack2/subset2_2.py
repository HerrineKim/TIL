def f(i, N, s, t):
    global cnt
    cnt += 1
    if s == t:
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    elif i == N:  # 더 이상 고려할 원소가 없으면
        return
    elif s > t:  # 고려한 원소의 합 s가 이미 목표를 초과한 경우
        return
    else:
        bit[i] = 1
        f(i+1, N, s + a[i], t)
        bit[i] = 0
        f(i+1, N, s, t)
    return


N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
cnt = 0
t = 55
f(0, N, 0, t)
