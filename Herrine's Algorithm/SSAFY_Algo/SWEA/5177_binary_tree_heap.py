def heap(n):  # 최소 힙을 만들기 위해 이진 트리를 정렬할 함수
    par = n // 2
    if par >= 0:
        if tree[par] > tree[n]:
            tree[n], tree[par] = tree[par], tree[n]
            heap(par)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드의 개수
    tree = [0] * (N+1)
    nodes = [0] + list(map(int, input().split()))
    for i in range(1, len(tree)):
        tree[i] = nodes[i]
        heap(i)
    # 출력값 구하기
    res = 0
    while N:
        N //= 2
        res += tree[N]

    print(f'#{tc} {res}')
