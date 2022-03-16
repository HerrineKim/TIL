def min_v():
    min_value = 1e10
    min_idx = -1
    for h in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i
    return min_idx


def max_v():
    max_value = -1
    max_idx = -1
    for j in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i
    return max_idx


for test_case in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    for i in range(N):
        box[max_v()] -= 1
        box[min_v()] += 1
    print(f'#{test_case} {box[max_v()] - box[min_v()]}')