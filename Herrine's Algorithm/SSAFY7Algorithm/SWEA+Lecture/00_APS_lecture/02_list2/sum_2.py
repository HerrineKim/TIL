for k in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    n = 100
    max_num = 0

    for i in range(n):  # 행의 합
        result = 0
        for j in range(n):
            result += arr[i][j]
        if max_num < result:
            max_num = result

    for i in range(n):  # 열의 합
        result = 0
        for j in range(n):
            result += arr[j][i]
        if max_num < result:
            max_num = result

    result = 0
    for i in range(n):  # 좌->우 대각선의 합
        result += arr[i][i]
        if max_num < result:
            max_num = result

    result = 0
    for i in range(n):  # 우->좌 대각선의 합
        result += arr[i][n - i - 1]
        if max_num < result:
            max_num = result

    print(f'#{test_case} {max_num}')
