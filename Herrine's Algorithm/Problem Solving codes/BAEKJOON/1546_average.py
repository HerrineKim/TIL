N = int(input())  # 시험 본 과목의 개수
scores = list(map(int, input().split()))  # 시험 본 과목의 점수
max_score = max(scores)  # 최대 점수

for i in range(N):
    scores[i] = scores[i] / max_score * 100

ans = sum(scores) / N
print(ans)