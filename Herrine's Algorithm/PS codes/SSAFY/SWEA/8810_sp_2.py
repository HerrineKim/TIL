# 8810_sweetpotato_2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]
    SPLi = []
    cnt = 0
    SP = 0  # 고구마의 개수
    for i in range(N):  # 밭의 개수만큼 반복
        if arr[i] < arr[i+1]:  # 만약 조건을 만족하면
            SP += arr[i]  # 고구마 개수를 더해줌
            cnt += 1
        else:
