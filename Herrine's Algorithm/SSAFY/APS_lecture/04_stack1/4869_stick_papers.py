def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + (2 * fibo(n - 2))


for tc in range(1, int(input())+1):
    print(f"#{tc} {fibo((int(input()) // 10) + 1)}")
