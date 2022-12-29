# 영어 끝말잇기
import math
def solution(n, words):
    # 사용된 단어들
    temp = []
    for idx, word in enumerate(words):
        # word가 사용되었거나, 단어가 이어지지 않은 경우
        if word in temp or (idx >= 1 and words[idx - 1][-1] != word[0]):
            # 실패한 사람과 실패한 라운드 return
            return [(idx % n) + 1, math.ceil((idx + 1) / n)]
        temp.append(word)
    return [0, 0]