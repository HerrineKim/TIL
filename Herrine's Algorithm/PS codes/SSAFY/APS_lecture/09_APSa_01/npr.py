def f(n, k):  # 순열 p[n]을 채우는 함수, k 배열의 크기
    if n == k:
        print(p)
    else:
        for i in range(k):  # used에서 사용하지 않은 숫자 검색
            if used[i] == 0:  # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1  # 사용함으로 표시
                p[n] = a[i] # p[n] 결정
                f(n+1, k)
                used[i] = 0  # a[i]를 다른 위치에서 사용할 수 있도록 함
    return


a = [1, 2, 3, 7, 8, 3]
p = [0] * 6
used = [0] * 6
f(0, 6)
