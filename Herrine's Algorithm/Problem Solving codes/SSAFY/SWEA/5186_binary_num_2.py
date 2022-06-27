# 5186. 이진수 2
import math

T = int(input())
for tc in range(1, T+1):
    N = float(input())  # N float 십진수
    res = ''  # 결과
    while N < 1:  # N이 1보다 작을 동안
        N *= 2  # 2를 곱해 정수부 만들기
        res += str(math.floor(N))  # 정수부 더해주기 (round는 반올림이다!)
        # 길이 초과하면 overflow 출력
        if len(res) >= 13:
            print(f'#{tc} overflow')
            break
        # 곱해준 값이 1보다 크면 1을 빼다시 반복, 0.~ 형태면 그냥 반복
        if N > 1:
            N -= 1
        # N == 1이면 반복문 종료
        elif N == 1:
            break

    if len(res) <= 12:  # 체크 안 해도 되나
        print(f'#{tc} {res}')
