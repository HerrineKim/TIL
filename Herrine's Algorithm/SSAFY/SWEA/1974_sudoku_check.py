# 1974. 스도쿠 검증(D2)
T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    res = 1
    # 가로 검사
    for i in range(9):
        cnt = 0
        for j in range(9):
            cnt += sudoku[i][j]
        if cnt != 45:
            res = 0
            print(f'#{tc} {res}')
            break

    # 세로 검사
    if res == 1:
        sudokuR = list(map(list, zip(*sudoku)))
        for i in range(9):
            cnt = 0
            for j in range(9):
                cnt += sudokuR[i][j]
            if cnt != 45:
                res = 0
                print(f'#{tc} {res}')
                break

    # 칸 검사
        if res == 1:
            dx = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
            dy = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
            points = [1, 4, 7]
            for k in points:
                for l in points:
                    cnt = 0
                    cnt += sudoku[k+dx[0]][l+dy[0]]
                    cnt += sudoku[k+dx[1]][l+dy[1]]
                    cnt += sudoku[k+dx[2]][l+dy[2]]
                    cnt += sudoku[k+dx[3]][l+dy[3]]
                    cnt += sudoku[k+dx[4]][l+dy[4]]
                    cnt += sudoku[k+dx[5]][l+dy[5]]
                    cnt += sudoku[k+dx[6]][l+dy[6]]
                    cnt += sudoku[k+dx[7]][l+dy[7]]
                    cnt += sudoku[k+dx[8]][l+dy[8]]
                    if cnt != 45:
                        res = 0
            print(f'#{tc} {res}')
