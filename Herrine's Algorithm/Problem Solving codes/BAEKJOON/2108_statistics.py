# 2108번 통계학
# 입력
import sys
N = int(input())
nums = []
nums_dict = {}
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
    if num not in nums_dict:
        nums_dict[num] = 1
    else:
        nums_dict[num] += 1
        
# 산술평균
print(round(sum(nums)/N))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
max_ = max(nums_dict.values()) # 최대 등장 횟수 찾기
temp = []
for key, value in nums_dict.items():
    if value == max_: # value가 최대 등장 횟수와 같은 숫자 따로 빼두기
        temp.append(key)

# 최빈 값이 여러 개 인 경우
if len(temp) != 1:
    # 정렬 후 두 번째로 작은 값 출력
    temp.sort()
    print(temp[1])
else:
    print(temp[0])
    
# 범위
print(nums[-1] - nums[0])
