# 카펫
# ans = [width, height]

ans = []
margin, inside = map(int, input().split())
for i in range(1, inside+1):
    if inside % i == 0:
        if (i + 2) * (inside // i + 2) - inside == margin:
            ans.append(inside // i + 2)
            ans.append(i + 2)
            break
        
print(ans)