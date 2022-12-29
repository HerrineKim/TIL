# 최소 거리를 구하는 BFS 기초 문제
# 속도 개선을 위한 deque 사용
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0))
    maps[0][0] = 1
    # BFS
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 최단 거리를 구하는 것이기에 지나가는 길마다 +1 누적
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
    # 더 이상 이동할 수 없을 때 (덱이 비었을 때),
    # 목표 지점이 아직 다다르지 못한 곳(숫자 1)이 아니면 여태까지의 누적 거리 return
    # 1이라면 -1 return
    if maps[n - 1][m - 1] != 1:
        return maps[n - 1][m - 1]
    else:
        return -1
