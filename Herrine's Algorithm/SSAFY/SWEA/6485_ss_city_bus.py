T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 버스 노선의 갯수 = 2
    myLi = [0] * 5001  # 인덱스가 많을 때는 항상 정신차리자! 통일시키기
    for i in range(N):
        # 가장 먼저 반복되어야 하는 것이 무엇인지 잘 살펴보기.
        # 먼저 범위가 주어지고, 그 다음에 그 범위에 해당되는 만큼 +1 해주면 되기 때문에 이러한 for 문 구조가 만들어진다
        A, B = map(int, input().split())
        for j in range(A, B+1):
            myLi[j] += 1
    P = int(input())  # 버스 정류장의 갯수 = 5
    resultLi = []
    for a in range(P):
        resultLi.append(myLi[int(input())])  # 활용도가 떨어지는 input 은 이렇게
    print(f'#{test_case}', end=' ')
    print(*resultLi)

'''
1
2
1 3
2 5
5
1
2
3
4
5
'''