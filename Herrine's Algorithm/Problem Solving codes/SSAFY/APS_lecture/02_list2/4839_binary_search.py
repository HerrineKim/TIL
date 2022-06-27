def binary_search(t, li):
    start, end = 1, len(li)
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == t:
            return cnt
        elif mid < t:
            start = mid
            cnt += 1
        else:
            end = mid
            cnt += 1


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(len(B)):
        target = B[i]
        if binary_search(target, A)

