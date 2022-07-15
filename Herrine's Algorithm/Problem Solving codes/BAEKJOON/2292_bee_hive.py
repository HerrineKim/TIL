# 2292. 벌집
N = int(input())

hive_nums = 1
cnt = 1
while N > hive_nums :
    hive_nums += 6 * cnt
    cnt += 1
print(cnt)