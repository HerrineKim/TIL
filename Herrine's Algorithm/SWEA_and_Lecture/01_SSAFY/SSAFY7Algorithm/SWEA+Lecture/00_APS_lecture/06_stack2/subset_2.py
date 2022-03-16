def f(i, N, K, S):  # S i-1원소까지 고려한 합
    global cnt
    cnt += 1
    if K == S:
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    elif i == N:    # 한 개의 부분집합이 완성된 경우
        return
    elif S > K:
        return
    else:
        bit[i] = 1
        f(i+1, N, K, S+a[i])
        bit[i] = 0
        f(i+1, N, K, S)
    return


N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
K = 5
cnt = 0

f(0, N, K, 0)  # 합이 K인 부분집합을 찾는 함수
print(cnt)
