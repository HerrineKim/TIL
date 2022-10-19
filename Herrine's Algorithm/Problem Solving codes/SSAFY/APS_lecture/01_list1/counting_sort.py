# 카운팅 정렬
# 정렬을 수행할 배열
def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [0] * (len(arr))
    for num in arr:
        idx = count[num]
        result[idx - 1] = num
        count[num] -= 1
    return result


arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]
print(counting_sort(arr))
# [1, 2, 3, 3, 4, 4, 5, 7, 9]