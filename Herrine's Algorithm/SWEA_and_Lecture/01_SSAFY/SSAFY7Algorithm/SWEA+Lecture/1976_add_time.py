# 1976 시각 덧셈
"""
시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)
3
3 17 1 39
8 22 5 10
6 53 2 12
"""
T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    sumH = h1 + h2
    sumM = m1 + m2
    if m1 + m2 >= 60:
        sumH += (m1 + m2) // 60
        sumM = m1 + m2 - (((m1 + m2) // 60) * 60)
    if sumH >= 12:
        sumH -= 12

    print(f'#{tc} {sumH} {sumM}')
