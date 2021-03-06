# input() = 한줄의 문자열(값)을 입력받는 함수
# map() = 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# list(map(int, input().split()))
# 공백을 기준으로 구분된 데이터를 입력 받을 때 사용

# a, b, c = map(int, input().split())
# 공백을 기준으로 구분된 데이터의 개수가 많지 않을 때 사용

'''
n = int(input())
data_1 = input().split()
data_2 = map(int, data_1) # data2 = map(int, input().split())
data_3 = list(data_2) # list(map(int, input().split())
print(n)
print(data_1)
print(data_2)
print(data_3)
'''



# 사용자로부터 입력을 빠르게 받아야 하는 경우
# sys.stdin.readline() 메서드를 이용
# 엔터가 줄 바꿈 기호이므로 rstrip() 메서드를 사용

'''
import sys

data = sys.stdin.readline().rstrip() # input() 과 똑같은 역할인듯?
data1 = list(map(int, data.split()))
print(data)
print(data1)
'''

# print는 기본적으로 출력 후에 개행을 함
# 개행을 피하고 싶으면 end = " " 추가

a = 1
b = 2
print(a)
print(b)
print(7, end=" ")
print(8, end=" ")