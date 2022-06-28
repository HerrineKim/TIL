import sys
from collections import deque
N = int(input())  # N 주어지는 명령의 수

queue = deque()
for i in range(N):
    direction = sys.stdin.readline().rstrip()
    if 'push' in direction:
        push, num = map(str, direction.split())
        queue.append(int(num))
    elif direction == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif direction == 'size':
        print(len(queue))
    elif direction == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif direction == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif direction == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])