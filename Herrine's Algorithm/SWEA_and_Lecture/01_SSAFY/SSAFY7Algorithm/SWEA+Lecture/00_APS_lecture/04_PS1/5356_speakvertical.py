T = int(input())
for test_case in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    sols = []
    for i in range(15):
        for j in range(5):
            if i < len(arr[j]):
                sols.append(arr[j][i])
    print(f'#{test_case} {"".join(sols)}')

'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx

#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''