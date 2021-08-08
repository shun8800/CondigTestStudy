# 람다 표현식으로 여러 줄의 함수를 한 줄로 정의 가능

'''
def add(a, b):
    return a+b

print(add(3, 7))

==

print((lambda a, b: a+b)(3, 7))

'''

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# map 함수 : 각각의 원소에 어떠한 규칙을 적용하고 싶을 때

result = map(lambda a, b : a+b, list1, list2)
print(list(result))
# 변수를 넣을때는 (lambda a,b : a+b)(3, 4)
# 리스트를 넣을때는 (lambda a,b : a+b, list1, list2)