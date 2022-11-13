# 14 힙(Heap), 우선순위 큐

### ✔우선순위 큐란?

큐나 스택과 비슷한 자료형이지만, 각 원소들은 우선순위를 가지고 있다. 우선순위 큐에서, 높은 우선순위를 가진 원소는 낮은 우선순위를 가진 원소보다 먼저 처리된다. 같은 우선순위를 가진다면, 먼저 들어온 원소를 처리한다. 우선순위 큐는 힙(heap)이라는 자료 구조를 통해 구현할 수 있다.

우선순위 큐는 최소한 두 가지 연산이 지원되어야 한다.

1. 하나의 원소를 우선순위를 지정하여 추가하는 함수(push)
2. 가장 높은 우선순위를 가진 원소를 큐에서 제거하고 반환하는 함수(pop)



#### 힙(Heap)이란?

> 완전 이진 트리(Complete Binary Tree)로, 부모 노드의 값이 항상 자식 노드들의 값보다 크거나(Max Heap), 작아야(Min Heap) 한다. 힙은 우선순위 큐를 구현하거나, 힙 정렬을 하는 데 사용된다. 루트 노드에 있는 값이 최대값, 혹은 최소값이며, 자식 노드들의 값의 위치는 기본적인 조건만 맞추면 된다.



##### Max Heap, Min Heap

https://chanhuiseok.github.io/posts/ds-4/ 사진 참조

![img](14%20%ED%9E%99(Heap),%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90.assets/oP565GF.png)

![img](14%20%ED%9E%99(Heap),%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90.assets/lvXIQ8L.png)



### ✔우선순위 큐의 Push

- 맨 끝 위치에 값을 저장
- 부모 노드와 비교하며, 조건을 만족하는 지 확인
  - 만족하지 않는다면, 서로 위치를 변경

https://chanhuiseok.github.io/posts/ds-4/ 사진 참조

![img](14%20%ED%9E%99(Heap),%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90.assets/VeuoJbK.png)



### ✔우선순위 큐의 Pop

- 가장 우선순위가 높은 값을 삭제
- 맨 끝의 노드를 비어있는 루트 노드로 끌어옴
- 루트 노드의 자식 노드들과 값을 비교, 위치 변경
  - 위치를 만족할 때까지 자식 노드와 위치를 변경하며 올바른 위치까지 이동

https://chanhuiseok.github.io/posts/ds-4/ 사진 참조

![img](14%20%ED%9E%99(Heap),%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90.assets/6dimHpq.png)





## 📌파이썬에서의 우선순위 큐

파이썬에서는 우선순위 큐의 활용을 위해, 모듈을 제공하고 있다.



### PriorityQueue

```python
from queue import PriorityQueue

q = PriorityQueue() 
q1 = PriorityQueue(maxsize=10) # maxsize를 활용하면 크기 제한 가능
```



#### put

- `.put(item)`

```python
q.put(3) # 원소를 넣는 과정
q.put(4)
q.put(1)

q1.put((1, 'apple')) # (우선순위, 값)의 형태로 저장할 수도 있음
```



#### get

- `.get()`

```python
# 원소 삭제 및 반환
q.get() # 1
q1.get()[1] # (우선순위, 값)의 형태에서 값 반환
```





## Heapq

자세한 내용은 https://docs.python.org/ko/3/library/heapq.html 참조

- 최소 힙(Min Heap)의 구조
- 모든 k에 대해 `heap[k] <= heap[2*k+1]` 또는 `heap[k] <= heap[2*k+2]` 만족
- 가장 작은 요소가 `heap[0]`에 위치
- 힙을 만들기 위해서는, 초기화된 리스트 `[]`를 사용하거나, `heapify`를 통해 값이 들어있는 리스트를 힙으로 변환 가능

```python
import heapq

hq = []
```



#### push

- `heapq.heappush(heap, item)`
- 힙의 형태를 유지하면서 item을 push

```python
heapq.heappush(hq, 4)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)
```



#### pop

- `heapq.heappop(heap)`
- 힙의 형태를 유지하면서 가장 작은 항목을 pop, 반환
- 비어있으면 IndexError 발생
- 반환하지 않고 접근하고 싶다면, `heap[0]` 활용

```python
heapq.heappop(hq) # 1
```



#### heapify

- `heapify(x)`
- 리스트 x를 선형 시간으로 제자리에서 heap으로 변환

```python
x = [4, 3, 1, 2, 5, 6]
print(x) # [4, 3, 1, 2, 5, 6]
heapq.heapify(x)
print(x) # [1, 2, 4, 3, 5, 6]
```