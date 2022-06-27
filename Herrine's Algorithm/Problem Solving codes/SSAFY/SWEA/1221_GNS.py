NumLi = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for test_case in range(1, T+1):
    N, length = map(str, input().split())
    length = int(length)
    nums = list(map(str, input().split()))
    result = []
    for i in range(len(NumLi)):
        for j in nums:
            if NumLi[i] == j:
                result.append(j)
    print(N)
    print(*result)
