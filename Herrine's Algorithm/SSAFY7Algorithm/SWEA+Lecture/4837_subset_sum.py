numbers = list(range(1, 13))
result = []

for i in range( 1 << len(numbers)):
    subli = []
    for j in range(len(numbers)):
        if i & (1 << j):
            subli.append(numbers[j])
    result.append(subli)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for k in result:
        if len(k) == N and sum(k) == K:
            count += 1
    print(f'#{test_case} {count}')