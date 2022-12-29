# 신고 결과 받기
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    singo = report
    # 아이디 별 신고 받은 횟수를 저장할 dict
    singo_dict = {x: 0 for x in id_list}
    
    # 여러 번 신고해도 소용이 없으니 set 처리한 신고 내역을 만들고 신고 dict를 만들어 준다.
    for s in set(singo):
        sender, receiver = s.split()
        singo_dict[receiver] += 1
    # 신고 횟수가 k 번이 넘은 피신고자의 신고자에게 고지 메일 +1을 해준다.
    for s in set(singo):
        sender, receiver = s.split()
        if singo_dict[receiver] >= k:
            answer[id_list.index(sender)] += 1
    
    return answer