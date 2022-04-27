T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    speed = 0
    move = 0
    for _ in range(N):
        arr = list(map(int, input().split()))
        # 갈 거리 구하기
        if arr[0] == 1:  # 가속
            speed += arr[1]
        elif arr[0] == 2:  # 감속
            if speed > arr[1]:  # 감속 작업
                speed -= arr[1]
            else:  # 0으로 초기화
                speed = 0
        move += speed  # for 문 마지막에서 이동
    print('#{} {}'.format(tc, move))
