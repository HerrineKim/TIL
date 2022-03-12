# 4875_miro
# 0 통로 1 벽 2 출발 3 도착
def OOR(x, y):
    if x < 0 or y < 0 or y >= N or x >= N:
        return True
    return False


# 상하좌우 delta
delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # 시작 지점 찾기
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                x = i
                y = j
    # 이동가능한 곳을 저장하는 Stack
    Stack = [(x, y)]  # 초기값: 출발점
    result = 0  # 결과 기본값: 0으로 설정
    while Stack:
        x, y = Stack.pop()
        miro[x][y] = 1  # 현재위치는 방문했으므로 1로 변경한다.
        # 상하좌우 주변을 체크한다.
        for nx, ny in delta:
            dx = x + nx
            dy = y + ny
            # 상하좌우 주변을 체크한다.
            # 미로를 벗어났으면 다음으로 인덱스로 넘어간다. 아니라면 그냥 다음 코드로 간다.
            if OOR(dx, dy):
                continue
            # 도착했으면 result를 1로 하고 출력한다.
            if miro[dx][dy] == 3:
                result = 1
                break
            # 통로라면 stack에 push한다.
            elif miro[dx][dy] == 0:
                Stack.append((dx, dy))
    print(f'#{tc} {result}')
