# 5208. 전기버스2
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    battery = [0] + arr[1:]
    station = [0] * N  # 누적해서 도달 가능 지점을 계산
    for i in range(N):
        station[i] = i + battery[i]

    cnt = 0
    idx = 1
    end = N
    while end > 1:  # 역순으로 카운팅
        if station[idx] >= end:  # 이 충전소에서 충전했을 때 목표 도달 가능하면
            cnt += 1  # 충전 고고
            end = idx  # 이 충전소로 엔드 수정
            idx = 1  # 충전소 처음부터 검색
        else:  # 목표 도달 안했으면
            idx += 1  # 인덱스만 + 1
    print(f'#{test_case} {cnt-1}')
