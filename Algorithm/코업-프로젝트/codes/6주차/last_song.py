# 방금그곡
def solution(m, musicinfos):
    # 문자 별로 자르기 위해 m에서 샵(#)이 붙은 음을 소문자로 대체한다.
    heard = m.replace("D#","d").replace("C#","c").replace("F#","f").replace("A#","a").replace("G#","g")
    # 조건을 만족하는 음악의 길이와 제목을 담아 줄 tuple을 만든다.
    temp = (0, '')
    
    for info in musicinfos:
        # 문자열을 나누고, 라디오에서 재생된 시간을 계산한다.
        splitted = info.split(",")
        start_time, end_time = splitted[0], splitted[1]
        play_time = int(end_time[-2:]) - int(start_time[-2:])
        if start_time[:2] != end_time[:2]:
            play_time += 60 * (int(end_time[:2]) - int(start_time[:2]))
        scores = splitted[3].replace("D#","d").replace("C#","c").replace("F#","f").replace("A#","a").replace("G#","g")
        
        # 재생된 노래 전체를 계산한다.
        whole_scores = (scores * (play_time // len(scores) + 1))[:play_time]
        # 들은 노래가 재생된 노래에 포함되고, temp보다 길이도 길다면 갱신해준다.
        if heard in whole_scores and temp[0] < play_time:
            temp = (play_time, splitted[2])
    # 입력된 노래들을 전부 순회했는데 temp가 갱신된 적 없다면 None return하고, temp가 갱신되었다면 노래 제목을 return한다.
    if temp[0] == 0:
        return '(None)'
    else:
        return temp[1]
