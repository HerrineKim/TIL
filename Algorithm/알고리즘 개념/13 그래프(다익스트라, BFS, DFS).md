# 13 그래프

## 13-1 그래프의 정의

그래프라 하면 일반적으로 '**정점(node)**'과 '**간선(edge)**'으로 이루어진 자료구조를 의미한다.
또한 간선의 방향 유무에 따라서 **단방향 그래프**와 **무방향 그래프**(또는 양방향)로 나뉜다.

![image_6319709181485828897310](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_6319709181485828897310.jpg)



**완전 그래프 (Complete Graph)**

완전 그래프는 각 정점에서 다른 모든 정점을 연결하여 가능한 최대의 간선 수를 가진 그래프다. 정점 n개인 무방향 그래프에서는 최대 간선 수가 n(n-1)/2 이고, 방향 그래프에서는 두 정점에 대하여 방향이 다른 두개의 간선을 연결할 수 있으므로 최대 간선 수는 무방향 그래프의 2개가 되어 n(n-1)이 된다.

![img](https://mblogthumb-phinf.pstatic.net/20120711_42/k97b1114_1342018161757X3KOg_JPEG/%B1%D7%B7%A1%C7%C1_-_%B9%AB%B9%E6%C7%E2_%B1%D7%B7%A1%C7%C1.JPG?type=w2)

위의 그래프는 정점이 4개 이므로, 간선수는 6개가 된다. 

 

**부분 그래프 (SubGraph)**

원래의 그래프에서 일부의 정점이나 간선을 제외하여 만든 그래프이다.

 

![img](https://mblogthumb-phinf.pstatic.net/20120716_282/k97b1114_1342370458973bEA46_JPEG/%B1%D7%B7%A1%C7%C1_-_%BA%CE%BA%D0_%B1%D7%B7%A1%C7%C1.JPG?type=w2)

G2는 G1의 부분 그래프이다.

 

**가중 그래프 (Weight Graph)**

정점을 연결하는 간선에 가중치(Weight)를 할당한 그래프이다. 네트워크(Network)라고도 한다.

 

![img](https://mblogthumb-phinf.pstatic.net/20120716_89/k97b1114_1342368519055Py1DQ_JPEG/%B1%D7%B7%A1%C7%C1_-_%B0%A1%C1%DF_%B1%D7%B7%A1%C7%C1.JPG?type=w2)



## 13-2 그래프의 표현 - 간선의 정보를 저장하는 방식

그래프를 표현하는 방식은 크게 **인접 행렬** 그래프와 **인접 리스트** 그래프의 두가지로 나눌 수 있다.
일반적으로는 인접행렬 방식을 많이 사용하며, 경우에 따라 인접리스트 방식을 사용한다.



### 1. 인접 행렬 그래프 - "모든 정보를 저장"

- 장점: **직관적**이며 **쉽게 구현** 가능
- 단점: **불필요한 정보의 저장**이 많으며, 노드의 개수가 간선의 개수보다 많으면 많을 수록 탐색 시간이 너무 많이 걸린다. **그래프의 크기가 커지면 메모리 초과가 발생**할 수 있음
- 구현: **int형의 2차원 배열**을 주로 이용하며, **이동할 수 있으면 1**, **없으면 0**으로 표기함

![image_5867957401485829917305](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_5867957401485829917305.jpg)



### 2. 인접 리스트 그래프 - "갈 수 있는 곳만 저장"

- 장점: **필요한 정보만 저장하여 메모리 절약** 가능
- 단점: **인접행렬에 비해 다소 어려움**
- 구현: **리스트(List)**나 **벡터(Vector)등의 자료구조를 이용**하여 **각 정점에서 이동가능한 정점들을 저장(List나 Vector를 이용한 2차원 배열이라 생각하면 이해하기 쉬움)**

![image_3029405931485831316448](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_3029405931485831316448.jpg)

![image_1713515921485831634971](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_1713515921485831634971.jpg)



## 13-3 그래프의 탐색

### 1. 그래프의 탐색 기법

그래프의 탐색 기법은 크게 4가지로 나눌 수 있으며 각 상황에 맞춰 사용된다.

![image_3379353481485840610900](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_3379353481485840610900.jpg)



#### 1-1. BFS 탐색

![image_3850977491485838880343](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_3850977491485838880343.jpg)



**BFS(Breadth First Search; 너비 우선 탐색)**는 **현재 정점과 연결된 정점들에 대해 우선적으로 넓게 탐색**하는 방식이다.

**큐**(Queue)**를 이용해서 구현하며, 아래로 깊은 그래프에 대해선 좋은 성능을 기대할 수 있으나, 옆으로 넓은 그래프에서는 탐색시간이 오래 걸린다.**

예를들어 A 정점에서 H정점을 방문하려 할 때, DFS를 사용하면 한번에 방문이 가능하나, BFS로는 8번만에 방문이 가능하다.

위의 그래프는 완전 이진 트리인데 BFS는 트리 탐색에서 Level Order(레벨 순회)와 동일하다.



### BFS 소스코드 예제 (Python)

```python
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

실행 결과

```python
1 2 3 8 7 4 5 6
```



#### 1-2. DFS 탐색

![image](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image.png)

**DFS(Depth First Search; 깊이 우선 탐색)**는 **현재 정점에서 연결된 정점을 하나 골라 파고들수 있는 최대한 깊게 파고 들어가며 탐색**하는 방법이다.

쉽게 생각해서 **"갈 수 있는 길을 찾아 쭉 내려감 -> 더 이상 못가면 1번 되돌아 간 뒤 -> 또 갈 수 있는 길을 찾아 쭉 내려감 -> ... "** 을 반복한다고 보면 된다. 이 원리를 응용한 알고리즘이 '**백 트래킹**(역추적)'이다.

**스택(Stack)**을 이용해서 구현하며, 직접 스택을 구현해도 되고, **시스템 스택(****재귀 호출)**을 사용할 수도 있다.
옆으로 넓은 그래프에 대해서 준수한 성능을 보이나 아래로 깊은 그래프의 경우 좋은 성능을 기대하기는 힘들다.** 예를 들어 C 정점을 방문하려 할 때, BFS에선 3번만에 방문할 수 있으나, DFS로는 12번만에 방문이 가능하다.

트리에서 DFS는 Inorder(중위 순회)와 동일하다.



### DFS 소스코드 예제 (Python)

```python
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

실행 결과

```python
1 2 7 6 8 3 4 5
```



#### 1-3. 다익스트라(Djikstra)

![image_6359776771485841053989](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_6359776771485841053989.jpg)

**다익스트(Dijkstra)**라 알고리즘은 **BFS의 응용**으로 "**어느 한 정점에서 모든 정점까지의 최단 경로**"를 찾는데 사용되며, **매 탐색마다 해당 정점까지의 가중치의 합을 최소값으로 갱신**시켜나가는 방식이다.

일반적으로 **큐 대신 최소 힙(PriorityQueue; 우선순위 큐)을 사용하여 시간을 단축**시킨다. (일반적으로 **거의 모든 경우에 최소 힙을 사용**한다.) **단, **음이 아닌 가중치에 대해서만 사용이 가능하다는 점에 유의해야 한다.



```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```



### 2. 그래프의 탐색 유형

![image_4888565491485842708240](13%20%EA%B7%B8%EB%9E%98%ED%94%84(%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC,%20BFS,%20DFS).assets/image_4888565491485842708240.jpg)

그래프의 탐색 유형은 크게 미로 탐색 유형과 정점 이동 유형의 2가지로 나눌 수 있다.

**미로 탐색 유형**은 주로 **현재 좌표에서 상, 하, 좌, 우 로 이동(x, y 값을 가감)하면서 길을 찾아**나가는 방식이다. 주로 **인접행렬 형태로 그래프**가 주어지며, 해당 행렬을 가지고 우측과 같은 그래프를 그릴 수 없는 경우가 대부분이다. **행렬을 그래프 표기로 이해하려기 보다는 지도나 그림 자체로 바라보는 것이 편하다.**

반면 **정점 탐색 유형**은 **현재 정점에서** **인접 정점으로 갈 수 있는지에 대한 정보가 주어**지고, 해당 정보를 바탕으로 **인접 행렬(또는 리스트)을 생성**해서 **연결된 길을 찾아 탐색**해나가는 방식이다. 특정 정점을 방문했는지 여부를 boolean 배열을 이용하여 체크해 나가는 방식으로 주로 탐색한다.

