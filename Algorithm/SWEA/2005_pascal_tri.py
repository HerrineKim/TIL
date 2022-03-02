
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [[0] * N for x in range(N)]

    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

    print('#{}'.format(tc))
    for k in pascal:
        result = []
        for l in k:
            if l != 0:
                result.append(l)
        print(*result)
