H, M = map(int, input().split())
cook_time = int(input())

new_M = (M + cook_time) % 60
if ((M + cook_time) // 60) + H >= 24:
    new_H = ((M + cook_time) // 60) + H - 24
else:
    new_H = ((M + cook_time) // 60) + H
print(new_H, new_M)