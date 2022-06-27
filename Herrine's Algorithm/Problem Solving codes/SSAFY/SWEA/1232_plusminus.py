# 1232. 사칙 연산
# 사칙 연산은 기본적 으로 후위 순회를 사용 하여 연산 한다.
def post_order(node):  # 후위 순회를 통해 식 완성
    if 0 < node:
        post_order(L[node])
        post_order((R[node]))
        sik.append(tree[node])


def cal(num1, num2, calculator):
    if calculator == '+':
        return num1 + num2
    elif calculator == '-':
        return num1 - num2
    elif calculator == '*':
        return num1 * num2
    elif calculator == '/':
        return num1 / num2


for tc in range(1, 11):
    N = int(input())  # N 정점 개수
    L = [0] * (N+1)
    R = [0] * (N+1)
    tree = [0] * (N+1)
    sik = []
    # 트리 완성 하기
    for _ in range(N):
        Li = list(input().split())
        if len(Li) == 4:  # 정점 번호, 연산자, 왼쪽 자식, 오른쪽 자식
            L[int(Li[0])] = int(Li[2])
            R[int(Li[0])] = int(Li[3])
            tree[int(Li[0])] = Li[1]
        else:  # 정점 번호, 정수
            tree[int(Li[0])] = int(Li[1])
    # 식 만들기
    post_order(1)
    # 식으로 계산 하기
    stack = []
    for x in sik:
        if type(x) == int:  # 숫자
            stack.append(x)
        else:  # 연산자
            second = stack.pop()
            first = stack.pop()
            res = cal(first, second, x)
            stack.append(res)
    ans = int(stack.pop())
    print(f'#{tc} {ans}')
