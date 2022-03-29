'''
<괄호 검사의 조건>
1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
2. 동일 타입의 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
3. **서로 다른 타입의 괄호 쌍이 서로를 교차하면 안 된다.**
'''

T = int(input())
for tc in range(1, T+1):
    s = input()
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{':
            st.append(s[i])
        elif s[i] == ')' or s[i] == '}':
            if len(st) == 0:
                st = list(s[i])
                break
            elif (s[i] == '}' and st[-1] != '{') or (s[i] == ')' and st[-1] != '('):
                st = list(s[i])
                break
            else:
                st.pop()

    if not len(st):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
