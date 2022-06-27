T = 10
for tc in range(1, T + 1):
    N = int(input())
    que = list(map(int, input().split()))
    ended = 0
    while True:
        for i in range(1, 6):
            que[0] -= i
            x = que.pop(0)
            que.append(x)
            if que[-1] <= 0:
                que[-1] = 0
                ended += 1
                break
        if ended:
            break
    print(f"#{tc}", end=' ')
    print(*que)
