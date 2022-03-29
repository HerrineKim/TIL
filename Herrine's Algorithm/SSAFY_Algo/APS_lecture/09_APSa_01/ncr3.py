# n 개에서 r개를 고르는 조합, s 선택 구간의 시작, k 고른 개수


def nCr(n, r, s, k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):  # n-r+k 선택할 수 있는 구간의 끝
            comb[k] = A[i]
            nCr(n, r, i+1, k+1)


n = 5
r = 3
A = [i for i in range(1, n+1)]
comb = [0] * r
nCr(n, 3, 0, 0)
