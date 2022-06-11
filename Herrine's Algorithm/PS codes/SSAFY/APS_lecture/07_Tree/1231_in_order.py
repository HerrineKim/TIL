# 1231. 중위순회

def in_order(v):
    if v <= N:
        in_order(v * 2)
        print(tree[v], end='')
        in_order(v * 2 + 1)


for tc in range(1, 11):
    N = int(input())  # 알파벳 개수
    tree = [0] * (N + 1)  # 트리
    for i in range(N):
        Li = list(input().split())
        tree[int(Li[0])] = Li[1]

    print(f'#{tc} ', end='')
    in_order(1)
    print()