import sys

money = int(input())
N = int(input())
temp = 0
for i in range (N):
    a, b = map(int, sys.stdin.readline().split())
    temp += a * b
if temp == money:
    print('Yes')
else:
    print('No')
