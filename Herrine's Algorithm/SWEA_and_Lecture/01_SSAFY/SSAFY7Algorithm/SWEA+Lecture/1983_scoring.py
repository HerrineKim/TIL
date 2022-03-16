# 1983 조교의 성적 매기기
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N 총 학생 수 K 알고 싶은 학생의 번호
    grades = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    scores = []
    for i in range(N):
        M, F, H = map(int, input().split())  # M 중간 F 기말 H 숙제
        score = 0.35 * M + 0.45 * F + 0.2 * H
        scores.append(score)
    KScore = scores[K-1]
    scores = sorted(scores)
    newK = scores.index(KScore)

    ans = grades[newK//(N//10)]
    print(f'#{tc} {ans}')
