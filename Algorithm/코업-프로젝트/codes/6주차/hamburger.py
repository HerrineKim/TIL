# 햄버거 만들기
def solution(ingredient):
    answer = 0
    # 재료의 순서를 점검할 리스트
    temp = []
    # 재료가 들어오는 대로 리스트에 넣고, 길이가 4 이상이고 햄버거 만들 수 있다면 만들고 재료는 소비한다.
    # 햄버거 하나 만들 때마다 answer +1 해준다.
    for i in ingredient:
        temp.append(i)
        if len(temp) >= 4 and i == 1 and temp[-2] == 3 and temp[-3] == 2 and temp[-4] == 1:
            for i in range(4):
                temp.pop()
            answer += 1
    
    return answer