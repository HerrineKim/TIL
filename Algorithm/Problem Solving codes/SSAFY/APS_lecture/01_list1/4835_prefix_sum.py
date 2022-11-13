# 4835. 구간합
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    samples = input().split()
    
    x = 0
    for i in range(M):
        x += int(samples[i])
    max_r = x
    min_r = x
    
    for j in range(1, N - M + 1):
        temp = 0
        for k in range(j, j + M):
            temp += int(samples[k])
        if temp > max_r:
            max_r = temp
        if temp < min_r:
            min_r = temp
    
    result = max_r - min_r
    print(f'#{tc} {result}')

'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
'''