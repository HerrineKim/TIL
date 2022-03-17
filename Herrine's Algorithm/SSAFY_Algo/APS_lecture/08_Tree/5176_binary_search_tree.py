def fTree(n):  # 1부터 N까지 트리 만들기
    global cnt
    if n <= N:
        fTree(n*2)
        tree[n] = cnt
        cnt += 1
        fTree(n*2+1)


T = int(input())
for tc in range(1, 1+T):
    N = int(input())  # 루트 노트의 값이자 최대값
    tree = [0] * (N+1)
    cnt = 1
    fTree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
