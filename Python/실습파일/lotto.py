import random

num_box = range(1, 46)

lotto_num = random.sample(num_box, 6)
print(lotto_num)

# import random
# numbers = range(1, 46)
# for i in range(5):
#     lotto_number = random.sample(numbers, 6)
#     print(sorted(lotto_number))   