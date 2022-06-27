

def nCr(n, r, s, k):  # n 개에서 r 개를 고르는 조합. s 고를 수 있는 구간의 시작 인덱스
    if r == 0:
        print(comb)
    else:
        for i in range(s, n-r+1):
            comb[k-r] = A[i]
            nCr(n, r-1, i+1, k)


n = 5
r = 4
k = r
comb = [0] * r
A = [i for i in range(1, n+1)]
nCr(n, r, 0, k)
