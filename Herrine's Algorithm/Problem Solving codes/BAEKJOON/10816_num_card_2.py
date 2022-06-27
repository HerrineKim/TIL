N = int(input())
cards = list(map(int, input().split()))

temp_dict = dict()
for i in cards:
    if i in temp_dict:
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1


M = int(input())
num_list = list(map(int, input().split()))

for j in num_list:
    if j in temp_dict:
        print(temp_dict[j], end=' ')
    else:
        print(0, end=' ')
