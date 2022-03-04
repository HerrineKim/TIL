def binary_search(target, data):
    datali = list(range(1, data+1))
    length = len(datali)
    left = 1
    right = length
    count = 0

    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return count
            break
        elif mid < target:
            left = mid
            count += 1
        else:
            right = mid
            count += 1

T = int(input())
for test_case in range(1, T+1):
    book, A, B = map(int, input().split())
    Ali = int(binary_search(A, book))
    Bli = int(binary_search(B, book))
    if Ali > Bli:
        print(f'#{test_case} B')
    if Ali < Bli:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')
