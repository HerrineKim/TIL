# 1984. 중간 평균값 구하기
"""
10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
"""
T = int(input())
for tc in range(1, T+1):
    numLi = list(map(int, input().split()))
    numLi = sorted(numLi)
    numSum = 0
    for i in range(1, 9):
        numSum += numLi[i]
    res = round(numSum/8)

    print(f'#{tc} {res}')
