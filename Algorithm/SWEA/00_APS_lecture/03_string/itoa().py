def itoa(a):
    s = ''
    while a > 0:
        s += chr(ord('0') + a % 10)
        a //= 10
    return s[::-1]


print(itoa(782346823))
