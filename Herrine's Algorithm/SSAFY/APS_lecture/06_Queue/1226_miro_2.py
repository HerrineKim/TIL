def bfs(x, y):  # 너비우선탐색
    que = [(x, y)]  # queue
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while que:
        x, y = que.pop(0)
        if miro[x][y] == 0 or 2:  # 지나간 곳은 1로 바꾸어 준다
            miro[x][y] = 1
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= 15 and 0 <= ny <= 15:
                    if miro[nx][ny] == 0:  # 탐색한 곳 중에 길이 있으면 queue에 담는다
                        que.append((nx, ny))
                    elif miro[nx][ny] == 3:  # 종점을 만나면 1을 return 한다
                        return 1
    return 0  # que가 비면 종점을 만나기 전에 길이 끊어졌다는 뜻이므로 0을 return 한다.


for _ in range(10):
    T = int(input())
    miro = [list(map(int, list(input()))) for _ in range(16)]
    for i in range(16):
        if 2 in miro[i]:
            rx, ry = i, miro[i].index(2)
            break
    print(f'#{T} {bfs(ry, rx)}')
