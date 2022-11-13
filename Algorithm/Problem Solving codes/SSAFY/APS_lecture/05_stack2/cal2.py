# APS2 교재 p12
def DFS(n, sum):
    global sol
    if sum > K:  # 가지치기(풀이 후 가장 마지막에 고려)
        return
    if n >= N:
        if sum == K:
            sol += 1
        return
    DFS(n+1, sum+lst[n])  # 숫자를 포함하는 경우
    DFS(n+1, sum)  # 숫자를 포함하지 않는 경우


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    sol = 0
    DFS(0, 0)
    print(f'#{test_case} {sol}')