# 최소 지갑
def solution(sizes):
    # 지갑의 최소 가로 세로 길이를 구해야 하므로 min 값을 문제에서 주어진 1로 설정하고 갱신해 나간다.
    min_w = 1
    min_h = 1
    for wh in sizes:
        # 가로 세로 뒤집기가 가능하므로, 항상 앞을 더 긴 것으로 만들어 주는 작업을 한다.
        if wh[0] < wh[1]:
            wh = wh[::-1]
        # 최소값 찾아 나간다.
        if min_w < wh[0]:
            min_w = wh[0]
        if min_h < wh[1]:
            min_h = wh[1]
    # 최종 지갑의 길이를 구한다.
    answer = min_w * min_h
    
    return answer