s = '기러기는기러기'
N = len(s)

ans = '회문 아님'
for i in range(N//2):
    if s[i] != s[N - 1 - i]:
        break
else:
    ans = '회문'
print(ans)
