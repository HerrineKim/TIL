# 09 큐, 덱(queue, deque)

## 09-1 큐 Queue

![img](09%20%ED%81%90,%20%EB%8D%B1(queue,%20deque).assets/images%252Fnnnyeong%252Fpost%252F3244e9fd-82e5-4c52-bef4-dee97640e246%252Fimage.png)

한쪽에서만 데이터의 삽입 삭제가 이루어졌던 스택과 달리 **큐는 양쪽 끝에서 데이터의 삽입과 삭제가 각각 이루어진다.** `FIFO (First In First Out)` 으로 동작하며 데이터가 삽입되는 곳을 `rear`, 데이터가 제거되는 곳을 `front` 라 한다. 데이터를 삭제하기 전에는 큐가 `empty` 한지, 큐에 데이터를 추가하려 할 때는 큐가 `full` 인지 확인 후 진행해야 한다.



### 선형 큐 Linear Queue

![img](09%20%ED%81%90,%20%EB%8D%B1(queue,%20deque).assets/images%252Fnnnyeong%252Fpost%252Fd185914f-c33a-4d02-8a92-1a4720635ce0%252Fimage.png)

- 선형 배열을 사용하여 구현된 큐
- 삽입을 위해서는 계속해서 요소들을 이동시켜야 함
- `front`, `rear` 는 증가만 하는 방식, 실제로는 `front` 앞쪽에 공간이 있더라도 삽입할 수 없는 경우가 발생할 수 있음



#### 소스코드

```python
>>> queue = [4, 5, 6]
>>> queue.append(7)
>>> queue.append(8)
>>> queue
[4, 5, 6, 7, 8]
>>> queue.pop(0)
4
>>> queue.pop(0)
5
>>> queue
[6, 7, 8]
```





### 원형 큐 Circular Queue

![img](09%20%ED%81%90,%20%EB%8D%B1(queue,%20deque).assets/images%252Fnnnyeong%252Fpost%252Ff439a687-709e-40cf-90c9-55206e834652%252Fimage.png)

- 선형 큐의 단점을 보완
- `front` = 맨 첫번째 요소 바로 앞을 가리킴
- `rear` = 마지막 요소 가리킴
- 큐 empty 상태 : `front == rear`
- 큐 full 상태 : `front == (rear+1) % MAX_QUEUE_SIZE`
- 공백 상태와 포화 상태를 구분하기 위해 하나의공간을 비워둠



### 시간 복잡도

큐 역시 `front`, `rear` 의 위치로 데이터 삽입 삭제가 바로 이루어지기 때문에 원소 삽입, 삭제의 시간 복잡도는 **O(1)** 이다.



### 장단점

- 데이터 접근, 삽입, 삭제가 빠르다.
- 큐 역시 스택과 마찬가지로 중간에 위치한 데이터에 대한 접근이 불가능하다.



### 활용

- 데이터를 입력된 순서대로 처리해야 할 때
- BFS 알고리즘
- 프로세스 관리
- 대기 순서 관리





## 09-2 덱 Deque

![img](09%20%ED%81%90,%20%EB%8D%B1(queue,%20deque).assets/images%252Fnnnyeong%252Fpost%252Fc412c1f6-9cf2-4fe2-b1c6-b166e2a58c99%252Fimage.png)

Deque 는 **Double - Ended Queue** 의 줄임말이다. 한쪽에서만 삽입, 다른 한쪽에서만 삭제가 가능했던 큐와 달리 양쪽 `front`, `rear` 에서 삽입 삭제가 모두 가능한 큐를 의미하는 자료구조이다.

연속적인 메모리를 기반으로 하는 시퀀스 컨테이너이고 선언 이후 크기를 줄이거나 늘릴 수 있는 가변적 크기를 갖는다. 또한 중간에 데이터가 삽입될 때 다른 요소들을 앞, 뒤로 밀 수 있다.



### 시간 복잡도

삽입 삭제 연산은 마찬가지로 **O(1)** 의 시간 복잡도를 가지고, 스택/큐와 달리 index 를 통해 요소들에 탐색이 가능하므로 이 역시 **O(1)** 의 시간 복잡도를 가진다.



### 장단점

- 데이터의 삽입 삭제가 빠르고 앞, 뒤에서 삽입 삭제가 모두 가능하다
- 가변적 크기
- index 를 통해 임의의 원소에 바로 접근이 가능하고
- 새로운 원소 삽입 시, 메모리를 재할당하고 복사하지 않고 새로운 단위의 메모리 블록을 할당하여 삽입한다.
- 중간에서의 삽입 삭제가 어렵고
- 스택, 큐에 비해 비교적 구현이 어렵다.



### 활용

- 데이터를 앞, 뒤쪽에서 모두 삽입 삭제하는 과정이 필요한 경우
- 데이터의 크기가 가변적일 때



### 소스코드

```python
from collections import deque

d = deque()
print(type(d)) # <class 'collections.deque'>


# 스택이나 큐처럼 덱의 오른쪽에서 요소 삽입 : append
for i in range(10):
    d.append(i)
print(d) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# 덱의 왼쪽에서 요소 삽입 : appendleft
d.appendleft(10)
print(d) # deque([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# 덱 중간에 요소 삽입 : insert
d.insert(5, 11)
print(d) # deque([10, 0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9])


# 덱 왼쪽/오른쪽에 iterable한 객체를 통째로 append 하여 연장시키는 연산 : extendleft / extend
d.extend([0, 0, 0])
print(d) # deque([10, 0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9, 0, 0, 0])
d.extendleft([0, 0, 0])
print(d) # deque([0, 0, 0, 10, 0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9, 0, 0, 0])


# 스택처럼 덱의 오른쪽에서 요소 삭제 : pop
for i in range(10):
    d.pop()
print(d) # deque([0, 0, 0, 10, 0, 1, 2, 3])


# 큐처럼 덱의 왼쪽에서 요소 삭제 : popleft
for i in range(3):
    d.popleft()
print(d) # deque([10, 0, 1, 2, 3])


# 작업을 완료한 후에는 일반적인 리스트처럼 이용할 수도 있다
print(list(d)) # [10, 0, 1, 2, 3]
```

