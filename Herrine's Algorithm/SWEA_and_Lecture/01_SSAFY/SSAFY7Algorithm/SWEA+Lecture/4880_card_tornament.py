# 4880_card_tournament
# 1 가위 2 바위 3 보
def rcp(f, s):  # 가위바위보 함수
    if cards[f] == cards[s] or cards[f] % 3 == (cards[s] + 1) % 3:
        return f  # 비겼거나, first가 이긴다면 first친구 return
    else:
        return s  # second가 이긴 경우에만 second return


def tourn(start, end):  # 토너먼트 함수
    if start == end:  # 한 명만 남은 경우
        return start  # 그대로 해당 인덱스 return
    else:  # 토너먼트 진행
        middle = (start + end) // 2
        first = tourn(start, middle)
        second = tourn(middle + 1, end)
    return rcp(first, second)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N 사람 수
    cards = list(map(int, input().split()))  # cards사람 수 만큼의 카드 리스트
    print(f'#{tc} {tourn(0, N-1) + 1}')
