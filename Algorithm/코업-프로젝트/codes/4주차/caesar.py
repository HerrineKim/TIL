# 시저 암호
# 1학기 과목평가 문제
# ASCII 코드표를 이용
# 대문자: 65~90, 소문자: 97~122(까먹었다)
# ord(): ASCII 값으로 변환, chr(): 다시 문자로 변환

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        # alphabet: 각 알파벳
        alphabet = s[i]
        # 소문자일 경우
        if alphabet.islower():
            if ord(alphabet) + n > 122:
                new_chr = chr(ord(alphabet) + n - 26)
            else:
                new_chr = chr(ord(alphabet) + n)
        # 대문자일 경우
        elif alphabet.isupper():
            if ord(alphabet) + n > 90:
                new_chr = chr(ord(alphabet) + n - 26)
            else:
                new_chr = chr(ord(alphabet) + n)
        # 공백일 경우: 변형하지 않는다.
        elif alphabet.isspace():
            new_chr = alphabet
        answer += new_chr
    return answer