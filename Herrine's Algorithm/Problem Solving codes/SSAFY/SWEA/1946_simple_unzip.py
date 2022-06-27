# 1946. 간단한 압축 풀기
T = int(input())
for tc in range(1, T + 1):
    res = ''
    N = int(input())
    for i in range(N):
        char, num = map(str, input().split())
        for j in range(int(num)):
            res += char
    L = len(res)
    print(f'#{tc}')
    for k in range(0, L, 10):
        print(res[k:k+10])
