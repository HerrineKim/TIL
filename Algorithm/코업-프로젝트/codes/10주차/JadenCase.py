# JadenCase 문자열 만들기
def solution(s):
    answer = ''
    # 소문자로 바꿈
    s = s.lower()
    # 단어를 리스트에 담음
    s_list = s.split(' ')
    for word in s_list:
        # 만약 공백이면 공백 문자가 연속으로 나왔다는 뜻이므로 공백 더하기
        if word == '':
            answer += ' '
        # 공백이 아니라면 단어 앞자리만 대문자로 바꾼 후 뒤에 공백을 붙여 더하기
        else:
            answer += word[0].upper() + word[1:] + ' '
    # 맨 마지막 공백 빼고 return
    return answer[:-1]