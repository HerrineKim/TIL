# 주차 요금 계산

# math.ceil(): 올림
import math
# 시간을 분으로 변환하는 함수
def to_minute(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(fees, records):
    answer = []
    # 입차 시간을 우선 저장해줄 dict
    in_time = {}
    # 주차 시간 dict
    parking_time = {}
    
    for record in records:
        time, car_num, in_out = record.split()
        # 입차 시간 기록
        if in_out == 'IN':
            in_time[car_num] = to_minute(time)
            # 주차 시간도 같이 초기화 해주기
            if car_num not in parking_time:
                parking_time[car_num] = 0
        # 출차 시간이 있다면 주차 시간 기록
        else:
            parking_time[car_num] += to_minute(time) - in_time[car_num]
            # 출차한 차들은 입차 기록 삭제
            in_time.pop(car_num)
    
    # print(parking_time)
    # 출차 기록 없는 차들의 주차 시간까지 계산
    for num, t in in_time.items():
        parking_time[num] += 23 * 60 + 59 - t

    # 요금 계산
    # dict.items()를 sorted() 함수에 넣으면 key 기준으로 오름차순 정렬된 dict 반환한다!
    for num, t in sorted(parking_time.items()):
        # 180분 이하면 기본 요금만
        if t <= fees[0]:
            answer.append(fees[1])
        # 그 이상이라면 추가 시간을 10으로 나눈 후 올림한 것에 추가 요금을 곱하고, 기본 요금과 더함
        else:
            answer.append(fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3])

    return answer


