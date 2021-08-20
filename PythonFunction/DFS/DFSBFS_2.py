# N x M 크기의 직사각형 형태의 미로에 갇힘
# 출발 위치는 (1, 1), 출구는 (N, M)
# 괴물이 있는 부분은 0 , 괴물이 없는 부분은 1
# 출발점과, 도착점을 모두 카운트해서 최소 이동을 몇칸을 해야하는가?
# BFS 이용 : 모든 경우의 수에서 최단 경로를 찾음

from collections import deque

def bfs(x, y):
    queue = deque()  # 큐 초기화
    queue.append((x, y))  # 초깃값인 0, 0 큐에 확장

    while queue:
        x, y = queue.popleft()  #  x, y 값 추출

        for i in range(4):  # 동, 서, 남, 북 탐방하면서 좌표값 nx, ny에 저장
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:  # 범위를 벗어나면 끝
                continue
            if graph[nx][ny]==0:  # 괴물을 만나면 끝
                continue
            if graph[nx][ny]==1:  # 갈 수 있는 길이면
                graph[nx][ny] = graph[x][y] + 1  # 처음 좌표값에 1을 더함
                queue.append((nx, ny))  # 다음 진행 좌표를 큐에 확장

    return graph[n-1][m-1]  # 다 돌면 n-1, m-1 좌표 값 출력


n, m = map(int, input().split())  # n, m을야 공백으로 입력 받음

graph = []  # 지도를 그릴 그래프 리스트를 초기화(2차원 배열 개념)

# 세로 열(n) 범위에서 값 입력(0, 1) = 지도 구성(길, 괴물)
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# bfs로 0,0 부터 시작
print(bfs(0, 0))