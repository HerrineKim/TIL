# 5248. 그룹 나누기
# Disjoint set
def find(x):
    if x == parents[x]:
        return x
    else:
        return find(parents[x])


def union(a, b):
    parents[find(a)] = find(b)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 출석번호 M 개의 번호쌍
    parents = [i for i in range(N+1)]
    num_li = list(map(int, input().split()))

    for i in range(M):
        union(num_li[i*2+1], num_li[i*2])

    ans = []  # 루트 노드들만 저장
    for j in range(1, N+1):
        ans.append(find(j))

    print(f"#{tc} {len(set(ans))}")
