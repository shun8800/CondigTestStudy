# 집합
data = set([1,1,2,2,3,3,4,4,5])
print(data)

data = {1, 2, 3, 4, 5}
print(data)

a= set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a|b)

# 교집합
print(a&b)

# 차집합
print(a-b)

data = set([1, 2, 3])
data.add(4) # 하나만 추가
print(data)

data.update([5, 6]) # 여러개 추가
print(data)

data.remove(3) # 값 삭제
print(data)