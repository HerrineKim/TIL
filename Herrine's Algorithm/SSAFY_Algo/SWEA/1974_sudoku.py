case_count = int(input())

for i in range(1, case_count + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    # 가로세로
    for row_index, row in enumerate(matrix):
        as_col = []
        if len({*row}) != 9:
            result = 0
            break
        else:
            for col in range(9):
                as_col.append(matrix[col][row_index])
            if len({*as_col}) != 9:
                result = 0
                break

    # 블록
    if result:
        for col in range(0, 9, 3):
            for row in range(0, 9, 3):
                block_numbers = []
                for j in range(3):
                    for k in range(3):
                        block_numbers.append(matrix[col+j][row+k])
                if len({*block_numbers}) != 9:
                    result = 0
                    break
    print('#{} {}'.format(i, result))