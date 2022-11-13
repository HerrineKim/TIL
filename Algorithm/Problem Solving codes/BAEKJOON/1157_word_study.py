# 1157. 단어 공부
S = input()
S_list = list(S.lower())
alphabets = list(set(S_list))
dictionary = {key: 0 for key in dict.fromkeys(alphabets).keys()}

for i in range(len(S_list)):
    dictionary[S_list[i]] += 1


# 가장 많은 값을 가진 key를 찾는다.
all_values = dictionary.values()
max_value = all_values[0]
for i in range(len(all_values)):
    if all_values[i] > max_value:
        max_value = all_values[i]
    
max_value = max(all_values)
max_key = 'a'
for value in all_values():
    if value == max_value:
        max_key = dictionary[value]
        break
print(max_key)

# print(dictionary)

# max_key = 'a'
# temp = 0
# print(temp)
# for key, value in dictionary.items():
#     if value > temp:
#         temp = value
#         max_key = key
#     elif value == temp:
#         print('?')
#         break
#     print(max_key.upper())