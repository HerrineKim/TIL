T = int(input())
for tc in range(1, T+1):
    code = list(input().split())
    stack = []
    cal = ['*', '/', '-', '+']
    res = 'error'  # 기본값 error

    for c in code:
        if c.isdigit():  # 숫자를 모두 스택에 넣는다
            stack.append(int(c))
        elif len(stack) != 0:  # 연산자 or 의 경우
            N1 = stack.pop()
            if c in cal and len(stack) != 0:
                N2 = stack.pop()
                if c == '*':
                    stack.append(N1*N2)
                elif c == '/':
                    stack.append(N1//N2)
                elif c == '+':
                    stack.append(N1+N2)
                elif c == '-':
                    stack.append(N2-N1)
            elif c == '.':  # 식이 끝나고 숫자도 하나인 경우
                if len(stack) != 0:
                    res = N1
    print(f'#{tc} {res}')
