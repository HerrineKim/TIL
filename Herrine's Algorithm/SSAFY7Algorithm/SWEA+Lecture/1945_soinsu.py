T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    li = [0]*5
    numli = [2, 3, 5, 7, 11]
    for i in range(len(numli)):
        while True:
            if N // numli[i] == 0:
                li[i] += 1
            else:
                break
    result = ' '.join(map(str, li))
    print(f'#{test_case} {result}')
