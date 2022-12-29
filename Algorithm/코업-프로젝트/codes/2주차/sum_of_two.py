# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(len(numbers)):
            if i != j:
                new_sum = numbers[i] + numbers[j]
                if new_sum not in answer:
                    answer.append(numbers[i] + numbers[j])
    # sorted()는 새로운 정렬된 목록을 반환하며, 원래 목록은 영향을 받지 않습니다.
    # sorted()은 list뿐만 아니라 반복 가능한 모든 작업에 적용할 수 있습니다.
    answer.sort()
    return answer