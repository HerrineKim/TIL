# 카펫
def solution(brown, yellow):
    answer = []
    # 의미를 명확하게 하기 위해 입력값을 새로운 변수에 담았다.
    margin = brown
    inside = yellow
    # 1부터 5000에서 2를 빼고 2로 나눈 후 2를 뺀 값까지 
    # (가로 넓이 - 2)를 i로 두고 가장자리와 내부 넓이를 이용해 방정식을 풀듯 i를 구한다.
    for i in range(1, 2498):
        if inside % i == 0:
            if ((i + 2) * ((inside / i) + 2)) - inside == margin:
                # 알맞은 i가 나오면 정답 리스트에 높이와 너비를 append하고 for문을 나간다.
                answer.append((inside / i) + 2)
                answer.append(i + 2)
                break
    return answer