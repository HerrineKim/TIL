from collections import deque
def bfs(a, b):
    queue = deque()
    visited[a] = 1
    queue.append(a)
    while queue:
        a = queue.popleft()
        cal = [a + 1, a - 1, a * 2, a - 10]
        for i in range(4):
            if cal[i] == b:  # 찾는 값이면 리턴
                return visited[a]
            if 0 < cal[i] <= 1000000 and visited[cal[i]] == 0:
                visited[cal[i]] = visited[a] + 1   # 누적해서 합하기
                queue.append(cal[i])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0 for _ in range(1000001)]
    print(f'#{tc} {bfs(N, M)}')
