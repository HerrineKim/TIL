def Cal(tokens):
    stk = []
    for to in tokens:
        if to == '+':
            stk.append(stk.pop()+stk.pop())
        elif to == '*':
            stk.append(stk.pop()*stk.pop())
        else:
            stk.append(int(to))
    return stk.pop()


for t in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''
    stack = [0] * N
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선순위
    for i in range(N):
        if '0' <= infix[i] <= '9':  # 피연산자인 경우
            postfix += infix[i]
        else:  # 연산자인 경우
            while top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]
    while top > -1:
        postfix += stack[top]
        top -= 1
    print(postfix)

    print(f'#{t} {Cal(list(postfix))}')
