# 1966. 숫자를 정렬하자
"""
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums = sorted(nums)
    print(f'#{tc}', *nums)
