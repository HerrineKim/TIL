# 1210. Ladder1
for t in range(10):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for i in range(100)]
    for i in range(102):
        if arr[99][i] == 2:
            X = i
    Y = 99
    while Y > 0:
        if arr[Y][X + 1] == 1:
            arr[Y][X] = 0
            X += 1
        elif arr[Y][X - 1] == 1:
            arr[Y][X] = 0
            X -= 1
        elif arr[Y - 1][X] == 1:
            Y -= 1

    print(f'#{tc} {X - 1}')
