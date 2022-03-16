T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 당근밭의 갯수
    carrots = list(map(int, input().split()))  # 각 당근밭의 당근 수
    minusli = []
    sum1 = 0  # 첫 농부
    for i in range(N-1):
        sum1 += carrots[i]
        sum2 = 0  # 둘째 농부
        for j in range(i + 1, N):
            sum2 += carrots[j]
            # 절대값 함수 abs()
        minusli.append(abs(sum1-sum2))

    minV = minusli[0]
    for k in range(len(minusli)):
        if minusli[k] < minV:
            minV = minusli[k]

    print(f'#{tc} {minusli.index(minV)+1} {minV}')
