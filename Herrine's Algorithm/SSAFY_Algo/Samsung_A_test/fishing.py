"""
강가를 따라서 낚시터 자리가 1~N까지 일렬로 늘어서 있다. 낚시터에는 3개의 출입구가 있으며,
각 출입구에는 낚시터에 입장하기 위해 대기하고 있는 낚시꾼들이 각각 존재한다.
모든 낚시꾼들은 한 사람당 하나의 낚시터에 자리를 잡아야 하며, 자리를 잡는 절차는 다음과 같다.

1. 혼잡을 피하기 위해 하나의 출입구씩 선택하여 순차적으로 입장 할 수 있다.
2. 출입구가 선택되면, 해당 출입구에 대기하고 있는 낚시꾼들은 자신의 위치에서 가장 가까운 빈 낚시터 자리로 한 명씩 이동하여 차례대로 자리를 잡는다.
  - 출입구에서 바로 위쪽의 낚시터까지의 거리는 1m 이며, 좌우로 한 칸씩 멀어질 때 마다 추가로 1m씩 멀어진다.
  - 예를 들어 [Fig. 1]의 Gate1에서 4번 자리까지는 1m 이고, 3번과 5번자리는 2m의 거리가 된다.
3. 해당 출입구의 맨 마지막 사람의 경우, 가장 가까운 빈 자리가 두 곳이라면 하나를 선택해야 한다.
   (맨 마지막 사람이 아닌 경우, 두 곳 중 아무데나 가도 결과는 같으므로 고려할 필요가 없다.)
4. 해당 출입구에 대기중인 모든 낚시꾼들의 자리잡기가 완료되면, 다음 출입구를 선택하여 위 1~3 과정을 반복 수행한다.

낚시터 자리의 개수 N이 주어지고, 출입구 3개의 위치 및 해당 출입구에 대기중인 각각의 낚시꾼들의 숫자가 주어진다.
이때 위의 낚시터 자리잡기 절차를 수행하면서 낚시꾼들 각각의 이동거리를 모두 더한 값이 최소가 되도록 자리잡는 방법을 찾고, 그때의 이동거리의 합을 출력하라.
5
10
4 5
6 2
10 2
10
8 5
9 1
10 2

#1 18
#2 25
#3 57
#4 86
#5 339
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 낚시터
    NLi = [0] * (N + 1)
    G1, M1 = map(int, input().split())
    G2, M2 = map(int, input().split())
    G3, M3 = map(int, input().split())
    GM1 = list(map(int, input().split()))
    GM2 = list(map(int, input().split()))
    GM3 = list(map(int, input().split()))
    GMs = [GM1, GM2, GM3]

    MLi = [GM1[1], GM2[1], GM3[1]]
    # The first process
    maxM = max(MLi)  # largest fisherman num / 5
    Idx = MLi.index(maxM)  # 0
    maxIdx = GMs[Idx][0]  # largest fishers' gate num / 4

    ans = 0  # answer
    # input largest fishers' possible range
    # num1
    if Idx == 0:
        start = 1
        end = N - M2 - M3
    elif Idx == 1:
        start = 1 + M1
        end = N - M3
    else:
        start = 1 + M1 + M3
        end = N
    if maxIdx - start >= end - maxIdx:
        for i in range(, end)

    else:

    # Middle Process

    # The Last Process