def f(i, N, K):  # i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, K 찾는 합
    if i == N:  # 한 개의 부분집합 완성
        s = 0
        for j in range(N):
            # print(bit, end=' ')
            if bit[j] == 1:
                s += a[j]
                # print(a[j], end=' ')
            # print()
        if s == K:  # 찾는 합이면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)
    return


a = [1, 2, 3, 5, 6, 7, 8]
N = len(a)
bit = [0] * N
f(0, N, 10)