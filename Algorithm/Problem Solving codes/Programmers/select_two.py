def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(len(numbers)):
            if i != j:
                new_sum = numbers[i] + numbers[j]
                if new_sum not in answer:
                    answer.append(numbers[i] + numbers[j])
    # sorted()는 새로운 정렬된 목록을 반환하며, 원래 목록은 영향을 받지 않습니다.
    # list.sort()은 list을 그 자리에서 정렬하고 목록 인덱스를 변경하고 None을 반환합니다.(모든 내부 작업은 동일).
    answer.sort()
    return answer