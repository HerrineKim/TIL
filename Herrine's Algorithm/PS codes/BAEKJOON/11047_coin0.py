# 11047 동전 0

N, K = map(int, input().split())  # N 동전 개수 K 가격

coin_list = []  # 동전의 개수를 담을 리스트
for i in range(N): 
    coin_list.append(int(input()))
coin_list.reverse()  # 큰 것부터 나눠주기 위해 뒤집기

ans = 0  # 필요한 동전의 개수를 담을 변수
num = 0  # 매 반복문바다 바뀔 몫
for j in range(N):
    if coin_list[j] <= K:  # 만약 동전의 가치가 가격보다 같거나 낮다면
        num = K // coin_list[j]  # 나눠주고
        K = K - (num * coin_list[j])  # 나눠준 만큼의 가격을 빼 준다
        ans += num  # 그리고 사용한 동전의 개수를 ans에 더한다
        if K % coin_list[j] == 0:  # 만약 나누어 떨어졌다면
            print(ans)  # 답을 출력한다
        