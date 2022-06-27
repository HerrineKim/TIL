T = int(input())
for tc in range(1, T+1):
    word = input()
    res = 0
    if len(word)%2 == 1:  # 길이가 홀수일 경우
        if word[0:len(word)//2] == word[len(word)-1:-(len(word)//2)-1:-1]:
            res = 1
        else:
            res = 0
    if len(word)%2 == 0:  # 길이가 짝수일 경우
        if word[0:len(word)//2] == word[len(word)-1:-(len(word)//2)-1:-1]:
            res = 1
        else:
            res = 0

    print(f'#{tc} {res}')
