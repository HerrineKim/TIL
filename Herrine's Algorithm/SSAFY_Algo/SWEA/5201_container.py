T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort()
    container.reverse()
    res = 0
    for i in range(len(truck)):
        for j in range(len(container)):
            if truck[i] >= container[j]:
                res += container[j]
                container.remove(container[j])
                break
    print(f'#{tc} {res}')
