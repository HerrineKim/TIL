import sys

def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        current = house[0]
        count = 1

        for i in range(1, len(house)):
            if house[i] >= current + mid:
                current = house[i]
                count += 1
        if count >= C:
            # 사이 거리 넓히기
            start = mid + 1
            answer = mid
        else:
            # 사이 거리 좁히기
            end = mid - 1
    return answer


input = sys.stdin.readline
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

# start는 최소거리, end는 최대거리
start = 1
end = house[-1] - house[0]

print(binary_search(start, end))