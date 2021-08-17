# BFS : 너비 우선 탐색(그래프에서 가까운 노드부터 우선적으로 탐색)
# 큐 자료구조 사용
# 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 위의 과정을 수행할 수 없을 때까지 반복
# DFS와의 차이점은 큐를 사용한다는 점
# 노드를 하나씩 넣어서 비교하지 않고 모두 큐에 삽입한다는 점

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)