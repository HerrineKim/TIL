T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge = list(map(int, input().split()))

    stop = [0] * (N+1)
    idx = 0
    cnt = 0

    for i in charge:
        stop[i] = 1
    while True:
        idx += K
        if idx >= N:
            break
        for k in range(idx, idx-K, -1):
            if stop[k] == 1:
                cnt += 1
                idx = k
                break
        else:
            cnt = 0
            break
    print(f'#{tc} {cnt}')

'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
'''