# 연습문제 2
# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7 bit 씩 묶어 십진수로 변환하여 출력해보자
# 01D06079861D79F99F

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())
    s = ''
    for i in range(N):
        s += f'{int(arr[i], 16):04b}'
    print(f'#{tc} ', end='')
    for i in range(N*4 // 7):
        print(int(s[i * 7:i * 7 + 7], 2), end=' ')
    print()