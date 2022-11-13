# stack
import sys

N = int(input())
stack = []

for i in range(N):
    a = sys.stdin.readline().rstrip()
    if 'push' in a:
        a = a.split()
        stack.append(a[1])
    elif a == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif a == 'size':
        print(len(stack))
    elif a == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)