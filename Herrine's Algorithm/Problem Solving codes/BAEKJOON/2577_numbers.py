num = 1
for i in range(3):
    num *= int(input())

num = list(str(num))
num_li = [0 for _ in range(10)]

for j in range(len(num)):
    num_li[int(num[j])] += 1

for k in range(10):
    print(num_li[k])