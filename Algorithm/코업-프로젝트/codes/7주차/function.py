# 기능 개발
def solution(progresses, speeds):
    answer = []
    p = progresses
    s = speeds
    # 작업이 모두 사라질 때까지 반복한다.
    while p :
        cnt = 0
        # 100 이상이 된 작업이 있으면 cnt += 1을 해주고 작업 목록에서 뺀다.
        while p and p[0] >= 100:
            cnt += 1
            p.pop(0)
            s.pop(0)
        # 하루마다 진행도를 올린다.
        for i in range(len(p)):
            p[i] += s[i]
        # cnt가 1 이상이면 답 목록에 추가하고 다음 날로 넘어간다.
        if cnt:
            answer.append(cnt)
    
    return answer