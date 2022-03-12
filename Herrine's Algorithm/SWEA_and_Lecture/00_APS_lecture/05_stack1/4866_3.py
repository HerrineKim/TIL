'''
<괄호 검사의 조건>
1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
2. 동일 타입의 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
3. **서로 다른 타입의 괄호 쌍이 서로를 교차하면 안 된다.**
'''

T = int(input())
for tc in range(1, T+1):
    s = input()
    st = []  # 스택
    for x in s:
        if s == '{' or s == '(':  # 여는 괄호는 무조건 스택에 담는다
            st.append(x)
        elif s == '}' or s == ')':  # 닫는 괄호일 경우 세 경우가 있다
            if len(st) == 0:  # 스택이 비어있는 경우 스택에 담고 0 출력
                st.append(s)
                break
            elif (s == '}' and st[-1] != '{') or (s == ')' and st[-1] != '('):  # 직전 값이 짝이 맞지 않으면 스택 담고 출력 0 출력
                st.append(s)
                break
            else:  # 짝이 맞는 경우는 pop하고 for문 맨 위로 고고
                st.pop()

    if len(st) != 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
