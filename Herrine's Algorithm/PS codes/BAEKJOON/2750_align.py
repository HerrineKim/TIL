N = int(input())

num_list = []

for i in range(N):
    num_list.append(int(input()))

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for num in num_list:
    print(num)