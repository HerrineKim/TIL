# 1948. 날짜 계산기
T = int(input())
for tc in range(1, T+1):
    M1, D1, M2, D2 = map(int, input().split())
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = 0
    if M1 == M2:
        res = D2 - D1 + 1
    else:
        for m in range(M1+1, M2):
            res += months[m]
        res += (months[M1] - D1) + D2 + 1
    print(f'#{tc} {res}')
