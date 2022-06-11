H, M = map(int, input().split())
if H == 0 and M < 45:
    nH = 23
    nM = M + 60 - 45
    print(nH, nM)
else:
    temp = H * 60 + M
    temp -= 45
    nH = temp // 60
    nM = temp - nH * 60
    print(nH, nM)
