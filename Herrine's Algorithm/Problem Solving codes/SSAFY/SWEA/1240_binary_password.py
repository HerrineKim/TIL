# 1240. 단순 2진 암호코드
my_amho = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 세로 M 가로
    arr = [input() for _ in range(N)]  # 암호들의 리스트
    # 유효한 코드 찾기
    my_code = ''
    for i in range(N):
        if sum(map(int, list(arr[i]))) == 0:  # 1이 없다면 continue
            continue
        else:  # 이진수로 이루어져 있는 것을 확인한 경우
            for j in range(M - 1, -1, -1):  # 암호를 1부터 거꾸로 탐색해 저장.
                if arr[i][j] == '1':
                    my_code = arr[i][j - 55:j + 1]
                    break
            break
    # 문제 이해가 잘 안 될때는 test case 살펴보기. 이 문제의 경우 암호 여러줄이 모두 같은 것이었음

    res = [my_amho[my_code[0:7]], my_amho[my_code[7:14]], my_amho[my_code[14:21]],
           my_amho[my_code[21:28]], my_amho[my_code[28:35]], my_amho[my_code[35: 42]],
           my_amho[my_code[42:49]], my_amho[my_code[49:56]]]
    # 암호 유효성 검증 후 합 제출
    if ((res[0] + res[2] + res[4] + res[6]) * 3 + res[1] + res[3] + res[5] + res[7]) % 10 == 0:
        print(f'#{tc} {sum(res)}')
    else:
        print(f'#{tc} 0')
