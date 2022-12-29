# 더 맵게
def solution(scoville, K):
    # 우선순위 큐: 최소 힙을 만족하는 자료 구조
    import heapq
    answer = 0
    # 우선순위 큐로 만들어주는 함수
    heapq.heapify(scoville)
    # print(scoville)
    
    # 조건을 만족할 때 까지 섞기
    while scoville[0] < K and len(scoville)>1:
            answer += 1
            # 음식을 섞는 공식(맨 앞, 즉 스코빌 지수가 가장 낮은 음식을 pop 하고 그 다음으로 낮은 음식을 pop)
            new_food = heapq.heappop(scoville)+ heapq.heappop(scoville) *2
            # heappush를 하면 우선순위 큐의 규칙을 깨지 않고 요소를 push 해 줌
            heapq.heappush(scoville, new_food)
    # 실패 조건
    if scoville[0] < K:
        return -1
    return answer