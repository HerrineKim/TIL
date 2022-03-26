from collections import deque

p = 1
q = deque()
N = 100000000  # 초기 마이쮸 개수
my = [0] * (N+1)
cnt = [0] * (N+1)
m = 0  # 나눠준 개수
v = 0

while m < N:
    q.append(p)
    cnt[p] += 1
    v = q.popleft()
    m += cnt[v]
    my[v] += cnt[v]

    q.append(v)
    cnt[v] += 1
    p += 1

print(f'마지막 받은 사람 : {v}')
