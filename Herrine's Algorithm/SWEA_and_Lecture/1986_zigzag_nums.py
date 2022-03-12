# 1986. 지그재그 숫자
"""
1부터 N 까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

2
5
6
"""
T = int(input())
for tc in range(1, T+1):
    num = int(input())
    numLi = []
    for n in range(1, num+1):
        numLi.append(n)
    res = 0
    for x in numLi:
        if x % 2 == 1:  # 홀수이면
            res += x
        else:  # 짝수이면
            res -= x
    print(f'#{tc} {res}')
