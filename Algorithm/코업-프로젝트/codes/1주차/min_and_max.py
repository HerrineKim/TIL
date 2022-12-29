# Title: 최댓값과 최솟값
def solution(s):
    s_list = list(map(int, s.split()))
    max_v = s_list[0]
    min_v = s_list[0]
    for i in range(len(s_list)):
        if s_list[i] < min_v:
            min_v = s_list[i]
        if s_list[i] > max_v:
            max_v = s_list[i]
    return f'{min_v} {max_v}'