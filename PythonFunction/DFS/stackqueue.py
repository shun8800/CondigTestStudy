# 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 대표적으로 DFS, BFS

# 스택 : 선입후출 자료구조 / 입구와 출구가 동일한 형태로 시각화 가능
# 삽입과 삭제로 이루어짐
# 리스트 자료형으로 구현 가능

'''
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])
print(stack)
'''


# 큐 : 선입선출 자료구조 / 입구와 출구가 모두 뚫려 있는 터널 구조

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)




