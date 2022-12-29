# 3진법 뒤집기
def solution(n):
    answer = 0
    input_number = n
    to_string = ''
    while input_number > 0:
        input_number, mod = divmod(input_number, 3)
        to_string += str(mod)
    answer = int(to_string, 3)    
    return answer