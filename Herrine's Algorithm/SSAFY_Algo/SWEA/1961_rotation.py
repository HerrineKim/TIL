T = int(input())
# 90도 회전하는 함수


def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 먼저 만들기
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotation(arr, N)
    rot_180 = rotation(rot_90, N)
    rot_270 = rotation(rot_180, N)

    print("#{}".format(tc))
    for k in range(N):
        print("".join(map(str, rot_90[k])), end=" ")
        print("".join(map(str, rot_180[k])), end=" ")
        print("".join(map(str, rot_270[k])), end=" ")
        print()
