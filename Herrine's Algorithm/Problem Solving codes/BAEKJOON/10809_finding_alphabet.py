# 10809. 알파벳 찾기
S = input()
alphabets =[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

for i in range(len(alphabets)):
    cnt = 0
    alpha = alphabets[i]
    for j in range(len(S)):
        if j == len(S)-1 and alpha != S[j]:
            print(-1, end=' ')
            break
        elif alpha == S[j]:
            print(cnt, end=' ')
            break
        elif alpha != S[j]:
            cnt += 1
