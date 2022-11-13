import sys

C = int(input())  # C 전체 테스트 케이스 개수
for t in range(C):
    temp_list = list(map(int, sys.stdin.readline().split()))
    N = temp_list[0]  # 학생의 수
    scores = temp_list[1:]  # 학생별 점수
    
    average_score = sum(scores) / N
    over_average = 0
    for i in range(N):
        if scores[i] > average_score:
            over_average += 1
    
    ans = round(over_average / N * 100, 3)
    
    print(f'{ans:.3f}%')