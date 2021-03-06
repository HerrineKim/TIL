"""
몬스터를 사냥하는 헌터가 있다. 헌터는 상하좌우로 움직이고 몬스터를 사냥한다.

헌터는 몬스터를 처리하고 몬스터를 없애줄 것을 요청한 고객이 몬스터가 처리된 것을 확인하면 작업이 완료된다.



몬스터를 처리하는 순서는 상관이 없다. 고객들에게 확인시켜 주는 순서도 상관이 없다.

몬스터를 처리했다고 해서 바로 그 몬스터를 처리해 달라고 요청한 고객에게 돌아가 확인할 필요도 없다.



헌터는 1시간에 한 칸씩 상하좌우로 움직인다.



몬스터를 처리하기 위해서는 헌터는 몬스터가 있는 위치로 가면 된다.

헌터가 실력이 좋아서 몬스터를 처리하는 데 걸리는 시간은 없다.



고객에게 몬스터를 처리한 것을 확인시켜 주기 위해서 고객이 있는 위치로 가면 된다.

고객이 확인하는 데 걸리는 시간은 없다.
[그림-3]의 경우가 주어진 예에서 가장 빨리 모든 작업을 완료할 수 있는 경우이다.



이와 같이 몬스터의 위치와 고객의 위치가 주어졌을 때,

모든 몬스터를 없애고 고객들에게 확인시켜 작업을 완료하는 데 가장 빠른 시간을 구하는 프로그램을 작성해라.



헌터는 처음 (1, 1)부터 시작하고, 몬스터와 고객의 위치가 서로 같은 경우는 없다.

몬스터와 고객의 위치는 (1, 1)로 주어질 수 있다.



[제약 사항]

1. 몬스터의 위치와 고객의 위치는 한 변의 길이 N이 3 이상 10 이하인 정사각형의 맵으로 주어진다. (3≤N≤10)

2. 고객 및 몬스터 개수 M은 1 이상 4 이하이다. (1≤M≤4)

3. 고객 및 몬스터는 1부터 M까지 번호가 부여되어 있다.

4. 고객의 번호는 처리해 달라는 몬스터의 번호이다.

5. 맵에서 몬스터는 양수로 주어지고 고객은 음수로 주어진다.

   그 수의 절대값은 몬스터의 번호 및 고객의 번호를 의미한다. 0인 경우는 아무것도 없는 경우이다.

6. 몬스터와 고객이 같은 위치를 가지는 경우는 없다.

7. 헌터는 상하좌우로 1시간에 한 칸씩 움직일 수 있다.

8. 헌터는 맵의 맨 왼쪽 위인 (1, 1)부터 시작한다.



[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다 (1≤T≤50)

그 다음 줄부터 테스트 케이스 T개 온다. 각 테스트 케이스는 모두 N + 1 줄로 구성되어 있다.

첫 줄은 맵의 한 변의 길이 N이 주어진다.

그 다음 N 줄에는 N*N 맵의 정보가 주어진다. 맵에서 양수는 몬스터, 음수는 고객을 뜻한다.
5

3

0 0 0

0 1 -1

0 0 0

4

-3 -1 1 0

-2 0 0 3

0 0 0 0

0 0 2 0

5

0 0 -3 0 0

0 0 0 3 0

0 0 0 0 2

0 0 1 0 0

-1 0 0 -2 0
#1 3

#2 13

#3 18

#4 22

#5 22


...

"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j]