# 4834. 숫자카드
T = int(input())
for tc in range(1, T + 1):
    card = int(input())
    lst = list(map(str, input()))
    cnt = [0] * 10

    for i in range(card):
        cnt[int(lst[i])] += 1

    result = 0
    for i in range(len(cnt)):
        if result <= cnt[i]:
            result = cnt[i]
            idx = i
    print(f"#{tc} {idx} {result}")

'''
input
3
5
49679
5
08271
10
7797946543
'''