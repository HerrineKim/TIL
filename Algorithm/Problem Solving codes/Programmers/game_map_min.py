# 게임 맵 최단거리

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0))
    maps[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
