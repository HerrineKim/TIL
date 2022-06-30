all_nums = set(range(1, 10001))
generated_nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_nums.add(i)
    
self_nums = sorted(all_nums - generated_nums)
for k in self_nums:
    print(k)