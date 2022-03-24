# 1242.암호코드 스캔
import sys
sys.stdin = open('1242input.txt', 'r')

sixteen_to_two = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                  '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                  'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
my_ratio = {
    '112': 0,
    '122': 1,
    '221': 2,
    '114': 3,
    '231': 4,
    '132': 5,
    '411': 6,
    '213': 7,
    '312': 8,
    '211': 9,
}


# 유효성 검증
def check(code):
    if ((code[7] + code[5] + code[3] + code[1]) * 3 + code[0] + code[2] + code[4] + code[6]) % 10:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 세로 M 가로
    arr = [input() for _ in range(N)]
    # 16진수 -> 2진수 배열 만들기
    for i in range(N):
        binary_str = ''
        for j in arr[i]:
            binary_str += sixteen_to_two[j]
        arr[i] = binary_str
    # 2진수를 코드로 만들기
    v = []  # 모든 암호 같지 않기에 visited 만들어야 한다
    ans = 0  # 최종 답 0으로 초기화
    for n in range(N):
        one, two, three = 0, 0, 0  # 비율 초기화
        my_code = []  # 코드 초기화
        if '1' not in arr[n]:
            continue
        # 비율로 암호 구하기
        for m in range(M * 4 - 1, -1, -1):
            if two == 0 and three == 0 and arr[n][m] == '1':
                one += 1
            elif one and three == 0 and arr[n][m] == '0':
                two += 1
            elif one and two and arr[n][m] == '1':
                three += 1
            elif three and arr[n][m] == '0':  # 3번까지 채워졌는데 또 0 나왔다면 암호 끝난것
                min_V = min(one, two, three)
                my_code.append(my_ratio[str(one // min_V) + str(two // min_V) + str(three // min_V)])
                one = two = three = 0
                if len(my_code) == 8:  # 길이가 조건과 맞고
                    if my_code not in v:  # visit 안 했다면
                        if check(my_code):  # 유효성 검사
                            ans += sum(my_code)  # 최종 암호로 바꾸어 ans 완성
                        v.append(my_code)  # visited 에 추가
    print(f'#{tc} {ans}')
