# 현주의 상자바꾸기

T = int(input())
for test_case in range(1, T+1):
    NQ = list(map(int, input().split()))  # [N = 상자 갯수, Q = 작업 횟수]
    boxnum = [0]*NQ[0]  # 상자 만들기

    for i in range(1, NQ[1]+1):  # 작업 횟수만큼 반복. 밑에서 i 쓰려고 1부터 시작
        LR = list(map(int, input().split()))  # 작업 횟수만큼 리스트가 들어옴
        for j in range(LR[0]-1, LR[1]):  # 바꿔줘야 하는 범위만큼 반복
            boxnum[j] = i  # 범위만큼의 숫자들을 i로 바꿔줌

    result = ' '.join(map(str, boxnum))
    print(f'#{test_case} {result}')