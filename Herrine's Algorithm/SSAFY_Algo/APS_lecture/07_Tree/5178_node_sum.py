T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N 노드의 개수 M 리프 노드의 개수 L 출력할 노드 번호
    tree = [0] * (N + 1)
    # 1. 트리 완성 하기
    for _ in range(M):
        n, v = map(int, input().split())  # n 노드 번호 v 노드 값
        tree[n] = v
    # 2. 자식 노드 값의 합을 부모 노드 들에 저장 하기
    for i in range(N, 0, -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]  # 부모 노드 * 2 (+1) -> 자식 노드의 값이라는 것을 이용
    # 3. 찾고 싶은 노드 값 출력
    print(f'#{tc} {tree[L]}')

