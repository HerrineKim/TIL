# 5185. 이진수

# 함수 만들기
def sixteen_two(sixteen):
    res = ''
    for i in sixteen:
        # 10진수 변환
        ten = int(i, 16)
        temp = ''
        # 2진수 변환
        for _ in range(4):
            ten, n = divmod(ten, 2)
            temp = str(n) + temp
        res += temp
    return res


T = int(input())
for tc in range(1, T + 1):
    N, Num = input().split()  # N 자리수 Num 수
    print(f'#{tc} {sixteen_two(Num)}')
