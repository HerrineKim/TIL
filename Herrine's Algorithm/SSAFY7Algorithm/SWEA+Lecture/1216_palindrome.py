def max_hwe(N, M, matrix):
    for i in range(N):
        for j in range(0, N-M+1):
            if matrix[i][j] == matrix[i][j+M-1]:
                for k in range(1, M):
                    if matrix[i][j+k] != matrix[i][j+M-1-k]:
                        break
                else: return True


    for i in range(N):
        for j in range(0, N-M+1):
            if matrix[j][i] == matrix[j+M-1][i]:
                for k in range(1, M):
                    if matrix[j+k][i] != matrix[j+M-1-k][i]:
                        break
                else: return True
    return False

for tc in range(10):
    T = int(input())
    matrix = [list(input()) for _ in range(100)]
    for M in range(100, -1, -1):
        if max_hwe(100, M, matrix):
            break
    print('#{0} {1}'.format(tc+1, M))