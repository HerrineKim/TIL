# 타겟 넘버
def solution(numbers, target):
    # global 외않되..?
    answer = 0
    target_number = target
    def dfs(numbers, target, index, value):
        nonlocal answer
        # 백트래킹
        if index == len(numbers):
            if value == target:
                answer += 1
            return
        dfs(numbers, target, index + 1, value + numbers[index])
        dfs(numbers, target, index + 1, value - numbers[index])
    dfs(numbers, target_number, 0, 0)

    return answer