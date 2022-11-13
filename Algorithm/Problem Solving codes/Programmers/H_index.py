# H-index
def solution(citations):
    answer = 0
    # key는 인용 횟수, value는 그 이상 인용된 논문 개수인 dictionary
    citation_and_cnt = {}
    for i in range(len(citations)):
        # 인용 횟수(i, 즉 h)마다 그 이상 인용된 논문이 몇 편인지 센다.
        cnt = 0
        for j in range(len(citations)):
            # 만약 j번째 논문이 h값보다 같거나 많이 인용되었다면 cnt += 1
            if citations[j] >= citations[i]:
                cnt += 1
        # 모두 센 후, h번 <= h편의 조건을 충족하여 H-index의 후보가 될 수 있는 조건이 된다면 dictionary에 넣는다.
        if citations[i] >= cnt:
            citation_and_cnt[citations[i]] = cnt
    # 모든 논문이 0회 인용되었을 경우, max 함수에 빈 값이 들어가 에러가 난다. 예외 처리한다.
    if citation_and_cnt == {}:
        return 0
    
    # 조건을 충족하는 후보들 중 최댓값을 구한다. 
    answer = max(citation_and_cnt.values())
    return answer