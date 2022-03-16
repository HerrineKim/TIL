T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    max_value_li = [0] * len(str1)  # str1의 각 알파벳들이 발견되는 횟수를 저장해 줄 list
    for i in range(len(str1)):  # str1의 알파벳들을 각각 순회
        for x in str2:  # str2의 알파벳들을 각각 순회
            if x == str1[i]:  # 만약 str1의 어떠한 알파벳이 str2에서 발견되면
                max_value_li[i] += 1  # 횟수 저장 list에서 그 알파벳 위치에 + 1
    max_value = 0  # 이제 최대값을 구하는 for 문 한 번만 돌려 주면 끝
    for j in max_value_li:
        if j > max_value:
            max_value = j
    print(f'#{test_case} {max_value}')
