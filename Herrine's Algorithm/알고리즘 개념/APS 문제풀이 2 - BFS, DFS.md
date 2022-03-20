# APS 문제풀이 2

> 2022년 3월 18일 금요일 수업

<br>

## [SWEA] 5105. 미로의 거리

> 미로/경로 찾기의 전형적인 템플릿. BFS
>
> BFS: 한 단계씩 발전 -> 최단거리, 영역/조건 탐색



NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 **5개의 칸**을 지나 도착할 수 있다.
(**칸 수를 꼭 직접 세어보세요**)


**[입력]**

첫 줄에 테스트 케이스 개수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

**[출력]**

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

```python
def bfs(si, sj, ei, ej):
    q = []  
    visited = [[0] * N for _ in range(N)]

    q.append(([si, sj]))  # Q에 초기데이터들 삽입, 방문표시
    visited[si][sj] = 1  # 출발점에 방문 표시

    while q:
        ci, cj = q.pop(0)  # 큐에서 출발점을 pop
        if ci == ei and cj == ej:  # 만약 방문한 곳이 끝 점과 같다면 종료
            return visited[ci][cj] - 2 # 현재 visited 값에서 시작점과 종료 지점을 뺀 값 return
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):  # 사방탐색
            ni, nj = ci + di, cj + dj
            # 만약 계속 탐색해나갈 수 있는 지점이라면 큐에 append
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] and MAP[ni][nj] != '1':
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1  # append 한 후에는 지나온 거리 + 1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '2':  # 출발 지점 찾기
                si, sj = i, j
            elif MAP[i][j] == '3':  # 도착 지점 찾기
                ei, ej = i, j

    sol = bfs(si, sj, ei, ej)  # 최소 칸 수를 return 해주는 bfs 함수
    print(f'#{test_case} {sol}')
```

<br>

## [SWEA] 1238. Contact

> BFS

비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.
 
**[예시]**

아래는 비상연락망을 나타낸 그림이다.
 

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV2XakJaDe8BBASl)

 
각 원은 개개인을 의미하며, 원 안의 숫자는 그사람의 번호를 나타내고 빨간원은 연락을 시작하는 당번을 의미한다.

화살표는 연락이 가능한 방향을 의미한다.

위의 예시에서는 7번과 1번은 서로 연락이 가능하다,

하지만 2번과 7번의 경우 2번은 7번에게 연락할 수 있지만 7번은 2번에게 연락할 수 없다.
 
비상연락망이 가동되면 아래 그림과 같이 연락을 시작하는 당번인 2번은 연락 가능한 7번과 15번에 동시에 연락을 취한다 (다자 간 통화를 사용한다고 가정).
 

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV2Xan_6DfABBASl)

 
그 다음 아래와 같이 7번은 1번에게, 15번은 4번에게 연락을 취한다 (이 과정은 동시에 일어난다고 가정한다).
 

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV2Xat3qDfEBBASl)


그 다음 아래와 같이 1번은 8번과 17번에게 동시에 연락하며, 이와 동시에 4번은 10번에게 연락한다.

7번과 2번의 경우는 이미 연락을 받은 상태이기 때문에 다시 연락하지 않는다.
 

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV2XaywKDfIBBASl)


위의 모습이 연락이 끝난 마지막 모습이 되며, 마지막에 동시에 연락 받은 사람은 8번, 10번, 17번의 세 명이다.

이 중에서 가장 숫자가 큰 사람은 17번이므로 17을 반환하면 된다.
 
※ 3, 6, 11, 22번은 시간이 지나도 연락을 받지 못한다.
 
**[제약 사항]**

연락 인원은 최대 100명이며, 부여될 수 있는 번호는 1이상, 100이하이다.

단, 예시에서 5번이 존재하지 않듯이 중간 중간에 비어있는 번호가 있을 수 있다.

한 명의 사람이 다수의 사람에게 연락이 가능한 경우 항상 다자 간 통화를 통해 동시에 전달한다.

연락이 퍼지는 속도는 항상 일정하다 (전화를 받은 사람이 다음사람에게 전화를 거는 속도는 동일).

비상연락망 정보는 사전에 공유되며 한 번 연락을 받은 사람에게 다시 연락을 하는 일은 없다.

예시에서의 3, 6, 11, 22번과 같이 연락을 받을 수 없는 사람도 존재할 수 있다.
 
**[입력]**

입력의 첫 번째 줄에는 입력 받는 데이터의 길이와 시작점이 주어진다.

그 다음 줄에 입력받는 데이터는 {from, to, from, to, …} 의 순서로 해석되며 예시의 경우는 {2, 7, 11, 6, 6, 2, 2, 15, 15, 4, 4, 2, 4, 10, 7, 1, 1, 7, 1, 8, 1, 17, 3, 22}와 같다.

그런데 순서에는 상관이 없으므로 다음과 같이 주어진 인풋도 동일한 비상연락망을 나타낸다 (같은 비상연락망을 표현하는 다양한 인풋이 존재 가능하다).

{1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 4, 2}

다음과 같이 동일한 {from, to}쌍이 여러 번 반복되는 경우도 있으며, 한 번 기록된 경우와 여러 번 기록된 경우의 차이는 없다.

{1, 17, 1, 17, 1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 11, 6, 4, 2}

**[출력]**

\#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

```python
def BFS(s):
    q = []
    v = [0]*101

    q.append(s)
    v[s] = 1
    sol = s

    while q:
        c = q.pop(0)
        # 정답처리
        # 가장 나중에 연락 받는 사람
        if v[sol] < v[c] or v[sol] == v[c] and sol < c:  # v 값이 가장 크거나, 같다면 번호 큰
            sol = c
        for j in range(1, 101):
            if adj[c][j] and v[j] == 0:  # 만약 c 지점과 연결되어 있고, 방문한 적이 없다면
                q.append(j)  # 계속 뻗어나갈 수 있는 지점이므로 큐에 append
                v[j] = v[c] + 1  # 하나 더 뻗어 나가기 위해 + 1
    return sol


T = 10
for test_case in range(1, T + 1):
    N, S = map(int, input().split())  # N 입력받는 데이터의 길이 S 시작 지점
    lst = list(map(int, input().split()))  # from, to, from to...
    # 데이터를 2차원 배열로 저장
    adj = [[0]*101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1  ## from to
    ans = BFS(S)  # 가장 나중에 연락 받을 사람을 return하는 함수
    print(f'#{test_case} {ans}')
```

<br>

## [SWEA] 1861. 정사각형 방

N2개의 방이 N×N형태로 늘어서 있다.

위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.

물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.


**[입력]**

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.

다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.

Ai, j는 모두 서로 다른 수이다.


**[출력]**

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.

이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


**[예제 풀이]**

첫 번째 테스트 케이스는 1 또는 3이 적힌 곳에 있어야 한다.

두 번째 테스트 케이스는 3 또는 6이 적힌 곳에 있어야 한다.

```python
def BFS(si, sj):
    q = []
    s = []

    q.append((si, sj))
    v[si][sj] = 1
    s.append(arr[si][sj])  # 방문한 번호 저장

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 사방탐색
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and abs(arr[ci][cj] - arr[ni][nj]) == 1:  # 배열 안에 있고, 차이가 1이라는 조건을 만족하며, 방문한 적 없다면
                q.append((ni, nj))  # 큐에 append
                v[ni][nj] = 1
                s.append(arr[ni][nj])  # 탐색했던 곳 append
    return min(s), len(s)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    num = N * N  # 최소 번호
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:  # 방문 안 한 곳이라면
                tn, tc = BFS(i, j)
                if cnt < tc or cnt == tc and num > tn:  # 갱신
                    cnt = tc
                    num = tn
    print(f'#{test_case} {num} {cnt}')

```

<br>

## 1953. 탈주범 검거

교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.

탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,

지하 터널 어딘가에서 은신 중인 것으로 추정된다.

터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.

탈주범은 시간당 1의 거리를 움직일 수 있다.

지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.

 

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV6Dn6RqAK8DFAU4)

**[표 1]**



[그림 1-1] 은 지하 터널 지도의 한 예를 나타낸다.

이 경우 지도의 세로 크기는 5, 가로 크기는 6 이다.

맨홀 뚜껑의 위치가 ( 2, 1 ) 으로 주어질 경우, 이는 세로 위치 2, 가로 위치 1을 의미하며 [그림 1-2] 에서 붉은 색으로 표기된 구역이다.

탈주범이 탈출 한 시간 뒤 도달할 수 있는 지점은 한 곳이다.

탈주범이 2시간 후 도달할 수 있는 지점은, [그림 1-3] 과 같이 맨홀 뚜껑이 위치한 붉은 색으로 표시된 지하도 와 파란색으로 표기된 지하도까지 총 3개의 장소에 있을 수 있다.

3시간 후에는 [그림 1-4] 과 같이 총 5개의 지점에 있을 수 있다.
    

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5P--laAo4DFAUq)          ![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5P_CI6Ao8DFAUq) 

**[그림 1-1]**                           **[그림 1-2]**

​    

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5P_L0aApADFAUq)          ![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5P_OXqApEDFAUq)

**[그림 1-3]**                           **[그림 1-4]**



[그림 2-1] 에서 맨홀뚜껑이 위치한 지점이 ( 2, 2 ) 이고 경과한 시간이 6 으로 주어질 경우,

[그림 2-2] 에서 맨홀뚜껑이 위치한 지점은 붉은 색, 탈주범이 있을 수 있는 장소가 푸른색으로 표기되어 있다.

탈주범이 있을 수 있는 장소는, 맨홀뚜껑이 위치한 지점을 포함하여 총 15 개 이다.
    

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5P_hjKApUDFAUq)          ![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5P_jr6ApYDFAUq)

**[그림 2-1]**                           **[그림 2-2]**



지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.


**[제약 사항]**

\1. 시간 제한 : 최대 50개 테이트 케이스를 모두 통과하는데, C/C++/Java 모두 1초

\2. 지하 터널 지도의 세로 크기 N, 가로 크기 M은 각각 5 이상 50 이하이다. (5 ≤ N, M ≤ 50)

\3. 맨홀 뚜껑의 세로 위치 R 은 0 이상 N-1이하이고 가로 위치 C 는 0 이상 M-1이하이다. (0 ≤ R ≤ N-1, 0 ≤ C ≤ M-1)

\4. 탈출 후 소요된 시간 L은 1 이상 20 이하이다. (1 ≤ L ≤ 20)

\5. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장된다.

\6. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재한다.

**[입력]**

첫 줄에 총 테스트 케이스의 개수 T가 주어진다.

두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.

각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.

그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.

숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0 은 터널이 없는 장소를 의미한다.

**[출력]**

테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.

각 줄은 “#x”로 시작하고 공백을 하나 둔 다음 정답을 기록한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)

출력해야 할 정답은 탈주범이 위치할 수 있는 장소의 개수이다.

```python
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]  # 파이프 종류
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)  # 사방탐색
opp = [1, 0, 3, 2]  # 반대 방향


def BFS(N, M, si, sj, L):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        if v[ci][cj] == L:  # 종료조건: 도착했을 때
            return cnt

        for k in range(4):  # 사방탐색
            ni, nj = ci + di[k], cj + dj[k]
            # 현 파이프의 이동 방향에 1이 있어야하고, 내가 이동할 파이프의 '반대'(opp) 방향에도 1이 있어야 함
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and \
                    pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # N 세로 M 가로 R 맨홀 x좌표 C 맨홀 y좌표 L 소요 시간
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 배열
    ans = BFS(N, M, R, C, L)  # 특정 시간이 경과한 후 탈주범이 위치할 수 있는 장소의 개수
    print(f'#{test_case} {ans}')

```

<br>

## 1486. 장훈이의 높은 선반

> DFS

장훈이는 서점을 운영하고 있다.

서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에, 선반 위의 물건을 자유롭게 사용할 수 있다.

어느 날 장훈이는 자리를 비웠고, 이 서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.

각 점원의 키는 Hi로 나타나는데, 점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 하였다.

점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.

탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.

탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.


**[입력]**

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N, B(1 ≤ N ≤ 20, 1 ≤ B ≤ S)가 공백으로 구분되어 주어진다.

S는 두 번째 줄에서 주어지는 점원들 키의 합이다.

두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며, 각 정수는 각 점원의 키 Hi (1 ≤ Hi ≤ 10,000)을 나타낸다.


**[출력]**

각 테스트 케이스마다 첫 번째 줄에는 ‘#t’(t는 테스트 케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 만들 수 있는 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 작은 것을 출력한다.


**[예제 풀이]**

테스트 케이스의 경우 키가 3, 3, 5, 6인 점원이 탑을 만들면 높이가 17(3 + 3 + 5 + 6)이 된다.

높이가 16인 탑은 만들 수 없으므로 높이가 17인 탑이 문제에서 구하려는 탑의 높이이다. 따라서 17 – 16 = 1이 답이 된다.

```python
def DFS(n, ssum):
    global ans

    if ssum >= B + ans:
        return

    if n == N:
        if ssum >= B and ans > ssum-B:
            ans = ssum - B
        return

    DFS(n+1, ssum+lst[n])  # 직원 포함하는 경우
    DFS(n+1, ssum)  # 직원포함하지 않는 경우


T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())  # N 점원의 수 B 선반 높이
    lst = list(map(int, input().split()))
    ans = 12345678
    DFS(0, 0)
    print(f'#{test_case} {ans}')
```

