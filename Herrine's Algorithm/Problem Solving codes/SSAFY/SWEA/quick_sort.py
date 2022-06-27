def quick_sort1(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    less, more, equal = [], [], []
    for _ in range(len(array)):
        each = array.pop()
        if each < pivot:
            less.append(each)
        elif each > pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick_sort1(less) + equal + quick_sort1(more)

print(quick_sort1([51, 20, 72, 63, 32, 75, 2, 88, 16, 29]))
