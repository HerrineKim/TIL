# 결정된 리턴값을 이전 단계에 전달

def f(i, N, v):
    if i == N:  # 배열을 벗어난 경우, 검색 실패
        return -1
    elif A[i] == v:
        return 1
    else:  # 배열을 벗어나지 않고 검색 실패한 경우
        return f(i+1, N, v)  # 리턴값을 다시 리턴


A = [7, 2, 5, 4, 1, 3]
N = len(A)
v = 5
print(f(0, N, v))