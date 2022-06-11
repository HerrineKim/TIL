def solve(lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i] + 1) % 2

        dec = 0  # 10진수로 변환
        for idx in range(len(lst2)):
            dec = dec * 2 + lst2[idx]

        s = []  # 3진수로 변환
        ret = dec
        while dec > 0:
            s.append(dec % 3)
            dec //= 3
        lst = lst3[::-1]
        # 우리 tc에서는 필요 없는 부분이긴 함
        cnt = 0
        for idx in range(min(len(s), len(lst))):
            if s[idx] != lst[idx]:
                cnt += 1
        cnt += abs(len(s) - len(lst))  # 길이가 다르다면 다른값

        if cnt == 1:
            return ret

        lst2[i] = (lst2[i] + 1) % 2  # 원래대로 복구


T = int(input())
for test_case in range(1, T + 1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve(lst3)
    print(f'#{test_case} {ans}')