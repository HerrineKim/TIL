# 2675. 문자열 반복
import sys

T = int(input())

for tc in range(T):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)
    for j in range(len(S)):
        print(S[j] * R, end='')
    print()