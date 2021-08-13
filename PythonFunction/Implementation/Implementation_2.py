# 여행가 A는 N x N 크기의 정사각형 공간 위에 서있음
# 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있음
# 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래는 (N, N)
# 여행가 A는 상하좌우로 움직일 수 있고 시작 좌표는 (1, 1)
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 함
# L : 왼쪽 한칸 이동
# R : 오른쪽 한칸 이동
# U : 위로 한칸 이동
# D : 아래로 한칸 이동
# 공간을 벗어나는 움직임은 무시됨

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:  # plan에 L, R, U, D 들어감
    for i in range(len(move_types)):  # == range(4)
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue

    x, y = nx, ny

print(x, y)