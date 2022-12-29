# 스킬트리
def solution(skill, skill_trees):
    answer = 0
    # 스킬 트리들마다 스킬 목록에 있는 것만 남기기
    for x in range(0, len(skill_trees)):
        skill_trees[x] = ''.join(a for a in skill_trees[x] if a in skill)
        # print(skill_trees[x])

    # 각 트리에 남은 스킬들과, 그 길이 만큼 skill에서 비교해 같은지 확인
    for tree in skill_trees:
        if tree == skill[0:len(tree)]:
            answer += 1
            
    return answer