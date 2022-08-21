# 16 서로소 집합(Disjoint-sets)

## 16-1 서로소 집합이란?

수학에서 서로소 집합이란 공통 원소가 없는 두 집합을 의미한다. 서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조라고 할 수 있다.

서로소 집합 자료구조는 **union과 find** 2개의 연산으로 조작할 수 있다. 그래서 서로소 집합 자료구조는 **union-find** 자료구조라고 불기기도 한다.

 



### Union(합집합) 연산

2개의 원소가 포함된 집합을 하나의 집합을 합치는 연산이다.



### find(찾기) 연산

특정한 원소가 속한 집합이 어떤 집합인지 알려 주는 연산이다.

 

## 16-2 구현 방법

### 서로소 집합 표현 - 트리

- 하나의 집합을 하나의 트리로 표현.
- 루트 노드가 대표자이다.
- 자식 노드는 부모 노드를 가리킨다.



### 서로소 집합 연산

- Make-Set(x)

  - 초기화
  - 유일한 멤버 x를 포함하는 새로운 집합을 생성

- Find-Set(x)

  - 찾기
  - x가 어떤 집합에 속해있는지 찾기

- Union(x, y) 

  - 합치기
  - x와 y를 포함하는 두 집합을 통합하기

  

### 연산 최적화

- Rank를 이용한 Union
  - union-by-rank (union-by-height)
  - 각 노드는 자신을 루트로 하는 서브 트리의 높이를 rank라는 이름으로 저장
  - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
- Path compression
  - find-set 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.
  - find-set은 특정 노드에서 루트까지의 경로를 찾아가면서 노드의 부모 정보를 갱신한다.

 

### 기본적인 서로소 집합 알고리즘의 소스코드

 find 함수는 **경로 압축 기법**을 적용하면 최적화가 가능하여 시간 복잡도를 개선시킬 수 있다. 경로 압축은 find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신하는 기법이다.

 

### 서로소 집합 자료구조: 경로 압축 (Python)

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

 

### 

## 서로소 집합을 활용한 사이클 판별

서로소 집합은 다양한 알고리즘에 사용될 수 있는데, 특히 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다.(방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.)

 

### 서로소 집합을 활용해 사이클을 판별하는 알고리즘

```markdown
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
   1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
   2. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.
```

이러한 사이클 판별 알고리즘은 그래프에 포함되어 있는 간선의 개수가 E개일 때 모든 간선을 하나씩 확인하며, 매 간선에 대하여 union 및 find 함수를 호출하는 방식으로 동작한다. 이 알고리즘은 간선에 방향성이 없는 무향 그래프에서만 적용 가능하다.

 

### 서로소 집합을 활용한 사이클 판별 소스코드

```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생하면 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았으면 합집합 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```

 