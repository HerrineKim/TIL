ans = 0
index = 0
for i in range(9):
    temp = int(input())
    if temp > ans:
        ans = temp
        index = i + 1
print(ans)
print(index)