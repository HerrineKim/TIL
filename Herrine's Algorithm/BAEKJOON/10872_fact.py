# def factorial(number):
#     if number == 1 or number == 0:
#         return 1
#     return number * factorial(number - 1)
#
#
# n = int(input())
# print(factorial(n))

from multiprocessing import context


def cycle(num):
    global cnt
    if num == 0:
        return 1
    elif num < 10:
        num = num * 2
        cnt += 1
        if num == N:
            return cnt
        cycle(num)
    else:
        temp = 0
        while num > 0:
            temp += num % 10
            num //= 10
        num = int(str(num % 10) + str(temp % 10))
        cnt += 1
        if num == N:
            return cnt
        cycle(num)


N = int(input())
cnt = 0
print(cycle(N))
