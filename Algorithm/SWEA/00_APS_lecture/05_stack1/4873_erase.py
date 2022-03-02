T = int(input())
for tc in range(1, T + 1):
    s = input()
    st = []  # 스택을 만들어 두 값이 똑같은 것이 들어오면 pop 해줄 것이다
    for i in range(len(s)):
        if len(st) == 0:  # 스택에 차례로 문자열을 넣어 준다
            st.append(s[i])
        else:  # 문자를 넣기 시작했다면 새로 들어오는 값과 비교해야 한다
            if st[-1] == s[i]:  # 만약 스택의 맨 위 값과 새로 들어갈 값이 같다면
                st.pop()  # 맨 위의 값을 삭제한 문자열을 반환한다
            else:  # 만약 두 값이 다르다면
                st.append(s[i])  # 그대로 더해 나간다
    res = len(st)  # 결과는 남은 문자열의 갯수
    print(f'#{tc} {res}')
