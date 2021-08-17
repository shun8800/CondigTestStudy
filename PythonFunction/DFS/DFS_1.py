# DFS : 깊이 우선 탐색(깊은 부분을 우선적으로 탐색하는 알고리즘)
# DFS는 스택 자료구조(혹은 재귀함수)를 이용
# 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
# 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
# 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
# 위의 과정을 수행할 수 없을 때까지 반복


# 문제 예시

def dfs(graph, v, visited):
    visited[v] = True  # v번째 노드 방문
    print(v, end=' ')

    for i in graph[v]:  # graph에 있는 값 i
        if not visited[i]:  # 만약 그 i 노드를 방문하지 않았다면
            dfs(graph, i, visited)  # dfs 재귀


graph = [
    [],  # 보통 첫번째 노드부터 시작하기 떄문에 0번째는 비워둠
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]  # 각 노드와 인접한 노드

visited = [False] * 9  # 각 노드가 방문된 정보를 표현(아직 방문 x)

dfs(graph, 1, visited)  # 시작노드가 1

# 중요한건 노드 연결을 파악할 수 있는 그래프 리스트
# 시작점(방향 및 조건)
# 방문 여부


