# BabyGin
T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 12
    num = int(input())
    for i in range(6):
        cnt[num % 10] += 1
        num //= 10

    tri = ruun = 0
    j = 0
    while j < 10:
        if cnt[j] >= 3:
            cnt[j] -= 3
            tri += 1
            continue
        if cnt[j] >= 1 and cnt[j+1] >= 1 and cnt[j+2] >= 1:
            cnt[j] -= 1
            cnt[j+1] -= 1
            cnt[j+2] -= 1
            ruun += 1
            continue
        j += 1

    if ruun + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print('Lose')

'''
input
3
444345
444456
644544
'''
