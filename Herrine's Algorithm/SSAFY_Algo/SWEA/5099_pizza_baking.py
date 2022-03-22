# 5099. 피자굽기
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 화덕 크기 M 피자 개수
    c = list(map(int, input().split()))  # 치즈 리스트
    pizza = []
    for i in range(M):
        pizza.append([i+1, c[i]])  # 피자와 치즈 쌍 리스트

    oven = pizza[:N]  # 오븐에 피자 채워넣기
    remain = pizza[N:]  # 오븐에 넣고 남은 피자

    while len(oven) > 1:  # 오븐이 비워져있는 동안 반복
        pizza_pop = oven.pop(0)
        pizza_pop[1] //= 2  # 치즈를 녹인다
        if pizza_pop[1] == 0:  # 치즈가 다 녹았다면
            if len(remain):  # 오븐에 안 들어간 피자가 더 남아있는 경우에
                oven.append(remain.pop(0))  # 오븐 맨 뒤로 넣어준다
        else:  # 안 녹았다면 뒤로 넣어준다.
            oven.append(pizza_pop)

    print(f'#{tc} {oven[0][0]}')
