# 롤케익 자르기
from collections import Counter

def solution(topping):
    answer = 0
    total = Counter(topping)
    set1 = set()
    while len(topping) > 1:
        element = topping.pop()
        set1.add(element)
        if total[element] > 1:
            total[element] = total[element]-1
        else:
            del total[element]

        if len(total) == len(set1):
            answer+=1
    return answer