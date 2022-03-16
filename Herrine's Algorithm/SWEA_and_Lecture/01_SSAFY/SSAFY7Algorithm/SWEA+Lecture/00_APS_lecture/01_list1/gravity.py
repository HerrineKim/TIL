# gravity
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                ans[i] += 1
    maxV = ans[0]
    for k in range(1, N):
        if maxV < ans[k]:
            maxV = ans[k]
    print(f'#{test_case} {maxV}')

'''
input
3
9
7 4 2 0 0 6 0 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
100
1 83 27 3 96 23 9 48 54 94 32 4 26 79 35 0 69 52 15 13 72 34 86 52 97 61 44 57 71 81 15 86 8 31 46 80 95 95 21 83 55 90 97 90 30 61 45 35 95 86 3 39 53 26 69 0 92 17 15 72 79 63 41 11 94 55 14 89 65 15 45 13 15 17 23 100 55 68 60 46 77 29 4 13 53 3 79 58 9 88 20 84 93 71 28 67 22 7 12 43 
'''