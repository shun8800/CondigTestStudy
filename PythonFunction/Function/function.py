# 함수의 종류 : 내장 함수 / 사용자 정의 함수
# 내장함수 : 파이썬이 기본적으로 제공하는 함수
# def 함수명(매개변수): ...
# global 키워드 : 전역 변수
# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음
'''
def add(a, b):
    return a+b

print(add(3, 4))
'''

'''
def add(a, b):
    return print('함수의 결과 : ', a+b)

add(3, 4) 
add(b=3, a=7) # 파라미티 변수 직접 지정
'''

'''
a = 0

def func():
    global a
    a+=1

for i in range(10):
    func()
'''

'''
def operator(a, b):
    add_var = a+b
    substract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var, substract_var, multipy_var, divide_var 

'''