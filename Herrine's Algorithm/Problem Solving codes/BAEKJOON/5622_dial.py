S = input()

cnt = 0
for i in range(len(S)):
    if S[i] in 'WXYZ':
        cnt += 10
    elif S[i] in 'TUV':
        cnt += 9
    elif S[i] in 'PQRS':
        cnt += 8
    elif S[i] in 'MNO':
        cnt += 7
    elif S[i] in 'JKL':
        cnt += 6
    elif S[i] in 'GHI':
        cnt += 5
    elif S[i] in 'DEF':
        cnt += 4
    elif S[i] in 'ABC':
        cnt += 3

print(cnt)