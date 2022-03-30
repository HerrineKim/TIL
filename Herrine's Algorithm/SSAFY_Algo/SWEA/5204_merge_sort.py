# 재귀 함수로 하나씩 쪼갠 후 
def div_to_one(array):
    if len(array) <= 1:
        return array
    M = len(array) // 2  # 중
    L = div_to_one(array[:M])  # 좌
    R = div_to_one(array[M:])  # 우
    return merge(L, R)


# 병합
def merge(L, R):
    global ans
    if R.pop() < L.pop():  #


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N 정수의 개수
    arr = list(map(int, input().split()))

    ans = 0  # 오른쪽 원소가 먼저 복사되는 경우
    res = div_to_one(arr)
    print(f'{tc} {res[N//2]} {ans}')