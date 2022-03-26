"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
V = int(input())  # 마지막 정점 번호, 정점 수. 만약 0번이 있는 경우 정점수는 마지막 번호 + 1
arr = list(map(int, input().split()))
E = V - 1  #


def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v)


def pre_order(v):
    if v:  # 존재하는 정점이면
        print(v)  # visit()
        post_order(ch1[v])  # 왼쪽 자식노드로 이동
        post_order(ch2[v])  # 오른쪽 자식드로 이동


def in_order(v):
    if v:
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])

# 부모를 인덱스로 자식번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E):  # 부모-자식 E개의 쌍이 주어진 상태
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:  # 아직 자식이 없는 경우
        ch1[p] = c
    else:
        ch2[p] = c

# 자식번호를 인덱스로 부모번호 저장 => root 찾기, 조상 찾기
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p

# root 찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0:
        root = i
        break
print(root)

pre_order(5)
in_order(5)
post_order(5)
