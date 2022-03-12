#4828. min max
T = int(input())
for x in range(1, T + 1):

    N = int(input())
    num_li = list(map(int, input().split()))

    max = num_li[0]
    min = num_li[0]
    for num in num_li:
        if max < num:
            max = num
        if num < min:
            min = num

    result = max - min

    print(f'#{x} {result}')

'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''