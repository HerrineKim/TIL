# 신규 아이디 추천
def solution(new_id):
    # 1. 소문자로 변경한다.
    new_id = new_id.lower()
    # 2. 사용 불가 문자 제거
    # 3. .. -> .
    new_id_list = []
    for i in new_id:
        # isalnum(): 문자인지 숫자인지 확인
        if i.isalnum() or i in ['-', '_', '.']:
            if new_id_list:
                if i ==  '.' and new_id_list[-1] == '.':
                    continue
            new_id_list.append(i)
            
    # 4. 마침표가 처음이나 끝에 있으면 제거
    if new_id_list:
        if new_id_list[0] == '.':
            new_id_list = new_id_list[1:]
    if new_id_list:
        if new_id_list[-1] == '.':
            new_id_list = new_id_list[:-1]
    
    # 5. 빈 문자열이면 'a' 대입
    if not new_id_list:
        new_id_list = [a]

    # 6. 16자 이상이면 15개 초과분은 자르기
    if len(new_id_list) >= 16:
        new_id_list = new_id_list[:15]
        if new_id_list[-1] == '.':
            new_id_list.pop()
    
    # 7. 2자 이하이면 마지막 문자를 한 번 더 붙이기
    if len(new_id_list) <= 2:
        last = new_id_list[-1]
        while len(new_id_list) <= 3:
            new_id_list.append(last)
    # join(): 지정된 구분자를 사용해 리스트를 문자열로 변환
    return ''.join(new_id_list)
