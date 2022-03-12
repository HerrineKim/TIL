T = int(input())
for tc in range(1, T+1):
    s = input()

    stack = [0]*1000
    top = -1
    ans = 1
    for x in s:
        if x == '(':
            top += 1  # push
            stack[top] = x
        elif x == ')':
            if top == -1:  # 닫는 괄호가 남은 경우
                ans = 0
            else:
                top -= 1  # pop
    else:
        if top != -1:  # 여는 괄호가 남은 경우
            ans = 0
    print(ans)
