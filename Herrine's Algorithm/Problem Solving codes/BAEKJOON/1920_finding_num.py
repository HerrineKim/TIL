def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 원하는 값 찾은 경우 인덱스 반환
        if array[mid] == target:
            return True
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1


N = int(input())
target_list = list(map(int, input().split()))
target_list.sort()
M = int(input())
num_list = list(map(int, input().split()))

for i in range(M):
    result = binary_search(target_list, num_list[i], 0, N - 1)
    if result:
        print(1)
    else:
        print(0)