# 2164. 카드2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])