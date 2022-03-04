# 회문 판별 1
word = input('단어를 입력하세요: ')
is_palindrome = True  # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):  # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False  # 회문이 아님
        break

print(is_palindrome)  # 회문 판별값 출력

# 회문 판별 2
word = input('단어를 입력하세요: ')

print(word == word[::-1])  # 원래 문자열과 반대로 뒤집은 문자열을 비교

# 회문 판별 3
word = 'level'
list(word) == list(reversed(word))

# 회문 판별 4
word = 'level'
word == ''.join(reversed(word))
