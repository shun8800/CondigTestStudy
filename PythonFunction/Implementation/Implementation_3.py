# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지
# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하기
# 가능한 경우의 수를 모두 검사해보는 탐색(완전 탐색)방법

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
