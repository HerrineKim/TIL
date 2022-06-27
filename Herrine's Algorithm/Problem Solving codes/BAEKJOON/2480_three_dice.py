a, b, c = map(int, input().split())
abc_list = [a, b, c]

if a == b == c:
    ans = 10000 + (a * 1000)
elif a == b or b == c or c == a:
    temp = []
    x = 0
    for i in range(3):
        if abc_list[i] in temp:
            x = abc_list[i]
        temp.append(abc_list[i])
    ans = 1000 + (x * 100)
else:
    x = max(abc_list)
    ans = x * 100

print(ans)