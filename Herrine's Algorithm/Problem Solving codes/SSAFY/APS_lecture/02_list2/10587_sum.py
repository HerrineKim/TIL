# 10587
T = int(input())
for test_case in range(1, T+1):
    A = list(map(int, input().split()))
    N = len(A)

    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += A[j]
        if s == 0:
            print(f'#{test_case} 1')
            break
    else:
        print(f'#{test_case} 0')

'''
10개의 정수를 입력 받아 부분 집합의 합이 0이 되는지 확인하는 프로그램을 만드시오.
입력
첫 줄에 테스트케이스 T, 다음 줄부터 테스트케이스 별로 절대값 1이상 20이하의 정수 10개가 제공된다.
1<=T<=10
출력
#과 테스트케이스 번호, 빈칸에 이어 부분집합의 합이 0이되는 경우가 있으며 1, 아니면 0을 출력한다.

3
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
7 7 19 1 -18 5 -9 -11 19 18
'''