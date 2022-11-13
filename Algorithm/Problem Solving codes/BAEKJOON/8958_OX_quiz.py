T = int(input())

for tc in range(T):
    answers = list(input())
    temp = 0
    temp_list = [0 for _ in range(len(answers))]
    if answers[0] == 'O':
        temp_list.insert(0, 1)
    else:
        temp_list.insert(0, 0)
    
    for i in range(1, len(answers)):
        if answers[i] == 'O':
            temp_list[i] = temp_list[i - 1] + 1
    
    ans = 0
    for j in range(len(temp_list)):
        ans += temp_list[j]
    
    print(ans)