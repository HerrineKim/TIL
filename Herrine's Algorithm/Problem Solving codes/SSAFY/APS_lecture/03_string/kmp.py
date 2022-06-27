def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    j = 0
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    i = 0
    j = 0
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            print(i-M, end=' ')
            j = lps[j]


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
