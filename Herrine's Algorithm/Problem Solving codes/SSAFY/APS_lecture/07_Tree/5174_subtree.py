def in_order(node):
    global cnt
    if node:
        cnt += 1
        in_order(L[node])
        in_order(R[node])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E 간선의 개수 N 루트
    arr = list(map(int, input().split()))  # 노드 쌍들의 입력

    # 왼/오 자식 노드의 리스트
    L = [0] * (E + 2)
    R = [0] * (E + 2)

    for i in range(0, len(arr), 2):  # 트리 구조 저장
        par, chd = arr[i], arr[i + 1]
        if L[par]:
            R[par] = chd
        else:
            L[par] = chd

    cnt = 0
    in_order(N)
    print(f'#{tc} {cnt}')