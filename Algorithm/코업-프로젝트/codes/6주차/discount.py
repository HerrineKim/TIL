# 할인 행사
# 시간이 모자라서 코드 참고했읍니다..

# Counter: 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 된다.
# 예)
# Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})
from collections import Counter

def solution(want, number, discount):
    answer = 0
    # 나의 장보기 목록(Counter와 비교할 것)
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    
    # for문으로 각 날짜마다 Counter를 만들어서 check와 같은지 비교한다.
    # 만약 만족한다면 회원가입 가능하므로 answer += 1한다.
    for i in range(len(discount) - 9):
        c = Counter(discount[i:i + 10])
        if c == check:
            answer += 1

    return answer