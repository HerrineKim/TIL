# 1970. 쉬운 거스름돈
T = int(input())
for tc in range(1, T+1):
    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0, 0, 0, 0, 0, 0, 0, 0]
    money = (int(input())//10) * 10
    for i in range(8):
        if money / coins[i] < 1:
            money = money
        else:
            ans[i] += money // coins[i]
            money -= (money // coins[i]) * coins[i]
    print(f'#{tc}')
    print(*ans)
