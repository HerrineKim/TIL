# 01_정렬(sorting)



## 😀 대표적인 정렬의 종류

1. 버블 정렬(Bubble Sort)
2. 카운팅 정렬(Counting Sort)
3. 선택 정렬(Selection Sort)
4. 퀵 정렬(Quick Sort)
5. 삽입 정렬(Insertion Sort)
6. 병합 정렬(Merge Sort)



## 🕛 시간 복잡도(빅 오 표기법)

> 알고리즘의 수행 성능을 분석할 때 사용

- 빅 오 표기법: 최악의 시나리오
- 연산 횟수가 다항식으로 표현될 경우, 계수를 제외한 최고차항으로 나타낸다.



- O(1): 입력 데이터에 상관 없이 언제나 일정한 시간이 걸리는 알고리즘 
- O(n): 데이터가 증가함에 따라 처리 시간도 비례해서 증가함 
- O(n^2): 데이터가 증가함에 따라 그래프가 수직에 가까운 모양이 됨. 더 빠르게 증가함.



### 1. 버블 정렬

> 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식, 시간 복잡도 O(n^2)

```python
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```



### 2. 카운팅 정렬

> 각 숫자가 몇 번 등장했는지를 세어 정렬하는 방식. 시간 복잡도 O(n+k)

(코드 출처: https://bowbowbow.tistory.com/8)

```python
#입력될 수 있는 숫자의 최대 크기를 의미합니다. 
MAX_NUM = 1000

#A는 입력된 숫자를 저장하는 배열 
A = list(map(int, input().split()))

#N은 입력된 숫자의 개수 입니다.
N = len(A)

#0으로 초기화된 입력될 MAX_NUM+1 길이의 배열 count를 생성합니다.
count =[0]*(MAX_NUM+1)

#countSum은 누적합을 저장하는 배열입니다.
countSum =[0]*(MAX_NUM+1)

#숫자 등장 횟수 세기
for i in range(0, N):
    count[A[i]] += 1

#숫자 등장 횟수 누적합 구하기  
countSum[0] = count[0]

for i in range(1, MAX_NUM+1):
	countSum[i] = countSum[i-1]+count[i];

#B는 정렬된 결과를 저장하는 배열  
B = [0]*(N+1)

for i in range(N-1, -1, -1):  
    B[countSum[A[i]]] = A[i]  
    countSum[A[i]] -= 1    

#수열 A를 정렬한 결과인 수열 B를 출력한다.
result = ""
for i in range(1, N+1):
	result += str(B[i]) + " "
	print(result)
```



### 3. 선택 정렬

> 배열에서 가장 작은 데이터를 선택하여 앞으로 보내는 정렬, 시간 복잡도 O(N^2)

```python
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```



### 4. 퀵 정렬

> 하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법. 시간 복잡도 O(nlogn)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
```



### 5. 삽입 정렬

> 삽입 정렬은 두 번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후 자료를 뒤로 옮기고 지정한 자리에 자료를 삽입하여 정렬하는 알고리즘. 시간 복잡도 O(n)

``` python
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
```



### 6. 병합 정렬

> 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법. 시간 복잡도 O(nlogn)

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

