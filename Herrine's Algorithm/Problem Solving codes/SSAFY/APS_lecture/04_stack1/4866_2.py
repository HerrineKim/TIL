T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = [0]*len(s)
    top = -1
    ans = 1
    for x in s:
        if x == '{' or x == '(':
            top += 1
            stack[top] = x
        elif x == '}' or x == ')':
            if top == -1:
                ans = 0
                break
            else:
                if x == '}' and stack[top] == '(':
                    ans = 0
                    break
                elif x == ')' and stack[top] == '{':
                    ans = 0
                    break
    if top != -1:
        ans = 0
    print(f'#{tc} {ans}')
