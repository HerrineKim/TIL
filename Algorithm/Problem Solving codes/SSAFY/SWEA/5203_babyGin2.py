# 5203. babyGin
T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input().split()))  # 카드덱
    A = [0] * 12  # A의 카드
    B = [0] * 12  # B의 카드
    winner = 0  # 0으로 초기화 (1 or 2 or 0)
    for c in range(0, len(cards), 2):  # 각자 카드 뽑아가기
        A[cards[c]] += 1
        B[cards[c+1]] += 1
        # A 검사
        for i in range(12):
            if max(A) >= 3 or (A[i] >= 1 and A[i+1] >= 1 and A[i+2] >= 1):
                winner = 1
                break
        if winner > 0:
            break
        # B 검사
        for i in range(12):
            if max(B) >= 3 or (B[i] >= 1 and B[i+1] >= 1 and B[i+2] >= 1):
                winner = 2
                break
        if winner > 0:
            break
    print(f'#{test_case} {winner}')
