def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:  # 검색 성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)