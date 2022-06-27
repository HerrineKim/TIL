# 11399. ATM
N = int(input())
people = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if people[j] > people[j+1]:
            people[j], people[j+1] = people[j+1], people[j]
            
temp = 0
res = [people[0]] * N
for i in range(0, N):
    for j in range(i+1):
        temp += people[j]
    res[i] = temp

print(max(res))