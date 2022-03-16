# 미완성
def enQ(data):
    global rear
    if (rear+1) & Qsize == front:
        print('Q is Full!')
    else:
        rear = (rear + 1) % Qsize
        return q[front]


def deQ():
    global front
    if front == rear:
        print('Q is Empty!')
    else:
        front = (front+1) % Qsize
        return q[front]


p = 1
N = 20  # 마이쮸 초기 개수
Qsize = 20
q = [0] * Qsize
front = 0
rear = 0
v = 0

m = 0  # 나눠준 개수
cnt = [0] * N  # 사람별로 줄 선 횟수, 받을 수 있는 사람 수 < N
my = [0] * N  # 사람별로 받은 마이쮸 개수
while m < N:  # 남은 마이쮸가 있으면
    enQ(p)
    cnt[p] += 1  # p번 사람이 줄 선 횟수 1회 증가
    # print(f'큐에 있는 사람 수: {}')
    v = deQ()  # 줄 맨 앞 사람 v
    m += cnt[v]
    my[v] += cnt[v]  # v가 받은 개수 누적

    enQ(v)  # 받은 사람 v가 바로 줄을 서면
    cnt[v] += 1  # 줄 선 횟수가 1번 늘어나고
    p += 1  # 따라서 줄 설 사람의 번호는 하나 증가

print(f'마지막 받은 사람 : {v}')  # 나눠준 개수 m >= N 원래의 개수가 될 때 받은 사람
