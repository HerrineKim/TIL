def f(i, N):
    if i == N:  # 모든 원소에 대해 고려한 경우
        s = 0
        cnt = 0
        for j in range(N):
            if bit[j] == 1:
                cnt += 1
                s += arr[j]
        if s == 0 and cnt > 0:  # 공집합 제외
            for j in range(N):
                if bit[j] == 1:
                    print(arr[j], end=' ')
            print()
    else:
        bit[i] = 0
        f(i+1, N)
        bit[i] = 1
        f(i+1, N)
    return

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)

bit = [0]*N
f(0, N)

# 바이너리카운팅
for i in range(1, 1 << N):  # 1 ~ 2**N-1, 공집합 제외, N개의 비트가 구분되는 숫자 범위
    s = 0  # i가 나타내는 부분집합의 합 초기화
    for j in range(N):  # 0 ~ N - 1 비트까지
        if i & (1 << j):  # j번 비트가 1이면 부분집합에 포함
            s += arr[j]  # 부분집합에 포함
    if s == 0:  # 원소의 합이 0인 부분집합인 경우
        for j in range(N):  # 0 ~ N-1 번 비트까지
            if i & (1 << j):  # j번 비트가 1이면 부분집합에 포함
                print(arr[j], end=' ')
        print()  # 한 줄에 한 부분집합의 원소 출력
