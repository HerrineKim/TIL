# 2447. 별찍기

def draw(num):
    if num == 1:
        return ['*']
    
    stars = draw(num // 3)
    ans = []
    for s in stars:
        ans.append(s * 3)
    for s in stars:
        ans.append(s + ' ' * (num // 3) + s)
    for s in stars:
        ans.append(s * 3)
    return ans

N = int(input())
print('\n'.join(draw(N)))