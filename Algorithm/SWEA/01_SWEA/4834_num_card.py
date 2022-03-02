T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    cnt = [0] * 10
    for x in card:
        cnt[x] += 1
    maxIdx = 0
    for i in range(10):
        if cnt[maxIdx] <= cnt[i]:
            maxIdx = i
    print(f'#{tc} {maxIdx} {cnt[maxIdx]}')