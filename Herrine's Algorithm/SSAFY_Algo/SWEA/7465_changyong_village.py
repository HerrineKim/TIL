# 7465. 창용 마을 무리의 개수
# disjoint set
def find_set(x):
    if x == par[x]:
        return x
    return find_set(par[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        par[root_y] = root_x
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nodes = [i for i in range(1, N + 1)]
    par = [i for i in range(N + 1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    root = set()
    for node in nodes:
        root.add(find_set(node))

    print(f'#{tc} {len(root)}')
