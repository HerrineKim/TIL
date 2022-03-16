# 남학생 1: 자신의 번호가 스위치 약수이면 스위치 상태 바꿈
# 여학생 2: 자신이 받은 번호의 스위치 기준 좌우 대칭인 부분 & 자신 상태 바꿈

N = int(input())  # 스위치 개수
arr = list(map(int, input().split()))  # 스위치 상태
S = int(input())  # 학생 수
for _ in range(S):
    s, n = map(int, input().split())
    # 1. 남학생
    if s == 1:
        for i in range(n - 1, N, n):
            if arr[i]:
                arr[i] = 0
            else:
                arr[i] = 1
    else:
        # 2. 여학생
        n -= 1
        left = right = n
        while left >= 0 and right < N:
            if arr[left] == arr[right]:
                if arr[left]:
                    arr[left] = 0
                    arr[right] = 0
                else:
                    arr[left] = 1
                    arr[right] = 1
            else:
                break
            left -= 1
            right += 1

if N <= 20:
    print(*arr)
else:
    for i in range(len(arr)):
        print(arr[i], end=" ")
        if i+1 >= 20 and (i+1)%20 == 0:
            print()
