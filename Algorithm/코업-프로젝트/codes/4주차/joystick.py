# 조이스틱
def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽 시작 방식, 연속된 A의 오른쪽 시작 방식 비교 및 갱신
        min_move = min([min_move, (2 * i) + len(name) - next, i + (2 * (len(name) - next))])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer

# def solution(name):
#     answer = 0
#     target_name = list(name)
#     # 원래 형태 만들기
#     A_name = ''
#     for i in range(len(name)):
#         A_name += 'A'
#     A_name = list(A_name)
#     # 이전 index
#     before_index = 0
#     # 현재 index
#     new_index = 0
#     # 순방향 index
#     right_index = 0
#     # 역방향 index
#     left_index = 0
    
#     cnt = 0
    
#     while A_name != target_name:
#         temp_left = 0
#         temp_right = 0
#         before_index = new_index
#         for new_index in range(new_index, -len(target_name), -1):
#             temp_left += 1
#             if target_name[new_index] != 'A':
#                 left_index = new_index
                
#         for new_index in range(new_index, len(target_name)):
#             temp_right += 1
#             if target_name[new_index] != 'A':
#                 right_index = new_index
#         if temp_left > temp_right:
#             new_index = right_index
#         else:
#             new_index = left_index
#         if (90 - ord(target_name[new_index])) + 1 <= ord(target_name[new_index]) - 65:
#             plus = (90 - ord(target_name[new_index])) + 1
#         else:
#             plus = ord(target_name[new_index]) - 65
#         answer += plus
#         target_name[new_index] = 'A'
#         if A_name == target_name:
#             break
#         else:
#             if before_index < 0 and new_index < 0:
#                 cnt += abs(before_index) - abs(new_index)
#             elif before_index < 0 and new_index >= 0:
#                 cnt += abs(before_index + new_index)
#             elif before_index >= 0 and new_index < 0:
#                 cnt += abs(before_index + new_index)
#             elif before_index >= 0 and new_index >= 0:
#                 cnt +=  abs(before_index - new_index)

            
#     answer += cnt
#     print(cnt)
#     return answer

# print(solution('JEROEN'))