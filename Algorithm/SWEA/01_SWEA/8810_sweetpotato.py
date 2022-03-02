# 8810. 당근밭 옆 고구마밭
T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 고구마밭의 개수
    arr = list(map(int, input().split()))   # 각 밭의 고구마 개수의 리스트
    Points = []  # 감소되는 값의 시작점들
    SumLi = [0]*1000
    cnt = [0]*1000
    for i in range(1, N):
        if arr[i-1] >= arr[i]:
            Points.append(i)

    if len(Points) == 0:
        for j in range(N):
            SumLi[0] += arr[j]
            cnt[0] += 1
    elif len(Points) == 1:
        for k in range(Points[0]):
            SumLi[0] += arr[k]
            cnt[0] += 1
        for l in range(Points[0], N):
            SumLi[1] += arr[l]
            cnt[1] += 1
    else:
        for m in range(len(Points)):
            if m == 0:
                for n in range(Points[0]):
                    SumLi[0] += arr[n]
                    cnt[0] += 1
            elif 0 < m:
                for o in range(Points[m-1], Points[m]):
                    SumLi[m] += arr[o]
                    cnt[m] += 1
        for p in range(Points[-1], len(arr)):
            SumLi[len(Points)] += arr[p]
            cnt[len(Points)] += 1

    while 0 in cnt:
        cnt.remove(0)
    while 0 in SumLi:
        SumLi.remove(0)
    LineN = 0
    for x in range(len(cnt)):
        if cnt[x] > 1:
            LineN += 1

    # print(cnt)
    # print(SumLi)

    Idx = cnt[0]
    for b in range(len(cnt)):
        if Idx < cnt[b]:
            Idx = cnt[b]
    MaxSum = SumLi[cnt.index(Idx)]
    if len(set(cnt)) == 1:
        MaxSum = max(SumLi)

    print(f'#{tc} {LineN} {MaxSum}')

'''
[5, 3]
[15, 6]
#1 2
[4, 1, 1, 1]
[10, 3, 2, 1]
#2 1
[3, 3, 3]
[6, 9, 6]
#3 3


[2, 3]
[10, 6]
#4 2
'''