T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # A 검색
    cntA = f(P, A)
    # B 검색
    cntB = f(P, B)
    ans = 0
    if cntA < cntB:
        ans = 'A'
    elif cntA > cntB:
        ans = 'B'
    print(f'#{tc} {ans}')
