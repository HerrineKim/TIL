# 고지식한 패턴 검색
t = 'TTTTAACT'
p = 'TTA'
N = len(t)
M = len(p)
ans = -1

for i in range(N - M - 1):
    for j in range(M):
        if t[i+j] != p[j]:
            break
    else:
        ans = i
        break
print(ans)
