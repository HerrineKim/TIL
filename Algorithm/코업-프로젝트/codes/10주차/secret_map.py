# 비밀지도
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # |: 비트 or 연산(둘 중 하나만 참이어도 참)
        # bin(): 10진수 -> 2진수를 string으로 반환. 맨 앞은 2진수라는 의미로 '0b'
        # zfill(n): 문자열의 길이가 n 될 때까지 앞부분을 0으로 채워줌
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))
    return answer