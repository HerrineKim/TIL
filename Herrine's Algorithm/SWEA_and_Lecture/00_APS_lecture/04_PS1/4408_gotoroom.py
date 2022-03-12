T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maxvalue = 0
    corridor = [0] * 201
    for i in range(N):
        start, end = map(int, input().split())
        if start < end:
            for j in range((start-1)//2, (end-1)//2 + 1):
                corridor[j] += 1
        else:
            for j in range((start-1)//2, (end-1)//2 - 1, -1):
                corridor[j] += 1

        for k in range(len(corridor)):
            if maxvalue < corridor[k]:
                maxvalue = corridor[k]
    print(f'#{tc} {maxvalue}')
