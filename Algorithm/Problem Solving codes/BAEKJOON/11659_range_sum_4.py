'''
# 시간초과
N, M = map(int, input().split())  # N 수의 개수 M 합을 구해야 하는 횟수
num_list = list(map(int, input().split()))

for i in range(M):
    start, end = map(int, input().split())
    temp = 0
    for j in range(start-1, end):
        temp += num_list[j]
    print(temp)
'''
import sys

N, M = map(int, sys.stdin.readline().split())  # N 수의 개수 M 합을 구해야 하는 횟수
num_list = list(map(int, sys.stdin.readline().split()))

prefix_value = 0
prefix_sum = [0]
for i in num_list:
    prefix_value += i
    prefix_sum.append(prefix_value)

for j in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start-1])