# 모의고사


def solution(answers):
    first_answer = [1, 2, 3, 4, 5]
    second_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    third_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = []
    first = 0
    second = 0
    third = 0
    
    for i in range(len(answers)):
        if answers[i] == first_answer[i%5]:
            first += 1
        if answers[i] == second_answer[i%8]:
            second += 1
        if answers[i] == third_answer[i%10]:
            third += 1
    
    max_score = max(first, second, third)
    
    if first == max_score:
        answer.append(1)
    if second == max_score:
        answer.append(2)
    if third == max_score:
        answer.append(3)
        
    return answer

print(solution([1, 2, 3, 4, 5])) # [1]
print(solution([1, 3, 2, 4, 2])) # [1, 2, 3]