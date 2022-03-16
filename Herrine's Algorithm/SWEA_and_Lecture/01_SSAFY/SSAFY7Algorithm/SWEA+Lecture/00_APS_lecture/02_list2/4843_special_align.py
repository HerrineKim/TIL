# 4843. 특별한 정렬
def bubble_sort(arr):
    n = len(arr)  # 배열의 크기를 측정
    # 배열의 크기만큼 반복
    for i in range(n):
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, n - i - 1):
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 서로 위치를 변환


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = []
    original = list(map(int, input().split()))
    bubble_sort(original)
    for i in range(len(original)):
        result.append(original[N-1])
        result.append(original[i])
        N = N-1
        if len(result) == 10:
            break
    print(f'#{test_case}', end=' ')
    print(*result)

'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11 
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26 
'''