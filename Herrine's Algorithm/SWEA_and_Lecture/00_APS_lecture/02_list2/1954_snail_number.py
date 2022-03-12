def SnailArray(n):
    arr = [[0 for i in range(n)] for j in range(n)]
    row = 0
    col = -1
    cnt = 1
    trans = 1  # 방향
    while n > 0:
        for i in range(n):
            col += trans  # 0, 0 으로 만들어줌.
            arr[row][col] = cnt
            cnt += 1
        n -= 1
        for j in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1
    return arr


def printList(Size):
    list = SnailArray(Case)
    for i in range(Size):
        for j in range(Size - 1):
            print(list[i][j], end=" ")
        print(list[i][Size - 1])


T = int(input())
for test_case in range(1, T+1):
    Case = int(input())
    print(f"#{test_case}")
    printList(Case)

'''
달팽이는 1부터 N*N 까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N 크기의 달팽이를 출력하시오.
2    
3   
4   
'''