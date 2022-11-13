import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 응시자 수, 상 받는 사람 수
score = list(map(int, input().split())) # 각 학생별 점수
score.sort(reverse=True) # 오름차순 정렬

print(score[k-1])