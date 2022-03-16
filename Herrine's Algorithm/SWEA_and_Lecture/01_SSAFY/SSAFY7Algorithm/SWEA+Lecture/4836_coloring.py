T = int(input())
for test_case in range(1, T+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]  # 10x10 격자판
    N = int(input())  # 색칠 영역
    count = 0  # 보라색 영역의 개수

    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        for row in range(x1, x2+1):
            for col in range(y1, y2+1):
                if color == 1:  # 만약 칠할 색이 빨강이면
                    if arr[row][col] == 0:  # 만약 아무런 색도 없다면
                        arr[row][col] = 1  # 그대로 칠해줌
                    elif arr[row][col] == 2:  # 만약 파란색이 들어가 있다면
                        arr[row][col] = 3  # 보라색으로 변경
                        count += 1  # 보라색 count +1
                else:  # 만약에 칠할 색이 파랑이면
                    if arr[row][col] == 0:  # 만약 아무런 색도 없다면
                        arr[row][col] = 2  # 그대로 칠해줌
                    elif arr[row][col] == 1:  # 만약 파란색이 들어가 있다면
                        arr[row][col] = 3  # 보라색으로 변경
                        count += 1  # 보라색 count +1

    print(f'#{test_case} {count}')
