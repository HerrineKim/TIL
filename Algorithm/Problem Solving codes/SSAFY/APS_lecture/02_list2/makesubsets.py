arr = [1, 2, 3]
for i in range(1 << 3):  # 공집합을 제외한 모든 부분집합 검사
    for j in range(3):  # arr의 모든 원소 루프
        if i & (1 << j):  # i의 j번째 비트 검사, j번째 비트가 1이라면 arr[j] 출력
            print(arr[j], end=' ')  # 출력하면 순서가 바뀜에 유의, 다시 말해서 0번째 비트를 검사하면 3의 위치를 검사하는데 arr[j]는 arr[0]을 말한다. 고로 1이 출력됨.
    print()
# print(1 << 3)
