def binary_search(t, li):
    global res
    start, end = 0, N-1
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if li[mid] == t:
            res += 1
            return
        elif li[mid] > t:
            if check == 1:
                break
            end = mid - 1
            check = 1
        else:
            if check == 2:
                break
            start = mid + 1
            check = 2


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    res = 0
    for i in range(len(B)):
        binary_search(B[i], A)
    print(f'#{test_case} {res}')

