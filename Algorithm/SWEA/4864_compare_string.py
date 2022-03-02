def Gojisik(search, arr):  # 고지식한 검색법 함수 구현
    i = 0  # arr의 인덱스
    j = 0  # search의 인덱스
    n = len(arr)
    m = len(search)
    while j < m and i < n:  # 각 인덱스가 길이보다 짧은 동안
        if arr[i] != search[j]:  # 만약에 다른 경우
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == m:
        return 1
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    longstr = input()
    targetstr = input()
    result = Gojisik(longstr, targetstr)
    print(f'#{test_case} {result}')