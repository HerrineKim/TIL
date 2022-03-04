def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i


print(atoi('234234324'))
