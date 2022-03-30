def merge(left, right):
    global cnt
    if right[-1] < left[-1]:
        cnt += 1
    v = list()
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1
    if i == len(left):
        v = v + right[j:len(right)]
    if j == len(right):
        v = v + left[i:len(left)]
    return v


def merge_sort(v):
    if len(v) <= 1:
        return v
    m = len(v) // 2
    left = merge_sort(v[0:m])
    right = merge_sort(v[m:len(v)])
    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(arr)
    print(f'#{tc} {res[N//2]} {cnt}')
