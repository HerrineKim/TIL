# 순열 생성
def f(i, N):
    if i == N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
N = 3
f(0, N)

'''
N = 5
P = [x for x in range(1, N+1)]
f(0, N)
'''
