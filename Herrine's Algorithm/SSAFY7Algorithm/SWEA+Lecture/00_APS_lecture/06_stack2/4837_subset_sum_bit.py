# 비트연산
def f1(i, M, N, K):
    global cnt
    if i == M:
        s = 0
        c = 0
        for j in range(M):  # M = 12
            if bit[j]:
                s += arr[j]
                c += 1
        if c == N and s == K:
            cnt += 1
    else:
        bit[i] = 1
        f1(i+1, M, N, K)
        bit[i] = 0
        f1(i+1, M, N, K)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [x for x in range(1, 13)]
    bit = [0] * 12
    cnt = 0
    f1(0, 12, N, K)

    print(f'#{tc} {cnt}')

# 가지치기를 있어보이는 말로 하면 백트래킹
