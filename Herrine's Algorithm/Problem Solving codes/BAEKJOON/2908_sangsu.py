# 2908. 상수
a, b = map(str, input().split())
aa = a[::-1]
bb = b[::-1]

if int(aa) > int(bb):
    print(aa)
else:
    print(bb)