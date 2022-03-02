def binary_search(target, data):
    # datas = list(range(1, data + 1))
    start, end = 1, int(data)
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == target:
            return cnt
        elif mid < target:
            start = mid
            cnt += 1
        else:
            end = mid
            cnt += 1


T = int(input())
for test_case in range(1, T+1):
    book, A, B = map(int, input().split())
    resultA = binary_search(A, book)
    resultB = binary_search(B, book)
    if resultA > resultB:
        print(f'#{test_case} B')
    elif resultA < resultB:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')
