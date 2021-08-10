# in 연산자와 not in 연산자(포함 관련, 하나 씩 방문)
# 파이썬은 부등호를 0 < x < 20 이런식으로 표현 가능
'''
array = [9, 8, 7, 6, 5]
tup = (1, 2, 3, 4, 5)

for x in tup:
    print(x)

for x in array:
    print(x)

# 1부터 9까지 순회하는 값

result = 0
for x in range(1, 10):
    result += x

print(result)
'''

'''
scores = [90, 52, 34, 14, 62]
cheating = {2, 4}

for i in range(5):
    if i+1 in cheating:
        continue # 조건문에 해당되면 뛰어넘기
    if scores[i]>=20:
        print(i+1, "번 학생 합격")
'''

data = list(map(int, input().split()))
data.sort()
print(data)

for i in data:
    print("hello")
