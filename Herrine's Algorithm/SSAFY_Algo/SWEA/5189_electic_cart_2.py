import sys
sys.stdin = open("input.txt")

T = int(input())

# 기본적인 원리는 다음과같다.
# y=0 즉 문제에서는 1열에서 출발하여서 임의의 x값들을 중복되지 않게 모두 바꾼다음
# 마지막 사무실로 돌아오는것 즉, x = 0 이 되는 조건으로 하였다.
# y값은 다음에는 x값이 되는 이어지는 원리이다.

# 배터리가 소모되는 함수
# 각각의 횟수랑 y의값 total 값을 받는다.
def battery(cnt, y, total):
    global result
    # 종료조건으로 만약 N회차이면 마지막 사무실에 돌아와야 하므로
    if cnt == N:
        # 마지막 사무실에 돌아오는 소모량 더해주고
        total += arr[y][0]
        # 총합이 기존의 결과값보다 작다면 갱신해주고 종료한다.
        if total < result:
            result = total
            return
    # 만약 실행 도중에 total 보다 커진다면 그냥 바로 종료한다.
    if total > result:
        return
    # 마지막 사무실에 돌아오는 것을 남겨두고 돌아보자
    for i in range(1, N):
        # 만약 구역에 도착했다면 ( n,n ) 이라면 0이므로 건너뛰기
        if not arr[y][i]:
            continue
        # 만약 방문한 적이 없다면
        if not visited[i]:
            # 방문체크 해주고
            visited[i] = 1
            # 다음 회차로 넘어가고 x값으로 들어오는 값을 y로 넘겨준다.
            battery(cnt+1, i, total + arr[y][i])
            # 방문해제
            visited[i] = 0



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    # 100이 최대라고 해서 최대값 다음과 같이 함
    result = 100 * N
    # 1회차 부터 시작한다.
    battery(1, 0, 0)

    print("#{} {}".format(tc, result))
