# 연습문제 1
# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
# 0000000111100000011000000111100110000110000111100111100111111001100111
"""
for i in range(len(n) // 7):
    tmp = 0
    for j in range(7):
        tmp += n[i * 7 + j] * (2 ** (6 - j))
    print(tmp, end=' ')
"""


string = '0000000111100000011000000111100110000110000111100111100111111001100111'
arr = list(map(int, string))
list_num = len(arr) // 7
lists = [[] * list_num]
cnt = 0
for i in range(list_num):
    for j in range(7):
        lists[i].append(arr[j])
        cnt += 1
        if cnt == len(string) - 1:
            break
print(lists)
