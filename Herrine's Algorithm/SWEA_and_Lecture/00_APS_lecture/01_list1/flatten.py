def minv():
    min_value = 1e10
    min_idx = -1
    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i
    return min_idx


def maxv():
    max_value = -1
    max_idx = -1
    for j in range(len(box)):
        if box[j] > max_value:
            max_value = box[j]
            max_idx = j
    return max_idx


for test_case in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    for k in range(N):
        box[maxv()] -= 1
        box[minv()] += 1
    print(f'#{test_case} {box[maxv()] - box[minv()]}')

