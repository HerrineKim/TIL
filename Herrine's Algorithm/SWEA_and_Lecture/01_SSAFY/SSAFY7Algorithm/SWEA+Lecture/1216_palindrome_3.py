for _ in range(10) :
    T = int(input())
    board = []
    for _ in range(100) :
        board.append(input())

    def check(string, length):
        max_hwe = length
        while(length <= 100):
            answer = 0
            for i in range(100):
                for j in range(101-length):
                    word = string[i][j:j+length]
                    if word == word[::-1]:
                        max_hwe = length
                        answer = 1
                        break
                if answer == 1 :
                    break
            length += 1
        return max_hwe

    # 가로줄
    row = check(board, 1)

    # 세로줄
    transposed_board = []
    for i in range(100) :
        list = ""
        for j in range(100) :
            list += board[j][i]
        transposed_board.append(list)

    col = check(transposed_board, 1)

    print("#{} {}".format(T, max(row, col)))