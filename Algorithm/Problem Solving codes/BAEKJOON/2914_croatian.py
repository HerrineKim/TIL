# 2941. 크로아티아 알파벳
arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
a = len(s)
b = 0

for i in arr:
    if i == 'z=':
        n = s.count(i) - s.count('dz=')
        a -= n * len(i)
        b += n
    else:
        a -= s.count(i) * len(i)
        b += s.count(i)
print(a + b)