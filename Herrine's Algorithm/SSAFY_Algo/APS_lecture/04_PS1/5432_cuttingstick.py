T = int(input())
for test_case in range(1, T+1):
    lst = input()
    sol = cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if lst[i-1] == '(':
                sol += cnt
            else:
                sol += 1
    print(f'#{test_case} {sol}')

'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())


#1 17
#2 24
'''