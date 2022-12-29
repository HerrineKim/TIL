def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n
    # 최대공약수
    def max_yaksu(a, b):
        # 더 작은 수인 n으로 나눠지면 n이 최대공약수
        if b % a == 0:
            return a
        else:
            yaksu = 0
            for y in range(1, a + 1):
                if n % y == 0 and m % y == 0:
                    yaksu = y
            return yaksu
                
    answer.append(max_yaksu(n, m))
    # 최소공배수
    # 두 수의 곱을 최대공약수로 나누기
    answer.append(n * m // max_yaksu(n, m))
    return answer