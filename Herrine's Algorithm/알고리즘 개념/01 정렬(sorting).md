# 01_μ λ ¬(sorting)



## π λνμ μΈ μ λ ¬μ μ’λ₯

1. λ²λΈ μ λ ¬(Bubble Sort)
2. μΉ΄μ΄ν μ λ ¬(Counting Sort)
3. μ ν μ λ ¬(Selection Sort)
4. ν΅ μ λ ¬(Quick Sort)
5. μ½μ μ λ ¬(Insertion Sort)
6. λ³ν© μ λ ¬(Merge Sort)



## π μκ° λ³΅μ‘λ(λΉ μ€ νκΈ°λ²)

> μκ³ λ¦¬μ¦μ μν μ±λ₯μ λΆμν  λ μ¬μ©

- λΉ μ€ νκΈ°λ²: μ΅μμ μλλ¦¬μ€
- μ°μ° νμκ° λ€ν­μμΌλ‘ ννλ  κ²½μ°, κ³μλ₯Ό μ μΈν μ΅κ³ μ°¨ν­μΌλ‘ λνλΈλ€.



- O(1): μλ ₯ λ°μ΄ν°μ μκ΄ μμ΄ μΈμ λ μΌμ ν μκ°μ΄ κ±Έλ¦¬λ μκ³ λ¦¬μ¦ 
- O(n): λ°μ΄ν°κ° μ¦κ°ν¨μ λ°λΌ μ²λ¦¬ μκ°λ λΉλ‘ν΄μ μ¦κ°ν¨ 
- O(n^2): λ°μ΄ν°κ° μ¦κ°ν¨μ λ°λΌ κ·Έλνκ° μμ§μ κ°κΉμ΄ λͺ¨μμ΄ λ¨. λ λΉ λ₯΄κ² μ¦κ°ν¨.



### 1. λ²λΈ μ λ ¬

> μΈμ ν λ κ°μ μμλ₯Ό λΉκ΅νλ©° μλ¦¬λ₯Ό κ³μ κ΅ννλ λ°©μ, μκ° λ³΅μ‘λ O(n^2)

```python
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```



### 2. μΉ΄μ΄ν μ λ ¬

> κ° μ«μκ° λͺ λ² λ±μ₯νλμ§λ₯Ό μΈμ΄ μ λ ¬νλ λ°©μ. μκ° λ³΅μ‘λ O(n+k)

(μ½λ μΆμ²: https://bowbowbow.tistory.com/8)

```python
#μλ ₯λ  μ μλ μ«μμ μ΅λ ν¬κΈ°λ₯Ό μλ―Έν©λλ€. 
MAX_NUM = 1000

#Aλ μλ ₯λ μ«μλ₯Ό μ μ₯νλ λ°°μ΄ 
A = list(map(int, input().split()))

#Nμ μλ ₯λ μ«μμ κ°μ μλλ€.
N = len(A)

#0μΌλ‘ μ΄κΈ°νλ μλ ₯λ  MAX_NUM+1 κΈΈμ΄μ λ°°μ΄ countλ₯Ό μμ±ν©λλ€.
count =[0]*(MAX_NUM+1)

#countSumμ λμ ν©μ μ μ₯νλ λ°°μ΄μλλ€.
countSum =[0]*(MAX_NUM+1)

#μ«μ λ±μ₯ νμ μΈκΈ°
for i in range(0, N):
    count[A[i]] += 1

#μ«μ λ±μ₯ νμ λμ ν© κ΅¬νκΈ°  
countSum[0] = count[0]

for i in range(1, MAX_NUM+1):
	countSum[i] = countSum[i-1]+count[i];

#Bλ μ λ ¬λ κ²°κ³Όλ₯Ό μ μ₯νλ λ°°μ΄  
B = [0]*(N+1)

for i in range(N-1, -1, -1):  
    B[countSum[A[i]]] = A[i]  
    countSum[A[i]] -= 1    

#μμ΄ Aλ₯Ό μ λ ¬ν κ²°κ³ΌμΈ μμ΄ Bλ₯Ό μΆλ ₯νλ€.
result = ""
for i in range(1, N+1):
	result += str(B[i]) + " "
	print(result)
```



### 3. μ ν μ λ ¬

> λ°°μ΄μμ κ°μ₯ μμ λ°μ΄ν°λ₯Ό μ ννμ¬ μμΌλ‘ λ³΄λ΄λ μ λ ¬, μκ° λ³΅μ‘λ O(N^2)

```python
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```



### 4. ν΅ μ λ ¬

> νλμ λ¦¬μ€νΈλ₯Ό νΌλ²(pivot)μ κΈ°μ€μΌλ‘ λ κ°μ λΉκ· λ±ν ν¬κΈ°λ‘ λΆν νκ³  λΆν λ λΆλΆ λ¦¬μ€νΈλ₯Ό μ λ ¬ν λ€μ, λ κ°μ μ λ ¬λ λΆλΆ λ¦¬μ€νΈλ₯Ό ν©νμ¬ μ μ²΄κ° μ λ ¬λ λ¦¬μ€νΈκ° λκ² νλ λ°©λ². μκ° λ³΅μ‘λ O(nlogn)

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



### 5. μ½μ μ λ ¬

> μ½μ μ λ ¬μ λ λ²μ§Έ μλ£λΆν° μμνμ¬ κ·Έ μ(μΌμͺ½)μ μλ£λ€κ³Ό λΉκ΅νμ¬ μ½μν  μμΉλ₯Ό μ§μ ν ν μλ£λ₯Ό λ€λ‘ μ?κΈ°κ³  μ§μ ν μλ¦¬μ μλ£λ₯Ό μ½μνμ¬ μ λ ¬νλ μκ³ λ¦¬μ¦. μκ° λ³΅μ‘λ O(n)

``` python
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
```



### 6. λ³ν© μ λ ¬

> νλμ λ¦¬μ€νΈλ₯Ό λ κ°μ κ· λ±ν ν¬κΈ°λ‘ λΆν νκ³  λΆν λ λΆλΆ λ¦¬μ€νΈλ₯Ό μ λ ¬ν λ€μ, λ κ°μ μ λ ¬λ λΆλΆ λ¦¬μ€νΈλ₯Ό ν©νμ¬ μ μ²΄κ° μ λ ¬λ λ¦¬μ€νΈκ° λκ² νλ λ°©λ². μκ° λ³΅μ‘λ O(nlogn)

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

