# 4839. 이진탐색
T = int(input())
for test_case in range(1, T + 1):
    Li = list(map(int, input().split()))
    result = []
    for j in range(2):
        start = 1
        end = Li[0]
        page = Li[j+1]
        count = 0

        while start <= end:
            mid = (start + end) // 2
            if mid == page:
                break
            elif mid < page:
                start = mid
                count += 1
            else:
                end = mid
                count += 1
        result.append(count)

    if result[0] < result[1]:
        print(f'#{test_case} A')
    elif result[0] == result[1]:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} B')
