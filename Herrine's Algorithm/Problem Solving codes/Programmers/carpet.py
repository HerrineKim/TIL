from sympy import Symbol, solve

def solution(brown, yellow):
    answer = []
    b = brown
    y = yellow
    garo = Symbol('garo')
    sero = Symbol('sero')
    equation1 = (garo + sero) * 2 - 4 - brown
    equation2 = (garo - 2) * (sero - 2) - yellow
    Result = solve((equation1, equation2), dict=True)

    print(Result)
    
    return answer