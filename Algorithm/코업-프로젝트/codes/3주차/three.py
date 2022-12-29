# 삼총사
from itertools import combinations 

def solution(number):
    count = 0
    com_list = list(combinations(number, 3))
    for i in range(len(com_list)):
        if sum(com_list[i]) == 0:
            count += 1
    return count