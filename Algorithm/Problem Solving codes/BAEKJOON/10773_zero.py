import sys

K = int(input())
stack = []
for i in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num:
        stack.append(num)
    elif num == False and stack:
        stack.pop()

ans = 0
for j in range(len(stack)):
    ans += stack[j]

print(ans)