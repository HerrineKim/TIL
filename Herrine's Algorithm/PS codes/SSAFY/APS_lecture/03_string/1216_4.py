def palindrome(n):
    column = list(map(list, zip(*n)))
    # print(column)
    # 뒤부터 회문을 돌리면 최대값을 구하기 좀 더 수월
    for i in range(100, 0, -1):
        for j in range(100):
            for k in range(101 - i):
                row_palin, column_palin = n[j][k:k + i], column[j][k:k + i]
                if row_palin == row_palin[::-1]:
                    return i
                if column_palin == column_palin[::-1]:
                    return i


for test in range(10):
    number = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    print(f'#{number} {palindrome(arr)}')
